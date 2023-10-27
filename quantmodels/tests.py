import unittest
from option_pricing import binomial_option_pricing, black_scholes_option_pricing, black_scholes_implied_volatility

class TestOptionPricing(unittest.TestCase):

    def test_binomial_option_pricing(self):
        # Test call option pricing using binomial model
        call_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'call')
        self.assertAlmostEqual(call_price, 10.4506, places=4)

        # Test put option pricing using binomial model
        put_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'put')
        self.assertAlmostEqual(put_price, 5.5735, places=4)
        
     def test_black_scholes_option_pricing(self):
        # Test call option pricing using Black-Scholes model
        call_price = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'call')
        self.assertAlmostEqual(call_price, 10.4506, places=4)

        # Test put option pricing using Black-Scholes model
        put_price = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'put')
        self.assertAlmostEqual(put_price, 5.5735, places=4)
        
    def test_black_scholes_implied_volatility(self):
        # Test implied volatility calculation using Black-Scholes model for call option
        implied_volatility_call = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'call')
        self.assertAlmostEqual(implied_volatility_call, 0.2000, places=4)

        # Test implied volatility calculation using Black-Scholes model for put option
        implied_volatility_put = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'put')
        self.assertAlmostEqual(implied_volatility_put, 0.2000, places=4)