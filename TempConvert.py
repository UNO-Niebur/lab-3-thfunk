#TempConvert.py
#Name: Taran Funk
#Date: 01/03/2026
#Assignment: Lab 3 - Temperature Converter


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("Enter a temperature in Fahrenheit: "))

  tempC = round((tempF - 32) * (5/9), 1)

  print(tempF, "is ", tempC, "degrees celsius.")
  
if __name__ == '__main__':
  main()
