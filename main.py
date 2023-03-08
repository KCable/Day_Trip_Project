
# Day Trip Project


import random


destination = ["Los Angeles", "San Diego", "San Francisco", "Las Vegas", "Seattle"]
# random_destination = random.choice(destination)


restaurant = ["Italian", "Mexican", "Sushi", "Steakhouse", "Buffet"]
# random_restaurant = random.choice(restaurant)


mode_of_transport = ["Car", "Bicycle", "Driver", "Walking", "Tour Bus"]
# random_mode_of_transport = random.choice(mode_of_transport)


entertainment = ["Spa Trip", "City Tour", "Local Attraction-Zoo/Amusement Park/etc", "Show-Theartre/Comedy/etc", "Beach/Pool Day"]
# random_entertainment = random.choice(entertainment)


# def determine_satisfaction(current_trip, trip options)

def trip_options():
   while True:
      
      random_destination = random.choice(destination)
      print(random_destination)

      random_restaurant = random.choice(restaurant)
      print(random_restaurant)

      random_mode_of_transport = random.choice(mode_of_transport)
      print(random_mode_of_transport)

      random_entertainment = random.choice(entertainment)
      print(random_entertainment)

      current_trip = trip_options 

      user_choice = input("Are you satisfied with the current selections? Y/N? ")
      if user_choice != "Y":
         print("Let's try again!")
      else:
         print("Enjoy your trip!")
         return current_trip
         
       
      
trip_options()


