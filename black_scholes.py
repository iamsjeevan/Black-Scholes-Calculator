import numpy as np
from scipy.stats import norm
from numpy import log, sqrt, exp

class BlackScholes:
    def __init__(self, time_to_maturity, strike, current_price, volatility, interest_rate):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def calculate_prices(self):
        d1 = (log(self.current_price / self.strike) +
              (self.interest_rate + 0.5 * self.volatility ** 2) * self.time_to_maturity) / (
                 self.volatility * sqrt(self.time_to_maturity)
              )
        d2 = d1 - self.volatility * sqrt(self.time_to_maturity)

        call_price = self.current_price * norm.cdf(d1) - (self.strike * exp(-self.interest_rate * self.time_to_maturity) * norm.cdf(d2))
        put_price = (self.strike * exp(-self.interest_rate * self.time_to_maturity) * norm.cdf(-d2)) - self.current_price * norm.cdf(-d1)

        # GREEKS
        call_delta = norm.cdf(d1)
        put_delta = 1 - norm.cdf(d1)

        # Gamma for both Call and Put
        call_gamma = norm.pdf(d1) / (self.strike * self.volatility * sqrt(self.time_to_maturity))
        put_gamma = call_gamma

        return call_price, put_price, call_delta, put_delta, call_gamma, put_gamma
