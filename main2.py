# For abstract class and abstract method
from abc import ABC, abstractmethod
# Instance variable vs class variable

import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


# Abstract class and Abstract method a must to define a method for for every class
# Inheriting the abstract class

class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class Hotel:
    # Class variable
    watermark = "Real Estate Company"

    def __init__(self, hotel_id):

        # Instance variable( uses self)
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    # Instance method( uses self)
    def book(self):
        """ changes availability to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """ Checks if hotel is available"""

        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # Class method:
    @classmethod
    def get_count(cls, data):
        return len(data)

    # Magic methods: use dir to see them
    # exple __eq__ method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

        # Property : if instance variable needs processing, use property

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    def generate(self):
        content = f"""
        Thank you
        your reservation is:
        Name:{self.the_customer_name}
        your hotel is {self.hotel.name}"""
        return content

    # Static method (utilities fonctions ex conversion)
    @staticmethod
    def convert(amount):
        amount = amount * 1.2
        return amount


# Instance variables :
hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")
hotel1.name
hotel2.name

# Class variable
print(Hotel.watermark)
print(hotel1.watermark)
print(hotel2.watermark)

# Class  method
print(Hotel.get_count(data=df))
print(hotel1.get_count(df))

# property
hotel = Hotel(hotel_id=188)
ticket = ReservationTicket(customer_name="IBRAHIMA BaRRY ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())
print(ReservationTicket.convert(33.32))

h1 = hotel1
h2 = hotel1
h1 == h2
