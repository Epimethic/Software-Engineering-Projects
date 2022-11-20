# List of vriables that will be used
air = True
full_insurance = True
gift = True
priority_delivery = True
round_up = True
shipping_cost = 0
insurance_cost = 0
gift_cost = 0
delivery_cost = 0
distance_air = 0
distance_sea = 0


# User is asked to input the cost of their package. 
# The float variable has been cast to the string.
print("Greetings and salutations to you!\n How can we help you today?")
cost_of_package = float(input("How much is the package you would like to purchase? "))

# This will ask the user to input whether they need to send the package via air.
air_or_sea = input("Would you like to send your package by air? y/n ")

# if statement telling Python that if "n" is entered then air will be False
if air_or_sea == "n":
    air = False

# if air is False then the user will be prompted to input the distance in km it will need to travel by sea.
# The else statement will be used if the user enters anything other than "n" and it will prompt the user to input the km the package will travel by air.
# These have been had float cast to them.
if air == False:
    distance_sea = float(input("How many km does your package need to travel by sea? "))
else:
    distance_air = float(input("How many km does your package need to travel by air? "))

# These two statements tell Python the cost of air mail is 0.36 * the input the user put in for distance_air
# and the cost of sea freight is 0.25 * the input the user put in for distance_sea
air_mail_cost = 0.36 *(distance_air)
sea_freight_cost = 0.25 * (distance_sea)

# If the user inputs 'n' for air mail then Python will calculate the shipping cost by sea_freight_cost + cost_of_package
# If the user inputs 'y' for air mail then Python will calculate the shipping cost by air_mail_cost + cost_of_package
if air == False:
    shipping_cost =  sea_freight_cost + cost_of_package
else: 
    shipping_cost = air_mail_cost + cost_of_package

insurance_check = input("Do you require full insurance? (y/n) ")

# If the user input 'n' for full insurance then value False is triggered
if insurance_check == "n":
    full_insurance = False

# if the value False is trigged then Python will calculate the insurance_cost is shipping_cost + 25
# if the value True is triggered then Python will calculate the insurance_cost is shipping_cost + 50
if full_insurance == False:
    insurance_cost = shipping_cost + 25
else:
    insurance_cost = shipping_cost + 50

# The user will be asked if they want their package gift wrapped
gift_check = input("Would you like to send your package gift wrapped? y/n ")

# if the user inputs 'n' then the gift boolean is False
if gift_check == "n":
    gift = False

# If the gift boolean is False then nothing is added to the total cost
# If the gift boolean is True then 15 is added to the total cost
if gift == False:
    gift_cost = insurance_cost + 0
else:
    gift_cost = insurance_cost + 15

# The user will be asked if they want their package sent via priority delivery
priority_delivery_check = input("Would you like to send your package via priority delivery? y/n. ")

# If the user inputs 'n' then the priority_delivery boolean is False
if priority_delivery_check == "n":
    priority_delivery = False

# if the priority_delivery boolean is False then Python calculates the delivey_cost as gift_cost + 20
# if the priority_delivery boolean is True then Python calculates the delivery_cost as gift_cost + 100
if priority_delivery == False:
    delivery_cost = gift_cost + 20
else: 
    delivery_cost = gift_cost + 100

# Python will then print out the statement "Your total amount to buy and send the package is: R delivery_cost
# The delivery cost has been rounded to 2 decimal places"
print(f"Your total amount to buy and send the package is: £{round(delivery_cost, 2)}")










