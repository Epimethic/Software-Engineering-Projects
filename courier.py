air = True
full_insurance = True
gift = True
priority_delivery = True
shipping_cost = 0
insurance_cost = 0
gift_cost = 0
delivery_cost = 0
distance_air = 0
distance_sea = 0

print("Greetings and salutations to you!\n How can we help you today?")
cost_of_package = float(input("How much is the package you would like to purchase? "))

air_or_sea = input("Would you like to send your package by air or sea? ")

if air_or_sea == "Sea" or "sea":
    air = False

if air == False:
    distance_sea = float(input("How many km does your package need to travel by sea? "))
else:
    distance_air = float(input("How many km does your package need to travel by air? "))

air_mail_cost = 0.36 *(distance_air)
sea_freight_cost = 0.25 * (distance_sea)

if air == False:
    shipping_cost =  sea_freight_cost + cost_of_package
else: 
    shipping_cost = air_mail_cost + cost_of_package

insurance_check = input("Do you require full insurance? (Yes or No) ")

if insurance_check == "No" or "no":
    full_insurance = False

if full_insurance == False:
    insurance_cost = shipping_cost + 25
else:
    insurance_cost = shipping_cost + 50

gift_check = input("Would you like to send your package gift wrapped? Yes or no. ")

if gift_check == "No" or "no":
    gift = False

if gift == False:
    gift_cost = insurance_cost + 0
else:
    gift_cost = insurance_cost + 15

priority_delivery_check = input("Would you like to send your package via priority delivery? Yes or no. ")

if priority_delivery_check == "No" or "no":
    priority_delivery = False

if priority_delivery == False:
    delivery_cost = gift_cost + 20
else: 
    delivery_cost = gift_cost + 100

print(f"Your total amount to buy and send the package is: £{delivery_cost}")







# User to input the cost of a package
# Ask the user how far, in km, the package needs to travel
# air mail costs R0.36 per km 
# Sea freight costs R0.25 per km

# Full insurance costs R50
# Limited insurance costs R25

# Gift costs R15
# No gift costs 0

# Priority delivery costs R100
# Standard delivery costs R20

# Work out the total costs based on the input
# Print total cost