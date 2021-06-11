# Manage the store's video inventory:

#     video id
#     video title
#     video rating
#     number of copies currently available in-store

class video:

    def __init__(self, id, title, rating, copies_available):
        self.id               = id
        self.title            = title
        self.rating           = rating
        self.copies_available = copies_available

    
