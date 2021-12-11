# %%
import numpy as np
from pathlib import Path

from xri_mtf import mtf


fdir = Path(__file__).parent

def test_load_mu_and_odd():
    assert len(mtf.from_csv(fdir/'Values.csv')) > 0

# test_load_mu_and_odd()

def test_load_originals():
    assert len(mtf.from_csv(fdir/'atten.csv')) > 0


def test_load_mm():
    assert len(mtf.from_csv(fdir/'Values_mm.csv')) > 0
# %%


def test_ideal_edge():
    m = mtf.from_csv(fdir/'ideal_edge_sim.csv')
    assert np.sum(m['MTF'] > 0.999) > 50
