#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    text = [ord(st) for st in s]
    revers_text = text[-1::-1]
    diff_text = [abs(text[i] - text[i+1])for i in range(len(text)-1)]
    diff_revers_text = [abs(revers_text[i] - revers_text[i+1])for i in range(len(revers_text)-1)]
    if diff_text == diff_revers_text:
        return "Funny"
    else:
        return "Not Funny"
    
