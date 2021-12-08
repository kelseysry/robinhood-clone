from flask import Blueprint, jsonify
from app.models import Stock

stock_routes = Blueprint('stocks', __name__)


@stock_routes.route('/<ticker>')
def get_stock(ticker):
    stock = Stock.query.filter(Stock.ticker==ticker).first().to_dict()
    return stock
    # return {"stock":stock}


# add route for adding a stock? 
