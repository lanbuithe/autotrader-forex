from autotrader import AutoTrader

at = AutoTrader()
at.configure(verbosity=3, 
            feed="oanda", 
            broker="oanda", 
            mode="continuous", 
            notify=1,
            notification_provider="telegram",
            home_currency="CAD",
            allow_dancing_bears=True,
            allow_duplicate_bars=True)
    
at.add_strategy("ema_crossover")
#at.add_strategy("long_ema_crossover")
at.add_strategy("macd")
#at.add_strategy("supertrend")
    
at.run()
