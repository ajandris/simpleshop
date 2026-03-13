# Implementation Evidence

This section provides evidence that the system meets the requirements defined in the project specification. Each requirement is supported with descriptions of the implemented functionality and references to the system architecture, repository structure, and deployed application.

---

# LO1 – Full Stack Django Application

## Django Application Design

The system is implemented as a full-stack Django web application that integrates backend business logic, a relational database, and a dynamic front end.

The application is structured as a Django project named `simpleshop` with multiple independent Django apps that separate responsibilities across the system:

- `home` – homepage, informational pages, and contact functionality  
- `products` – product catalogue and product detail pages  
- `cart` – shopping cart functionality and calculations  
- `orders` – order creation, persistence, and history  
- `payments` – payment-related logic  
- `payments_stripe` – Stripe payment integration  

This modular architecture demonstrates separation of concerns and maintainable system design.

The project configuration is located within the `simpleshop` directory and includes environment configuration, application registration, database configuration, and middleware.

---

## Front-End Design and User Interaction

The application provides a fully interactive front-end interface built using:

- HTML templates rendered through Django
- CSS stylesheets for layout and visual styling
- JavaScript for client-side interaction

Users interact with the system through a structured interface including:

- homepage navigation
- product category browsing
- product detail pages
- shopping cart interface
- checkout interface
- account management pages
- order history views

The main navigation is defined in the base template and is accessible from all pages. The navigation includes links to:

- Home
- Product Categories
- About
- Contact
- Cart
- Profile
- Orders
- Login / Logout
- Sign Up

This consistent navigation ensures usability and accessibility across the application.

---

## Django File Structure

The project follows Django's recommended file structure and conventions. The repository is organised into applications, static files, templates, and testing modules.

Example structure:

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
│
├── manage.py
└── requirements.txt
```

Each Django application contains its own models, views, URLs, and templates where appropriate.

---

## Forms and Backend Model Interaction

The system contains several validated forms that interact with database models.

Examples include:

- user registration and login forms via `django-allauth`
- checkout forms that collect shipping and order details
- contact form allowing users to submit messages
- address forms within user profiles

These forms include server-side validation to ensure correct input before records are created or updated in the database.

---

## Custom Python Logic

The system includes custom backend logic implemented using Python.

Examples include:

- shopping cart price calculations
- coupon validation logic
- stock availability validation
- order creation and verification
- payment verification using Stripe
- order state management

Conditional statements and loops are used throughout the codebase to enforce business rules such as:

- verifying product stock levels
- validating coupon date ranges
- calculating VAT and totals
- rebuilding orders from cart contents
- validating payment status

This demonstrates the use of compound Python statements and structured backend logic.

---

## Manual and Automated Testing

The system includes automated backend tests written using `pytest` and `pytest-django`.

Test suites are located in the repository under the `test` directory and validate key business logic including:

- shopping cart validation
- product stock availability
- coupon validity
- price calculations
- order creation
- cart hash verification

These tests ensure that the core commerce functionality behaves correctly under different conditions.

---

# LO2 – Relational Data Model and CRUD Functionality

## Relational Database Design

The system uses a relational database to persist application data.

The production deployment uses:

PostgreSQL

The testing environment uses:

SQLite (in-memory)

The database schema includes several related models such as:

- Product
- Category
- Cart
- CartItem
- Order
- OrderItem
- Coupon
- User Profile
- Address
- Payment

These entities are connected using relational fields such as foreign keys, allowing the system to model relationships between customers, orders, products, and payments.

---

## Custom Django Models

The application includes multiple custom Django models representing the core domain of the system.

Examples include:

- Order
- OrderItem
- Product
- Cart
- Coupon

These models define database tables and relationships used throughout the system.

---

## Validated Data Entry

The system allows users to create and update database records through validated forms.

Examples include:

- account registration
- address creation
- order creation during checkout
- contact form submissions

Input validation is performed both client-side and server-side to ensure the integrity of stored data.

---

## CRUD Functionality

The application supports full CRUD functionality for relevant entities.

Create operations allow users to:

- create accounts
- create orders
- create address records
- create contact messages

Read operations allow users to:

- browse products
- view product details
- view order history
- view profile data

Update operations allow users to:

- update cart quantities
- update address information
- update account profile data

Delete operations include:

- removing items from the shopping cart
- clearing the cart after successful payment

These operations demonstrate full lifecycle management of application data.

---

# LO3 – Authentication and Authorisation

## User Authentication

User authentication is implemented using `django-allauth`.

The system supports:

- user registration
- login
- logout
- password management

Authentication allows the application to associate orders and profiles with individual users.

---

## Access Control

Access to certain pages and functionality is restricted to authenticated users.

Examples include:

- viewing profile information
- managing saved addresses
- viewing order history

Anonymous users can browse products but must register or log in to complete purchases.

---

## Secure Data Access

The system ensures that the database cannot be accessed directly by users.

All database operations are performed through Django models and views. Sensitive credentials such as database access keys, email credentials, and Stripe API keys are stored in environment variables rather than the repository.

---

# LO4 – E-Commerce Payment Integration

## Online Payment Processing

The system integrates the Stripe payment gateway to process online payments.

A dedicated Django application named `payments_stripe` handles payment interactions.

The payment process includes:

1. Creating a Stripe payment intent
2. Collecting card information using Stripe Elements
3. Confirming payment with Stripe
4. Updating the order payment status
5. Displaying success or failure feedback
6. Clearing the user's shopping cart

This integration enables secure payment processing for customer orders.

---

## Payment Feedback

The system provides feedback to the user regarding payment status.

Possible outcomes include:

- successful payment confirmation
- payment failure messages
- redirection to order confirmation pages

Django messages are used to provide user feedback across pages.

---

# LO5 – Version Control, Deployment, and Documentation

## Deployment

The final application is deployed and publicly accessible at:

https://theoldechristmasmarket.projects.andris.jancevskis.com/

The deployed version mirrors the development version and provides the same functionality.

---

## Version Control

The project is managed using Git version control and hosted on GitHub.

Repository:

https://github.com/ajandris/simpleshop

Version control enables tracking of changes, feature development, and collaboration.

---

## Security

Sensitive credentials are not stored in the repository.

The system loads the following configuration values from environment variables:

- Django secret key
- database credentials
- Stripe API keys
- email configuration
- reCAPTCHA keys

This ensures that sensitive information is protected and not exposed in source control.

---

## Documentation

The project repository includes documentation describing:

- system purpose
- application architecture
- installation instructions
- testing procedures
- payment workflow

This documentation supports maintainability and provides guidance for developers reviewing or extending the system.

---

# Summary

The Olde Christmas Market application implements a complete Django-based e-commerce system that satisfies the requirements of the project specification.

The system includes:

- a modular Django architecture
- a relational database model
- full CRUD operations
- authentication and user management
- Stripe-based payment processing
- automated backend testing
- version control and deployment

These components demonstrate the development of a functional full-stack web application using modern web technologies.