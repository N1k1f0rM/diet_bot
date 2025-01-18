import requests
from typing import Dict, Any
from config import info_logger, error_logger

def get_food_info(product_name: str) -> Dict[str, Any]:
    url = f"https://world.openfoodfacts.org/cgi/search.pl?action=process&search_terms={product_name}&json=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        products = data.get('products', [])
        if products:
            first_product = products[0]

            info_logger.info(f"Для запроса {url} найдено {first_product}")

            return {
                'name': first_product.get('product_name', 'Неизвестно'),
                'calories': first_product.get('nutriments', {}).get('energy-kcal_100g', 0)
            }
        return None
    error_logger.error(f"Для запроса {url} Ошибка: {response.status_code}")
    return None
