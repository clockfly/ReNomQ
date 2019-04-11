# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def reset(self):
    """ Apply reset gate to quantum register.

    Thie gate is available only when resetting all quantum register.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.reset()
    """
    qubit = self.Qr.qubit
    self.Qr.qubit = np.array([complex(0.) for i in range(self.Qr.q_states)])
    self.Qr.qubit[0] = 1.
    if self.print_matrix_bool:
        self.matrixlist.append('\n---------------- reset() ----------------\n'
                               + str(np.array(qubit).reshape(self.Qr.q_states, 1)) +
                               ' → \n\n' +
                               str(np.array(self.Qr.qubit).reshape(self.Qr.q_states, 1)))
    for qc in range(len(self.Qr.numlist)):
        q_name = [k for k, v in self.Qr.dict.items() if v == qc][0]
        val = self.Qr.dict[q_name]
        if self.qasm_bool:
            for i in range(self.Qr.numlist[val]):
                self.qasmlist.append('reset ' + q_name + '[' + str(i) + '];')

    return self
