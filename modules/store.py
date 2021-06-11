# store.py
from modules.customer import Customer
from modules.video import Video
import os
import csv

class Store:

    def __init__(self, name):
        self.name     = name
        self.videos    = Video.objects()
        self.customers = Customer.objects()

    def view_all_videos(self):
        print('\n')
        print('ID\tTITLE')
        for i, video in enumerate(self.videos):
            print(f'{i + 1}. {video.title}')

    # Viewing a customer's current rented videos customer by id
    def view_customer_rental_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer.current_video_rentals

        #  customer_id = input('Please enter Customer ID')
        #  for i, customer in enumerate(self.customers):
        #     if customer.id == customer_id:
        #         return customer.current_video_rentals
        #     else:
        #         return None

    # def save(self):
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../data/inventory.csv")

    #     with open(path, 'w') as csvfile:
    #         video_csv = csv.writer(csvfile, delimiter=',')
    #         video_csv.writerow(['id', 'title', 'rating', 'school_id', 'copies_available'])
    #         for video in self.inventory:
    #             video_csv.writerow([video.id, video.title, video.rating, video.copies_available])