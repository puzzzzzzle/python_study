import consts
import logging
import unittest

logger = logging.getLogger(__name__)


def foo():
    logger.info("starting...")
    begin = 1
    while begin < 10:
        begin += 1
        res = yield begin
        logger.info(f"res: {res}")


class SimpleTest(unittest.TestCase):
    def test(self):
        g = foo()

        # for i in g:
        #     logger.info(i)
        next(g)

        g.send(5)

        for i in g:
            logger.info(i)
        self.assertTrue(False)
