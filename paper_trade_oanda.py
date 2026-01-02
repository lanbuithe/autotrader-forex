from autotrader import AutoTrader
#from myoanda import Broker
from myautotrader import MyAutoTrader

# Create AutoTrader instance, configure it, and run paper mode
at = MyAutoTrader()

at.configure(home_currency="CAD",
             verbosity=1, 
             feed="oanda", 
             broker="myoanda", 
             notify=1,
             notification_provider="telegram",
#ERROR             allow_dancing_bears=True,
#ERROR             environment="live",
#ERROR             mode="continuous",
             update_interval="1h",
             show_plot=True)

at.add_strategy("ema_crossover")

at.run()
