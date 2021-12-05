from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name='Demo', last_name='User', username='Demo', email='demo@aa.io', password='password', buying_power=10000, bank_id=5)
    kelsey = User(
        first_name='Kelsey', last_name='Sry', username='kelsey', email='kelsey@aa.io', password='password', buying_power=3000, bank_id=1)
    lisa = User(
        first_name='Lisa', last_name='Sry', username='lisa', email='lisa@aa.io', password='password', buying_power=5000, bank_id=3)

    db.session.add(demo)
    db.session.add(kelsey)
    db.session.add(lisa)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;') # drop all users in db, included ones you submitted via form
    db.session.commit()
