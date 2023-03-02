
# def run_day_trip_generator:

import random

destination = ["Los Angeles", "San Diego", "San Francisco", "Las Vegas", "Seattle"]
random_destination = random.choice(destination)
print(random_destination)

restaurant = ["Italian", "Mexican", "Sushi", "Steakhouse", "Buffet"]
random_restaurant = random.choice(restaurant)
print(random_restaurant)

mode_of_transport = ["Car", "Bicycle", "Driver", "Walking", "Tour Bus"]
random_mode_of_transport = random.choice(mode_of_transport)
print(random_mode_of_transport)

entertainment = ["Spa Trip", "City Tour", "Local Attraction-Zoo/Amusement Park/etc", "Show-Theartre/Comedy/etc", "Beach/Pool Day"]
random_entertainment = random.choice(entertainment)
print(random_entertainment)

# def determine_satisfaction(current_trip, trip_options):


current_trip = input("Are you satisfied with the current selections? Yes/No? ")
if current_trip != "Yes":
   print("Which item would you like to change? destination, restaurant, mode of transport or entertainment?")
else:
   print("Enjoy your trip!")

# trip_options = re_select



# def re_select_option(current_trip, options):



# def print_full_trip(list_of_options):
    


# run_day_trip_generator()
