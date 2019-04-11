# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def gate_base2(self, gate_matrix, ctl, tgt, gatemark):
    self.measure_bool = True
    gate = np.zeros((self.Qr.q_states, self.Qr.q_states), dtype=complex)
    for i in range(self.Qr.q_states):
        bit_c = int(int(format(i, 'b')) / 10**(self.Qr.num - ctl - 1) % 2)
        if bit_c == 1:
            bit_t = int(int(format(i, 'b')) / 10**(self.Qr.num - tgt - 1) % 2)
            bit_list = list(format(i, '0' + str(self.Qr.num) + 'b'))
            bit_list[tgt] = '1' if bit_t == 0 else '0'
            idx = int("".join(bit_list), 2)
            if i < idx:
                gate[i, i] = gate_matrix[bit_t, 0]
                gate[i, idx] = gate_matrix[bit_t, 1]
            else:
                gate[i, i] = gate_matrix[bit_t, 1]
                gate[i, idx] = gate_matrix[bit_t, 0]
        else:
            gate[i, i] = 1.
    if self.print_matrix_bool:
        tensor = '\n---------------- ' + gatemark + ' ----------------\n' + str(gate)
        self.tensorlist.append(tensor)

    return gate
