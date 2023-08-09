import math
from scipy.stats import norm
from scipy.optimize import newton
import logging

# Configure logging
logging.basicConfig(filename='option_pricing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

# Commented out the Example Usage block
# if __name__ == "__main__":
#     logging.info("Calculating binomial option pricing")
#     call_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'call')
#     put_price = binomial_option_pricing(100, 100, 1, 0.05, 0.2, 100, 'put')
#     logging.info(f"Binomial Call Option Price: {call_price:.2f}")
#     logging.info(f"Binomial Put Option Price: {put_price:.2f}")
# 
#     logging.info("Calculating Black-Scholes option pricing")
#     call_price_bs = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'call')
#     put_price_bs = black_scholes_option_pricing(100, 100, 1, 0.05, 0.2, 'put')
#     logging.info(f"Black-Scholes Call Option Price: {call_price_bs:.2f}")
#     logging.info(f"Black-Scholes Put Option Price: {put_price_bs:.2f}")
# 
#     logging.info("Calculating Black-Scholes implied volatility")
#     implied_volatility_call = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'call')
#     implied_volatility_put = black_scholes_implied_volatility(10, 100, 100, 1, 0.05, 'put')
#     logging.info(f"Implied Volatility for Call Option: {implied_volatility_call:.4f}")
#     logging.info(f"Implied Volatility for Put Option: {implied_volatility_put:.4f}")