import consts
import os
import mmap
import pathlib
import logging
import random

__byteorder = "little"
__singed = True


def write_data(data, byte_len, val):
    data.write(val.to_bytes(byte_len, byteorder=__byteorder, signed=__singed))


def read_data(data, byte_len):
    return int.from_bytes(data.read(byte_len), byteorder=__byteorder, signed=__singed)


def write_int(data, val):
    write_data(data, 4, val)


def write_byte(data, val):
    write_data(data, 1, val)


def read_int(data):
    return read_data(data, 4)


def read_byte(data):
    return read_data(data, 1)


def truck_file_size(file_name, size):
    with open(file_name, "wb") as f:
        f.truncate()
        f.seek(size - 1)
        f.write(b"\x00")


def mmap_file(file_name):
    assert os.path.exists(file_name)
    size = os.path.getsize(file_name)
    fd = os.open(file_name, os.O_RDWR)
    return mmap.mmap(fd, size, access=mmap.ACCESS_WRITE)


def clear_bytes(file_name, x_len, ylen, gap):
    logging.info(f"write file name {file_name}")
    truck_file_size(file_name, x_len * ylen + 12)
    with mmap_file(file_name) as data:
        assert data is not None
        write_int(data, x_len)
        write_int(data, ylen)
        write_int(data, gap)


class BinHolder(object):
    def __init__(self):
        self.x_len = 0
        self.y_len = 0
        self.gap = 0
        self.data = []

    def dump(self, path_name):
        clear_bytes(path_name, self.x_len, self.y_len, self.gap)
        with mmap_file(path_name) as data:
            write_int(data, self.x_len)
            write_int(data, self.y_len)
            write_int(data, self.gap)
            for x in range(self.x_len):
                for y in range(self.y_len):
                    write_byte(data, self.data[x][y])

    def load(self, path_name):
        with mmap_file(path_name) as data:
            self.x_len = read_int(data)
            self.y_len = read_int(data)
            self.gap = read_int(data)
            assert data.size() == self.x_len * self.y_len + 4*3
            self.data = []
            for x in range(self.x_len):
                self.data.append([])
                for y in range(self.y_len):
                    self.data[x].append(read_byte(data))

    def clear(self, x_len, y_len, gap):
        self.x_len = x_len
        self.y_len = y_len
        self.gap = gap
        self.data = []

    def __str__(self):
        return f"head:x{self.x_len},y:{self.y_len},gap:{self.gap},data:{self.data}"

    def rand_data(self):
        for x in range(self.x_len):
            self.data.append([])
            for y in range(self.y_len):
                self.data[x].append(random.randrange(0, 127))


if __name__ == '__main__':
    file_name = str(pathlib.Path(consts.projectDir) / "data" / "basic.bin")
    bin_file = BinHolder()
    bin_file.clear(15, 10, 2)
    bin_file.rand_data()
    logging.info(bin_file)
    bin_file.dump(file_name)
    load_file = BinHolder()
    load_file.load(file_name)
    logging.info(f"after load: {load_file}")
