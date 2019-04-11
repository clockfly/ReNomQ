# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def u1(self, lam, q_num):
    """ Apply u1 gate to quantum register.

    Args:
        lam (float):
            The paramater of unitary gate U1.
        q_num (tuple):
            A tuple of a quantum register and its index (ex:q[0]).

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.u1(math.pi, q[0])
    """
    name, origin_num = q_num
    name, num = self.convert_q_number(q_num)
    u1gate = np.array([[1., 0.], [0., np.exp(1.0j * lam)]])
    gate = self.gate_base1(u1gate, num, 'U1')
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- u1(' + str(lam) + ', ' + name + '[' + str(origin_num) + ']) ----------------\n'
                               + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))

    if self.qasm_bool: 
        self.qasmlist.append('u1(' + str(lam) + ') ' + name + '[' + str(origin_num) + '];')

    return self
