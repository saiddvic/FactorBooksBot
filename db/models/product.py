from sqlalchemy import BigInteger, VARCHAR, ForeignKey, select
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.base import CreateModel, db


class Category(CreateModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    products: Mapped[list['Product']] = relationship("Product", back_populates="category")


class Product(CreateModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    price: Mapped[float] = mapped_column(BigInteger, nullable=True)
    category_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(Category.id, ondelete='CASCADE'))
    category: Mapped[Category] = relationship("Category", back_populates="products")


    @classmethod
    async def get_products_by_category_id(cls, category_id):
        query = select(cls).where(cls.category_id == category_id)
        return (await db.execute(query)).scalars()