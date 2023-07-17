import json
from flask import Flask, request, jsonify, Response
from app.utils import *
from app.db.flight import *
from app.db.hotel import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Testing Flask App"

@app.route('/flight')
def flight():
    args = request.args

    # missing query params
    try:
        departure_date = args['departureDate']
        return_date = args['returnDate']
        destination = args['destination']
    except:
        return Response("failed query parameters", status=400)
    
    # check ISO date format
    if not verify_date(departure_date):
        return Response("wrong departure date format", status=400)
    
    if not verify_date(return_date):
        return Response("wrong return date format", status=400)
    
    # check return_date > departure_date
    if not is_date_greater_or_equal(start_date=departure_date, end_date=return_date):
        return Response("return is earlier than departure", status=400)
    
    departure_date = convert_to_datetime(departure_date)
    return_date = convert_to_datetime(return_date)

    # get the cheapest flights
    response_list = get_cheapest_flight_list(destination, departure_date, return_date)

    return Response(json.dumps(response_list), status=200)
    
@app.route('/hotel')
def hotel():
    args = request.args

    # missing query params
    try:
        check_in_date = args['checkInDate']
        check_out_date = args['checkOutDate']
        destination = args['destination']
    except:
        return Response("failed query parameters", status=400)
    
    # check ISO date format
    if not verify_date(check_in_date):
        return Response("wrong departure date format", status=400)
    
    if not verify_date(check_out_date):
        return Response("wrong return date format", status=400)
    
    # check check_out_date > check_in_date
    if not is_date_greater_or_equal(start_date=check_in_date, end_date=check_out_date):
        return Response("return is earlier than departure", status=400)
    
    check_in_date = convert_to_datetime(check_in_date)
    check_out_date = convert_to_datetime(check_out_date)

    # get the cheapest hotels for those dates
    response_list = get_cheapest_hotel_list(destination, check_in_date, check_out_date)

    return Response(json.dumps(response_list), status=200)