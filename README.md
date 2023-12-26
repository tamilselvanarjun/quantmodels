#### quantmodels

#### Overview

`quantmodels` is a Python package that provides implementations of various financial models commonly used in finance and investment analysis.

#### Installation

You can install the package using pip:
pip install quantmodels

Included Financial Models
1. Binomial Option Pricing Model (BOPM)
The Binomial Option Pricing Model is a numerical method used for option pricing. It calculates the option price and call option price based on parameters such as underlying price, strike price, risk-free rate, volatility, time to maturity, and the number of steps in the binomial tree


from quantmodels.opm import binomial_option_pricing

#### Example usage for Put Option Price

Parameters
underlying_price: Current price of the underlying asset.

strike_price: Strike price of the option.

risk_free_rate: Risk-free interest rate.

volatility: Volatility of the underlying asset.

time_to_maturity: Time to maturity of the option.

num_steps: Number of steps in the binomial tree.

```bash
call_price = binomial_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, periods, 'call')

put_price = binomial_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, periods, 'put')

print(f"Call Option Price: {call_price:.2f}")
print(f"Put Option Price: {put_price:.2f}")
```
#### Example usage for Black-Scholes Option Pricing Model

The Black-Scholes Option Pricing Model is a mathematical model used for pricing options. It calculates the option price based on parameters such as underlying price, strike price, risk-free rate, volatility, and time to maturity.

**Usage:**

```python
from quantmodels.opm import black_scholes_option_pricing

# Example usage for Black-Scholes Option Pricing Model
call_price_bs = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'call')
put_price_bs = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'put')


```bash
implied_volatility_call = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'call')
implied_volatility_put = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'put')
```