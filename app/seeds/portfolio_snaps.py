from app.models import db, Portfolio_Snap

def seed_portfolio_snaps():

  portfolio_snap1 = Portfolio_Snap(
    value=2000.00, portfolio_id=1)

  portfolio_snap2 = Portfolio_Snap(
    value=543.45, portfolio_id=2)

  db.session.add(portfolio_snap1)
  db.session.add(portfolio_snap2)

  db.session.commit()



def undo_portfolio_snaps():
    db.session.execute('TRUNCATE portfolio_snaps RESTART IDENTITY CASCADE;')
