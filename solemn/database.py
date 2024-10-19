from pymongo import MongoClient
from solemn.base.ego import ego_dicts
from solemn.base.formation import formation_dicts
from solemn.base.personality import personality_dicts
from solemn.base.item import item_dicts
import argparse

db = MongoClient("mongodb://localhost:27017/")["limbus"]

ego_collection = db["egoes"]
personality_collection = db["personalities"]
formation_collection = db["formations"]
item_collection = db["items"]


def setup_database():
    ego_collection.insert_many(ego_dicts)
    formation_collection.insert_many(formation_dicts)
    personality_collection.insert_many(
        personality_dicts
    )
    item_collection.insert_many(item_dicts)
    print("Database setup completed.")


try:
    parser = argparse.ArgumentParser(
        description="Database setup for Limbus."
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run database setup.",
    )
    args = parser.parse_args()
    if args.setup:
        setup_database()
except Exception as e:
    raise RuntimeError(
        "An error occurred during the database setup process."
    ) from e
