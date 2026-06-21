import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class SKU:
    id: int
    name: str
    on_hand: int
    forecast: int

@dataclass
class FulfillmentCenter:
    id: int
    name: str
    min_stock: int
    max_capacity: int

def optimize_allocation(skus: List[SKU], centers: List[FulfillmentCenter]) -> Dict[int, Dict[int, int]]:
    allocation = {}
    for sku in skus:
        allocation[sku.id] = {}
        for center in centers:
            allocation[sku.id][center.id] = min(sku.forecast, center.max_capacity - center.min_stock)
    return allocation

def export_to_csv(allocation: Dict[int, Dict[int, int]]) -> str:
    csv = "SKU,Center,Quantity\n"
    for sku_id, center_allocations in allocation.items():
        for center_id, quantity in center_allocations.items():
            csv += f"{sku_id},{center_id},{quantity}\n"
    return csv

def load_data(file_path: str) -> (List[SKU], List[FulfillmentCenter]):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            skus = [SKU(**sku_data) for sku_data in data['skus']]
            centers = [FulfillmentCenter(**center_data) for center_data in data['centers']]
            return skus, centers
    except FileNotFoundError:
        print(f"File {file_path} not found. Using default data.")
        return [SKU(1, 'Test SKU', 100, 50)], [FulfillmentCenter(1, 'Test Center', 10, 100)]

def main():
    skus, centers = load_data('data.json')
    allocation = optimize_allocation(skus, centers)
    csv = export_to_csv(allocation)
    print(csv)

if __name__ == '__main__':
    main()
