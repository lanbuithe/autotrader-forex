from autotrader import AutoTrader
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
from myautotrader import MyAutoTrader

def trade():
    # Create AutoTrader instance, configure it, and run paper mode
    at = AutoTrader()

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

def stop_active_bot():
    #
    print(f"The stop active bot task has run at {datetime.now()}")
    base_dir = './active_bots'
    files = [f for f in os.listdir(base_dir) if f.startswith('autotrader_instance')]
    for f in files:
        print(f"{base_dir} folder contain {f}")
        tokenize = f.split('_')
        full_path = os.path.join(base_dir, f)
        if int(tokenize[-1]) > 1:
            os.remove(full_path)
            print(f"Deleted {full_path}")

def start_scheduler():
    scheduler = BlockingScheduler(timezone='America/Vancouver')
    # interval hours=, minutes=, seconds=
    interval = 15
    scheduler.add_job(trade, 'interval', minutes=interval)
    scheduler.add_job(stop_active_bot, 'interval', minutes=interval)
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
