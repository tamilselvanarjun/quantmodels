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