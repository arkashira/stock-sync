import csv
import io
from dataclasses import dataclass
from typing import List

@dataclass
class SKU:
    id: str
    name: str
    category: str
    base_lead_time: int

class SKUCatalog:
    def __init__(self):
        self.skus = {}

    def upload_csv(self, csv_data: bytes) -> dict:
        if len(csv_data) > 10 * 1024 * 1024:
            raise ValueError("CSV file too large")

        csv_reader = csv.DictReader(io.StringIO(csv_data.decode()))
        created_skus = []
        duplicate_skus = []

        for row in csv_reader:
            sku_id = row['SKU']
            if sku_id in self.skus:
                duplicate_skus.append(sku_id)
                continue

            try:
                sku = SKU(
                    id=sku_id,
                    name=row['name'],
                    category=row['category'],
                    base_lead_time=int(row['base lead time'])
                )
                self.skus[sku_id] = sku
                created_skus.append(sku_id)
            except KeyError as e:
                raise ValueError(f"Missing required field: {e}")

        return {
            'created': created_skus,
            'duplicates': duplicate_skus
        }

    def get_sku(self, sku_id: str) -> SKU:
        return self.skus.get(sku_id)
