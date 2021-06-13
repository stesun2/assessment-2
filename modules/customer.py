# customer.py
# Manage customer information:

#     customer id
#     first name
#     last name
#     current list of video rentals (by title)
import csv
import os.path

class Customer:

    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id                    = id
        self.first_name            = first_name
        self.last_name             = last_name
        self.current_video_rentals = current_video_rentals

    # Reading from the inventory CSV file
    @classmethod
    def objects(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**dict(row)))
        
        return customers
