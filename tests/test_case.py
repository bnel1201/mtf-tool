import sys
sys.path.append('..')
import mtf

def test_load_mu_and_odd():
    fname = r'Values.csv'
    m = mtf.from_csv(fname)
    print(m.to_string())

test_load_mu_and_odd()
