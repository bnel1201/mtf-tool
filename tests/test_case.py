from xri_mtf import mtf
from pathlib import Path

fdir = Path(__file__).parent

def test_load_mu_and_odd():
    fname = fdir / 'Values.csv'
    m = mtf.from_csv(fname)
    assert len(m) > 0

# test_load_mu_and_odd()

def test_load_originals():
    fname = fdir / 'atten.csv'
    m = mtf.from_csv(fname)
    assert len(m) > 0


def test_load_mm():
    fname = fdir/'Values_mm.csv'
    m = mtf.from_csv(fname)
    print(m.to_string())
    assert len(m) > 0

test_load_mm()