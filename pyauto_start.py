# -*- coding: utf-8 -*-
import keyboard as keyb
from time import sleep
import pyautogui
import os
import subprocess
import psutil
import logging.config
from settings import logger_config
import get_settings as set
from ctypes import windll


logging.config.dictConfig(logger_config)
logger = logging.getLogger('pyautogui_logger')
err_logger=logging.getLogger('telega_logger')




def transfer_fanuc():
    sleep(0.5)
    pyautogui.leftClick(294, 461,duration=0.25)#первая программа
    keyb.press('shift')
    sleep(2)
    pyautogui.leftClick(295, 531,duration=0.25)#последняя программа
    keyb.release('shift')
    sleep(2)
    pyautogui.rightClick(295, 531,duration=0.25)#контекстн меню
    sleep(2)
    pyautogui.leftClick(354, 550,duration=0.25)#uploat
    sleep(2)
    pyautogui.leftClick(374, 654,duration=0.25)#yes to all
    sleep(5)
    if pyautogui.locateCenterOnScreen(r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\upload_prog_fanuc.png'):
        logger.info('Upload complite')
    else:
        logger.info('None')
    pyautogui.leftClick(936, 621,duration=0.25)# complite
    sleep(6)
    pyautogui.leftClick(1051, 593,duration=0.25)
    sleep(1)

def program_transfer_tool(a,dict1):
    # if a == 'nexturn26':
    #     dict1={'machine':(106, 464),'part1':(136, 588),'part2':(136, 603)}
    # elif a=='hanhwa':
    #     dict1 = {'machine': (106, 477), 'part1': (92, 510), 'part2': (92,528)}
    # elif a=='miano':
    #     dict1 = {'machine': (106, 495), 'part1': (92, 525), 'part2': (92, 540)}
    # elif a=='colchester':
    #     dict1 = {'machine': (106, 513), 'part1': (92, 541), 'part2': (92, 540)}
    # elif a=='nexturn12':
    #     dict1 = {'machine': (106, 549), 'part1': (92, 574), 'part2': (92, 591)}
    # else:
    #     return False

    picture = r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\fanuc_last_mod.png'
    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()
    sleep(4)
    os.startfile(r'C:\Program Files (x86)\FANUC\Program Transfer Tool\Bin\PttMain.exe')
    sleep(6)
    keyb.press_and_release('win + up')#full screen
    sleep(2)
    logger.info(f'Начало {a}')
    pyautogui.moveTo(dict1.get('machine'))
    pyautogui.leftClick(dict1.get('machine'),duration=0.25)#открываем next26
    sleep(2)
    pyautogui.moveTo(dict1.get('part1'))
    pyautogui.leftClick(dict1.get('part1'), duration=0.25)  # part1
    sleep(2)
    centr_picture(a, picture)
    # pyautogui.leftClick(1074, 447,duration=0.25)#последняя модификация
    # sleep(3)
    transfer_fanuc()
    if a!='colchester':
        pyautogui.moveTo(dict1.get('part2'))
        pyautogui.leftClick(dict1.get('part2'), duration=0.25)  # part2
        sleep(3)
        transfer_fanuc()
    # pyautogui.leftClick(dict1.get('k4'), duration=0.25)
    sleep(2)
    # pyautogui.leftClick(dict1.get('k5'), duration=0.25)
    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()
    sleep(3)
    return True


def sitizen(a,dict1):
    picture_link = r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture'
    # if a == 'sitizen-1':
    #     dict1 = {'machine': (1102, 351),
    #              'pic_machine_lst': (
    #                  (os.path.join(picture_link, 'citizen1.png'), os.path.join(picture_link, 'citizen12.png')))}
    # elif a == 'sitizen-2':
    #     dict1 = {'machine': (1137, 366),
    #              'pic_machine_lst': (
    #                  (os.path.join(picture_link, 'citizen2.png'), os.path.join(picture_link, 'citizen22.png')))}
    # else:
    #     return False

    for process in (process for process in psutil.process_iter() if process.name() == "FileControl.exe"):
        process.kill()
        sleep(4)

    os.startfile(r'C:\Program Files (x86)\FileControl\FileControl.exe')
    logger.info(f'Начало {a}')
    sleep(3)

    pyautogui.leftClick(1220, 340,duration=0.25)
    logger.debug('выбор машины')
    sleep(2)
    pyautogui.leftClick(dict1.get('machine'),duration=0.25)
    logger.debug(f'выбор станок {a}')
    sleep(2)
    pyautogui.leftClick(943, 338,duration=0.25)
    logger.debug('выбор папки на компе')
    sleep(2)
    for x in range(3):
        pyautogui.leftClick(1096, 599)
        logger.debug('клик вниз')
        sleep(1)
    pic_machine = next((item for item in list(
        map(lambda x: pyautogui.locateCenterOnScreen(x), dict1.get('pic_machine_lst'))) if item is not None), None)
    logger.debug(f'вывод = {pic_machine}')
    i=0
    while pic_machine==None:
        sleep(0.1)
        for x in  dict1.get('pic_machine_lst'):
            pic_machine=pyautogui.locateCenterOnScreen(x)
            if pic_machine!=None:
                break
            else:
                i += 1
                logger.debug(f'счетчик {i} pic2={pic_machine}')
        if i>10 :
            logger.debug(f'станок {a} не открывается')
            return
    pyautogui.moveTo(pic_machine)
    pyautogui.leftClick(pic_machine,duration=0.25)
    logger.debug(f'выбор папки {a}')
    pyautogui.leftClick(1002, 660,duration=0.25)
    logger.debug('кнопка ок')
    sleep(2)
    pyautogui.leftClick(717, 288,duration=0.25)
    logger.debug('edit')
    sleep(2)
    pyautogui.leftClick(767, 334,duration=0.25)
    logger.debug(f'select all on machine {a}')
    sleep(2)
    pyautogui.leftClick(999, 676,duration=0.25)
    logger.debug('transfer to pc')
    sleep(2)
    pyautogui.leftClick(1012, 572,duration=0.25)
    logger.debug('да')
    sleep(2)
    pyautogui.leftClick(927, 615,duration=0.25)
    logger.debug('хз')
    sleep(55)
    for process in (process for process in psutil.process_iter() if process.name() == "FileControl.exe"):
        process.kill()
    return True


def nomura(a,pic_machine_lst):
    picture_link=r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture'
    picture_lst=(os.path.join(picture_link, 'hat1.png'),os.path.join(picture_link, 'hat2.png'),os.path.join(picture_link, 'hat3.png'))

    # if a == 'nomura20-1':
    #     pic_machine_lst = (os.path.join(picture_link, 'nom1.png'), os.path.join(picture_link, 'nom11.png'))
    # elif a == 'nomura20-2':
    #     pic_machine_lst = (os.path.join(picture_link, 'nom2.png'), os.path.join(picture_link, 'nom22.png'))
    # elif a == 'nomura20-3':
    #     pic_machine_lst = (os.path.join(picture_link, 'nom3.png'), os.path.join(picture_link, 'nom33.png'))
    # elif a == 'nomura10':
    #     pic_machine_lst = (os.path.join(picture_link, 'nom10.png'), os.path.join(picture_link, 'nom110.png'))
    # else:
    #     return False

    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

    logger.info(f'Начало {a}')
    pyautogui.leftClick(1914, 1067,duration=0.25)
    logger.debug(f'свернуть все')
    pyautogui.moveTo(719, 974,duration=0.25)
    sleep(2)
    pyautogui.doubleClick(719, 974,button='LEFT',duration=0.25)
    logger.debug(f'открыть nc exploer')
    # pyautogui.doubleClick(button="LEFT")
    sleep(5)
    keyb.press_and_release('win + up')  # full screen
    logger.debug(f'full screen {a}')
    sleep(1)
    pic_machine = next((item for item in list(map(lambda x: pyautogui.locateCenterOnScreen(x),pic_machine_lst)) if item is not None), None)
    logger.debug(f'вывод = {pic_machine}')
    i=0
    while pic_machine==None:
        sleep(0.1)
        for x in  pic_machine_lst:
            pic_machine=pyautogui.locateCenterOnScreen(x)
            if pic_machine!=None:
                break
            else:
                i += 1
                logger.debug(f'счетчик {i} pic2={pic_machine}')
        if i>10 :
            logger.debug(f'станок {a} не открывается')
            return
    pyautogui.moveTo(pic_machine)
    pyautogui.doubleClick(pic_machine,button='LEFT',duration=0.25)
    # pyautogui.moveTo(x,y)
    # sleep(3)
    # pyautogui.doubleClick(x, y, button='LEFT',duration=0.25)#координаты папки
    sleep(1)
    for x in range(3):
        pyautogui.doubleClick(214, 126,button='LEFT',duration=0.25)
        sleep(1)
    pyautogui.moveTo(300,200,duration=0.25)
    # sleep(3)

    pict_hat = next((item for item in list(map(lambda x: pyautogui.locateCenterOnScreen(x), picture_lst)) if item is not None), None)
    logger.debug(f'шапка таблицы {pict_hat}')
    while pict_hat == None:
        sleep(0.1)
        for x in  picture_lst:
            pict_hat=pyautogui.locateCenterOnScreen(x)
            if pict_hat!=None:
                logger.debug(f'шапка таблицы найдена {pict_hat}')
                break
            else:
                i += 1
                logger.debug(f'поиск шапки {i}')
        if i > 3:
            logger.debug(f'шапка таблицы не найдена {pict_hat}')
            break
    i=0
    if pict_hat==None:
        logger.debug(f'выбор режима таблицы')
        sleep(1.5)
        pyautogui.moveTo(1856, 71, duration=0.25)
        pyautogui.leftClick(1856, 71, duration=0.25)
        pic_table=pyautogui.locateCenterOnScreen(r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\table.png')
        while pic_table==None:
            pic_table = pyautogui.locateCenterOnScreen(
                r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\table.png')
            i += 1
            if i > 5:
                logger.debug(f'выбор режима таблицы не открывается')
                return
        else:
            pyautogui.moveTo(pic_table, duration=0.25)
            pyautogui.leftClick(pic_table, duration=0.25)
            logger.debug(f'выбор режима таблицы готово')

        logger.debug(f'выбор шапки дата изменения таблицы')
        izm_table=pyautogui.locateCenterOnScreen(r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\izm_table.png')
        i=0
        while izm_table==None:
            izm_table = pyautogui.locateCenterOnScreen(
                r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\izm_table.png')
            i += 1
            if i > 5:
                logger.debug(f'не правильная шапка дата изменения таблицы - не найдено')
                break
        else:
            pyautogui.moveTo(izm_table, duration=0.25)
            pyautogui.leftClick(izm_table, duration=0.25)
            logger.debug(f'правильная шапка дата изменения таблицы готово')

        pict_hat = next(
            (item for item in list(map(lambda x: pyautogui.locateCenterOnScreen(x), picture_lst)) if item is not None),
            None)
        if pict_hat==None:
            logger.debug(f'шапка таблицы не найдена вторая проверка {pict_hat}')
            return
        else:
            logger.debug(f'шапка таблицы вторая проверка {pict_hat}')
    pyautogui.leftClick(214, 126,duration=0.25)  # первая программа
    sleep(1)
    keyb.press('shift')
    sleep(1)
    pyautogui.moveTo(228, 356,duration=0.25)
    pyautogui.leftClick(228, 356)  # последняя программа
    keyb.release('shift')
    sleep(1)
    keyb.press_and_release('ctrl + c')
    sleep(1)
    os.startfile(os.path.join(set.SOURCE,a))
    sleep(3)
    keyb.press_and_release('win + up')  # full screen
    sleep(3)
    keyb.press_and_release('ctrl + v')
    sleep(3)
    pyautogui.leftClick(760, 712,duration=0.25)
    sleep(1)
    pyautogui.leftClick(860, 462,duration=0.25)
    sleep(10)
    pyautogui.leftClick(1898, 5,duration=0.25)
    pyautogui.leftClick(1898, 5,duration=0.25)
    sleep(2)
    return True

# def check_folder(a, flag, i):
#     if os.listdir(os.path.join(set.SOURCE, a)) != []:
#         fl = False
#         logger.info(f'Конец {a}')
#     else:
#         fl = True
#         hh=3
#         logger.info(f'Программы не скинулись {a} осталось {hh - i} попытки')
#         if i == 3:
#             fl = False
#             logger.info(f'количество попыток закончилось {a}')
#     return fl

def centr_picture(a,path):
    w = pyautogui.locateCenterOnScreen(path)
    i=0
    while w == None:
        sleep(0.1)
        w = pyautogui.locateCenterOnScreen(path)
        i += 0.1
        print(i)
        if i > 2:
            logger.error(f'нет подключения к станку{a}')
            break
    pyautogui.moveTo(w)
    pyautogui.leftClick(w)

# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    pass


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
