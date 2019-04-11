# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


class QuantumRegister:
    """ Definite a quantum register.

    Args:
        num (int):
            The number of quantum bits.
        name (str):
            A name of quantum bits. Defaults to 'q'.

    Example:
        >>> import renom_q
        >>> q = renom_q.QuantumRegister(1)
    """
    def __init__(self, num, name=None):
        self.name = 'q' if name is None else name
        self.dict = {self.name: 0}
        self.num = num
        self.numlist = [num]
        self.q_states = 2**num
        self.qubit = [complex(0.) for i in range(self.q_states)]
        self.qubit[0] = 1.
        self.q_number = [i for i in range(self.q_states)]
        self.qasmcode = 'qreg ' + str(self.name) + '[' + str(self.num) + '];'

    def __getitem__(self, num):
        """
        Args:
            num (int):
                The quantum bit number. If definited 3 quantum bits,
                most significant bit number is 0 and least significant bit
                number is 2.

        Returns:
            (tuple):
                A tuple of a name of quantum bits and the quantum bit number.

        Example:
            >>> import renom_q
            >>> q = renom_q.QuantumRegister(1, 'qbit')
            >>> q[0]
            ('qbit', 0)
        """
        return self.name, num

    def __str__(self):
        """
        Returns:
            (str): A name of quantum bits.

        Example:
            >>> import renom_q
            >>> q = renom_q.QuantumRegister(1, 'qbit')
            >>> print(q)
            qbit
        """
        return self.name
