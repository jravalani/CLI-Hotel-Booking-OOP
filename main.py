import pandas as pd

df = pd.read_csv("hotels.csv")
card_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
card_security_df = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def is_available(self):
        """Check if the hostel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass

class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA Reservation!
        Here are your details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.card_number = number

    def is_valid(self, expiration, holder, cvc):
        card_data = {"number": self.card_number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in card_df:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def is_authenticate(self, given_password):
        password = card_security_df.loc[card_security_df["number"] == self.card_number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False



print(df)
hotel_ID = int(input("Enter the id of the hotel: "))
hotel = SpaHotel(hotel_ID)

if hotel.is_available():
    number = input("Enter your credit card number: ")
    credit_card = SecureCreditCard(number=number)
    if credit_card.is_valid(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.is_authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Card not authenticated successfully!")
    else:
        print("Credit card is not valid!")
    spa_answer = input("Would you like to book a spa package? (yes/no): ")
    if spa_answer == "yes":
        hotel.book_spa_package()
        spa_ticket = SpaReservationTicket(name, hotel)
        print(spa_ticket.generate())
    else:
        pass
else:
    print("Hotel is currently full.")
