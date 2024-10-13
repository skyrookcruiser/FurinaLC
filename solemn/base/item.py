from models.types import ItemFormat

item_list = [
    ItemFormat(item_id=11, num=404),
    ItemFormat(item_id=2, num=404),
    ItemFormat(item_id=301, num=404),
]

item_dicts = [{"item_id": i.item_id, "num": i.num} for i in item_list]
