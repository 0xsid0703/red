import numpy as np
import requests
from properscoring import crps_ensemble
from scipy.stats import t

def get_asset_price(asset="BTC"):
    """
    Retrieves the current price of the specified asset.
    Currently, supports BTC via Pyth Network.

    Returns:
        float: Current asset price.
    """
    if asset == "BTC":
        btc_price_id = (
            "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43"
        )
        endpoint = f"https://hermes.pyth.network/api/latest_price_feeds?ids[]={btc_price_id}"  # TODO: this endpoint is deprecated
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()
            if not data or len(data) == 0:
                raise ValueError("No price data received")
            price_feed = data[0]
            price = float(price_feed["price"]["price"]) / (10**8)
            return price
        except Exception as e:
            print(f"Error fetching {asset} price: {str(e)}")
            return None
    else:
        # For other assets, implement accordingly
        print(f"Asset '{asset}' not supported.")
        return None


def simulate_single_price_path(
    current_price, time_increment, time_length, sigma
):
    """
    Simulate a single crypto asset price path using t-distribution.
    """
    one_hour = 3600
    dt = time_increment / one_hour
    num_steps = int(time_length / time_increment)
    std_dev = sigma * np.sqrt(dt)
    price_change_pcts = np.random.normal(0, std_dev, size=num_steps)
    cumulative_returns = np.cumprod(1 + price_change_pcts)
    cumulative_returns = np.insert(cumulative_returns, 0, 1.0)
    price_path = current_price * cumulative_returns

    return price_path

def generate_sigma(num_samples=100):
    # Define the ranges and their probabilities
    ranges = [(0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8)]
    probabilities = [0.10, 0.20, 0.20, 0.20, 0.20, 0.10]

    # Generate random numbers based on the specified ranges and probabilities
    sigmas = []
    for _ in range(num_samples):  # Generate 'num_samples' random numbers
        selected_range = np.random.choice(len(ranges), p=probabilities)
        low, high = ranges[selected_range]
        sigma = np.random.uniform(low, high)
        sigmas.append(sigma / 100)  # Scaling by 100 as per your previous code

    return sigmas

def simulate_crypto_price_paths(
    current_price, time_increment, time_length, num_simulations
):
    """
    Simulate multiple crypto asset price paths.
    """
    sigmas = generate_sigma(num_simulations)
    price_paths = []
    for i in range(num_simulations):
        price_path = simulate_single_price_path(
            current_price, time_increment, time_length, sigmas[i]
        )
        price_paths.append(price_path)

    return np.array(price_paths)
