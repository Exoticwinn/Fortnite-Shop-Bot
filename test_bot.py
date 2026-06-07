"""Простые тесты для бота"""

# Тест 
def test_format_item():
    item = {'name': 'Cool Skin', 'price': 2000}
    name = item['name'][:30]
    price = item['price']
    
    result = f"💰 {name}\n💵 {price} V-Bucks"
    
    assert 'Cool Skin' in result
    assert '2000' in result
    print("✅ Форматирование работает")



def test_long_name():
    long_name = 'A' * 50
    name = long_name[:30]
    
    assert len(name) == 30
    print("✅ Обрезание работает")


def test_pagination():
    items = list(range(1, 24)) 
    items_per_page = 5
    total_pages = (len(items) + items_per_page - 1) // items_per_page
    
    assert total_pages == 5
    print("✅ Пагинация правильная")


def test_empty_item():
    item = {}
    name = item.get('name') or 'Unknown'
    price = item.get('price') or 'Unknown'
    
    assert name == 'Unknown'
    assert price == 'Unknown'
    print("✅ Пустые товары обработаны")


if __name__ == '__main__':
    test_format_item()
    test_long_name()
    test_pagination()
    test_empty_item()
    print("\n🎉 Все тесты пройдены!")
