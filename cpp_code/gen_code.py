# -*- coding: utf-8 -*-
import os
import sys
import pathlib
if __name__ == '__main__':
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.curdir))
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    os.chdir(base_dir)
    target = sys.argv[1]
    target_dir = str(pathlib.Path(f"{base_dir}/cpp_gen/{target}"))
    print(f"process target {target} {target_dir}")
    try:
        os.mkdir(target_dir)
    except Exception as e:
        print(e)
    cmd_str = f'swig -o cpp_gen/{target}/{target}_warpper.cxx -outdir cpp_gen/{target} -c++ -python -py3 cpps/{target}/{target}.i'
    print(cmd_str)
    # os.system(cmd_str)
    print("end")
