# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np
import copy
from .quantumregister import QuantumRegister
from .classicalregister import ClassicalRegister



class QuantumCircuit:
    """ Definite a quantum circuit.

    Args:
        *args (renom_q.QuantumRegister and renom_q.ClassicalRegister):
            Quantum registers and classical registers that a quantum
            circuit consists of. In both registers, defining multiple
            registers is possible, but at least one register needed.
        circuit_number (int):
            The number used when conflating multiple quantum circuits. There
            is no need for the user to input.

    Example 1:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)

    Example 2:
        >>> import renom_q
        >>> qa = renom_q.QuantumRegister(1, 'qa')
        >>> qb = renom_q.QuantumRegister(1, 'qb')
        >>> ca = renom_q.ClassicalRegister(1, 'ca')
        >>> cb = renom_q.ClassicalRegister(1, 'cb')
        >>> qc = renom_q.QuantumCircuit(qa, ca, qb, cb)

    Example 3:
        >>> import renom_q
        >>> qa = renom_q.QuantumRegister(1, 'qa')
        >>> qb = renom_q.QuantumRegister(1, 'qb')
        >>> ca = renom_q.ClassicalRegister(1, 'ca')
        >>> cb = renom_q.ClassicalRegister(1, 'cb')
        >>> qca = renom_q.QuantumCircuit(qa, ca)
        >>> qcb = renom_q.QuantumCircuit(qb, cb)
        >>> qc = qca + qcb
    """

    def __init__(self, *args, set_qasm=False, set_print_matrix=False, circuit_number=0):
        qr = []
        cr = []
        for i in range(len(args)):
            if type(args[i]) is QuantumRegister:
                qr.append(args[i])
            elif type(args[i]) is ClassicalRegister:
                cr.append(args[i])

        if len(qr) == 1:
            self.Qr = copy.deepcopy(qr[0])
        else:
            try:
                q_num = qr[0].num
                q_numlist = qr[0].numlist
                q_dict = qr[0].dict
                q_qasmcode = qr[0].qasmcode
                for i in range(1, len(qr)):
                    q_num += qr[i].num
                    q_numlist.extend(qr[i].numlist)
                    assert qr[i].name not in q_dict, qr[i].name + \
                        " is already used. Please use a different name."
                    q_dict.update([(qr[i].name, i)])
                    q_qasmcode += qr[i].qasmcode
                Q = QuantumRegister(q_num)
                Q.numlist = q_numlist
                Q.dict = q_dict
                Q.qasmcode = q_qasmcode
                self.Qr = copy.deepcopy(Q)
            except AssertionError as e:
                raise

        if len(cr) == 1:
            self.Cr = copy.deepcopy(cr[0])
        else:
            try:
                c_num = cr[0].num
                c_numlist = cr[0].numlist
                c_dict = cr[0].dict
                c_qasmcode = cr[0].qasmcode
                for i in range(1, len(cr)):
                    c_num += cr[i].num
                    c_numlist.extend(cr[i].numlist)
                    assert cr[i].name not in c_dict, cr[i].name + \
                        " is already used. Please use a different name."
                    c_dict.update([(cr[i].name, i)])
                    c_qasmcode += cr[i].qasmcode
                C = ClassicalRegister(c_num)
                C.numlist = c_numlist
                C.dict = c_dict
                C.qasmcode = c_qasmcode
                self.Cr = copy.deepcopy(C)
            except AssertionError as e:
                raise

        self.qubit = self.Qr.qubit.copy()
        self.circuit_number = circuit_number
        self.Codelist = []
        self.matrixlist = []
        self.tensorlist = []
        self.qasmlist = [self.Qr.qasmcode, self.Cr.qasmcode]
        self.idgate = np.array([[1., 0.], [0., 1.]])
        self.statevector = []
        self.measure_bool = True
        self.print_matrix_bool = set_print_matrix
        self.qasm_bool = set_qasm


    def __add__(self, other):
        try:
            q_num = self.Qr.num + other.Qr.num
            q_numlist = self.Qr.numlist
            q_numlist.extend(other.Qr.numlist)
            q_dict = self.Qr.dict
            assert other.Qr.name not in q_dict, other.Qr.name + \
                " is already used. Please use a different name."
            q_dict.update([(other.Qr.name, self.circuit_number + 1)])
            Q = QuantumRegister(q_num)
            Q.numlist = q_numlist
            Q.dict = q_dict
            Q.qasmcode = self.Qr.qasmcode + other.Qr.qasmcode

            c_dict = self.Cr.dict
            C = self.Cr
            if other.Cr.name not in c_dict:
                c_dict.update([(other.Cr.name, self.circuit_number + 1)])
                c_num = self.Cr.num + other.Cr.num
                c_numlist = self.Cr.numlist
                c_numlist.extend(other.Cr.numlist)
                C = ClassicalRegister(c_num)
                C.numlist = c_numlist
                C.dict = c_dict
                C.qasmcode = self.Cr.qasmcode + other.Cr.qasmcode

            return QuantumCircuit(Q, C, circuit_number=self.circuit_number + 1)
        except AssertionError as e:
            raise


    def qasm(self):
        """Print the qasm code of quantum circuit.

        Returns:
            qasm_string (str):
                A string of qasm code of quantum circuit.

        Example:
            >>> import renom_q
            >>> q = renom_q.QuantumRegister(1)
            >>> c = renom_q.ClassicalRegister(1)
            >>> qc = renom_q.QuantumCircuit(q, c, set_qasm=True)
            >>> qc.x(q[0])
            >>> qc.measure()
            >>> print(qc.qasm())
            OPENQASM 2.0;
            include "qelib1.inc";
            qreg q[1];
            creg c[1];
            x q[0];
            measure q[0] -> c[0];
        """
        qasm_string = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n'
        for i in self.qasmlist:
            qasm_string += str(i)+'\n'
        return qasm_string


    def measure_exec(self, statevector):
        qubit = statevector
        p = [i**2 for i in np.abs(qubit)]
        bit_list = list(format(np.random.choice(self.Qr.q_number, p=p),
                               '0' + str(self.Qr.num) + 'b'))
        return bit_list


    def convert_q_number(self, q_num):
        name, num = q_num
        val = self.Qr.dict[name]
        for i in range(val):
            num += self.Qr.numlist[i]
        return name, num


    def convert_c_number(self, c_num):
        name, num = c_num
        val = self.Cr.dict[name]
        for i in range(val):
            num += self.Cr.numlist[i]
        return name, num
