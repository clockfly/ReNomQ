# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)

from renom_q.quantumregister import QuantumRegister
from renom_q.classicalregister import ClassicalRegister
from renom_q.quantumcircuit import QuantumCircuit


def measure(self, *args):
    """ Measure the quantum state of the qubits.

    args:
        *args (renom_q.QuantumRegister and renom_q.ClassicalRegister, tuple and tuple or None):
            If arg type is tuple and tuple (ex: q[0], c[0]), measured a quantum
            register No.0 into a classical register No.0. If arg type is a
            renom_q.QuantumRegister and a renom_q.ClassicalRegister, measured
            all quantum registers in renom_q.QuantumRegister into all classical
            registers in renom_q.ClassicalRegister. If arg is None, measured
            all of multiple quantum registers into all classical registers
            in renom_q.ClassicalRegister. Only when definited single classical
            register, coding like example1 is possible.

    Example 1:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(2)
        >>> c = renom_q.ClassicalRegister(2)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.h(q[0])
        >>> qc.measure()

    Example 2:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(2)
        >>> c = renom_q.ClassicalRegister(2)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.h(q[0])
        >>> qc.measure(q, c)

    Example 3:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(2)
        >>> c = renom_q.ClassicalRegister(2)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.h(q[0])
        >>> for i in range(2):
        ...     qc.measure(q[i], c[i])
    """
    if self.measure_bool:
        self.statevector.append(self.Qr.qubit)
        idx = len(self.statevector) - 1
        self.Codelist.append('list=circuit.measure_exec(circuit.statevector[' + str(idx) + ']);\n')
        self.measure_bool = False

    if args == ():
        c_name = self.Cr.name
        for qc in range(len(self.Qr.numlist)):
            q_name = [k for k, v in self.Qr.dict.items() if v == qc][0]
            val = self.Qr.dict[q_name]
            for i in range(self.Qr.numlist[val]):
                q_name, calc_num1 = self.convert_q_number((q_name, i))
                self.Codelist.append(
                    'circuit.Cr.cbit[' + str(calc_num1) + '] = list[' + str(calc_num1) + '];\n')
                if self.qasm_bool:
                    self.qasmlist.append('measure ' + q_name + '[' + str(i) + '] -> '
                                         + c_name + '[' + str(calc_num1) + '];')

    elif type(args[0]) is QuantumRegister and type(args[1]) is ClassicalRegister:
        q_name = args[0].name
        c_name = args[1].name
        val = self.Qr.dict[q_name]
        for i in range(self.Qr.numlist[val]):
            q_name, calc_num1 = self.convert_q_number((q_name, i))
            c_name, calc_num2 = self.convert_c_number((c_name, i))
            self.Codelist.append(
                'circuit.Cr.cbit[' + str(calc_num2) + '] = list[' + str(calc_num1) + '];\n')
            if self.qasm_bool:
                self.qasmlist.append('measure ' + q_name + '[' + str(i) + '] -> '
                                     + c_name + '[' + str(i) + '];')

    elif type(args[0]) is tuple and type(args[1]) is tuple:
        q_name, num1 = args[0]
        q_name, calc_num1 = self.convert_q_number(args[0])
        c_name, num2 = args[1]
        c_name, calc_num2 = self.convert_c_number(args[1])
        self.Codelist.append('circuit.Cr.cbit[' + str(calc_num2) +
                             '] = list[' + str(calc_num1) + '];\n')
        if self.qasm_bool:
            self.qasmlist.append('measure ' + q_name + '[' + str(num1) + '] -> '
                                 + c_name + '[' + str(num2) + '];')

    return self
