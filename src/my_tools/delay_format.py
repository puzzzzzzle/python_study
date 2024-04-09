import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def delay_format(msg):
    def get_show_msg_str():
        return f" msg is {msg}"

    aaa = 42
    bbb = 33
    logger.debug(
        f">>> send {aaa} %s {bbb}",
        lambda: get_show_msg_str())


if __name__ == '__main__':
    delay_format("hello world")