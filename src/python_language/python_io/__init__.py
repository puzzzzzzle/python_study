import time
import logging
import src as project

logging.info(
    f">>> import {__file__} at time {time.asctime(time.localtime(time.time()))} for project pos {project.projectDir}")
