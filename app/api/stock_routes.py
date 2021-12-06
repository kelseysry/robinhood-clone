from flask import Blueprint, jsonify
from app.models import Stock

stock_routes = Blueprint('stocks', __name__)


@stock_routes.route('/<ticker>')
def get_stock(ticker):
    stock = Stock.query.filter(Stock.ticker==ticker).first().to_dict()
    print("stock in api", stock)
    return {"stock":stock}
