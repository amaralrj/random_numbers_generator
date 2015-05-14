#!/usr/bin/python

import sys
from random import randint
import argparse

def main(args):
    initial_range = args['<initial>'] 
    end_range = args['<end>']
    total_numbers = args['<total>']
    result = []

    for x in range(total_numbers):
        number = str(randint(initial_range,end_range)).zfill(2)
        while number in result:
            number = str(randint(initial_range,end_range)).zfill(2)
        result.append(number)

    result.sort()
    print 'Boa Sorte: "', result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='script to get sorted numbers')
    parser.add_argument('<initial>', type=int, help="Initial number of range")
    parser.add_argument('<end>', type=int, help="End number of range")
    parser.add_argument('<total>', type=int, help="Total sorted numbers")
    args = parser.parse_args()
    main(vars(args))
