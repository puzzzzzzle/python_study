import copy
import random
import logging

import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def do_simulate(
        max_generations=10,
        max_born_num=5, is_one_priority=False, generation_info=None, ):
    logger.info(
        f"start max_generations: {max_generations} max_born_num: {max_born_num} is_one_priority: {is_one_priority}")
    if generation_info is None:
        generation_info = [(10000, 10000)]
    generation_info = copy.copy(generation_info)
    for pre_generation in range(max_generations):
        pre_info = generation_info[pre_generation]
        zero_num = 0
        one_num = 0
        for each_person in range(pre_info[0]):
            for each_chile in range(max_born_num):
                born = random.choice((0, 1))
                if born == 0:
                    zero_num += 1
                else:
                    one_num += 1

                if is_one_priority:
                    # 优先策略
                    if born == 1:
                        break
                else:
                    # 平均策略
                    pass
        generation_info.append((zero_num, one_num))
        logger.info(
            f"generation {pre_generation + 1} end, zero: {zero_num}, one: {one_num} zero/one: {zero_num / one_num}"
            f" total: {zero_num + one_num} total/pre_total: {(zero_num + one_num) / (pre_info[0] + pre_info[1])}")
    return generation_info


do_simulate(7, 5, False)
do_simulate(20, 5, True)
