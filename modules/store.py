# store.py
from modules.customer import Customer
from modules.video import Video
import os
import csv

class Store:

    def __init__(self, name):
        self.name     = name
        self.video    = Video.objects()
        # self.customer = Customer.objects()

    def view_all_videos(self):
        print('\n')
        for i, video in enumerate(self.inventory):
            print(f'{i + 1}. {video.title} {video.id}')