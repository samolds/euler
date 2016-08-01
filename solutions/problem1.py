#!/usr/bin/python2.7

# Project Euler - Problem 1 Solution
# https://projecteuler.net/problem=1
# Sam Olds

# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.


def main():
  i = 0
  runningSum = 0
  while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
      runningSum += i
    i += 1
  print runningSum


if __name__ == '__main__':
  main()
