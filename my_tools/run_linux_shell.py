import subprocess
import os
from functools import partial
import logging
import select

logger = logging.getLogger(__name__)


def print_out_put(outs: list, output):
    if output is None:
        return
    try:
        decoded_output = output.decode('utf-8').strip()
        print(decoded_output)
        outs.append(decoded_output)
    except Exception as e:
        logging.error(f"decode error {e}")
        outs.append(f"decode error {e}")


def run_shell_command(command, env_vars=None, cwd=None):
    """
    运行一段shell, 并实时获取输出
    """
    logging.debug(f"will run : {command} ; env : {env_vars}")

    # 获取当前环境变量
    env = os.environ.copy()

    # 更新环境变量
    if env_vars:
        env.update(env_vars)

    # 启动子进程
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=cwd)
    outs = []
    print_out = partial(print_out_put, outs)
    # 实时读取输出
    while True:
        reads = [process.stdout.fileno(), process.stderr.fileno()]
        ret = select.select(reads, [], [])

        for fd in ret[0]:
            if fd == process.stdout.fileno():
                output = process.stdout.readline()
                print_out(output)
            if fd == process.stderr.fileno():
                error_output = process.stderr.readline()
                print_out(error_output)

        if process.poll() is not None:
            break

    # 确保子进程资源被正确释放
    process.wait()

    # 获取错误码
    return_code = process.returncode
    logging.info(f"run end with ret code {return_code}")
    if return_code != 0:
        raise RuntimeError(f"shell run fail with exit code {return_code}")
    return outs