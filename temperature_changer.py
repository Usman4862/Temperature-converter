print("TEMPRATURE CONVERTER")
# celsius to fahrenheit....
print("*****CELSIUS TO FAHRENHEIT*****")
celsius = int(input("Enter Temparture in Celsius: "))
#(0°C × 9/5) + 32 = 32°F
fahrenheit = (celsius*9/5) + 32
fahrenheit = int(fahrenheit)
print(f"{celsius}°C is {fahrenheit} in Fahrenheit.")

# fahrenheit to celsius......
print("*****FAHRENHEIT TO CELSIUS*****")

fahrenheit = int(input("Enter Temparture in Fahrenheit: "))
# (32°F − 32) × 5/9 = 0°C
celsius = (fahrenheit - 32)* 5/9
celsius = int(celsius)
print(f"{fahrenheit}°F is {celsius} in Celsius.")


