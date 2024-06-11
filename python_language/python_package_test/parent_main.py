import logging

import flask_test.python_language.python_package_test.l1_pack1 as l1

# l1.l2_pack1.l2_pack1_py1.show_name()

import flask_test.python_language.python_package_test.l1_pack1 .l1_pack1_py1 as l1py
from flask_test.python_language.python_package_test.l1_pack1 import *
from flask_test.python_language.python_package_test.l1_pack1.l2_pack1 import *
from flask_test.python_language.python_package_test.l1_pack1.l2_pack1.l3_pack1 import *

if __name__ == '__main__':
    logging.info(f"l1 name is {dir(l1)}")
    logging.info(f"l1 all is {l1.__all__}")
    l1py.show_name()
    l1_pack1_py1.show_name()
    l2_pack1_py1.show_name()
    l3_pack1_py1.show_name()
    pass
