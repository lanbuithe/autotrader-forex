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
                show_plot=True)

    at.add_strategy("ema_crossover")

    at.run()

def stop_active_bot():
    #
    print(f"The stop active bot task has run at {datetime.now()}")
    files = [f for f in os.listdir('./active_bots') if os.path.isfile(f)]
    for f in files:
        print(f"active_bots folder contain {f}")
        tokenize = f.split('_')
        if int(tokenize[-1] > 1):
            os.remove(f)
            print(f"Deleted {f}")

if __name__ == "__main__":
    trade()
    #scheduler = BlockingScheduler(timezone='US/Pacific')
    scheduler = BlockingScheduler()
    scheduler.add_job(stop_active_bot, 'interval', min=1)
    scheduler.start()