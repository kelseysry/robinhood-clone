from app.models import db, Bank

def seed_banks():
    bank1 = Bank(
        bank_name='Chase')
    bank2 = Bank(
        bank_name='Wells Fargo')
    bank3 = Bank(
        bank_name='Bank Of America')
    bank4 = Bank(
        bank_name='Capital One')
    bank5 = Bank(
        bank_name='US Bank')
    bank6 = Bank(
        bank_name='Arvest')
    bank7 = Bank(
        bank_name='Citizens')

    db.session.add(bank1)
    db.session.add(bank2)
    db.session.add(bank3)
    db.session.add(bank4)
    db.session.add(bank5)
    db.session.add(bank6)
    db.session.add(bank7)

    db.session.commit()



def undo_banks():
    db.session.execute('TRUNCATE banks RESTART IDENTITY CASCADE;') # drop all users in db, included ones you submitted via form
    db.session.commit()
