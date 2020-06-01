import os
import time
import logging
from pathlib import Path

__all__ = [""]

sourceDir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
projectDir = os.path.abspath(Path(sourceDir) / "..")


def __init_logger():
    """
    初始化日志系统
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel("DEBUG")
    basic_format = "[%(asctime)s]\t[%(levelname)s]\t%(message)s\t[\"%(pathname)s:%(lineno)s\"]\t\
    [%(thread)d:%(threadName)s]"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(basic_format, date_format)
    # cli
    cli_log = logging.StreamHandler()
    cli_log.setFormatter(formatter)
    cli_log.setLevel("DEBUG")
    logger.addHandler(cli_log)
    # curr log file
    once_log = logging.FileHandler(str(Path(projectDir) / "logs/all.log"))
    once_log.setFormatter(formatter)
    logger.addHandler(once_log)
    # all log file
    all_log = logging.FileHandler(str(Path(projectDir) / "logs/curr.log"), "w")
    all_log.setFormatter(formatter)
    logger.addHandler(all_log)
    logging.info(f"log init at {time.asctime(time.localtime(time.time()))}")


__init_logger()

logging.info(f"project root dir is {projectDir}")
logging.info(f">>> import {__file__} at time {time.asctime(time.localtime(time.time()))}")
