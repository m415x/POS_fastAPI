import reflex as rx
import sqlalchemy
from typing import List
from sqlmodel import select

# import states
from ..states import State

# import models
from .models import ItemModel


class ItemQuery(State):
    items: List[dict]

    def get_items(self):
        with rx.session() as session:
            # Fetch all 'ItemModel' records from the database
            statement = select(ItemModel).options(
                sqlalchemy.orm.selectinload(ItemModel.categories),
                sqlalchemy.orm.selectinload(ItemModel.units),
                sqlalchemy.orm.selectinload(ItemModel.suppliers),
                sqlalchemy.orm.selectinload(ItemModel.users),
            )
            results = session.exec(statement).all()
            items_list = []
            for result in results:
                item_dict = result.__dict__
                item_dict['category'] = item_dict['categories'].__dict__
                item_dict['unit'] = item_dict['units'].__dict__
                item_dict['supplier'] = item_dict['suppliers'].__dict__
                item_dict['user'] = item_dict['users'].__dict__
                del item_dict['categories']
                del item_dict['units']
                del item_dict['suppliers']
                del item_dict['users']
                items_list.append(item_dict)
            self.items = items_list
