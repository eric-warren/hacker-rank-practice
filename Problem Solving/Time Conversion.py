'''
Given a time in

-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

    s: a string representing time in 

    hour format

Input Format

A single string
containing a time in -hour clock format (i.e.: or ), where and

.

Constraints

    All input times are valid

Output Format

Convert and print the given time in
-hour format, where

.

Sample Input 0

07:05:45PM

Sample Output 0

19:05:45

'''

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if ("AM" in s and s.split(":")[0] != "12") or ("PM" in s and s.split(":")[0] == "12"):
        return s[:-2]

    else:
        s = s[:-2]
        s = s.split(":")
        if s[0] == "12":
            s[0] = "00"
        else:
            s[0] = str(int(s[0])+12)
        return s[0] + ":" + s[1] + ":" + s[2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
