
---

# Purpose of the System

The system aims to provide a realistic example of an online retail platform while showcasing:

- server-rendered web architecture
- shopping cart and checkout functionality
- payment integration
- user authentication and account management
- backend business-logic testing

The application demonstrates typical patterns used in modern web stores while maintaining a seasonal **Christmas market theme**.

---

# Audience of the System

The system is designed for three primary audiences.

## Customers / Visitors

Customers are the main users of the system. They visit the website to browse festive products and purchase items.

Customers can:

- browse product categories
- view product details
- add products to a shopping cart
- apply discount coupons
- manage delivery addresses
- complete secure payments
- view order history

---

## Store Administrators

Administrators manage the marketplace and ensure that products and orders are maintained correctly.

Administrators can:

- manage products and categories
- configure shipping methods
- manage coupons and discounts
- view and manage customer orders
- maintain system content

---

## Developers / Assessors

The project also serves as a demonstration or educational project for developers evaluating:

- Django application architecture
- e-commerce workflow design
- Stripe payment integration
- backend testing strategies

---

# Key Features

## Product Catalogue

Customers can browse products organised into categories such as:

- Christmas Decorations  
- Toys and Gifts  
- Festive Homeware  
- Holiday Apparel

Each product has a dedicated page displaying description, price, and images.

---

## Shopping Cart

Users can:

- add products to the cart
- update quantities
- remove items
- apply coupons
- see updated totals automatically

The cart dynamically calculates:

- subtotal
- discount
- VAT
- shipping costs
- final total

---

## Checkout

The checkout process allows customers to:

- review cart items
- select shipping
- provide delivery details
- confirm order details

Order totals are validated both on the client and server side.

---

## User Accounts

The platform supports user authentication and account management through **django-allauth**.

Registered users can:

- create an account
- log in or log out
- manage saved addresses
- update personal information
- view order history

---

## Orders

Orders are generated when a customer completes checkout.

Order lifecycle:

Pending → Paid → Confirmed → Completed

The system records:

- purchased items
- payment status
- order totals
- customer details

---

## Stripe Payments

Payments are processed through **Stripe** using Stripe Elements.

Payment flow:

1. Create payment intent
2. Enter card details
3. Confirm payment
4. Update order status
5. Send confirmation
6. Clear cart

---

# System Architecture

The project follows a **monolithic Django architecture** with modular applications.

## Backend

Django applications include:

- home
- products
- cart
- orders
- payments
- payments_stripe

Each module manages a specific part of the e-commerce workflow.

---

## Frontend

Frontend components consist of:

- Django templates
- custom CSS stylesheets
- client-side JavaScript

The frontend enhances usability but core logic remains server-side.

---

## Database

Production database:

PostgreSQL

Testing database:

SQLite (in-memory)

---

# Technology Stack

Backend

- Python
- Django
- PostgreSQL
- pytest / pytest-django

Frontend

- HTML
- CSS
- JavaScript

Libraries and services

- Stripe
- django-allauth
- WhiteNoise
- python-dotenv

---

# Project Structure

Example repository structure:
```
simpleshop/
│
├── cart/
├── home/
├── orders/
├── payments/
├── payments_stripe/
├── products/
│
├── static/
│ ├── css/
│ └── js/
│
├── templates/
│
├── test/
│ ├── cart tests
│ └── order tests
│
└── manage.py
```

---

# User Stories

## Customer Stories

As a visitor  
I want to browse product categories  
So that I can discover items easily.

As a customer  
I want to view product details  
So that I can decide whether to buy.

As a shopper  
I want to add items to a cart  
So that I can purchase multiple items.

As a customer  
I want to apply a coupon code  
So that I can receive a discount.

As a registered user  
I want to save addresses  
So that checkout is faster.

As a buyer  
I want to pay securely  
So that I can complete my purchase.

As a customer  
I want to see order history  
So that I can track purchases.

---

## Administrator Stories

As an administrator  
I want to manage products  
So that the catalogue stays accurate.

As an administrator  
I want to manage shipping options  
So that delivery costs are correct.

As an administrator  
I want to view orders  
So that I can monitor purchases.

---

