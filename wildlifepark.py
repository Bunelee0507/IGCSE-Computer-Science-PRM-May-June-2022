# PRM June 2022 in Python. Code written by Anurag Thakur. This code is commented and explained.
# I am using datetime to get the date and time to show the available days.

import datetime
from datetime import timedelta, date

date_object = datetime.date.today()
EndDate = date.today() + timedelta(days=6)

# Number of people

pplt = int(input("How many total people are in your group?"))

# variable for price.

price = int(0)

# offer

offer = 0

# unique booking number

booknum = 0

# Next I am declaring 5 2x1 matrices (arrays) to store the data for both one-day and two-day attractions.

# Below comment explains these matrices.

# one adult
# one child (an adult may bring up to two children)
# one senior
# family ticket (up to two adults or seniors, and three children)
# groups of six people or more, price per person
# second entry is the price for 2 days, first is for 1 day

type1 = [20, 30]
type2 = [12, 18]
type3 = [16, 24]
type4 = [60, 90]
type5 = [15, 22.5]

childnums = [0, 1, 0, 3, 3]

adultnums = [1, 0, 0, 2, 2]

seniornums = [0, 0, 1, 2, 2]

ty = ["", "", "", "", ""]

ty[0] = "one adult"
ty[1] = "one child (an adult may bring up to two children)"
ty[2] = "one senior"
ty[3] = "family ticket (up to two adults or seniors, and three children)"
ty[4] = "groups of six people or more, price per person"

# prices for extra attractions (below comments show the order)

e1 = 2.5
e2 = 2
e3 = 5

# lion feeding
# penguin feeding
# evening barbecue (two-day tickets only)

ex1 = "lion feeding"
ex2 = "penguin feeding"
ex3 = "evening barbecue (two-day tickets only)"

# Next we will display the options, attractions and prices for one-day tickets as required.
print("Below are the bookings that you can make for a zoo visit.")
for i in range(5):
    print(ty[i])
print("Here are the prices for a one day visit in dollars.")

# one-day prices printed

print(type1[0])
print(type2[0])
print(type3[0])
print(type4[0])
print(type5[0])

# These are the extra attractions

print("These are the extra attractions and their prices in dollars.")

print(ex1, e1)
print(ex2, e2)
print(ex3, e3)

# Now to print 2 day attractions.

print("Below are the bookings that you can make for a zoo visit.")
for i in range(5):
    print(ty[i])
print("Here are the prices for a one day visit in dollars.")

# two-day prices printed

print(type1[1])
print(type2[1])
print(type3[1])
print(type4[1])
print(type5[1])

# Now to show the date range

print("You can book from today, which is " + str(date_object), "to", str(EndDate))

# booking a date

date_booked = datetime.date(2020, 7, 7)

while date_booked < date_object or date_booked > EndDate:
    print("Type your date like asked below. It must be within the next 7 days, today inclusive.")
    month = int(input('Enter the month you want to book (numbered 01 - 12 respectively)'))
    day = int(input('Enter the day of that month that you want to book'))

    date_booked = datetime.date(2021, month, day)

# booking a ticket

print("Scroll up. Please look at what was printed for the one-day attractions, two-day attractions and their respective prices. For one day attractions, enter '1' for the next input. For two day attractions, enter 2 for the next input.")

oday_tday = int(input("..."))
typick = int(input("enter a number from 0 to 5. This number will represent your choice for the group you need. (Eg, one adult will be 0). Make sure to scroll up and double check in case you forgot. This is for the " + str(oday_tday) + " attractions."))

print("For the next input, select 0 for no extra attractions, 1 for the first extra attraction, 2 for the second extra attraction, and so on.")

exa = 10

if oday_tday == 2:
    while exa > 3 or exa < 0:
        exa = int(input("Input here for the above line. Make sure it is 0, 1, 2 or 3."))

if oday_tday == 1:
    while exa > 2 or exa < 0:
        exa = int(input("Input here for the above line. Make sure it is 0, 1, or 2."))

adults = int(input("Enter the number of adults you have in your group."))
kids = int(input("Enter the number of kids you have in your group."))
seniors = int(input("Enter the number of seniors you have in your group."))

# incrementing price based on group size and days

if typick == 0:
    price += type1[oday_tday - 1]

if typick == 1:
    price += type2[oday_tday - 1]

if typick == 2:
    price += type3[oday_tday - 1]

if typick == 3:
    price += type4[oday_tday - 1]

if typick == 4:
    price += type5[oday_tday - 1] * pplt

# saving current price for task 3

price_s = price


# incrementing price based on extra attractions

if exa == 0:
    print(" ")
if exa == 1:
    price += 2.5
if exa == 2:
    price += 2
if exa == 3:
    price += 5

booknum += 1

print(booknum, "is your unique booking number")

print("your current price is,", price, "in dollars.")

# Two adults and two children only - offer family pack
# Two adults and three children only - offer family pack
# X number of people only - if the number of adults and seniors add up to 2, offer a family pack if price is more

if adults == 2 and kids == 2:
    if price_s > 60 and oday_tday == 1 or price_s > 90 and oday_tday == 2:
        print("You can take the family pack. It is cheaper. Enter 1 if you want this deal, 0 if you don't.")
        offer = int(input("..."))

elif adults == 2 and kids == 3:
    if price_s > 60 and oday_tday == 1 or price_s > 90 and oday_tday == 2:
        print("You can take the family pack. It is cheaper. Enter 1 if you want this deal, 0 if you don't.")
        offer = int(input("..."))
elif seniors == 2 and kids == 2:
    if price_s > 60 and oday_tday == 1 or price_s > 90 and oday_tday == 2:
        print("You can take the family pack. It is cheaper. Enter 1 if you want this deal, 0 if you don't.")
        offer = int(input("..."))
elif seniors == 2 and kids == 3:
    if price_s > 60 and oday_tday == 1 or price_s > 90 and oday_tday == 2:
        print("You can take the family pack. It is cheaper. Enter 1 if you want this deal, 0 if you don't.")
        offer = int(input("..."))
else:
    offer == 0
if offer == 1 and oday_tday == 1:
    price = 60

    if exa == 0:
        print(" ")
    if exa == 1:
        price += 2.5
    if exa == 2:
        price += 2
    if exa == 3:
        price += 5

if offer == 1 and oday_tday == 2:
    price = 90

    if exa == 0:
        print(" ")
    if exa == 1:
        price += 2.5
    if exa == 2:
        price += 2
    if exa == 3:
        price += 5

# scales number of family packs for price optimisation

scaler = 1

if pplt >= 6 and (adults + seniors > 2) and kids > 3:
    if oday_tday == 1:
        while price_s > scaler * 60 and scaler < 100:
            scaler += 1
    if oday_tday == 2:
        while price_s > scaler * 90 and scaler < 100:
            scaler += 1
if scaler < 100 and scaler != 0 and scaler != 1:
    print("It would be cheaper if you bought", scaler - 1, "family packs. Press 1 if you want this, press 0 otherwise.")
    offer2 = int(input("..."))
    if offer2 == 1 and oday_tday == 1:
        price = 60 * (scaler - 1)
        if exa == 0:
            print(" ")
        if exa == 1:
            price += 2.5
        if exa == 2:
            price += 2
        if exa == 3:
            price += 5

    if offer2 == 1 and oday_tday == 2:
        price = 90 * (scaler - 1)
        if exa == 0:
            print(" ")
        if exa == 1:
            price += 2.5
        if exa == 2:
            price += 2
        if exa == 3:
            price += 5


print(price, "is final price in dollars.", "Booking successful.")