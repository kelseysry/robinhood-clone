from app.models import db, Portfolio

def seed_portfolios():
    portfolio1 = Portfolio(
        userId=1)
    portfolio2 = Portfolio(
        userId=2)
    portfolio3 = Portfolio(
        userId=3)
    # portfolio4 = Portfolio(
    #     userId=4)
    # portfolio5 = Portfolio(
    #     userId=5)
    # portfolio6 = Portfolio(
    #     userId=6)
    # portfolio7 = Portfolio(
    #     userId=7)

    db.session.add(portfolio1)
    db.session.add(portfolio2)
    db.session.add(portfolio3)
    # db.session.add(portfolio4)
    # db.session.add(portfolio5)
    # db.session.add(portfolio6)
    # db.session.add(portfolio7)

    db.session.commit()



def undo_portfolios():
    db.session.execute('TRUNCATE portfolios RESTART IDENTITY CASCADE;') 
    db.session.commit()
