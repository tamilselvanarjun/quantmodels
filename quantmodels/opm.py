import math
from scipy.stats import norm
from scipy.optimize import newton
import math

def binomial_option_pricing(S, K, T, r, sigma, n, option_type='call'):
    dt = T / n
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)

    option_values = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(n + 1):
        option_values[n][j] = max(0, S * (u**j) * (d**(n - j)) - K if option_type == 'call' else K - S * (u**j) * (d**(n - j)))

    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option_values[i][j] = math.exp(-r * dt) * (p * option_values[i + 1][j + 1] + (1 - p) * option_values[i + 1][j])

    return option_values[0][0]

# Example Usage
#if __name__ == "__main__":
#    underlying_price = 100  # Current price of the underlying asset
#    strike_price = 100      # Strike price of the option
#    time_to_maturity = 1    # Time to maturity in years
#    risk_free_rate = 0.05   # Risk-free interest rate
#    volatility = 0.2       # Volatility of the underlying asset
#    periods = 100           # Number of periods in the binomial model

#    call_price = binomial_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, periods, 'call')
#    put_price = binomial_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, periods, 'put')
#    print(f"Call Option Price: {call_price:.2f}")
#    print(f"Put Option Price: {put_price:.2f}")

def black_scholes_option_pricing(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * math.exp(-r * T) * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * math.exp(-r * T) * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    return price
    
# Example Usage
if __name__ == "__main__":
    underlying_price = 100  # Current price of the underlying asset
    strike_price = 100      # Strike price of the option
    time_to_maturity = 1    # Time to maturity in years
    risk_free_rate = 0.05   # Risk-free interest rate
    volatility = 0.2        # Volatility of the underlying asset

    call_price = black_scholes_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, 'call')
    put_price = black_scholes_option_pricing(underlying_price, strike_price, time_to_maturity, risk_free_rate, volatility, 'put')
    print(f"Black-Scholes Call Option Price: {call_price:.2f}")
    print(f"Black-Scholes Put Option Price: {put_price:.2f}")


def black_scholes_implied_volatility(option_price, S, K, T, r, option_type='call'):
    def black_scholes_price(sigma):
        d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        if option_type == 'call':
            price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        elif option_type == 'put':
            price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")

        return price - option_price

    implied_volatility = newton(black_scholes_price, x0=0.5)

    return implied_volatility

# Example Usage
# if __name__ == "__main__":
#     option_price = 10            # Market price of the option
#     underlying_price = 100       # Current price of the underlying asset
#     strike_price = 100           # Strike price of the option
#     time_to_maturity = 1         # Time to maturity in years
#     risk_free_rate = 0.05        # Risk-free interest rate
# 
#     implied_volatility_call = black_scholes_implied_volatility(option_price, underlying_price, strike_price, time_to_maturity, risk_free_rate, 'call')
#     implied_volatility_put = black_scholes_implied_volatility(option_price, underlying_price, strike_price, time_to_maturity, risk_free_rate, 'put')
#     
#     print(f"Implied Volatility for Call Option: {implied_volatility_call:.4f}")
#     print(f"Implied Volatility for Put Option: {implied_volatility_put:.4f}")
