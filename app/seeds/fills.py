from app.models import db, Fill

def seed_fills():
    fill1 = Fill(
        portfolio_id=1, stock_id=1, shares=2)
    fill1 = Fill(
        portfolio_id=2, stock_id=2, shares=3)

    db.session.add(fill1)
    db.session.add(fill2)

    db.session.commit()



def undo_fills():
    db.session.execute('TRUNCATE fills RESTART IDENTITY CASCADE;') 
    db.session.commit()
