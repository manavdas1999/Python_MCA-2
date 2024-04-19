#Q4. Write a python program for converting Temperature to and from Celsius and Fahrenheit. 

tempInCelsius = int(input("Enter Temperature in Celsius:"))
tempInFahrenheit = (tempInCelsius * 9/5) + 32

# Fahrenheit to Celcius:
# tempInCelsius = (tempInFahrenheit - 32) * 5/9

print("Temperature in Celsiust:", tempInCelsius)
print("Temperature in Fahrenheit:", tempInFahrenheit)
