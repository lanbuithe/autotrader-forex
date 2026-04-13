from autotrader import AutoTrader
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import urllib3

def trade():
    # Create AutoTrader instance, configure it, and run paper mode
    at = AutoTrader()
    at.configure(verbosity=3, 
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
    at.add_strategy("long_ema_crossover")
    at.add_strategy("macd")
    #at.add_strategy("supertrend")
    
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

def scrap():
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Define the initial URL that may redirect
    initial_url = "https://autotrader-forex.streamlit.app/"

    try:
        # Make a GET request with allow_redirects set to True
        response = http.request('GET', initial_url, redirect=True)

        # Check if the request was successful (status code 200)
        if response.status == 200:
            # Print the final response URL after following redirects
            print("Final Response URL:")
            print(response.geturl())
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch data. Status Code: {response.status}")
    
    except urllib3.exceptions.RequestError as e:
        print(f"Error: {e}")

def start_scheduler():
    scheduler = BlockingScheduler(timezone='America/Vancouver')
    # interval hours, minutes, seconds
    scheduler.add_job(trade, 'interval', minutes=10)
    #scheduler.add_job(stop_active_bot, 'interval', minutes=15)
    scheduler.add_job(scrap, 'interval', hours=1)
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
