# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:07:08 2020

@author: kumar
"""
"""
import sys
sys.argv=['']
del sys
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", type=int, help="first number")
    parser.add_argument("number2", type=int,  help="second number")
    parser.add_argument("operation", help="operations", choices=["add","subtract","multiply"])

    args = parser.parse_args()
    #args = vars(parser.parse_args())

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1= int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result=n1+n2
    elif args.operation == "subtract":
        result=n1-n2
    elif args.operation== "multiply":
        result=n1*n2


    print("Result:",result)
