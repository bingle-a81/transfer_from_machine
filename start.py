# -*- coding: utf-8 -*-
import os, shutil, time, io
import logging.config
from settings import logger_config
import get_settings





#
def main():
    logging.config.dictConfig(logger_config)
    logger = logging.getLogger('app_logger')


    # logger_email = logging.getLogger('email_logger')
    counter_start1 = time.perf_counter()
    logger.error("Start ")

    logger.info("End")
    # logger_email.info('start')


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
