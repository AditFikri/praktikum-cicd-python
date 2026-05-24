from calculator import tambah, kurang

def test_tambah():
    assert tambah(2, 3) == 5

def test_kurang():
    assert kurang(5, 2) == 3