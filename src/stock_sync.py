import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import argparse

@dataclass
class StockLevel:
    current_level: int
    forecasted_level: int

def forecast_stock_level(current_level: int, historical_data: list) -> StockLevel:
    """
    Forecast the stock level based on historical data.

    Args:
    - current_level (int): The current stock level.
    - historical_data (list): A list of historical stock levels.

    Returns:
    - StockLevel: An object containing the current and forecasted stock levels.
    """
    if not historical_data:
        return StockLevel(current_level, current_level)

    # Simple moving average forecast
    forecasted_level = sum(historical_data) / len(historical_data)
    return StockLevel(current_level, int(forecasted_level))

def main():
    parser = argparse.ArgumentParser(description='Stock Sync')
    parser.add_argument('--current_level', type=int, help='Current stock level')
    parser.add_argument('--historical_data', type=json.loads, help='Historical stock levels')
    args = parser.parse_args()

    stock_level = forecast_stock_level(args.current_level, args.historical_data)
    print(f"Current stock level: {stock_level.current_level}")
    print(f"Forecasted stock level: {stock_level.forecasted_level}")

if __name__ == "__main__":
    main()
