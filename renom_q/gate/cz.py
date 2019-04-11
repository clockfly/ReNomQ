# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def cz(self, q_num1, q_num2):
    """ Apply cz gate to quantum register.

    Args:
        q_num1 (tuple):
            A tuple of a quantum register and its index (ex:q[0]). It's the
            control qubit.
        q_num2 (tuple):
            A tuple of a quantum register and its index (ex:q[0]). It's the
            target qubit.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(2)
        >>> c = renom_q.ClassicalRegister(2)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.cz(q[0], q[1])
    """
    name1, origin_num1 = q_num1
    name1, num1 = self.convert_q_number(q_num1)
    name2, origin_num2 = q_num2
    name2, num2 = self.convert_q_number(q_num2)
    zgate = np.array([[1., 0.], [0., -1.]])
    gate = self.gate_base2(zgate, num1, num2, 'cZ')
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- cz(' + name1 + '[' + str(origin_num1) +
                               '], ' + name2 + '[' + str(origin_num2) + ']) ----------------\n'
                               + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))

    if self.qasm_bool:           
        self.qasmlist.append('cz ' + name1 + '[' + str(origin_num1) + '], '
                             + name2 + '[' + str(origin_num2) + '];')

    return self
