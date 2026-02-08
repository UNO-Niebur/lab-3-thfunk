#ApproxPi.py
#Name: Taran Funk
#Date: 01/03/2026
#Assignment: Lab 3 - Approximate Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  print("To how many decimal places would you like our approximation of pi to be accurate to?")
  decimal = int(input("Choose a number from 1 - 10:"))
  
  start = time.time()
  approxPi = 4
  count = 1
  #Loop until the level of percision is reached
  while abs(round(realPi,decimal) - round(approxPi,decimal))>0:
    approxPi = approxPi + ((-1)**count)*(4/(1 + 2*(count)))
    count += 1
  end = time.time()

  elapsedTime = end - start
  print("It took ",elapsedTime, " seconds to find this approximation:", round(approxPi,decimal))
  

if __name__ == '__main__':
  main()
