import inspect
import time
import logging
import types

logging.basicConfig(level=logging.DEBUG)


### mock c++ impl
class NetMock:
    def __init__(self):
        self.wait_recv = {}
        self.on_receive = None
        pass

    def set_on_receive(self, on_receive):
        self.on_receive = on_receive

    def send_tcp_package(self, seq, req, target):
        if seq in self.wait_recv:
            raise RuntimeError("send fail")
        self.wait_recv[seq] = (time.time(), req)
        # mock send to net ...
        logging.info(f"send seq({seq}); {req} -> {target}")

    def on_recv(self, seq, rsp):
        self.on_receive(seq, rsp)

    def one_loop(self):
        # mock recv from net ...
        still_wait = self.wait_recv
        self.wait_recv = {}
        for seq, v in still_wait.items():
            if time.time() - v[0] > 1:
                self.on_recv(seq, f"recv req from {v[1]}")
            else:
                self.wait_recv[seq] = v


### mock c++ impl end


net = NetMock()


class Task:
    def __init__(self, coro):
        self.coro = coro  # 协程对象
        self.step()  # 开始执行协程

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self.coro.throw(exc)
            else:
                fut = self.coro.send(value)
            fut.set_callback(self.step)
        except StopIteration as e:
            # 协程完成
            logging.info(f"task finished with : {e.value}")
            return e.value


class NetRpcCall:
    def __init__(self, seq, req, target):
        self.seq = seq
        self.req = req
        self.target = target

        self.result = None

        self._callbacks = []

    def set_result(self, result):
        self.result = result
        for callback in self._callbacks:
            callback(self)

    def set_callback(self, callback):
        self._callbacks.append(callback)

    def __await__(self):
        net.send_tcp_package(self.seq, self.req, self.target)
        logging.debug(f"co switch out")
        yield self
        logging.debug(f"co switch in")
        return self.result


class EventLoop:
    def __init__(self):
        self.seq = 1
        self.wait_rsp = {}

    def inc_seq(self):
        self.seq += 1
        return self.seq

    def create_rpc(self, req, target):
        seq = self.inc_seq()
        rpc = NetRpcCall(seq, req, target)
        self.wait_rsp[seq] = rpc
        return rpc

    def on_net_call_back(self, seq, rsp):
        if seq not in self.wait_rsp:
            return
        rpc: NetRpcCall = self.wait_rsp[seq]
        del self.wait_rsp[seq]
        rpc.set_result(rsp)
        pass


loop = EventLoop()
net.set_on_receive(loop.on_net_call_back)


async def rpc_a_service(req):
    logging.debug(f"req a server")
    rsp = await loop.create_rpc(req, "net::a_server")
    logging.info(f"rpc end {req} -> {rsp}")
    return rsp


async def rpc_b_service(req):
    logging.debug(f"req b server")
    rsp = await loop.create_rpc(req, "net::b_server")
    logging.info(f"rpc end {req} -> {rsp}")
    return rsp


async def direct_get_data(req):
    logging.debug(f"req direct data")
    return f"direct get data {req}"


async def business_1(req: str) -> str:
    a_data = await rpc_a_service("query a server")
    b_data = await rpc_b_service("query b server")
    direct_data = await direct_get_data("query direct get data")
    return f"business_1 ret : {a_data, b_data, direct_data}"


async def business_2(req):
    a_data = await rpc_a_service("query a server")
    b_data = await rpc_b_service("query b server")
    return f"business_1 ret : {a_data, b_data}"


def get_function_signature(func):
    # 获取函数的签名
    sig = inspect.signature(func)

    # 获取函数的参数类型
    params = sig.parameters
    param_types = {name: (param.annotation if param.annotation != inspect._empty else None) for name, param in
                   params.items()}

    # 获取函数的返回值类型
    return_type = sig.return_annotation if sig.return_annotation != inspect._empty else None

    return param_types, return_type


if __name__ == '__main__':
    ret = get_function_signature(business_2)
    business = business_1("bussiness 1")
    # 启动一个task
    # 理论上不需要保存task, 没有协程时直接运行结束
    # 有协程时, 由于task的step函数, 被协程对象记录, task本身也不会被回收
    Task(business)
    # 模拟网络驱动
    for i in range(20):
        time.sleep(0.5)
        net.one_loop()

    pass
