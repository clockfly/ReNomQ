# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def cs(self, q_num1, q_num2):
    """ Apply cs gate to quantum register.

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
        >>> qc.cs(q[0], q[1])
    """
    name1, origin_num1 = q_num1
    name1, num1 = self.convert_q_number(q_num1)
    name2, origin_num2 = q_num2
    name2, num2 = self.convert_q_number(q_num2)
    sgate = np.array([[1., 0.], [0., 1.0j]])
    gate = self.gate_base2(sgate, num1, num2, 'cS')
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
            self.matrixlist.append('\n---------------- cs(' + name1 + '[' + str(origin_num1) +
                                   '], ' + name2 + '[' + str(origin_num2) + ']) ----------------\n'
                                   + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                                   ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))

    return self
