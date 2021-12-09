from numpy.fft import fft
from scipy.interpolate import interp1d
import numpy as np
import pandas as pd
import argparse

def interpolate_signal(x_pos, y_grayval, oversampling=10):
    f = interp1d(x_pos, y_grayval, kind='cubic')
    x = np.linspace(x_pos[0], x_pos[-1], len(x_pos)*oversampling) #replace 1000 with oversampling*len(x_pos)
    y = f(x)
    return x, y

def center_peak(psf, crop_factor):
    peak_idx = psf.argmax()
    start_idx = peak_idx - len(psf)//crop_factor
    end_idx =  peak_idx + len(psf)//crop_factor
    return psf[start_idx:end_idx] # center the psf

def retrieve_MTF(x_pos, y_grayval, oversampling=10, crop_factor=4, unit='mm'):
    x, y = interpolate_signal(x_pos, y_grayval, oversampling=oversampling)

    psf = np.diff(y)
    x = x[1:]

    psf = psf/psf.sum()
    # center and smooth edge noise
    psf = center_peak(psf, crop_factor=crop_factor)
    psf *= np.hanning(len(psf))

    # compute MTF
    # determining frequencies (because I always forget): <https://www.mathworks.com/matlabcentral/answers/88685-how-to-obtain-the-frequencies-from-the-fft-function>
    N = len(psf)
    dx = np.diff(x)[0] # mm
    fmax = 1/(2*dx) # 1/mm
    df = fmax / (N // 2)
    freq = np.arange(0, fmax, df)

    mtfs = np.abs(fft(psf)/np.sum(psf))[:len(psf)//2]

    mtf = pd.DataFrame({f'frequency [1/{unit}]' : freq, 'MTF': mtfs})
    mtf = mtf.applymap(lambda x: np.round(x, decimals=3))
    return mtf

def from_csv(fname):
    '''
    csv expected to be in ImageJ output format produced by Radial Profile plugin: <https://imagej.nih.gov/ij/plugins/radial-profile.html>
    Radius_[units], Normalized_Integrated_intensity
    '''
    df = pd.read_csv(fname, encoding = 'latin1')
    unit = df.columns[0].split('_')[-1][1:-1]
    data = df.to_numpy()
    x_pos = data[:, 0]
    y_grayval = data[:, 1]
    return retrieve_MTF(x_pos, y_grayval, unit=unit)


def cli():
    parser = argparse.ArgumentParser('Calculate MTF from an ImageJ radial line profile')
    parser.add_argument('csv_filename', help='path to csv file output from ImageJ radial line profile')
    parser.add_argument('-output_file', default=None)

    args = parser.parse_args()

    mtf = from_csv(args.csv_filename)

    if args.output_file:
        mtf.to_csv(args.output_file)
    else:
        print(mtf[(mtf['MTF']<0.01).cumsum()<1].to_string()) #only print MTFs > 1% the rest is useless noise


if __name__ == '__main__':
    cli()