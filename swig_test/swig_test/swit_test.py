import consts

import logging

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info("start")
    import cpp.template.word.word as cpp_word
    p = cpp_word.word("cpp test")
    # p = cpp_word("hello cpp")
    logger.info(f"from cpp {p.getWord()}")


    # import cpp_code.cpp_gen.word_1.word_1 as cpp_word_1
    # word_1 = cpp_word("hello cpp 1")
    # logger.info(f"from cpp {word_1.getWord()}")
