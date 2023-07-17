import sys
from app.db import *
from app.models import *
from app.utils import *

def get_cheapest_hotel_list(destination, check_in_date, check_out_date):
    cheapest_hotel_list = []
    result_dict = {}

    collection = db['hotels']
    results = collection.find({"city": destination,
                               "date" : {"$gte": check_in_date, "$lte": check_out_date}})
    for result in results:
        if result_dict.get(result['hotelName']):
            result_dict[result['hotelName']]['price'] += result['price']
            result_dict[result['hotelName']]['count'] += 1
        else:
            result_dict[result['hotelName']] = { 'price': int(result['price']), 'count': 1}

    total_days = get_number_of_days(start_date=check_in_date, end_date=check_out_date)
    cheapest_price = sys.maxsize
    cheapest_hotel_name_list = []

    for key, value in result_dict.items():
        if value['count'] == total_days:
            if value['price'] < cheapest_price:
                cheapest_hotel_name_list.clear()
                cheapest_hotel_name_list.append(key)
                cheapest_price = value['price']
                continue

            if value['price'] == cheapest_price:
                cheapest_hotel_name_list.append(key)
                continue
    
    for hotel in cheapest_hotel_name_list:
        # hotel_instance = vars(HotelResponse(city=destination,
        #                                     check_in_date=check_in_date.strftime("%Y-%m-%d"),
        #                                     check_out_date=check_out_date.strftime("%Y-%m-%d"),
        #                                     hotel=hotel,
        #                                     price=result_dict[hotel]['price']
        #                                     ))
        hotel_instance = {
            "City": destination,
            "Check In Date": check_in_date.strftime("%Y-%m-%d"),
            "Check Out Date": check_out_date.strftime("%Y-%m-%d"),
            "Hotel": hotel,
            "Price": result_dict[hotel]['price']
        }
        cheapest_hotel_list.append(hotel_instance)
    

    return cheapest_hotel_list