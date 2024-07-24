import pandas
df = pandas.read_csv("hotels.csv", dtype=str)


class User:
    pass


class Hotel:
    # View list of hotels
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        # Squeeze is used to produce string instead of index like '0 id'
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, user_name, hotel_name):
        pass

    def generate(self):
        pass


print(df)
hotel_id = input("Enter the id of the hotel:")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name:")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free.")
