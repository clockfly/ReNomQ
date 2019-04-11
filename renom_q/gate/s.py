# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def s(self, q_num):
    """ Apply s gate to quantum register.

    Args:
        q_num (tuple):
            A tuple of a quantum register and its index (ex:q[0]).

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.s(q[0])
    """
    name, origin_num = q_num
    name, num = self.convert_q_number(q_num)
    sgate = np.array([[1., 0.], [0., 1.0j]])
    gate = self.gate_base1(sgate, num, 'S')
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- s(' + name + '[' + str(origin_num) + ']) ----------------\n'
                               + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))

    if self.qasm_bool:                       
        self.qasmlist.append('s ' + name + '[' + str(origin_num) + '];')

    return self
