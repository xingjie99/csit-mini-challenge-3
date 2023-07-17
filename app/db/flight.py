import sys
from app.db import *
from app.models import *

def extract_cheapest_departure_flights(destination, departure_date):
    cheapest_departure_flights = []
    cheapest_price = sys.maxsize

    collection = db['flights']
    results = collection.find({"srccity": "Singapore", 
                               "destcity": destination, 
                               "date": departure_date})
    
    for result in results:
        if result['price'] < cheapest_price:
            cheapest_departure_flights.clear()
            cheapest_departure_flights.append(result)
            cheapest_price = result['price']
            continue

        if result['price'] == cheapest_price:
            cheapest_departure_flights.append(result)
            continue

    return cheapest_departure_flights


def extract_cheapest_return_flights(destination, return_date):
    cheapest_return_flights = []
    cheapest_price = sys.maxsize

    collection = db['flights']
    results = collection.find({"srccity": destination, 
                               "destcity": "Singapore", 
                               "date": return_date})

    for result in results:
        if result['price'] < cheapest_price:
            cheapest_return_flights.clear()
            cheapest_return_flights.append(result)
            cheapest_price = result['price']
            continue

        if result['price'] == cheapest_price:
            cheapest_return_flights.append(result)
            continue

    return cheapest_return_flights


def get_cheapest_flight_list(destination, departure_date, return_date):
    cheapest_flight_list = []

    cheapest_departure_flight_list = extract_cheapest_departure_flights(destination=destination, departure_date=departure_date)
    cheapest_return_flight_list = extract_cheapest_return_flights(destination=destination, return_date=return_date)

    for departure_flight in cheapest_departure_flight_list:
        for return_flight in cheapest_return_flight_list:
            flight_instance = vars(FlightResponse(city=departure_flight['destcity'],
                                                  departure_date=departure_date.strftime("%Y-%m-%d"),
                                                  departure_airline=departure_flight['airlinename'],
                                                  departure_price=departure_flight['price'],
                                                  return_date=return_date.strftime("%Y-%m-%d"),
                                                  return_airline=return_flight['airlinename'],
                                                  return_price=return_flight['price']
                                                  ))
            cheapest_flight_list.append(flight_instance)
    
    return cheapest_flight_list
