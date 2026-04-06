

## Table: product_dimensions
Table comment: Available Product Dimensions list


### Primary Key: 
"product_dimensions_pkey" on column "id"


### Unique Key: 
"product_dimensions_name_key" on column "name"

### Referenced-by: 

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_1_id_10205828_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_1_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_2_id_ec36533c_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_2_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_3_id_d7e03b97_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_3_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_4_id_861be997_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_4_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_5_id_07fd708f_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_5_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_6_id_9be16d13_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_6_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_7_id_ae65bafd_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_7_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_8_id_f55f9d9c_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_8_id)

TABLE "product_dimensions" CONSTRAINT "product_variants_dimension_name_9_id_bdab6838_fk_product_d" FOREIGN KEY (id) REFERENCES product_variants(dimension_name_9_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|name|varchar(25) |||


## Table: product_variants

### Primary Key: 
"product_variants_pkey" on column "id"


### Unique Key: 
"product_variants_sku_key" on column "sku"

### Foreign Key constraints: 

"product_variants_dimension_name_1_id_10205828_fk_product_d" FOREIGN KEY (dimension_name_1_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_2_id_ec36533c_fk_product_d" FOREIGN KEY (dimension_name_2_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_3_id_d7e03b97_fk_product_d" FOREIGN KEY (dimension_name_3_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_4_id_861be997_fk_product_d" FOREIGN KEY (dimension_name_4_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_5_id_07fd708f_fk_product_d" FOREIGN KEY (dimension_name_5_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_6_id_9be16d13_fk_product_d" FOREIGN KEY (dimension_name_6_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_7_id_ae65bafd_fk_product_d" FOREIGN KEY (dimension_name_7_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_8_id_f55f9d9c_fk_product_d" FOREIGN KEY (dimension_name_8_id) REFERENCES product_dimensions(id)

"product_variants_dimension_name_9_id_bdab6838_fk_product_d" FOREIGN KEY (dimension_name_9_id) REFERENCES product_dimensions(id)

"product_variants_product_id_019d9f04_fk_products_id" FOREIGN KEY (product_id) REFERENCES products(id)

"product_variants_user_id_78b52bb3_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Columns
| |Column Name|Data Type| Key |Description|
|---|---|---|-----|---|
|1|id|bigint | YES ||
|2|sku|varchar(25) |     ||
|3|stock|integer |     ||
|4|price|numeric |     ||
|5|sales_price|numeric |     ||
|6|dimension_value_1|varchar(70) |     |Dimension 1 Value|
|7|dimension_value_2|varchar(70) |     |Dimension 2 Value|
|8|dimension_value_3|varchar(70) |     |Dimension 3 Value|
|9|dimension_value_4|varchar(70) |     |Dimension 4 Value|
|10|dimension_value_5|varchar(70) |     |Dimension 5 Value|
|11|dimension_value_6|varchar(70) |     |Dimension 6 Value|
|12|dimension_value_7|varchar(70) |     |Dimension 7 Value|
|13|dimension_value_8|varchar(70) |     |Dimension 8 Value|
|14|dimension_value_9|varchar(70) |     |Dimension 9 Value|
|15|inserted_at|datetime |     ||
|16|updated_at|datetime |     ||
|17|dimension_name_1_id|bigint |     |Dimension 1 Name|
|18|dimension_name_2_id|bigint |     |Dimension 2 Name|
|19|dimension_name_3_id|bigint |     |Dimension 3 Name|
|20|dimension_name_4_id|bigint |     |Dimension 4 Name|
|21|dimension_name_5_id|bigint |     |Dimension 5 Name|
|22|dimension_name_6_id|bigint |     |Dimension 6 Name|
|23|dimension_name_7_id|bigint |     |Dimension 7 Name|
|24|dimension_name_8_id|bigint |     |Dimension 8 Name|
|25|dimension_name_9_id|bigint |     |Dimension 9 Name|
|27|product_id|bigint |     ||
|28|user_id|integer |     ||


## Table: products
Table comment: Product


### Primary Key: 
"products_pkey" on column "id"


### Unique Key: 
"products_sku_key" on column "sku"

"products_slug_key" on column "slug"

"products_title_key" on column "title"

### Foreign Key constraints: 

"products_category_id_a7a3a156_fk_categories_id" FOREIGN KEY (category_id) REFERENCES categories(id)

"products_image_id_686de2af_fk_images_id" FOREIGN KEY (image_id) REFERENCES images(id)

"products_user_id_0be7171c_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "products" CONSTRAINT "cart_item_product_id_17acb13c_fk_products_id" FOREIGN KEY (id) REFERENCES cart_item(product_id)

TABLE "products" CONSTRAINT "product_variants_product_id_019d9f04_fk_products_id" FOREIGN KEY (id) REFERENCES product_variants(product_id)

TABLE "products" CONSTRAINT "products_productimages_product_id_24647d74_fk_products_id" FOREIGN KEY (id) REFERENCES product_images(product_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|title|varchar(150) |||
|3|short_description|text |||
|4|description|text |||
|5|slug|varchar(50) |||
|6|stock|integer |||
|7|price|numeric |||
|8|sales_price|numeric |||
|9|sku|varchar(25) |||
|10|inserted_at|datetime |||
|11|updated_at|datetime |||
|12|image_id|bigint |||
|13|user_id|integer |||
|14|tags|text |||
|15|is_featured|boolean ||Is this product featured?|
|16|category_id|bigint |||


## Table: product_images

### Primary Key: 
"products_productimages_pkey" on column "id"

### Foreign Key constraints: 

"products_productimages_image_id_a329e87d_fk_images_id" FOREIGN KEY (image_id) REFERENCES images(id)

"products_productimages_product_id_24647d74_fk_products_id" FOREIGN KEY (product_id) REFERENCES products(id)

"products_productimages_user_id_8d54aff6_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|number_in_gallery|integer |||
|3|created_at|datetime |||
|4|updated_at|datetime |||
|5|image_id|bigint |||
|6|product_id|bigint |||
|7|user_id|integer |||


## Table: categories
Table comment: Products Categories


### Primary Key: 
"categories_pkey" on column "id"


### Unique Key: 
"categories_slug_key" on column "slug"

"categories_title_key" on column "title"

### Foreign Key constraints: 

"categories_image_id_d79bf798_fk_images_id" FOREIGN KEY (image_id) REFERENCES images(id)

"categories_user_id_4315f8c7_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "categories" CONSTRAINT "products_category_id_a7a3a156_fk_categories_id" FOREIGN KEY (id) REFERENCES products(category_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|title|varchar(100) |||
|3|slug|varchar(50) |||
|4|description|text |||
|5|inserted_at|datetime |||
|6|updated_at|datetime |||
|7|user_id|integer |||
|8|image_id|bigint |||
|9|is_featured|boolean ||Is featured|


## Table: images
Table comment: Products and Categories Images


### Primary Key: 
"images_pkey" on column "id"


### Unique Key: 
"images_name_key" on column "name"

### Foreign Key constraints: 

"images_user_id_401d96d0_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "images" CONSTRAINT "categories_image_id_d79bf798_fk_images_id" FOREIGN KEY (id) REFERENCES categories(image_id)

TABLE "images" CONSTRAINT "products_image_id_686de2af_fk_images_id" FOREIGN KEY (id) REFERENCES products(image_id)

TABLE "images" CONSTRAINT "products_productimages_image_id_a329e87d_fk_images_id" FOREIGN KEY (id) REFERENCES product_images(image_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|name|varchar(100) |||
|3|url|varchar(100) |||
|4|inserted_at|datetime |||
|5|updated_at|datetime |||
|6|user_id|integer |||


## Table: cart_item
Table comment: Cart items


### Primary Key: 
"cart_item_pkey" on column "id"

### Foreign Key constraints: 

"cart_item_cart_id_157ecf5f_fk_cart_id" FOREIGN KEY (cart_id) REFERENCES cart(id)

"cart_item_product_id_17acb13c_fk_products_id" FOREIGN KEY (product_id) REFERENCES products(id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|qty|integer |||
|3|price|numeric |||
|4|created_at|datetime |||
|5|updated_at|datetime |||
|6|cart_id|bigint |||
|7|product_id|bigint |||
|8|user_id|integer |||


## Table: shipping
Table comment: Shipping rates


### Primary Key: 
"shipping_pkey" on column "id"


### Unique Key: 
"shipping_code_key" on column "code"

"shipping_title_key" on column "title"

### Foreign Key constraints: 

"shipping_user_id_bb3e4177_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|title|varchar(50) |||
|3|code|varchar(50) |||
|4|text_html|varchar(150) |||
|5|price|numeric |||
|6|discount_threshold|numeric |||
|7|price_discounted|numeric |||
|8|created_at|datetime |||
|9|updated_at|datetime |||
|10|user_id|integer |||


## Table: cart
Table comment: Shopping cart


### Primary Key: 
"cart_pkey" on column "id"


### Unique Key: 
"cart_cart_number_key" on column "cart_number"

### Foreign Key constraints: 

"cart_discount_id_a01db4c8_fk_coupons_id" FOREIGN KEY (discount_id) REFERENCES coupons(id)

### Referenced-by: 

TABLE "cart" CONSTRAINT "cart_item_cart_id_157ecf5f_fk_cart_id" FOREIGN KEY (id) REFERENCES cart_item(cart_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|cart_number|varchar(32) |||
|4|created_at|datetime |||
|5|updated_at|datetime |||
|6|owner_id|integer |||
|7|user_id|integer |||
|8|discount_id|bigint |||
|10|shipping_method|varchar(50) |||


## Table: address
Table comment: User Addresses


### Primary Key: 
"home_address_pkey" on column "id"

### Foreign Key constraints: 

"home_address_profile_id_352e3950_fk_profile_owner_id" FOREIGN KEY (profile_id) REFERENCES profile(owner_id)

"home_address_user_id_fea03c2b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|is_default|boolean |||
|3|address_line1|varchar(250) |||
|4|address_line2|varchar(250) |||
|5|state|varchar(100) |||
|6|country|varchar(2) |||
|7|inserted_at|datetime |||
|8|updated_at|datetime |||
|9|user_id|integer |||
|10|profile_id|integer |||
|11|postal_code|varchar(10) |||
|12|for_billing|boolean |||
|13|for_shipping|boolean |||
|14|city|varchar(100) |||


## Table: profile
Table comment: User profiles


### Primary Key: 
"profile_pkey" on column "owner_id"

### Foreign Key constraints: 

"profile_owner_id_1ff3cbce_fk_auth_user_id" FOREIGN KEY (owner_id) REFERENCES auth_user(id)

"profile_user_id_2aeb6f6b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "profile" CONSTRAINT "home_address_profile_id_352e3950_fk_profile_owner_id" FOREIGN KEY (owner_id) REFERENCES address(profile_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|owner_id|integer |||
|2|name|varchar(100) |||
|3|surname|varchar(100) |||
|4|email|varchar(100) |||
|5|inserted_at|datetime |||
|6|updated_at|datetime |||
|7|user_id|integer |||


## Table: coupons
Table comment: Coupons


### Primary Key: 
"coupons_pkey" on column "id"

### Foreign Key constraints: 

"coupons_user_id_bee5d0f0_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "coupons" CONSTRAINT "cart_discount_id_a01db4c8_fk_coupons_id" FOREIGN KEY (id) REFERENCES cart(discount_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|code|varchar(30) |||
|3|value|numeric |||
|4|type|varchar(30) ||amount or percent|
|5|effective_from|date |||
|6|effective_to|date |||
|7|created_at|datetime |||
|8|updated_at|datetime |||
|9|user_id|integer |||
|10|min_subtotal|numeric |||


## Table: order_statuses

### Primary Key: 
"order_statuses_pkey" on column "id"


### Unique Key: 
"order_statuses_code_key" on column "code"

### Foreign Key constraints: 

"order_statuses_user_id_bf23a76d_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "order_statuses" CONSTRAINT "orders_status_id_e763064e_fk_order_statuses_id" FOREIGN KEY (id) REFERENCES orders(status_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|code|varchar(50) |||
|3|name|varchar(50) |||
|4|description|text |||
|5|inserted_at|datetime |||
|6|updated_at|datetime |||
|7|user_id|integer |||


## Table: order_items

### Primary Key: 
"orders_orderitem_pkey" on column "id"

### Foreign Key constraints: 

"orders_orderitem_order_id_fe61a34d_fk_orders_id" FOREIGN KEY (order_id) REFERENCES orders(id)

"orders_orderitem_user_id_b421299c_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|sku|varchar(50) |||
|3|item|text |||
|4|quantity|integer |||
|5|unit_price|numeric |||
|6|inserted_at|datetime |||
|7|updated_at|datetime |||
|8|order_id|bigint |||
|9|user_id|integer |||


## Table: orders

### Primary Key: 
"orders_pkey" on column "id"


### Unique Key: 
"orders_order_no_key" on column "order_no"

### Foreign Key constraints: 

"orders_owner_id_d1edb064_fk_auth_user_id" FOREIGN KEY (owner_id) REFERENCES auth_user(id)

"orders_status_id_e763064e_fk_order_statuses_id" FOREIGN KEY (status_id) REFERENCES order_statuses(id)

"orders_user_id_7e2523fb_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "orders" CONSTRAINT "orders_orderitem_order_id_fe61a34d_fk_orders_id" FOREIGN KEY (id) REFERENCES order_items(order_id)

### Columns
| |Column Name|Data Type|Key|Description|
|---|---|---|---|---|
|1|id|bigint |YES||
|2|order_no|uuid |||
|3|order_date|datetime |||
|5|subtotal|numeric |||
|6|total|numeric |||
|7|vat_included|numeric |||
|9|currency|varchar(3) |||
|10|cart_no|varchar(100) |||
|11|billing_address|text |||
|12|shipping_address|text |||
|13|billing_name|varchar(50) |||
|14|billing_surname|varchar(50) |||
|15|shipping_name|varchar(50) |||
|16|shipping_surname|varchar(50) |||
|17|shipping_method|varchar(30) |||
|18|shipping_price|numeric |||
|19|discount_amount|numeric |||
|20|inserted_at|datetime |||
|21|updated_at|datetime |||
|22|user_id|integer |||
|23|status_id|bigint |||
|24|owner_id|integer |||
|25|email|varchar(254) ||Email to send order status updates|
