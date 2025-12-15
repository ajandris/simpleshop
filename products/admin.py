from django.contrib import admin
from products.models import Product, Images, Category, ProductDimensions, ProductVariants, ProductImages
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.


class ProductResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='id')
    sku = fields.Field(attribute='sku', column_name='sku')
    title = fields.Field(attribute='title', column_name='title')
    category = fields.Field(attribute='category', column_name='category_id',
                            widget=ForeignKeyWidget(Category, "id"))
    description = fields.Field(attribute='description', column_name='description')
    short_description = fields.Field(attribute='short_description', column_name='short_description')
    tags = fields.Field(attribute='tags', column_name='tags')
    price = fields.Field(attribute='price', column_name='price')
    sales_price = fields.Field(attribute='sales_price', column_name='sales_price')
    image = fields.Field(attribute='image', column_name='image_id',
                         widget=ForeignKeyWidget(Images, "id"))
    stock = fields.Field(attribute='stock', column_name='stock')
    user = fields.Field(attribute='user', column_name='user_id',
                        widget=ForeignKeyWidget(User, 'id'))

    class Meta:
        model = Product
        # optional: list fields explicitly
        fields = ('id', "sku", "title", "category", "slug", "description", "short_description", "tags", "price",
                  "sales_price", "image", "stock", "user")
        import_id_fields = ('id',)  # prevents duplicates


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'short_description', 'description', 'slug', 'stock', 'price', 'sales_price',
                    'sku', 'tags', 'inserted_at', 'updated_at', 'user')
    readonly_fields = ['inserted_at', 'updated_at']
    search_fields = ('sku', 'title', 'description', 'tags')
    # list_filter = ('supplier__code', 'tags',)


class ImagesResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='id')
    name = fields.Field(attribute='name', column_name='name')
    url = fields.Field(attribute='url', column_name='url')
    user = fields.Field(attribute='user', column_name='user_id',
                widget=ForeignKeyWidget(User, 'id'),
                )
    inserted_at = fields.Field(attribute='inserted_at', column_name='inserted_at')
    updated_at = fields.Field(attribute='updated_at', column_name='updated_at')

    class Meta:
        model = Images
        fields = ('id', 'name', 'url', 'user', 'inserted_at', 'updated_at',)
        readonly_fields = ['inserted_at', 'updated_at']
        import_id_fields = ('id',)  # prevents duplicates


@admin.register(Images)
class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource


class CategoryResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='id')
    title = fields.Field(attribute='title', column_name='title')
    slug = fields.Field(attribute='slug', column_name='slug')
    image = fields.Field(attribute='image', column_name='image_id',
                widget=ForeignKeyWidget(Images, 'id'),
                )
    is_featured = fields.Field(attribute='is_featured', column_name='is_featured')
    description = fields.Field(attribute='description', column_name='description')
    user = fields.Field(attribute='user', column_name='user_id',
                widget=ForeignKeyWidget(User, 'id'),
                )
    inserted_at = fields.Field(attribute='inserted_at', column_name='inserted_at')
    updated_at = fields.Field(attribute='updated_at', column_name='updated_at')

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'is_featured', 'user',
            'inserted_at', 'updated_at', 'slug', 'description',)
        list_display = ('image', 'title', 'slug', 'is_featured', 'inserted_at',
            'updated_at', 'user')
        readonly_fields = ['inserted_at', 'updated_at']
        import_id_fields = ('id',)  # prevents duplicates


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

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
    id = fields.Field(attribute='id', column_name='id')
    product = fields.Field(attribute='product', column_name='product_id',
                        widget=ForeignKeyWidget(Product, 'id'))

    image = fields.Field(attribute='image', column_name='image_id',
                        widget=ForeignKeyWidget(Images, 'id'))

    number_in_gallery = fields.Field(attribute='number_in_gallery', column_name='Sequence')

    user = fields.Field(attribute='user', column_name='user_id',
                        widget=ForeignKeyWidget(User, 'id'))
    inserted_at = fields.Field(attribute='inserted_at', column_name='inserted_at')
    updated_at = fields.Field(attribute='updated_at', column_name='updated_at')

    class Meta:
        model = ProductImages
        fields = ('id', 'product', 'image', 'number_in_gallery','inserted_at', 'updated_at', 'user')
        readonly_fields = ['inserted_at', 'updated_at']
        import_id_fields = ("image", "product",)  # prevents duplicates
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

@admin.register(ProductImages)
class ProductImageAdmin(ImportExportModelAdmin):
    resource_class = ProductImagesResource
