# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def cu1(self, lam, q_num1, q_num2):
    """ Apply cu1 gate to quantum register.

    Args:
        lam (float):
            The paramater of unitary gate cU1.
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
        >>> qc.cu1(math.pi, q[0], q[1])
    """
    name1, origin_num1 = q_num1
    name1, num1 = self.convert_q_number(q_num1)
    name2, origin_num2 = q_num2
    name2, num2 = self.convert_q_number(q_num2)
    u1gate = np.array([[1., 0.], [0., np.exp(1.0j * lam)]])
    gate = self.gate_base2(u1gate, num1, num2, 'cU1')
    qubit = self.Qr.qubit
    self.Qr.qubit = np.dot(gate, self.Qr.qubit)

    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- cu1(' + str(lam) + ', ' + name1 + '['
                               + str(origin_num1) + '], ' + name2 +
                               '[' + str(origin_num2) + ']) ----------------\n'
                               + str(gate) + '・\n\n' + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' = \n\n' + str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))

    if self.qasm_bool:
        self.qasmlist.append('cu1(' + str(lam) + ') ' + name1 + '[' + str(origin_num1) + '], '
                             + name2 + '[' + str(origin_num2) + '];')
                             
    return self
