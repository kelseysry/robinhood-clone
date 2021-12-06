from flask import Blueprint, jsonify
from app.models import Stock

stock_routes = Blueprint('stocks', __name__)


@stock_routes.route('/<ticker>')
def get_stock(ticker):
    stock = Stock.query.filter(Stock.ticker==ticker).first().to_dict()
    print("hello", stock)
    return {"stock":stock}



    # this_pony = Pony.query.filter(Pony.name=='Alice').first()
    # not_alice = Pony.query.filter(Pony.name != 'Alice').all()
    # name_te_include = Pony.query.filter(Pony.name.ilike("%te%")).all()
    # old_ponies = Pony.query.filter(Pony.birth_year < 2000).all()
    # in_list = Pony.query.filter(Pony.birth_year.in_([1993, 2002]))
    # not_in_list = Pony.query.filter(Pony.birth_year.notin_([1993, 2002]))
    # last_two_ponies = Pony.query.order_by(Pony.name.desc()).limit(2)
