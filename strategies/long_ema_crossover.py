# Import packages
from finta import TA
from autotrader import Order
from autotrader.indicators import crossover


class LongEMAcrossOver:
    """Long EMA Crossover example strategy."""

    def __init__(self, parameters, data, instrument):
        """Define all indicators used in the strategy."""
        self.name = "Strategy name"
        self.data = data
        self.params = parameters
        self.instrument = instrument

        # EMA's
        self.slow_ema = TA.EMA(data, self.params["slow_ema"])

        self.fast_ema = TA.EMA(data, self.params["fast_ema"])

        self.crossovers = crossover(self.fast_ema, self.slow_ema)

        # Construct indicators dict for plotting
        self.indicators = {
            "Fast EMA": {"type": "MA", "data": self.fast_ema},
            "Slow EMA": {"type": "MA", "data": self.slow_ema},
        }

    
