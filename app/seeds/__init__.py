from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stocks import seed_stocks, undo_stocks
from .banks import seed_banks, undo_banks
from .portfolios import seed_portfolios, undo_portfolios
from .fills import seed_fills, undo_fills
from .news import seed_news, undo_news
from .watch_lists import seed_watchlists, undo_watchlists
from .portfolio_snaps import seed_portfolio_snaps, undo_portfolio_snaps

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_banks()
    seed_users() # look in /seeds/users.py to see seed_users() function
    seed_news()
    seed_stocks()
    seed_portfolios()
    seed_watchlists()
    seed_portfolio_snaps()
    seed_fills()




# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_fills()
    undo_portfolio_snaps()
    undo_watchlists()
    undo_portfolios()
    undo_stocks()
    undo_news()
    undo_users()
    undo_banks()
