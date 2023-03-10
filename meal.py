
time = input("What time is now? ")
mealtime = time.split(":")
hours = float(mealtime[0]) + round(float(mealtime[1])/60, 2)

if 7 <= hours <= 8:
    print("Breakfast time")
elif 12 <= hours <= 13:
    print("Lunch time")
elif 18 <= hours <= 19:
    print("Dinner time")