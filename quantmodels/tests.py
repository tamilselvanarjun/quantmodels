import unittest
from option_pricing import binomial_option_pricing, black_scholes_option_pricing, black_scholes_implied_volatility

class TestOptionPricing(unittest.TestCase):

    def test_binomial_option_pricing(self):
        
        call_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'call')
        self.assertAlmostEqual(call_price, 10.4506, places=4)

        # Test put option pricing using binomial model.
        put_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'put')
        self.assertAlmostEqual(put_price, 5.5735, places=4)