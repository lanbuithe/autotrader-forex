from autotrader import AutoTrader
#from myoanda import Broker
from myautotrader import MyAutoTrader

# Create AutoTrader instance, configure it, and run paper mode
at = MyAutoTrader()

at.configure(verbosity=2, 
             feed="oanda", 
             broker="myoanda", 
             notify=1,
             notification_provider="telegram",
             home_currency="CAD",
#             allow_dancing_bears=True,
#             environment="live",
             show_plot=True)

at.add_strategy("ema_crossover")

at.run()
