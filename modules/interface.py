# interface.py
from modules.video import Video
from modules.customer import Customer
from modules.store import Store

class Interface:

    def __init__(self, store_name):
        self.store = Store(store_name)

    def menu(self):
        return ("\n"
        "Welcome to Code Platoon Video!\n"
        "1. View video inventory\n"
        "2. View customer's rented videos\n"
        "3. Rent video\n"
        "4. Return video\n"
        "5. Add new customer\n"
        "6. Exit\n")

    # 1. View video inventory
    def view_video_inventory(self):
        self.store.view_all_videos()

    # 2. View customer's rented videos
    def view_customer_rented_videos(self):
        customer_id = input('Enter Customer ID:')
        customer_str = str(self.customer.view_customer_rental_by_id(customer_id))
        print(customer_str)

    # 3. Rent vide
    # 4. Return video\n
    # 5. Add new custome

    def run(self):
        while True:
            mode = input(self.menu())
            if mode == '1':
                self.view_video_inventory()
            elif mode == '2':   
                self.view_customer_rented_videos()
            elif mode == '3':   
                self.rent_video()
            elif mode == '4':   
                self.return_video()
            elif mode == '5':   
                self.add_new_customer()
            elif mode == '6':
                break
            
