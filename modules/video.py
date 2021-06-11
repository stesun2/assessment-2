# Manage the store's video inventory:

#     video id
#     video title
#     video rating
#     number of copies currently available in-store
import csv
import os.path

# No inheritence
class Video:

    def __init__(self, id, title, rating, copies_available):
        self.id               = id
        self.title            = title
        self.rating           = rating
        self.copies_available = copies_available

    # string method
    def __str__(self):
        return f'\n{self.title.upper()}\n---------------\nTitle: {self.title}\nID: {self.id}\n'

    # Reading from the inventory CSV file
    @classmethod
    def objects(cls):
        videos = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                videos.append(Video(**dict(row)))

        return videos

    

    
