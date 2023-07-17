class FlightResponse:
    def __init__(self, city, departure_date, departure_airline, departure_price, return_date, return_airline, return_price):
        self.city = city
        self.departure_date = departure_date
        self.departure_airline = departure_airline
        self.departure_price = departure_price
        self.return_date = return_date
        self.return_airline = return_airline
        self.return_price = return_price

class HotelResponse:
    def __init__(self, city, check_in_date, check_out_date, hotel, price):
        self.city = city
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.hotel = hotel
        self.price = price

