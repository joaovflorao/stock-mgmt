from core.schemas import BaseModel
from django.db import models
from .product_brand import ProductBrand
from .product_category import ProductCategory
from .unit_of_measure import UnitOfMeasure


class ProductBase(BaseModel):
    class Meta:
        db_table = "product_base"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    name = models.CharField(
        verbose_name="Nome",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Descrição",
        blank=True,
    )
    brand = models.ForeignKey(
        ProductBrand,
        verbose_name="Marca",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        ProductCategory,
        verbose_name="Categoria",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    unit_of_measure = models.ForeignKey(
        UnitOfMeasure,
        verbose_name="Unidade de Medida",
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return str(self.name)
