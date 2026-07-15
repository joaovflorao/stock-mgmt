from django.contrib import admin

from .models import (
    AttributeName,
    ProductBase,
    ProductBrand,
    ProductCategory,
    ProductItem,
    UnitOfMeasure,
)

@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_on")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "created_on")
    search_fields = ("name",)
    list_filter = ("is_active", "parent")


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation", "is_active")
    search_fields = ("name", "abbreviation")


@admin.register(AttributeName)
class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on")
    search_fields = ("name",)


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1
    fields = ("sku", "barcode", "attributes", "cost_price", "sale_price", "is_active")


@admin.register(ProductBase)
class ProductBaseAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "unit_of_measure", "is_active", "created_on")
    search_fields = ("name", "description")
    list_filter = ("is_active", "brand", "category")
    inlines = [ProductItemInline]


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("sku", "product", "barcode", "cost_price", "sale_price", "is_active")
    search_fields = ("sku", "barcode", "product__name")
    list_filter = ("is_active",)
