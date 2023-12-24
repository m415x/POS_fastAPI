import reflex as rx
import datetime
import sqlmodel
import sqlalchemy
from typing import List, Optional


class ItemModel(rx.Model, table=True):
    # attributes
    id: int = sqlmodel.Field(primary_key=True)
    category_id: int = sqlmodel.Field(foreign_key="categorymodel.id")
    info: str
    stock: float
    unit_id: int = sqlmodel.Field(foreign_key="unitmodel.id")
    cost: float
    price: float
    img: Optional[str]
    supplier_id: int = sqlmodel.Field(foreign_key="suppliermodel.id")
    user_id: int = sqlmodel.Field(foreign_key="usermodel.id")
    is_delete: bool = False
    create: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update",
            sqlalchemy.DateTime(timezone=True),
            onupdate=sqlalchemy.func.now(),
            server_default=sqlalchemy.func.now(),
        ),
    )
    # relationships
    categories: Optional["CategoryModel"] = sqlmodel.Relationship(
        back_populates="items",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    units: Optional["UnitModel"] = sqlmodel.Relationship(
        back_populates="items",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    suppliers: Optional["SupplierModel"] = sqlmodel.Relationship(
        back_populates="items",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    users: Optional["UserModel"] = sqlmodel.Relationship(
        back_populates="items",
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class CategoryModel(rx.Model, table=True):
    # attributes
    id: int = sqlmodel.Field(primary_key=True)
    name: str
    description: str
    create: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update",
            sqlalchemy.DateTime(timezone=True),
            onupdate=sqlalchemy.func.now(),
            server_default=sqlalchemy.func.now(),
        ),
    )
    # relationships
    items: List[ItemModel] = sqlmodel.Relationship(
        back_populates="categories",
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class UnitModel(rx.Model, table=True):
    # attributes
    id: int = sqlmodel.Field(primary_key=True)
    name: str
    symbol: str
    unit_type: str = "int"
    create: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update",
            sqlalchemy.DateTime(timezone=True),
            onupdate=sqlalchemy.func.now(),
            server_default=sqlalchemy.func.now(),
        ),
    )
    # relationships
    items: List[ItemModel] = sqlmodel.Relationship(
        back_populates="units",
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class SupplierModel(rx.Model, table=True):
    # attributes
    id: int = sqlmodel.Field(primary_key=True)
    name: str
    email: str
    phone: str
    is_active: bool = True
    create: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update",
            sqlalchemy.DateTime(timezone=True),
            onupdate=sqlalchemy.func.now(),
            server_default=sqlalchemy.func.now(),
        ),
    )
    # relationships
    items: List[ItemModel] = sqlmodel.Relationship(
        back_populates="suppliers",
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class UserModel(rx.Model, table=True):
    # attributes
    id: int = sqlmodel.Field(primary_key=True)
    username: str
    email: str
    password: str
    role: str
    is_active: bool = True
    create: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update",
            sqlalchemy.DateTime(timezone=True),
            onupdate=sqlalchemy.func.now(),
            server_default=sqlalchemy.func.now(),
        ),
    )
    # relationships
    items: List[ItemModel] = sqlmodel.Relationship(
        back_populates="users",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
