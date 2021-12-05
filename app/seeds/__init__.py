from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stocks import seed_stocks, undo_stocks
from .banks import seed_banks, undo_banks

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users() # look in /seeds/users.py to see seed_users() function
    seed_stocks()
    seed_banks()
    # Add other seed functions here that you want to seed
    # from your database like
    # seed_items()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_stocks()
    undo_banks() 
    # Add other undo functions here
