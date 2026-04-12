from autotrader import AutoTrader
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

def trade():
    # Create AutoTrader instance, configure it, and run paper mode
    at = AutoTrader()
    at.configure(verbosity=2, 
                feed="oanda", 
                broker="oanda", 
                mode="continuous", 
                notify=1,
                notification_provider="telegram",
                home_currency="CAD",
                allow_dancing_bears=True,
                show_plot=True,
                allow_duplicate_bars=True)
    at.add_strategy("ema_crossover")
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
    # interval hours, minutes, seconds
    scheduler.add_job(trade, 'interval', hours=1)
    #scheduler.add_job(stop_active_bot, 'interval', minutes=10)
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
