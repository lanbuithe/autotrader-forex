# Import packages
from finta import TA
from autotrader import Order
from autotrader.indicators import crossover


class LongEMAcrossOver:
    """Long EMA Crossover example strategy."""

    def __init__(self, parameters, data, instrument):
        """Define all indicators used in the strategy."""
        self.name = "Long EMA Crossover Strategy"
        self.data = data
        self.params = parameters
        self.instrument = instrument

        # EMA's
        self.slow_ema = TA.EMA(data, self.params["slow_ema"])

        self.fast_ema = TA.EMA(data, self.params["fast_ema"])

        #self.crossovers = crossover(self.fast_ema, self.slow_ema)

        # Construct indicators dict for plotting
        self.indicators = {
            "Fast EMA": {"type": "MA", "data": self.fast_ema},
            "Slow EMA": {"type": "MA", "data": self.slow_ema},
        }
        
   def calculate_crossovers(self, data: DataFrame):
        """Calculates the indicators required to run the strategy."""
        # EMA's
        slow_ema = TA.EMA(data, self.params["slow_ema"])
        fast_ema = TA.EMA(data, self.params["fast_ema"])
        crossovers = crossover(fast_ema, slow_ema)
        return crossovers

    def generate_signal(self, dt: datetime):
        """Define strategy to determine entry signals."""
        orders = []

        # Get data and generate crossovers
        data = self.broker.get_candles(self.instrument, granularity="1h", count=300)
        if len(data) < 300:
            # Not ready to trade yet
            return None
        crossovers = self.calculate_crossovers(data)

        # Get current position
        current_position = self.broker.get_positions(self.instrument)

        # Put entry strategy here
        if len(current_position) == 0:
            # Not currently in any position, okay to enter long
            if crossovers.iloc[-1] == 1:
                # Fast EMA has crossed above slow EMA, enter long
                order = Order(
                    direction=1,
                    size=1,
                )
                orders.append(order)
        else:
            # Already in a position, only look for long exits
            if crossovers.iloc[-1] == -1:
                net_position = current_position[self.instrument].net_position
                order = Order(direction=-1, size=-net_position)
                orders.append(order)

        return orders



    
