# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np

from renom_q.quantumcircuit import QuantumCircuit


def gate_base1(self, gate_matrix, num, gatemark):
    self.measure_bool = True
    mark = ''
    tensor = ''
    if num == 0 and self.Qr.num == 1:
        gate = gate_matrix
        if self.print_matrix_bool:
            mark = gatemark
            tensor += str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    elif num == 0 and self.Qr.num != 1:
        gate = np.kron(gate_matrix, self.idgate)
        if self.print_matrix_bool:
            mark += str(gatemark) + ' ⊗ I'
            tensor += str(gate_matrix) + ' ⊗ \n\n' + str(self.idgate)
        for i in range(self.Qr.num - num - 2):
            gate = np.kron(gate, self.idgate)
            if self.print_matrix_bool:
                mark += ' ⊗ I'
                tensor += ' ⊗ \n\n' + str(self.idgate)
        if self.print_matrix_bool:
            tensor += ' = \n\n' + str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    elif num == 1 and self.Qr.num == 2:
        gate = np.kron(self.idgate, gate_matrix)
        if self.print_matrix_bool:
            mark += 'I ⊗ ' + str(gatemark)
            tensor += str(self.idgate) + ' ⊗ \n\n' + str(gate_matrix) + ' = \n\n' + str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    elif num == 1 and self.Qr.num != 2:
        gate = np.kron(self.idgate, gate_matrix)
        if self.print_matrix_bool:
            mark += 'I ⊗ ' + str(gatemark)
            tensor += str(self.idgate) + ' ⊗ \n\n' + str(gate_matrix)
        for i in range(self.Qr.num - num - 1):
            gate = np.kron(gate, self.idgate)
            if self.print_matrix_bool:
                mark += ' ⊗ I'
                tensor += ' ⊗ \n\n' + str(self.idgate)
        if self.print_matrix_bool:
            tensor += ' = \n\n' + str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    elif num == self.Qr.num - 1:
        gate = np.kron(self.idgate, self.idgate)
        if self.print_matrix_bool:
            mark += 'I ⊗ I'
            tensor += str(self.idgate) + ' ⊗ \n\n' + str(self.idgate)
        for i in range(num - 2):
            gate = np.kron(gate, self.idgate)
            if self.print_matrix_bool:
                mark += ' ⊗ I'
                tensor += ' ⊗ \n\n' + str(self.idgate)
        gate = np.kron(gate, gate_matrix)
        if self.print_matrix_bool:
            mark += ' ⊗ ' + str(gatemark)
            tensor += ' ⊗ \n\n' + str(gate_matrix) + ' = \n\n' + str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    else:
        gate = np.kron(self.idgate, self.idgate)
        if self.print_matrix_bool:
            mark += 'I ⊗ I'
            tensor += str(self.idgate) + ' ⊗ \n\n' + str(self.idgate)
        for i in range(num - 2):
            gate = np.kron(gate, self.idgate)
            if self.print_matrix_bool:
                mark += ' ⊗ I'
                tensor += ' ⊗ \n\n' + str(self.idgate)
        gate = np.kron(gate, gate_matrix)
        if self.print_matrix_bool:
            mark += ' ⊗ ' + str(gatemark)
            tensor += ' ⊗ \n\n' + str(gate_matrix)
        for i in range(self.Qr.num - num - 1):
            gate = np.kron(gate, self.idgate)
            if self.print_matrix_bool:
                mark += ' ⊗ I'
                tensor += ' ⊗ \n\n' + str(self.idgate)
        if self.print_matrix_bool:
            tensor += ' = \n\n' + str(gate)
            tensor = '\n---------------- ' + mark + ' ----------------\n' + tensor
            self.tensorlist.append(tensor)

    return gate
