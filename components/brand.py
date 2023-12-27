import utils.json_service as json_service
import components.product as product


# Полный список
def brand_get_all():
    db = json_service.get_database()
    return db["brand"]


# Получить id категории товаров
def brand_get_one_by_name(name):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["brand"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


# Удалить категорию товаров
def brand_delete_one_by_id(id):
    db = json_service.get_database()  # Чтение базы данных
    for i, elem in enumerate(db["brand"]):
        if elem["id"] == id:
            candidate = db["brand"].pop(i)
            json_service.set_database(db)  # Перезапись базы данных

            for item in db['product']:
                if item['brand_id'] == id:
                    product.delete_one_by_id(item['id'])

            return candidate
    return {"message": f"Элемент с {id} не найден"}


# Добавить категорию товаров
def brand_create_one(brand):
    db = json_service.get_database()  # Чтение базы данных
    last_brand_id = brand_get_all()[-1]["id"]
    db["brand"].append({"id": last_brand_id + 1, **brand})
    json_service.set_database(db)  # Перезапись базы данных


def get_id_by_brand(brand):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["brand"]:
        if elem["name"] == brand:
            return elem['id']
    return {"message": f"Элемент с {brand} не найден"}


def get_brand_by_id(id):
    db = json_service.get_database()
    for elem in db['brand']:
        if elem['id'] == id:
            return elem['name']
    return {"message": f"Элемент с id {id} не найден"}
