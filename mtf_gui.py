from mtf_cli import from_csv
from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser(description='Calculate MTF from an ImageJ radial line profile')
    parser.add_argument('csv_filename',
                         help='path to csv file output from ImageJ radial line profile',
                         widget="FileChooser")
    parser.add_argument('-output_file', default=None)

    args = parser.parse_args()

    mtf = from_csv(args.csv_filename)

    if args.output_file:
        mtf.to_csv(args.output_file)
    else:
        print(mtf[(mtf['MTF']<0.01).cumsum()<1].to_string()) #only print MTFs > 1% the rest is useless noise

main()