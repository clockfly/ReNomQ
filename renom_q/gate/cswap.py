# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def cswap(self, q_ctl, q_num1, q_num2):
    """ Apply cswap gate to quantum register.

    Args:
        q_ctl (tuple):
            A tuple of a quantum register and its index (ex:q[0]). It's the
            control qubit.
        q_num1 (tuple):
            A tuple of a quantum register and its index (ex:q[0]). It's the
            exchanging qubit.
        q_num2 (tuple):
            A tuple of a quantum register and its index (ex:q[0]). It's the
            exchanging qubit.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(3)
        >>> c = renom_q.ClassicalRegister(3)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.cswap(q[0], q[1], q[2])
    """
    name_ctl, origin_ctl = q_ctl
    name_ctl, ctl = self.convert_q_number(q_ctl)
    name1, origin_num1 = q_num1
    name1, num1 = self.convert_q_number(q_num1)
    name2, origin_num2 = q_num2
    name2, num2 = self.convert_q_number(q_num2)
    gate = np.zeros((self.Qr.q_states, self.Qr.q_states), dtype=complex)
    for i in range(self.Qr.q_states):
        bit_c = int(int(format(i, 'b')) / 10**(self.Qr.num - ctl - 1) % 2)
        if bit_c == 1:
            bit_1 = int(int(format(i, 'b')) / 10**(self.Qr.num - num1 - 1) % 2)
            bit_2 = int(int(format(i, 'b')) / 10**(self.Qr.num - num2 - 1) % 2)
            if bit_1 == bit_2:
                gate[i, i] = 1.
            else:
                bit_list = list(format(i, '0' + str(self.Qr.num) + 'b'))
                bit_list[num1] = str(bit_2)
                bit_list[num2] = str(bit_1)
                idx = int("".join(bit_list), 2)
                gate[i, idx] = 1.
        else:
            gate[i, i] = 1.
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- cswap(' + name_ctl + '[' + str(origin_ctl)
                               + '], ' + name1 +
                               '[' + str(origin_num1) + '], ' + name2 +
                               '[' + str(origin_num2) + ']) ----------------\n'
                               + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))
        tensor = '\n---------------- cSWAP ----------------\n' + str(gate)
        self.tensorlist.append(tensor)

    if self.qasm_bool:
        self.qasmlist.append('cswap ' + name_ctl + '[' + str(origin_ctl) + '], '
                             + name1 + '[' + str(origin_num1) + '], ' + name2 + '[' + str(origin_num2) + '];')

    return self
