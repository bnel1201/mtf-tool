import argparse
from xri_mtf.mtf import from_csv

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