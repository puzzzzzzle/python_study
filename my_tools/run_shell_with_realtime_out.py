import subprocess
import os
from functools import partial
import logging
import platform

import select

logger = logging.getLogger(__name__)


def _print_out_put(outs: list, output):
    if output is None:
        return
    try:
        # 尝试使用 UTF-8 解码
        decoded_output = output.decode('utf-8').strip()
    except UnicodeDecodeError as e_utf8:
        try:
            # 如果 UTF-8 解码失败，尝试使用 GBK 解码
            decoded_output = output.decode('gbk').strip()
        except UnicodeDecodeError as e_gbk:
            # 如果 GBK 解码也失败，记录错误信息
            error_message = f"decode error: UTF-8: {e_utf8}, GBK: {e_gbk}"
            print(error_message)
            outs.append(error_message)
            return
    print(decoded_output)
    outs.append(decoded_output)


def print_out_put(outs: list, output):
    try:
        _print_out_put(outs, output)
    except Exception as e:
        logger.error(f"print out fail, ignore")


def _read_realtime_out_unix(process):
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
    return outs


def _read_output_windows(pipe, print_out, lock):
    """
    windows 没有非阻塞的读取函数, 只能用线程模拟
    """
    while True:
        line = pipe.readline()
        if not line:
            break
        # 多个线程竞争一个outs和输出机会, 改为加锁串行
        with lock:
            print_out(line)


def _read_real_time_out_windows(process):
    import threading

    outs = []
    lock = threading.Lock()
    print_out = partial(print_out_put, outs)

    # 创建线程分别读取标准输出和标准错误输出
    stdout_thread = threading.Thread(target=_read_output_windows, args=(process.stdout, print_out, lock))
    stderr_thread = threading.Thread(target=_read_output_windows, args=(process.stderr, print_out, lock))

    # 启动线程
    stdout_thread.start()
    stderr_thread.start()

    # 等待线程结束
    stdout_thread.join()
    stderr_thread.join()

    return outs


def read_real_time_out(process):
    if platform.system().lower() == 'windows':
        return _read_real_time_out_windows(process)
    else:
        return _read_realtime_out_unix(process)


def run_shell_command(command, env_vars=None, cwd=None):
    logging.debug(f"will run : {command} ; env : {env_vars} at {cwd}")

    # 获取当前环境变量
    env = os.environ.copy()

    # 更新环境变量
    if env_vars:
        env.update(env_vars)

    # 启动子进程
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=cwd)
    # 获取实时输出
    outs = read_real_time_out(process)
    # 确保子进程资源被正确释放
    process.wait()

    # 获取错误码
    return_code = process.returncode
    logging.info(f"run end with ret code {return_code}")
    if return_code != 0:
        raise RuntimeError(f"shell run fail with exit code {return_code}")
    return outs
