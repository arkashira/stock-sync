import pytest
from sku_catalog import SKUCatalog, SKU

def test_upload_csv():
    catalog = SKUCatalog()
    csv_data = b"SKU,name,category,base lead time\n123,Test SKU,Test Category,10"
    result = catalog.upload_csv(csv_data)
    assert result['created'] == ['123']
    assert result['duplicates'] == []

def test_upload_csv_duplicate():
    catalog = SKUCatalog()
    csv_data = b"SKU,name,category,base lead time\n123,Test SKU,Test Category,10\n123,Test SKU,Test Category,10"
    result = catalog.upload_csv(csv_data)
    assert result['created'] == ['123']
    assert result['duplicates'] == ['123']

def test_upload_csv_missing_field():
    catalog = SKUCatalog()
    csv_data = b"SKU,name,category\n123,Test SKU,Test Category"
    with pytest.raises(ValueError):
        catalog.upload_csv(csv_data)

def test_upload_csv_large_file():
    catalog = SKUCatalog()
    csv_data = b"a" * (10 * 1024 * 1024 + 1)
    with pytest.raises(ValueError):
        catalog.upload_csv(csv_data)

def test_get_sku():
    catalog = SKUCatalog()
    csv_data = b"SKU,name,category,base lead time\n123,Test SKU,Test Category,10"
    catalog.upload_csv(csv_data)
    sku = catalog.get_sku('123')
    assert isinstance(sku, SKU)
    assert sku.id == '123'
    assert sku.name == 'Test SKU'
    assert sku.category == 'Test Category'
    assert sku.base_lead_time == 10
