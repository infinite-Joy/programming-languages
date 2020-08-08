#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the whatFlavors function below.
# this can be done using hashmaps
def whatFlavors(cost, money):
    rems = {}
    for idx, c in enumerate(cost, 1):
        rem = money - c
        if rem in rems:
            print(rems[rem], idx)
            return
        rems[rem] = idx


