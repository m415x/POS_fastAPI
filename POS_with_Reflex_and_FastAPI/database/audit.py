import reflex as rx
import sqlmodel
from datetime import datetime
from typing import List, Optional


class AuditBase(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    created_at: datetime = sqlmodel.Field(default=datetime.utcnow())
    updated_at: datetime = sqlmodel.Field(
        default=datetime.utcnow(), onupdate=datetime.utcnow())


class ItemAudit(AuditBase):
    category_id: int
    info: str
    stock: float
    unit_id: int
    cost: float
    price: float
    img: str
    supplier_id: int
    user_id: int
    is_delete: bool


class UnitAudit(AuditBase):
    name: str
    type_of_unit: str


class SupplierAudit(AuditBase):
    name: str
    email: str
    phone: str
    is_active: bool


class UserAudit(AuditBase):
    username: str
    email: str
    role: str
    is_active: bool


class CategoryAudit(AuditBase):
    name: str
    description: str
