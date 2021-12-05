from app.models import db, Stock


# Adds a demo user, you can add other users here if you want
def seed_stocks():
    stock1 = Stock(
    name='Tesla',
    ticker='TSLA',
    about='Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles, energy generation and storage systems. It also provides vehicle service centers, supercharger station, and self-driving capability.',
    ceo='Elon Reeve Musk',
    employee_count=70757,
    headquarters='Palo Alto, California',
    founded=2003,
    market_cap='1.02T',
    dividend_yield =0,
    price_earnings_ratio=328.64,
    average_volume='24.91M',
    high_today=1090.58,
    low_today=1000.21,
    open_price=1084.67,
    volume='30.77M',
    week52_high=1243.49,
    week52_low=539.49,
    news_id=2,
    market_price=1008.00
  )


    stock2 = Stock(
    name='Square',
    ticker='SQ',
    about='Square, Inc. engages in the provision of credit card payment processing solutions. It is a cohesive commerce ecosystem that helps sellers start, run, and grow their businesses.',
    ceo='Jack Dorsey',
    employee_count=5477,
    headquarters='San Francisco, California',
    founded=2009,
    market_cap='83.63',
    dividend_yield =0,
    price_earnings_ratio=172.07,
    average_volume='10.86M',
    high_today=191.32,
    low_today=174.34,
    open_price=191.31,
    volume='19.17M',
    week52_high=289.23,
    week52_low=174.34,
    news_id=2,
    market_price=181.15
        )


    db.session.add(stock1)
    db.session.add(stock2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_stocks():
    db.session.execute('TRUNCATE stocks RESTART IDENTITY CASCADE;') # drop all users in db, included ones you submitted via form
    db.session.commit()
