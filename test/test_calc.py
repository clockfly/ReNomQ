from renom_q import *
from math import *


def test_culc1():
    bn = 9
    q = QuantumRegister(bn)
    c = ClassicalRegister(bn)
    qc = QuantumCircuit(q, c)

    qc.reset().id(q[0]).x(q[1]).z(q[2]).y(q[3]).h(q[4]).barrier()
    qc.s(q[5]).sdg(q[6]).t(q[7]).tdg(q[8])

    qc.measure()

    r = execute(qc)

    assert r


def test_culc2():
    bn = 6
    q = QuantumRegister(bn)
    c = ClassicalRegister(bn)
    qc = QuantumCircuit(q, c)

    qc.rx(pi, q[0]).ry(pi, q[1]).rz(pi, q[2]).u1(pi, q[3]).u2(0, pi, q[4])
    qc.u3(pi, 0, pi, q[5]).barrier(q)

    qc.measure(q, c)

    r = execute(qc)

    assert r


def test_culc3():
    bn = 9
    q = QuantumRegister(bn)
    c = ClassicalRegister(bn)
    qc = QuantumCircuit(q, c)

    qc.x(q[0]).cx(q[0], q[1]).cy(q[0], q[2]).cz(q[0], q[3]).ch(q[0], q[4])
    qc.cs(q[0], q[5]).cu1(pi, q[0], q[6]).cu3(pi, 0, pi, q[0], q[7])
    qc.crz(pi, q[0], q[8]).barrier(q[1]).barrier(q[4])

    for i in range(bn):
        qc.measure(q[i], c[i])

    r = execute(qc)

    assert r


def test_culc4():
    bn = 5
    q = QuantumRegister(bn)
    c = ClassicalRegister(bn)
    qc = QuantumCircuit(q, c)

    qc.x(q[0]).x(q[1]).swap(q[0], q[2]).swap(q[2], q[0])
    qc.ccx(q[0], q[1], q[3]).cswap(q[0], q[1], q[4])

    qc.measure()

    r = execute(qc)

    assert r


def test_culc5():
    bn = 2
    qa = QuantumRegister(bn, 'qa')
    ca = ClassicalRegister(bn, 'ca')
    qb = QuantumRegister(bn, 'qb')
    cb = ClassicalRegister(bn, 'cb')
    qc = QuantumCircuit(qa, ca, qb, cb)

    qc.x(qa[0]).x(qa[1]).x(qb[0]).x(qb[1]).barrier(qa, qb)

    qc.measure(qa, ca).measure(qb, cb)

    r = execute(qc)

    assert r


def test_culc6():
    bn = 2
    qa = QuantumRegister(bn, 'qa')
    ca = ClassicalRegister(bn, 'ca')
    qb = QuantumRegister(bn, 'qb')
    cb = ClassicalRegister(bn, 'cb')
    qca = QuantumCircuit(qa, ca)
    qcb = QuantumCircuit(qb, cb)
    qc = qca + qcb

    qc.x(qa[0]).x(qa[1]).x(qb[0]).x(qb[1]).barrier()

    for i in range(bn):
        qc.measure(qa[i], ca[i])
    for i in range(bn):
        qc.measure(qb[i], cb[i])

    r = execute(qc)

    assert r


def test_culc7():
    bn = 2
    cn = 4
    qa = QuantumRegister(bn, 'qa')
    ca = ClassicalRegister(cn, 'ca')
    qb = QuantumRegister(bn, 'qb')
    qc = QuantumCircuit(qa, ca, qb)

    qc.x(qa[0]).x(qa[1]).x(qb[0]).x(qb[1]).barrier(qa[1]).barrier(qb[1])

    qc.measure()

    r = execute(qc)

    assert r


def test_culc8():
    bn = 2
    q = QuantumRegister(bn)
    c = ClassicalRegister(bn)
    qc = QuantumCircuit(q, c, set_qasm=True, set_print_matrix=True)

    qc.x(q[0]).h(q[1])

    qc.measure()

    r = execute(qc)
    print(q)
    print(c)
    print(qc)
    print(r)
    print_matrix(qc)
    print(statevector(qc))
    print(qc.qasm())

    assert r
