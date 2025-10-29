from django.contrib import admin
from products.models import Product, Images, Category, ProductDimensions, ProductVariants

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'description', 'slug', 'stock', 'price', 'sales_price',
                    'sku', 'tags', 'inserted_at', 'updated_at', 'user')
    readonly_fields = ['inserted_at', 'updated_at']
    search_fields = ('sku', 'title', 'description', 'tags')
    # list_filter = ('supplier__code', 'tags',)

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductDimensions)
class ProductDimensionAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductVariants)
class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ('product__title', 'sku', 'stock', 'price', 'sales_price',
                    'dimension_name_1', 'dimension_value_1', 'dimension_name_2', 'dimension_value_2',
                    'dimension_name_3', 'dimension_value_3','dimension_name_4', 'dimension_value_4',
                    'dimension_name_5', 'dimension_value_5','dimension_name_6', 'dimension_value_6',
                    'dimension_name_7', 'dimension_value_7','dimension_name_8', 'dimension_value_8',
                    'dimension_name_9', 'dimension_value_9',
                    'inserted_at', 'updated_at', 'user')
    readonly_fields = ['inserted_at', 'updated_at']
    search_fields = ('sku', 'title',
                     'dimension_name_1', 'dimension_value_1', 'dimension_name_2', 'dimension_value_2',
                     'dimension_name_3', 'dimension_value_3', 'dimension_name_4', 'dimension_value_4',
                     'dimension_name_5', 'dimension_value_5', 'dimension_name_6', 'dimension_value_6',
                     'dimension_name_7', 'dimension_value_7', 'dimension_name_8', 'dimension_value_8',
                     'dimension_name_9', 'dimension_value_9',
                     'inserted_at', 'updated_at', 'user')
    list_filter = ('dimension_name_1', 'dimension_value_1', 'dimension_name_2', 'dimension_value_2',
                   'dimension_name_3', 'dimension_value_3', 'dimension_name_4', 'dimension_value_4',
                   'dimension_name_5', 'dimension_value_5', 'dimension_name_6', 'dimension_value_6',
                   'dimension_name_7', 'dimension_value_7', 'dimension_name_8', 'dimension_value_8',
                   'dimension_name_9', 'dimension_value_9'
                   )

