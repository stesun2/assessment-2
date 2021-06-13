# store.py
from modules.customer import Customer
from modules.video import Video
import os
import csv

class Store:

    def __init__(self, name):
        self.name      = name
        self.videos    = Video.objects()
        self.customers = Customer.objects()

    # View Video Inventory
    def view_all_videos(self):
        print('\n')
        print('ID\tTITLE\t\tRATING\tQTY')
        for i, video in enumerate(self.videos):
            print(f'{i + 1}. {video.title} {video.rating} {video.copies_available}')

    # Viewing a customer's current rented videos customer by id
    def view_customer_rental_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return "Current movies: " + customer.current_video_rentals

    # Renting Video
    def rent_video_to_customer(self, video_title, customer_id):
        # counting the total number movies checked out
        total_rentals = 0
        for customer in self.customers:
            if customer.id == customer_id:
                for rental in customer.current_video_rentals:
                    if rental == '/':
                        total_rentals += 1
                        print(total_rentals)

        # Simple way of counting the number of movies checked out
        # Probably should do a Dictionary to seperate the number of movies checked out per customer        
        if total_rentals < 2:
            for video in self.videos:
                if video.copies_available != 0 and video.title == video_title:
                    # print('video title:', video.title)
                    return ('Copies available', video.copies_available)
                else:
                    print('The movie you have selected is not in stock')
        else:
            return 'Exceeded the maximum amount rental allowed (3)' 

    # Function which is called to update the Inventory/Qty of the store
    def update_inventory(self):
        pass


    # Return Video
    def return_video_from_customer(self, current_video_rentals):
        pass

    # Adding new customer
    def add_new_customer(self, customer_data):
        self.customers.append(Customer(**customer_data))
        self.save_customer()
    
    def save_customer(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(['id', 'first_name', 'last_name', 'current_video_rentals'])
            for customer in self.customers:
                customer_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])


        # return total_rentals
        # Check bot if movie title and customer id matches
        # If both are true, check to see if customer more than 3 movies checked out
        # If not check to see if the copies available is more than 0
        # Is true, write/update the csv file with the new changes
        # for customer in self.customers:
            # if customer.current_video_rentals == customer_id:
            # print(customer.current_video_rentals)
                # return customer.current_video_rentals
            # if customer.current_video_rentals > 3:
            #     return 'Exceeded the maximum amount rental allowed'

        # for video in self.videos:
            # if video.title == video_title:
            #     return ('Copies available', video.copies_available)
            # else:
            #     return 'The movie you have selected is not in stock'

        # print(video_title, customer_id)