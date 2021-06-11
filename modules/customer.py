# customer.py
# Manage customer information:

#     customer id
#     first name
#     last name
#     current list of video rentals (by title)

class Customer:

    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id                    = id
        self.first_name            = first_name
        self.last_name             = last_name
        self.current_video_rentals = current_video_rentals

    