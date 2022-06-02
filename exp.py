#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from string import ascii_letters, digits
from pwn import *
from itertools import product

table = ascii_letters + digits


class Solve():
    def __init__(self):
        self.sh = remote('127.0.0.1', 12345)
        # self.sh = remote('121.36.197.254', 9999)

    def proof_of_work(self):
        # [+] sha256(XXXX+JaakUDSfxkW0xjzV) == 4dbfdc61cb88f5bd08d87493ac62e5ab174780f5f019051f91df8b3c36564ed0
        # [+] Plz tell me XXXX:
        proof = self.sh.recvuntil(b'[+] Plz tell me XXXX:')
        tail = proof[16:32].decode()
        _hash = proof[37:101].decode()
        for i in product(table, repeat=4):
            head = ''.join(i)
            print(head)
            t = hashlib.sha256((head + tail).encode()).hexdigest()
            if t == _hash:
                self.sh.sendline(head.encode())
                break

    def solve(self):
        self.proof_of_work()
        self.sh.recvline()
        flag = self.sh.recvline()[:-1].decode()
        print(flag)
        self.sh.close()


if __name__ == '__main__':
    solution = Solve()
    solution.solve()
