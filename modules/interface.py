# interface.py

class interface:

    def __init__(self) -> None:
        pass

    def menu(self):
        return ("\n"
        "Welcome to Code Platoon Video!\n"
        "1. View video inventory\n"
        "2. View customer's rented videos\n"
        "3. Rent video\n"
        "4. Return video\n"
        "5. Add new customer\n"
        "6. Exit")


    def run(self):
        while True:
            mode = input(self.menu())
            if mode == '1':
                self.view_all_videos()
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
            
