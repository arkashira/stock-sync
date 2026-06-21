import pytest
from stock_sync import optimize_allocation, export_to_csv, load_data, SKU, FulfillmentCenter

def test_optimize_allocation():
    skus = [SKU(1, 'Test SKU', 100, 50)]
    centers = [FulfillmentCenter(1, 'Test Center', 10, 100)]
    allocation = optimize_allocation(skus, centers)
    assert allocation[1][1] == 50

def test_export_to_csv():
    allocation = {1: {1: 40}}
    csv = export_to_csv(allocation)
    assert csv == "SKU,Center,Quantity\n1,1,40\n"

def test_load_data():
    skus, centers = load_data('data.json')
    assert len(skus) == 1
    assert len(centers) == 1

def test_main():
    # This test is not ideal, but it's hard to test the main function without running it
    # We can test that it doesn't raise any exceptions
    try:
        from stock_sync import main
        main()
    except Exception as e:
        assert False, f"Main function raised an exception: {e}"

def test_optimize_allocation_edge_case():
    skus = [SKU(1, 'Test SKU', 100, 150)]
    centers = [FulfillmentCenter(1, 'Test Center', 10, 100)]
    allocation = optimize_allocation(skus, centers)
    assert allocation[1][1] == 90

def test_export_to_csv_edge_case():
    allocation = {1: {1: 0}}
    csv = export_to_csv(allocation)
    assert csv == "SKU,Center,Quantity\n1,1,0\n"
