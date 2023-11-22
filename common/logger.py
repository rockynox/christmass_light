import logging
import os
import sys


def setup_logger(level):
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    if os.uname().nodename == "lalapi":
        file_handler = logging.FileHandler("/home/pi/christmass_light/main.log", mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
