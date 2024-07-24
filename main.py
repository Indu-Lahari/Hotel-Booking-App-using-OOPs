import pandas
df = pandas.read_csv("hotels.csv")


class User:
    pass


class Hotel:
    # View list of hotels
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, user_name, hotel_name):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel:")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name:")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free.")
