# -*- coding: utf-8 -*-
import json,os
import time
import logging.config
from settings import logger_config
import get_settings as set
from To_UP import serch_in_check,find_name_prog

logging.config.dictConfig(logger_config)
logger = logging.getLogger('json_logger')
# logger.addFilter(settings.CustomFilter())

# -----------------------------------------------------------------------
def chek_json(path_for_base):
    time_start = time.localtime()
    counter_start = time.perf_counter()
    logger.info( f'Проверка JSON файла начата в {time.strftime("%H:%M:%S", time_start)}\n')
    logger.info(f'****************************')
    if os.path.isfile(r"c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\guide.json")==False:
        with open(r"c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\guide.json",'w') as f:
            f.write(r'{ }')
    for file in serch_in_check(path_for_base):  #ищем файл в папке  со станков
        file_name_new = file.split('\\')[-1]  # имя файла файла со станков
        # print(file_name_new)
        dir_file = '\\'.join(file.split('\\')[:10])  # путь до папки в БД УП
        # print(dir_file)

        a = [file.endswith(a) for a in
             ['jpg', 'pdf', 'bin', 'PDF', 'doc', 'zip', 'lnk', 'exe', 'db', 'docx', 'png', 'bmp', 'ICO', 'bat', '0L',
              '0C', 'gif', 'GIF','bmp','vbs','css','dtd','htm','htm','pptx','iso','sfv','prt','x_b','STEP','ipt','cdd','djvu',
              '__meta__','xlsx','PNG','tcl','dll','frw','bak','out','cdw','log','m3d','tif','rar','xls','spw','JPG']]
        if any(a) != True:
            name_prog = find_name_prog(file)  # парсер названия
            jsonFile = open("guide.json", "r", encoding="utf-8")  # Open the JSON file for reading
            data = json.load(jsonFile)  # Read the JSON into the buffer
            jsonFile.close()  # Close the JSON file

            if name_prog not in data:
                data[name_prog] = dir_file
                logger.info(f'{data[name_prog]}')
            else:
                continue
            ## Save our changes to JSON file
            jsonFile = open("guide.json", "w+", encoding="utf-8")
            jsonFile.write(json.dumps(data,indent=4,ensure_ascii=True))
            jsonFile.close()
        else:
            pass

    time_finish = time.localtime()
    counter_end = time.perf_counter()
    logger.info(  f'Проверка JSON файла закончена в {time.strftime("%H:%M:%S", time_finish)}\n ' \
                  f'Время проверки {time.strftime("%H:%M:%S", time.gmtime(counter_end - counter_start))} \n' )
    logger.info(f'****************************')

def main():
    pass


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()