import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
    watermark = "The ABC Corp"

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

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 6.10


hotel1 = Hotel(hotel_id=134)
hotel2 = Hotel(hotel_id=188)

print(hotel1.name)
print(hotel2.name)

print(hotel2.watermark)
print(hotel1.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel2.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="jay ravalani", hotel_object=hotel2)

print(ticket.the_customer_name)
print(ticket.customer_name)
print(ticket.hotel)

ticket.generate()

print(ticket.generate())

print(ReservationTicket.convert(20))
