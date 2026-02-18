import http.server
import socketserver
#from autotrader import AutoTrader
#from myoanda import Broker
from myautotrader import MyAutoTrader

###
PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Start the server and keep it running until you stop the script
    httpd.serve_forever()

# Create AutoTrader instance, configure it, and run paper mode
at = MyAutoTrader()

at.configure(home_currency="CAD",
             verbosity=3, 
             feed="oanda", 
             broker="myoanda", 
             notify=1,
             notification_provider="telegram",
#ERROR             allow_dancing_bears=True,
#ERROR             environment="live",
#ERROR             mode="continuous",
#ERROR             update_interval="1h",
             show_plot=True)

at.add_strategy("ema_crossover")
at.add_strategy("long_ema_crossover")
at.add_strategy("macd")
at.add_strategy("supertrend")

at.run()



