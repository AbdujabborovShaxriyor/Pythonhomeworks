farenheit = int(input("Enter a temperature in degrees F: "))
def convert_far_to_cel(farenheit):
    celcius = round((farenheit - 32) * 5/9,2)
    print(f"{farenheit} degrees F = {celcius} degrees C")
convert_far_to_cel(farenheit)
celcius = int(input("Enter a temperature in degrees C: "))
def convert_cel_to_far(celcius):
    farenheit = round((celcius * 9/5)+32,2)
    print(f"{celcius} degrees C = {farenheit} degrees F")
convert_cel_to_far(celcius)
