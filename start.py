# -*- coding: utf-8 -*-
import os, shutil, time, io
import logging.config
from settings import logger_config
import get_settings as set
import pyauto_start
from make_json import chek_json
from join_and_transfert import common_files_nomura, trans_other_macine
from To_UP import start as copy_to_database


def trans_from_machine(machine):
    picture_link = r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture'
    if machine == 'nomura20-1':
        pic_machine_lst = (os.path.join(picture_link, 'nom1.png'), os.path.join(picture_link, 'nom11.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nomura20-2':
        pic_machine_lst = (os.path.join(picture_link, 'nom2.png'), os.path.join(picture_link, 'nom22.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nomura20-3':
        pic_machine_lst = (os.path.join(picture_link, 'nom3.png'), os.path.join(picture_link, 'nom33.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nomura20-4':
        pic_machine_lst = (os.path.join(picture_link, 'nom4.png'), os.path.join(picture_link, 'nom44.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nomura20-5':
        pic_machine_lst = (os.path.join(picture_link, 'nom5.png'), os.path.join(picture_link, 'nom55.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nomura10':
        pic_machine_lst = (os.path.join(picture_link, 'nom10.png'), os.path.join(picture_link, 'nom110.png'))
        pyauto_start.nomura(machine, pic_machine_lst)
    elif machine == 'nexturn26':
        dict1 = {'machine': (106, 464), 'part1': (136, 588), 'part2': (136, 603)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'hanhwa':
        dict1 = {'machine': (106, 477), 'part1': (92, 510), 'part2': (92, 528)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'miano':
        dict1 = {'machine': (106, 495), 'part1': (92, 525), 'part2': (92, 540)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'colchester':
        dict1 = {'machine': (106, 513), 'part1': (92, 541), 'part2': (92, 540)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'nexturn12-1':
        dict1 = {'machine': (106, 549), 'part1': (92, 574), 'part2': (92, 591)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'nexturn12-2':
        dict1 = {'machine': (101, 522), 'part1': (92, 558), 'part2': (92, 573)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'Tsugami-SS263':
        dict1 = {'machine': (101, 554), 'part1': (130, 700), 'part2': (130, 715)}
        pyauto_start.program_transfer_tool(machine, dict1)
    elif machine == 'sitizen-1':
        dict1 = {'machine': (1102, 351),
                 'pic_machine_lst': (
                     (os.path.join(picture_link, 'citizen1.png'), os.path.join(picture_link, 'citizen12.png')))}
        pyauto_start.sitizen(machine, dict1)
    elif machine == 'sitizen-2':
        dict1 = {'machine': (1137, 366),
                 'pic_machine_lst': (
                     (os.path.join(picture_link, 'citizen2.png'), os.path.join(picture_link, 'citizen22.png')))}
        pyauto_start.sitizen(machine, dict1)
    else:
        return


def update_folder(path, folder):
    aa = os.path.join(path, folder)
    if os.path.isdir(aa) == True:
        shutil.rmtree(aa, ignore_errors=True)
    os.makedirs(aa)


#
def main():

    logger5 = logging.getLogger('telega_logger')
    logger5.error('Start script')
    folders_machine_new_program = (
        'nomura20-1', 'nomura20-2', 'nomura20-3', 'nomura20-4','nomura20-5', 'nomura10', 'colchester', 'hanhwa', 'miano', 'nexturn12-1',
        'nexturn12-2','nexturn26','Tsugami-SS263','nomura16', 'sitizen-1', 'sitizen-2','NONE')

    logging.config.dictConfig(logger_config)
    logger = logging.getLogger('app_logger')

    counter_start1 = time.perf_counter()

    if os.path.isfile(set.LOG_FILE): os.remove(set.LOG_FILE)  # log файл
    if os.path.isfile(set.LOG_FILE_DEBUG): os.remove(set.LOG_FILE_DEBUG)  # log файл


    logger.info(f'Start Transfer_from_machine\n')
    counter_start2 = time.perf_counter()

    for machine in folders_machine_new_program:
        if (machine == 'nomura16') or (machine == 'NONE'):
            update_folder(set.PATH_FOR_CHECK, machine)
        else:
            update_folder(set.SOURCE, machine)
            update_folder(set.PATH_FOR_CHECK, machine)
    for machine in folders_machine_new_program:
        if (machine == 'nomura16') or (machine == 'NONE'):
            pass
        else:
            flag = True
            count_attempt = 0
            number_of_attempts = 3
            while flag:
                logger.info((f'Start {machine}\n'))
                trans_from_machine(machine)
                count_attempt += 1
                if os.listdir(os.path.join(set.SOURCE, machine)) != []:
                    flag = False
                    logger.info(f'Конец {machine}')
                else:
                    flag = True
                    logger.info(
                        f'Программы не скинулись {machine} осталось {number_of_attempts - count_attempt} попытки')
                    if count_attempt == number_of_attempts:
                        flag = False
                        logger.info(f'количество попыток закончилось {machine}')
            logger.info((f'End {machine}\n'))
    logger.info(f'End Transfer_from_machine \n')
    logger5.error(f'End Transfer_from_machine \n')

    logger.info(f'Start join nomura')
    for machine in folders_machine_new_program[:6]:
        logger.info(f'Start join {machine}')
        common_files_nomura(set.SOURCE, machine)
        logger.info(f'End join {machine}')
    logger.info(f'End join nomura')

    logger.info(f'Start other machine')
    for machine in folders_machine_new_program[6:]:
        logger.info(f'Start join {machine}')
        trans_other_macine(set.SOURCE, machine)
        logger.info(f'End join {machine}')

    if os.path.isfile(r"c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\guide.json"):
        if (time.time()) - os.path.getctime(r"c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\guide.json") > (
                60 * 60 * 24 * 3):
            os.remove(r"c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\guide.json")
            logger.info("Update file json")
            chek_json(set.PATH_FOR_BASE)
            logger.info("end json")
            logger5.error(f'End json \n')
        else:
            logger.info("json don't update")
    else:
        logger.info("Create file json")
        chek_json(set.PATH_FOR_BASE)
        logger.info("end json")
        logger5.error(f'End json \n')

    logger.info("Start copy to database ")
    for program in folders_machine_new_program:
        copy_to_database(program)
    logger.info("End copy to database")

    logger.info(f'Время проверки {time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - counter_start2))} \n')
    counter_end1 = time.perf_counter()
    # ----------отсылаем письмо------------------------------------
    logger.info(f'Время проверки {time.strftime("%H:%M:%S", time.gmtime(counter_end1 - counter_start1))} \n')
    logger5.error(
        f'Finish script\n Время проверки {time.strftime("%H:%M:%S", time.gmtime(counter_end1 - counter_start1))} \n')
    logger1 = logging.getLogger('email_logger')  # debag file в почту
    with open(set.LOG_FILE, 'r') as r:
        text = r.read()
    logger1.error(text)

    os.system('shutdown -r -t 100')


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
