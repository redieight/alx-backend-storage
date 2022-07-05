#!/usr/bin/env python3
"""Module for using PyMongo"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection."""
    return mongo_collection.insert_one(kwargs).inserted_id
