
import connections

price = connections.get_price()

if price < 400:
    connections.send_email(price=price, url=connections.watch_url)







