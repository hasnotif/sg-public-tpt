# Calculates passenger volume per individual bus stop over user-specified time period (given in months)

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description = "Calculates passenger volume per individual bus stop over user-specified time period")
    parser.add_argument("-s", "--start_month", help = "specify starting month in YY-MM format, eg. 22-10")
    parser.add_argument("-e", "--end_month", help = "specify ending month in YY-MM format, eg. 22-12")
    parser.add_argument("-o", "--output_filename", help = "specify filename of output file", default = "pv_busstop.txt")
    args = parser.parse_args()

    cwd = os.getcwd()
    datad = os.path.join(cwd, "data")

    # get starting and ending months
    start_mth = int(args.start_month[3:])
    end_mth = int(args.end_month[3:])

    for i in range(start_mth, end_mth+1):
        print(i)

if __name__ == "__main__":
    main()