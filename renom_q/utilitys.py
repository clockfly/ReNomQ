# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


import numpy as np
import collections
import matplotlib.pyplot as plt


def plot_histogram(counts):
    """ Plot the execution result with histogram.

    Args:
        counts (dict):
            A dict of the execution result of quantum circuit mesurement.

    Returns:
        matplotlib.figure:
            A matplotlib figure object for the execution result of quantum
            circuit mesurement.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.measure()
        >>> r = renom_q.execute(qc)
        >>> renom_q.plot_histogram(r)
    """
    width = 0.5
    shots = np.sum([i for i in counts.values()])
    x = [i[0] for i in counts.items()]
    y = [i[1] / shots for i in counts.items()]
    for i in range(len(counts)):
        plt.text(x[i], y[i], str(y[i]), ha='center')
    plt.bar(x, y, width=width)
    plt.tick_params(top=1, right=1, direction='in')
    plt.xticks(rotation=60)
    plt.ylabel('Probabilities')
    plt.show()


def execute(circuit, shots=1024):
    """ Execute the quantum circuit mesurement.

    Args:
        circuit (renom_q.QuantumCircuit):
            A class of QuantumCircuit.
        shots (int):
            The number of excutions of quantum circuit mesurement. Defaults to
            1024.

    Returns:
        (dict):
            A execution result of quantum circuit mesurement. The key is the
            measured classical bits. The value is the number of classical bits
            measured.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.measure()
        >>> renom_q.execute(qc)
        {'0': 1024}
    """
    code = ''
    cn = []
    for i in circuit.Codelist:
        code += i
    else:
        code += 'cn.append(\'\'.join(circuit.Cr.cbit));'
    # print(Code)
    for i in range(shots):
        exec(compile(code, '<string>', 'exec'))

    return dict(sorted(collections.Counter(cn).items(), key=lambda x: x[0]))



def print_matrix(circuit, tensorgate=False):
    """ Print all matrix calculation of unitary conversion.

    Args:
        circuit (renom_q.QuantumCircuit):
            A class of QuantumCircuit.
        tensorgate (bool):
            When set to True, added matrix calculation of quantum gate tensor
            product. Defaults to False.

    Returns:
        matrix(str):
            Strings of the final result of qubit statevector and all matrix
            calculation of unitary conversion.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.x(q[0])
        >>> renom_q.print_matrix(qc)
        ---------------- result qubit ----------------
        [0.+0.j 1.+0.j]
        ---------------- x(q[0]) ----------------
        [[0. 1.]
        [1. 0.]]・
                                                            \\
        [[1.+0.j]
        [0.+0.j]] =
                                                            \\
        [[0.+0.j]
        [1.+0.j]]
    """
    matrix = '---------------- result qubit ----------------\n' + str(circuit.Qr.qubit)
    if tensorgate is True:
        matrixlist = np.array([circuit.matrixlist, circuit.tensorlist])
        for i in range(len(circuit.matrixlist)):
            matrix += matrixlist[0, i]
            matrix += matrixlist[1, i]
    else:
        for i in circuit.matrixlist:
            matrix += i
    print(matrix)


def statevector(circuit):
    """ Get the qubit statevector.

    Args:
        circuit (renom_q.QuantumCircuit):
            A class of QuantumCircuit.

    Returns:
        (array):
            A array of the qubit statevector.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
        >>> c = renom_q.ClassicalRegister(1)
        >>> qc = renom_q.QuantumCircuit(q, c)
        >>> qc.x(q[0])
        >>> renom_q.statevector(qc)
        array([0.+0.j, 1.+0.j])
    """
    return circuit.Qr.qubit
