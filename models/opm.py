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
