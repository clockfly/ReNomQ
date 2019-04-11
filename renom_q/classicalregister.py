# -*- coding: utf-8 -*-

# Copyright 2019, Grid.
#
# This source code is licensed under the ReNom Subscription Agreement, version 1.0.
# ReNom Subscription Agreement Ver. 1.0 (https://www.renom.jp/info/license/index.html)


class ClassicalRegister:
    """ Definite a classical register.

    Args:
        num (int):
            The number of classical bits.
        name (str):
            A name of classical bits. Defaults to 'c'.

    Example:
        >>> import renom_q
        >>> c = renom_q.ClassicalRegister(1)
    """
    def __init__(self, num, name=None):
        self.name = 'c' if name is None else name
        self.dict = {self.name: 0}
        self.num = num
        self.numlist = [num]
        self.cbit = [0 for i in range(self.num)]
        self.qasmcode = 'creg ' + str(self.name) + '[' + str(self.num) + '];'

    def __getitem__(self, num):
        """
        Args:
            num (int):
                The classical bit number. If definited 3 classical bits,
                most significant bit numberis 0 and least significant bit
                number is 2.

        Returns:
            (tuple):
                A tuple of a name of classical bits and the classical bit number.

        Example:
            >>> import renom_q
            >>> c = renom_q.ClassicalRegister(1, 'cbit')
            >>> c[0]
            ('cbit', 0)
        """
        return self.name, num

    def __str__(self):
        """
        Returns:
            (str):
            A name of classical bits.

        Example:
            >>> import renom_q
            >>> c = renom_q.ClassicalRegister(1, 'cbit')
            >>> print(c)
            cbit
        """
        return self.name
