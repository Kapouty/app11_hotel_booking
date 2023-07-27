import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_card = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you
        your reservation is:
        Name:{self.customer_name}
        your hotel is {self.hotel.name}"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_card:
            return True
        else:
            return False


class CreditCardSecurity(CreditCard):
    def authentificate(self, given_pwd):
        pwd = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if given_pwd == pwd:
            return True
        else:
            return False


class SpaReservation(Hotel):
    def generate(self):
        content = f"""

            Here is your SPA booking data:
            Name:{ reservation_ticket.customer_name}
            your hotel is {spa_reservation.name}"""
        return content


print(df)
hotel_id = input("Enter a hotel ID")
hotel = Hotel(hotel_id)
if hotel.available():
    credit_card = CreditCardSecurity(number="5678")
    credit_card.validate(expiration="12/28", holder="JANE SMITH", cvc="456")
    if credit_card.validate(expiration="12/28", holder="JANE SMITH", cvc="456"):
        credit_card.authentificate(given_pwd="mypass")
        if credit_card.authentificate(given_pwd="mypass"):
            hotel.book()
            name = input("Enter your name:")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            spa_demand = input("Do you want to reserve a SPA ?")
            spa_reservation = SpaReservation(hotel_id)
            print(reservation_ticket.generate())
            if spa_demand:
                print(spa_reservation.generate())
    else:
        print("Credit card validation failed !")



else:
    print("Hotel is not available")
