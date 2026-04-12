# Shameerah Dixon
# April 12, 2026
# p2lab2.py
# Writing a program that creates a dictionary where the key and value pairs

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#Get keys from dictionary
cars_keys = cars.keys()

print (cars_keys)

print(*cars_keys, sep = ", ")

#Get a carfrom user 
car_name = input("Enter a vehicle to see its mpg: ")
print()
#Get mpg for the given car
car_mpg = cars[car_name]
print(f"The {car_name} get {car_mpg} mpg.")
print()
#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))
print()
#Calculate 
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")