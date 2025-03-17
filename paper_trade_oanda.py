from autotrader import AutoTrader

# Create AutoTrader instance, configure it, and run paper mode
at = AutoTrader()

at.configure(verbosity=2, 
             feed="oanda", 
             broker="oanda", 
             home_currency="CAD",
             show_plot=True)

at.add_strategy("ema_crossover")

at.run()
