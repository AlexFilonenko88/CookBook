# from cookbook.models.recipe import Recipe
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from cookbook.models.base import Base

if TYPE_CHECKING:
    from cookbook.models.recipe import Recipe


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship(
        secondary="recipe_ingredients", back_populates="ingredients"
    )
