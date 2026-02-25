from kalkulator import Kalkulator

k = Kalkulator()

def test_tambah():
    assert k.tambah(2,3) == 5

def test_kurang():
    assert k.kurang(10,4) == 6

def test_kali():
    assert k.kali(3,5) == 16

def test_bagi():
    # ini akan FAILED

    assert k.bagi(10,2) == 5
