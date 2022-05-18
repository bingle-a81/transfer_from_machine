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

logging.config.dictConfig(logger_config)
logger = logging.getLogger('pyautogui_logger')
err_logger=logging.getLogger('telega_logger')


def transfer_fanuc():
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
    pyautogui.leftClick(936, 621,duration=0.25)# complite
    sleep(6)
    pyautogui.leftClick(1051, 593,duration=0.25)
    sleep(1)

def Program_Transfer_Tool():
    logger.info(f'Start fanuc')
    os.startfile(r'C:\Program Files (x86)\FANUC\Program Transfer Tool\Bin\PttMain.exe')
    sleep(3)
    keyb.press_and_release('win + up')#full screen
    sleep(2)
    a='nexturn26'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(106, 464,duration=0.25)#открываем next26
    sleep(2)
    pyautogui.leftClick(136, 588,duration=0.25)#part1
    sleep(2)
    pyautogui.leftClick(1074, 447,duration=0.25)#последняя модификация
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(136,603,duration=0.25) # part2
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(28, 463,duration=0.25)
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')
    #--------------------------------------
    a='hanhwa'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(106, 477) # hanhwa
    sleep(3)
    pyautogui.leftClick(92, 510) # part1
    sleep(2)
    transfer_fanuc()
    pyautogui.leftClick(92,528) # part2
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(28, 479)
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')
    #--------------------------------------
    a='miano'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(106, 495) # miano
    sleep(3)
    pyautogui.leftClick(92, 525) # part1
    sleep(2)
    transfer_fanuc()
    pyautogui.leftClick(92, 540) # part2
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(28, 496)
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')
    #--------------------------------------
    a='colchester'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(106, 513) # colchester
    sleep(3)
    pyautogui.leftClick(92, 541) # part1
    sleep(2)
    transfer_fanuc()
    pyautogui.leftClick(28, 514)
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')
    #--------------------------------------
    a='nexturn12'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(106, 549) # nexturn12
    sleep(3)
    pyautogui.leftClick(92, 574) # part1
    sleep(2)
    transfer_fanuc()
    pyautogui.leftClick(92, 591) # part2
    sleep(3)
    transfer_fanuc()
    pyautogui.leftClick(28, 545)
    sleep(3)
    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')

def sitizen():
    os.startfile(r'C:\Program Files (x86)\FileControl\FileControl.exe')
    a = 'sitizen-1'
    logger.debug(f'Начало {a}')
    sleep(3)
    pyautogui.leftClick(1220, 340)
    sleep(2)
    pyautogui.leftClick(1102, 351)
    sleep(2)
    pyautogui.leftClick(925, 345)
    sleep(2)
    pyautogui.leftClick(1015, 591)
    sleep(2)
    pyautogui.leftClick(1002, 660)
    sleep(2)
    pyautogui.leftClick(717, 288)
    sleep(2)
    pyautogui.leftClick(767, 334)
    sleep(2)
    pyautogui.leftClick(999, 676)
    sleep(2)
    pyautogui.leftClick(1012, 572)
    sleep(2)
    pyautogui.leftClick(927, 615)
    sleep(40)

    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')

    a='sitizen-2'
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(1220, 340)
    sleep(2)
    pyautogui.leftClick(1137, 366)
    sleep(2)
    pyautogui.leftClick(943, 338)
    sleep(2)
    pyautogui.leftClick(1096, 599)
    sleep(2)
    pyautogui.leftClick(1096, 599)
    sleep(2)
    pyautogui.leftClick(1023, 579)
    sleep(2)
    pyautogui.leftClick(717, 288)
    sleep(2)
    pyautogui.leftClick(767, 334)
    sleep(2)
    pyautogui.leftClick(999, 676)
    sleep(2)
    pyautogui.leftClick(1012, 572)
    sleep(2)
    pyautogui.leftClick(927, 615)
    sleep(40)
    for process in (process for process in psutil.process_iter() if process.name() == "FileControl.exe"):
        process.kill()
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')

def nomura(a):
    if a== 'nomura20-1':x,y=214, 126
    elif a=='nomura20-2':x,y=221, 155
    elif a=='nomura20-3':x,y=234, 174
    elif a=='nomura10':x,y=231, 197
    logger.debug(f'Начало {a}')
    pyautogui.leftClick(1914, 1067)
    pyautogui.doubleClick(719, 974,button='LEFT',duration=0.25)
    # pyautogui.doubleClick(button="LEFT")
    sleep(5)
    keyb.press_and_release('win + up')  # full screen
    sleep(3)
    pyautogui.doubleClick(x, y, button='LEFT',duration=0.25)#координаты папки
    sleep(1)
    for x in range(3):
        pyautogui.doubleClick(214, 126,button='LEFT',duration=0.25)
        sleep(1)
    pyautogui.moveTo(300,200,duration=0.25)
    sleep(10)
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
    sleep(20)
    pyautogui.leftClick(1898, 5,duration=0.25)
    pyautogui.leftClick(1898, 5,duration=0.25)
    sleep(10)
    if os.listdir(os.path.join(set.SOURCE,a))!=[]:
        logger.debug(f'Конец {a}')
    else:
        err_logger.error(f'Программы не скинулись {a}')


# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    pass
    # koordinati()
    # nomura(214, 126,r'C:\Users\Programmer\Desktop\pro\STANKI\nomura20-1')
    # nomura(221, 155, r'C:\Users\Programmer\Desktop\pro\STANKI\nomura20-2')
    # nomura(234, 174, r'C:\Users\Programmer\Desktop\pro\STANKI\nomura20-3')
    # nomura(231, 197, r'C:\Users\Programmer\Desktop\pro\STANKI\nomura10')
    # Program_Transfer_Tool()
    # sitizen()

# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
