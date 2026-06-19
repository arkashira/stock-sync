from stock_sync import forecast_stock_level, StockLevel

def test_forecast_stock_level():
    current_level = 100
    historical_data = [90, 110, 105]
    stock_level = forecast_stock_level(current_level, historical_data)
    assert stock_level.current_level == 100
    assert stock_level.forecasted_level == 101

def test_forecast_stock_level_empty_historical_data():
    current_level = 100
    historical_data = []
    stock_level = forecast_stock_level(current_level, historical_data)
    assert stock_level.current_level == 100
    assert stock_level.forecasted_level == 100

def test_forecast_stock_level_zero_current_level():
    current_level = 0
    historical_data = [10, 20, 30]
    stock_level = forecast_stock_level(current_level, historical_data)
    assert stock_level.current_level == 0
    assert stock_level.forecasted_level == 20
