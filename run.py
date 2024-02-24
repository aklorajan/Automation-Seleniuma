from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    print('exiting ...')
    bot.change_currency(currency='GBP')

