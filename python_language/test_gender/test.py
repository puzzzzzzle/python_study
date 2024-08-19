import copy
import enum
import random
import logging

import numpy as np
from numpy.ma.extras import average

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Priority(enum.Enum):
    average = 0,
    one_priority = 1,
    one_priority_less_half = 2,


def do_simulate(
        max_generations=10,
        max_born_num=5, priority: Priority = Priority.average, generation_info=None, ):
    logger.info(
        f"start max_generations: {max_generations} max_born_num: {max_born_num} is_one_priority: {priority}")
    if generation_info is None:
        generation_info = [(10000, 10000)]
    generation_info = copy.copy(generation_info)
    half_born = max_born_num // 2
    for pre_generation in range(max_generations):
        pre_info = generation_info[pre_generation]
        zero_num = 0
        one_num = 0
        for each_person in range(pre_info[0]):
            for each_child in range(max_born_num):
                born = random.choice((0, 1))
                if born == 0:
                    zero_num += 1
                else:
                    one_num += 1
                if priority == Priority.average:
                    # 平均策略
                    pass
                elif priority == Priority.one_priority:
                    # 优先策略
                    if born == 1:
                        break
                elif priority == Priority.one_priority_less_half:
                    if born == 1 and each_child > half_born:
                        break
        generation_info.append((zero_num, one_num))
        logger.info(
            f"generation {pre_generation + 1} end, zero: {zero_num}, one: {one_num} zero/one: {zero_num / one_num}"
            f" total: {zero_num + one_num} total/pre_total: {(zero_num + one_num) / (pre_info[0] + pre_info[1])}")
    return generation_info


do_simulate(5, 8, Priority.average)
do_simulate(20, 8, Priority.one_priority)
do_simulate(20, 8, Priority.one_priority_less_half)
