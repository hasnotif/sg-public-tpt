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

    # prepare bus stop dict
    bus_stops = {}

    # extract relevant data
    os.chdir(datad)
    data_list = os.listdir(datad)
    
    for i in range(start_mth, end_mth+1):
        curr_file = [k for k in data_list if k[-6:-4] == str(i)][0]
        with open(curr_file, 'r') as r:
            lines = r.readlines()[1:]
            for line in lines:
                tabs = line.split(",")
                bus_stop_code = tabs[4]
                if len(bus_stop_code) == 4:
                    bus_stop_code = "0" + bus_stop_code
                tap_in_h_vol = int(tabs[5])
                tap_out_h_vol = int(tabs[6])
                total_h_vol = tap_in_h_vol + tap_out_h_vol
                if bus_stop_code not in bus_stops:
                    bus_stops[bus_stop_code] = total_h_vol
                else:
                    curr_vol = bus_stops[bus_stop_code]
                    new_vol = curr_vol + total_h_vol
                    bus_stops[bus_stop_code] = new_vol
    
    # obtain bus stop with lowest passenger volume
    min_bus_stop = min(bus_stops, key = bus_stops.get)
    print(f"{min_bus_stop} had the lowest passenger volume ({bus_stops[min_bus_stop]}) in Q4 2022")

    # obtain bus stops with highest passenger volumes, then cross-check online to see if it is an interchange or not
    res = dict(sorted(bus_stops.items(), key = lambda x: x[1])[:11])
    print(str(res))
            
if __name__ == "__main__":
    main()