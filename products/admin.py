from django.contrib import admin
from products.models import Product, Images, Category, ProductDimensions, ProductVariants, ProductImages
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.


class ProductResource(resources.ModelResource):

    sku = fields.Field(attribute='sku', column_name='sku')
    title = fields.Field(attribute='title', column_name='Product Title')
    category = fields.Field(attribute='category', column_name='Category',
                            widget=ForeignKeyWidget(Category, "title"))
    description = fields.Field(attribute='description', column_name='Description (HTML)')
    short_description = fields.Field(attribute='short_description', column_name='Description (HTML)')
    tags = fields.Field(attribute='tags', column_name='tags')
    price = fields.Field(attribute='price', column_name='generated_price')
    sales_price = fields.Field(attribute='sales_price', column_name='Sales_price')
    image = fields.Field(attribute='image', column_name='image',
                         widget=ForeignKeyWidget(Images, "name"))
    stock = fields.Field(attribute='stock', column_name='stock')
    user = fields.Field(attribute='user', column_name='username',
                        widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = Product
        # optional: list fields explicitly
        fields = ("sku", "title", "category", "description", "short_description", "tags", "price",
                  "sales_price", "image", "stock", "user")
        import_id_fields = ("sku",)  # prevents duplicates


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'short_description', 'description', 'slug', 'stock', 'price', 'sales_price',
                    'sku', 'tags', 'inserted_at', 'updated_at', 'user')
    readonly_fields = ['inserted_at', 'updated_at']
    search_fields = ('sku', 'title', 'description', 'tags')
    # list_filter = ('supplier__code', 'tags',)


class ImagesResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Name')
    url = fields.Field(attribute='url', column_name='url')
    user = fields.Field(attribute='user', column_name='username',
                        widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = Images
        fields = ('name', 'url', 'inserted_at', 'updated_at', 'user')
        readonly_fields = ['inserted_at', 'updated_at']
        import_id_fields = ("name",)  # prevents duplicates


@admin.register(Images)
class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'slug', 'is_featured', 'inserted_at', 'updated_at', 'user')
    readonly_fields = ['inserted_at', 'updated_at']

@admin.register(ProductDimensions)
class ProductDimensionAdmin(admin.ModelAdmin):
    list_display = ('name',)

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


class ProductImagesResource(resources.ModelResource):
    product = fields.Field(attribute='product', column_name='Product Name',
                        widget=ForeignKeyWidget(Product, 'title'))

    image = fields.Field(attribute='image', column_name='Name',
                        widget=ForeignKeyWidget(Images, 'name'))

    number_in_gallery = fields.Field(attribute='number_in_gallery', column_name='Sequence')

    user = fields.Field(attribute='user', column_name='username',
                        widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = ProductImages
        fields = ('product', 'image', 'number_in_gallery','inserted_at', 'updated_at', 'user')
        readonly_fields = ['inserted_at', 'updated_at']
        import_id_fields = ("image", "product",)  # prevents duplicates
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
@admin.register(ProductImages)
class ProductImageAdmin(ImportExportModelAdmin):
    resource_class = ProductImagesResource
