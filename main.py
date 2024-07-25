import pandas
df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


class User:
    pass


class Hotel:
    # View list of hotels
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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
        self.user_name = user_name
        self.hotel = hotel_name

    def generate(self):
        content = f"""
        Thank you for your reservation
        Here is your booking date:
        Name: {self.user_name}
        Hotel Name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


# Inheritance: CreditCard- Parent class & SecureCreditCard - Child class
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel = Hotel(hotel_ID)

# Main Loops
if hotel.available():
    credit_card = SecureCreditCard(number="1234")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name:")
            reservation_ticket = ReservationTicket(user_name=name, hotel_name=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed !")
    else:
        print("Payment Unsuccessful! Check your details")
else:
    print("Hotel is not free.")
