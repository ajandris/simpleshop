from django.contrib.auth.models import User
from django.db import models
from home.utils import unique_slugify
from django.utils.text import slugify

# Create your models here.


class Images(models.Model):
    """
    Image Model for storing product and category images
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Image Name",
        db_comment="Image Name",
    )
    url = models.ImageField(
        upload_to="images/", verbose_name="Image", db_comment="Image"
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        db_table = "images"
        db_table_comment = "Products and Categories Images"


class Category(models.Model):
    """
    Product Category Model
    """

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Category Title",
        db_comment="Category Title",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug",
        null=True,
        blank=True,
        db_comment="Slug",
    )
    image = models.ForeignKey(
        Images, on_delete=models.CASCADE, db_comment="Image"
    )
    is_featured = models.BooleanField(
        default=False, verbose_name="Is Featured", db_comment="Is featured"
    )
    description = models.TextField(
        verbose_name="Description", db_comment="Description"
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to provide custom saving logic.
        """
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"
        db_table_comment = "Products Categories"


class Product(models.Model):
    """
    Product Model
    """

    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Product Title",
        blank=False,
        null=False,
        db_comment="Product Title",
    )
    short_description = models.TextField(
        verbose_name="Short Description", db_comment="Short Description"
    )
    description = models.TextField(
        verbose_name="Description", db_comment="Description"
    )
    tags = models.TextField(
        verbose_name="Tags", null=True, blank=True, db_comment="Tags"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug",
        null=True,
        blank=True,
        db_comment="Slug",
    )
    stock = models.IntegerField(
        verbose_name="Stock",
        blank=False,
        null=False,
        default=0,
        db_comment="Stock",
    )
    price = models.DecimalField(
        verbose_name="Price",
        decimal_places=2,
        max_digits=10,
        default=0,
        null=True,
        blank=True,
        db_comment="Price",
    )
    sales_price = models.DecimalField(
        verbose_name="Sales Price",
        decimal_places=2,
        max_digits=10,
        default=0,
        db_comment="Sales Price",
    )
    sku = models.CharField(
        max_length=25, unique=True, verbose_name="SKU", db_comment="SKU"
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="Is Featured",
        db_comment="Is this product featured?",
    )
    image = models.ForeignKey(
        Images,
        on_delete=models.CASCADE,
        verbose_name="Images",
        db_comment="Images",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Category",
        db_comment="Category",
    )
    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to provide custom saving logic.
        """
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"
        db_table_comment = "Product"


class ProductDimensions(models.Model):
    """
    Product Dimensions to create Product Variants
    """

    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Dimension Name",
        blank=False,
        null=False,
        db_comment="Dimension Name",
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return self.name

    class Meta:
        verbose_name = "Product Dimension"
        verbose_name_plural = "Product Dimensions"
        db_table = "product_dimensions"
        db_table_comment = "Available Product Dimensions list"


class ProductVariants(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Product",
        db_comment="Product",
    )
    sku = models.CharField(
        max_length=25, unique=True, verbose_name="SKU", db_comment="SKU"
    )
    stock = models.IntegerField(
        verbose_name="Stock",
        blank=False,
        null=False,
        default=0,
        db_comment="Stock",
    )
    price = models.DecimalField(
        verbose_name="Variant Price",
        decimal_places=2,
        max_digits=10,
        default=0,
        db_comment="Variant Price",
    )
    sales_price = models.DecimalField(
        verbose_name="Variant Sales Price",
        decimal_places=2,
        max_digits=10,
        default=0,
        null=True,
        blank=True,
        db_comment="Variant Sales Price",
    )
    dimension_name_1 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_1",
        verbose_name="Dimension 1 Name",
        blank=True,
        null=False,
        db_comment="Dimension 1 Name",
    )
    dimension_value_1 = models.CharField(
        verbose_name="Dimension 1 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 1 Value",
    )
    dimension_name_2 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_2",
        verbose_name="Dimension 2 Name",
        blank=True,
        null=False,
        db_comment="Dimension 2 Name",
    )
    dimension_value_2 = models.CharField(
        verbose_name="Dimension 2 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 2 Value",
    )
    dimension_name_3 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_3",
        verbose_name="Dimension 3 Name",
        blank=True,
        null=False,
        db_comment="Dimension 3 Name",
    )
    dimension_value_3 = models.CharField(
        verbose_name="Dimension 3 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 3 Value",
    )
    dimension_name_4 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_4",
        verbose_name="Dimension 4 Name",
        blank=True,
        null=False,
        db_comment="Dimension 4 Name",
    )
    dimension_value_4 = models.CharField(
        verbose_name="Dimension 4 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 4 Value",
    )
    dimension_name_5 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_5",
        verbose_name="Dimension 5 Name",
        blank=True,
        null=False,
        db_comment="Dimension 5 Name",
    )
    dimension_value_5 = models.CharField(
        verbose_name="Dimension 5 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 5 Value",
    )
    dimension_name_6 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_6",
        verbose_name="Dimension 6 Name",
        blank=True,
        null=False,
        db_comment="Dimension 6 Name",
    )
    dimension_value_6 = models.CharField(
        verbose_name="Dimension 6 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 6 Value",
    )
    dimension_name_7 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_7",
        verbose_name="Dimension 7 Name",
        blank=True,
        null=False,
        db_comment="Dimension 7 Name",
    )
    dimension_value_7 = models.CharField(
        verbose_name="Dimension 7 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 7 Value",
    )
    dimension_name_8 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_8",
        verbose_name="Dimension 8 Name",
        blank=True,
        null=False,
        db_comment="Dimension 8 Name",
    )
    dimension_value_8 = models.CharField(
        verbose_name="Dimension 8 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 8 Value",
    )
    dimension_name_9 = models.ForeignKey(
        ProductDimensions,
        on_delete=models.CASCADE,
        related_name="dimension_9",
        verbose_name="Dimension 9 Name",
        blank=True,
        null=False,
        db_comment="Dimension 9 Name",
    )
    dimension_value_9 = models.CharField(
        verbose_name="Dimension 9 Value",
        blank=False,
        null=False,
        max_length=70,
        db_comment="Dimension 9 Value",
    )

    inserted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record inserted",
        db_comment="DateTime when record inserted",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record updated",
        db_comment="DateTime when record updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return f"{self.product}: {self.product.title}"

    class Meta:
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"
        db_table = "product_variants"
        db_table_comment = "Product Variants"


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, db_comment="Product"
    )
    image = models.ForeignKey(
        Images, on_delete=models.RESTRICT, db_comment="Image"
    )
    number_in_gallery = models.IntegerField(
        null=False, blank=False, default=1000, db_comment="Number in gallery"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="DateTime when record created",
        db_comment="DateTime when record created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="DateTime when record was updated",
        db_comment="DateTime when record was updated",
    )
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, db_comment="User"
    )

    class Meta:
        db_table = "product_images"
        db_table_comment = "Product Images"
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        ordering = (
            "product__title",
            "number_in_gallery",
        )

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        return f"{self.product.title} - {self.number_in_gallery}"
