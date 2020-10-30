#!/usr/bin/env python3

import argparse
import re
from pathlib import Path

if __name__ == "__main__":
    cmd_parser = argparse.ArgumentParser(description="Tool that splits csv files created by network-stats into 5 minute long files")
    cmd_parser.add_argument("-i", "--input", help="csv file to be split; will not be modified", required=True, type=argparse.FileType('r'))
    cmd_parser.add_argument("-o", "--output", help="Directory to put split files", default=".")
    cmd_parser.add_argument("-d", "--duration", help="Duration in minutes to split the input file by", default=5)

    args = cmd_parser.parse_args()
    output_path = Path(args.output)

    if False == output_path.is_dir():
        print("Error:  Output \"" + args.output + "\" is not a directory.")
        cmd_parser.print_usage()
        exit()

    # TODO: verify input file actually ends in .csv
    filename_prefix = re.compile('(.*)\.csv').match(args.input.name).group(1)

    time_pattern = re.compile('\d+')
    file_header = args.input.readline()
    file_start_time = 0
    file_name_int = 0
    
    output_file = None
    duration = int(args.duration) * 60

    for line in args.input:
        time = int(time_pattern.match(line).group())
        if time > file_start_time + duration:
            file_name = filename_prefix + "-" + str(file_name_int) + '.csv'
            output_file_path = output_path / file_name
            output_file = output_file_path.open('w')
            output_file.write(file_header)
            file_start_time = time
            file_name_int+=1
        output_file.write(line)
