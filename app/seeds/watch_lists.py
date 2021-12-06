from app.models import db, WatchList

def seed_watchlists():

  watchlist1 = WatchList(
    userId=1, stock_id=1)

  watchlist2 = WatchList(
    userId=2, stock_id=2)


  db.session.add(watchlist1)
  db.session.add(watchlist2)
  # db.session.add(watchlist3)

  db.session.commit()



def undo_watchlists():
    db.session.execute('TRUNCATE watchlists RESTART IDENTITY CASCADE;')
