# -*- coding: utf-8 -*-
import os, shutil, time, io
import logging.config
from settings import logger_config
import get_settings as set
import pyauto_start
from make_json import chek_json
from join_and_transfert import common_files_nomura,trans_other_macine
from To_UP import start as copy_to_database

def update_folder(path,folder):
    aa=os.path.join(path,folder)
    if os.path.isdir(aa)==True:
        shutil.rmtree(aa,ignore_errors=True)
    os.makedirs(aa)
#
def main():
    folders_machine_new_program = (
    'nomura20-1', 'nomura20-2', 'nomura20-3', 'nomura10', 'colchester', 'hanhwa', 'miano', 'nexturn12', 'nexturn26',
    'nomura16', 'sitizen-1', 'sitizen-2', 'NONE')
    logging.config.dictConfig(logger_config)
    logger = logging.getLogger('app_logger')
    counter_start1 = time.perf_counter()
    if os.path.isfile(set.LOG_FILE): os.remove(set.LOG_FILE)  # log файл

    logger.info(f'Start Transfer_from_machine\n')
    counter_start2 = time.perf_counter()

    for a in folders_machine_new_program:
        if (a!='nomura16') or (a!='NONE') :
            update_folder(set.SOURCE,a)
    for a in folders_machine_new_program:
        update_folder(set.PATH_FOR_CHECK,a)
    logger.info((f'Start nomura\n'))
    for a in folders_machine_new_program[:4]:
        pyauto_start.nomura(a)
    logger.info((f'End nomura\n'))
    logger.info((f'Start fanuc\n'))
    pyauto_start.Program_Transfer_Tool()
    logger.info((f'End fanuc\n'))
    logger.info((f'Start sitizen\n'))
    pyauto_start.sitizen()
    logger.info((f'End sitizen\n'))
    logger.info(f'End Transfer_from_machine \n')
    logger.info(f'Start join nomura')
    for a in folders_machine_new_program[:4]:
        logger.info(f'Start join {a}')
        common_files_nomura(set.SOURCE,a)
        logger.info(f'End join {a}')
    logger.info(f'End join nomura')
    logger.info(f'Start other machine')
    for a in folders_machine_new_program[4:]:
        logger.info(f'Start join {a}')
        trans_other_macine(set.SOURCE,a)
        logger.info(f'End join {a}')

    logger.info("Start json")
    chek_json(set.PATH_FOR_BASE)
    logger.info("end json")
    logger.info("Start copy to database ")
    for x in folders_machine_new_program:
        copy_to_database(x)
    logger.info("End copy to database")



    logger.info( f'Время проверки {time.strftime("%H:%M:%S", time.gmtime(time.perf_counter()- counter_start2))} \n')
    counter_end1 = time.perf_counter()
    # ----------отсылаем письмо------------------------------------
    logger.info( f'Время проверки {time.strftime("%H:%M:%S", time.gmtime(counter_end1 - counter_start1))} \n')

    logger1 = logging.getLogger('email_logger')#debag file в почту
    with open(set.LOG_FILE, 'r') as r:
        text = r.read()
    logger1.error(text)


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