# HTML, CSS, and JavaScript

## HTML

The frontend uses **Django templates** to render pages dynamically.

Templates include:

- homepage
- product catalogue
- product details
- cart
- checkout
- user profile
- order history

---

## CSS

Styling is handled through dedicated stylesheets:

- main.css
- cart.css
- checkout.css
- stripe_checkout.css

These files control layout, responsiveness, and checkout presentation.

---

## JavaScript

JavaScript enhances the shopping experience through:

- cart.js
- checkout.js
- product_gallery.js
- stripe_elements.js
- profile.js

These scripts provide functionality such as:

- cart recalculation
- dynamic totals
- product image gallery
- Stripe payment handling
- profile page interaction

---

# Testing

The project includes automated backend tests using **pytest**.

Tests validate the business logic of the system.

Test configuration:

- pytest
- pytest-django

---

## Cart Tests

Cart tests verify:

- product availability
- stock validation
- quantity limits
- coupon validity
- subtotal calculations
- discount calculations
- VAT calculations
- order totals

---

## Order Tests

Order tests verify:

- order creation
- order rebuilding
- cart integrity checks
- hash consistency between cart and order

---

# HTML, CSS, and JavaScript Test Results

The repository does not currently contain a dedicated automated frontend testing framework.

Specifically:

| Component | Automated Tests |
|-----------|----------------|
| HTML | No automated tests present |
| CSS | No automated tests present |
| JavaScript | No automated test suite present |

Frontend behaviour is validated through **manual testing and browser interaction**, while backend business logic is validated through automated tests.

---

# Installation

Clone the repository:

git clone https://github.com/ajandris/simpleshop.git


Navigate into the project directory:


cd simpleshop


Create a virtual environment:


python -m venv venv


Activate the environment.

Mac/Linux


source venv/bin/activate


Windows


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


Run migrations:


python manage.py migrate


Start the development server:


python manage.py runserver


---

# Running Tests

Run automated tests using:


pytest


---

# Future Improvements

Potential improvements include:

- automated frontend testing
- improved UI responsiveness
- expanded order lifecycle
- order cancellation and refund support
- delivery tracking
- admin dashboard improvements

---

# License

This project is provided for educational and demonstration purposes.

---

# Implementation Evidence

This section provides evidence that the system meets the requirements defined in the project specification.

## Django Application Design

The system is implemented as a full-stack Django web application that integrates backend business logic, a relational database, and a dynamic front end.

The application is structured as a Django project named `simpleshop` with multiple independent Django apps separating responsibilities across the system including `home`, `products`, `cart`, `orders`, `payments`, and `payments_stripe`.

---

## Front-End Design and User Interaction

The application provides an interactive front-end built with Django templates, CSS, and JavaScript. Users interact with the system through navigation menus, product browsing, shopping cart interactions, and checkout processes.

The base template provides consistent navigation across the site including Home, Categories, Cart, Profile, Orders, Login, and Logout.

---

## Relational Database

The application uses a relational database structure where entities such as Products, Orders, Cart items, Coupons, and User Profiles are connected through relational fields.

Production uses PostgreSQL while automated tests run using an in-memory SQLite database.

---

## CRUD Operations

The system supports full CRUD functionality.

Users can create accounts and orders, read product information and order history, update cart quantities and address data, and delete items from the shopping cart.

---

## Authentication

Authentication is implemented using django-allauth. Users can register, log in, log out, and manage their profile information. Authentication ensures that orders and profile data are associated with individual users.

---

## Payment Integration

Stripe payment integration allows users to securely complete purchases. The payment workflow includes creating payment intents, confirming payments, updating order status, and clearing the cart after successful payment.

---

## Testing

Automated backend tests are implemented using pytest and pytest-django. These tests validate cart calculations, coupon validation, order creation, and order consistency.

---

## Deployment

The application is deployed publicly and accessible through the live URL. The deployed version reflects the functionality of the development version.

---

## Security

Sensitive configuration values such as the Django secret key, database credentials, and Stripe keys are stored in environment variables rather than within the repository.

---

## Version Control

The project uses Git for version control and is hosted on GitHub, allowing version tracking and collaborative development.