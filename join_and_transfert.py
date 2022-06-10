# -*- coding: utf-8 -*-
import os, shutil, time, io
import logging.config
from settings import logger_config
import get_settings as set

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

def serch_in_check_nomura(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def common_files_nomura(path_for_check_join,machine):
    if os.path.isdir(os.path.join(set.PATH_FOR_CHECK,machine))== False:
        os.makedirs(os.path.join(set.PATH_FOR_CHECK,machine))
    spisok = []
    if os.path.isfile(os.path.join(path_for_check_join,machine+'-ignor.txt')):
        with open(os.path.join(path_for_check_join,machine+'-ignor.txt'),'r') as f:
            spisok=list(f.read().split(' '))
    path_folder=os.path.join(path_for_check_join,machine)
    if os.path.isdir(path_folder) == False:
        os.makedirs(path_folder)
    for file in serch_in_check_nomura(path_folder):  # ищем файл в папке  со станков
        file_name = file.split('\\')[-1]  # имя файла файла со станков
        if file_name not in spisok:
            if '$2' not in file_name:
                file_name_2='$2$'+file_name
                if os.path.exists(os.path.join(path_folder,file_name_2)):
                    first_file=open(os.path.join(path_folder,file_name),'r')
                    second_file=open(os.path.join(path_folder,file_name_2),'r')
                    common_file=open(os.path.join(set.PATH_FOR_CHECK,machine,file_name),'w')
                    a='\n$1\n'
                    for line in first_file:
                        if '%' not in line:
                            a=a+line
                    common_file.write(a)
                    a='$2\n'
                    for line in second_file:
                        if '%' not in line:
                            a=a+line
                        else:
                            a=a+'%'
                    common_file.write(a)
                    first_file.close()
                    second_file.close()
                    common_file.close()
                    logger.info(f'Join {file_name}')
        else:
            logger.info(f'{file_name} in spisok')



def trans_other_macine(path_for_check_join,machine):
    if os.path.isdir(os.path.join(set.PATH_FOR_CHECK,machine))== False:
        os.makedirs(os.path.join(set.PATH_FOR_CHECK,machine))
    path_folder = os.path.join(path_for_check_join, machine)
    spisok = []
    if os.path.isfile(os.path.join(path_for_check_join,machine+'-ignor.txt')):
        with open(os.path.join(path_for_check_join,machine+'-ignor.txt'),'r') as f:
            spisok=list(f.read().split(' '))
    for file in serch_in_check_nomura(path_folder):  # ищем файл в папке  со станков
        file_name = file.split('\\')[-1]  # имя файла файла со станков

        if file_name not in spisok:
            shutil.copy(file,os.path.join(set.PATH_FOR_CHECK,machine,file_name))  # клонируем папки в папку для разбора
        else:
            logger.info(f'{file_name} in spisok')



# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    pass


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
