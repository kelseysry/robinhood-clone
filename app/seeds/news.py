from app.models import db, News

def seed_news():
    news1 = News(
        publisher='Bloomberg',
        title='Elon Musk’s Wealth Drops $15 Billion as Tech Stocks Plunge',
        description='The richest U.S. tech moguls dropped tens of billions in collective wealth as technology stocks tumbled amid fears of inflation and economic tightening.',
        image_url='https://s.yimg.com/ny/api/res/1.2/J2yrVIZboxCUiVIx7QC1Tw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/s50Dsu2ccTO6z_F_L4dOWA--~B/aD0xMzM0O3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/bloomberg_markets_842/29435adc498fdd22d23c447dacbe5dd1',
        date_published='Dec 3'
        )




    db.session.add(news1)

    db.session.commit()



def undo_news():
    db.session.execute('TRUNCATE news RESTART IDENTITY CASCADE;')
    db.session.commit()
