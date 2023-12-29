#### quantmodels

#### Overview

`quantmodels` is a Python package that provides implementations of various financial models commonly used in finance and investment analysis.

#### Installation

You can install the package using pip:
pip install quantmodels

Included Financial Models
1. Binomial Option Pricing Model (BOPM)
The Binomial Option Pricing Model is a numerical method used for option pricing. It calculates the option price and call option price based on parameters such as underlying price, strike price, risk-free rate, volatility, time to maturity, and the number of steps in the binomial tree

2. Black-Scholes Option Pricing Model (BSOPM)
The Black-Scholes Option Pricing Model is a widely used mathematical model for pricing European options. It calculates the theoretical price of call and put options based on parameters such as the current price of the underlying asset, the strike price of the option, the risk-free interest rate, the volatility of the underlying asset, and the time to maturity of the option.


from quantmodels.opm import binomial_option_pricing

#### Example usage for Binomial Option Pricing Model

The Binomial Option Pricing Model is a numerical method used for option pricing. It calculates the option price and call option price based on parameters such as underlying price, strike price, risk-free rate, volatility, time to maturity, and the number of steps in the binomial tree.

**Usage:**

```python
from quantmodels.opm import binomial_option_pricing

# Example usage for Binomial Option Pricing Model
underlying_price = 100  # Current price of the underlying asset
strike_price = 100      # Strike price of the option
time_to_maturity = 1    # Time to maturity in years
risk_free_rate = 0.05   # Risk-free interest rate
volatility = 0.2        # Volatility of the underlying asset
periods = 100           # Number of steps in the binomial tree

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
```

#### Example usage for Black-Scholes Implied Volatility

The Black-Scholes Implied Volatility is a method used to estimate the volatility of an underlying asset based on its option price. It calculates the implied volatility for call and put options based on parameters such as option price, underlying price, strike price, risk-free rate, and time to maturity.

**Usage:**

```python
from quantmodels.opm import black_scholes_implied_volatility

# Example usage for Black-Scholes Implied Volatility
implied_volatility_call = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'call')
implied_volatility_put = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'put')
```