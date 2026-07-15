from core.schemas import BaseModel
from django.db import models
from .product_base import ProductBase


class ProductItem(BaseModel):
    class Meta:
        db_table = "product_item"
        verbose_name = "Item de Produto"
        verbose_name_plural = "Itens de Produto"
        ordering = ["sku"]

    product = models.ForeignKey(
        ProductBase,
        verbose_name="Produto",
        on_delete=models.CASCADE,
        related_name="items",
    )
    sku = models.CharField(
        verbose_name="SKU",
        max_length=50,
        unique=True,
    )
    barcode = models.CharField(
        verbose_name="Código de barras",
        max_length=50,
        blank=True,
        null=True,
        unique=True,
    )
    attributes = models.JSONField(
        verbose_name="Atributos",
        default=dict,
        blank=True,
    )
    cost_price = models.DecimalField(
        verbose_name="Preço de custo",
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    sale_price = models.DecimalField(
        verbose_name="Preço de venda",
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    weight = models.DecimalField(
        verbose_name="Peso",
        max_digits=8,
        decimal_places=3,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.product.name} ({self.sku})"

    def save(self, *args, **kwargs):
        self.attributes = self._normalize_attributes(self.attributes)
        super().save(*args, **kwargs)

    @staticmethod
    def _normalize_attributes(attributes: dict) -> dict:
        normalized = {}
        for key, value in attributes.items():
            clean_key = key.strip().title()
            clean_value = str(value).strip()
            normalized[clean_key] = clean_value
            ProductAttributeName.objects.get_or_create(name=clean_key)
        return normalized