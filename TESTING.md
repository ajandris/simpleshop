TESTING
=======

Software testing, a crucial step in software development, is the process of evaluating and verifying whether a software 
application meets its expected requirements and functions correctly, ensuring the end product is of high quality and 
meets user expectations.

It aims to identify defects, bugs, or missing features in contrast to the specified requirements.

Essentially, it answers two critical questions:
* Is the software built correctly? (does the software correctly implement specific functions?)
* Is it the right product?” (does the software align with customer requirements or user stories?)

This project uses manual testing, acceptance testing and automated tests (TDD).

During **manual testing**, the test operator manually checks if the system works as expected by navigating through all 
screens and simulating end-user behaviour. The user interface is also checked for look and feel during this test. 
In web development, web pages are tested against different screen sizes, browsers, and operation systems.

The system's functionality can be automated using test scripts. For this purpose, automated tests are used. Automated 
tests are helpful for large projects to ensure that new functionality does not alter existing behaviour. They increase 
testing speed but add extra work for writing them. One of the testing frameworks for JavaScript is Jest. 

In this project, **automated tests** are used only for testing the cart and order amounts calculation by 
implementing TDD approach.

**TDD (Test-Driven Development)** is a software development approach where you write a failing test first, then 
write the minimum code needed to make it pass, and finally refactor the code while keeping the tests green.

The usual cycle is:

1. **Red** — write a test for the desired behavior and see it fail.
2. **Green** — implement just enough code to pass the test.
3. **Refactor** — improve the code structure without changing behavior.

TDD helps produce more reliable, maintainable code and encourages small, incremental development steps.

## TDD for cart and order calculations
Before start building any tests on calculations, need to understand what really are the numbers that test should check.
For that reason, an external tools are used like spreadsheets where easily can calculate, for example, VAT amount.

### About the tests
The ```pytest``` provided all the necessary instruments to build the test cases - 20 in total.

To avoid tampering with a real database the ```sqlite``` is used and configured in the settings.py file. 

All test files are located in the ```<project root>/test/``` directory, except ```pytest.ini```
file that is in the ```<project root>/``` directory.

### The result
The final result without error is shown in the image below.
<img src="readme_assets/success/pytest_success.png" alt="Automated test result" width="75%">

## CSS Validation
Checking css for errors in Jigsaw site.
<a href="https://jigsaw.w3.org/css-validator/">CSS Validation Service</a>

### file: main.css
Errors on checking:

<img src="readme_assets/errors/main_css_errors.png" alt="main.css errors" width="75%">

No errors after fixing:

<img src="readme_assets/success/main_css_no_errors.png" alt="main.css no errors" width="75%">

### file: cart.css
No errors on checking:

<img src="readme_assets/success/cart_css_no_errors.png" alt="cart.css no errors" width="75%">

However, there are some warnings that ar enot related to the programming:

<img src="readme_assets/success/cart_css_warnings.png" alt="warnings on cart.css" width="75%">

### file: checkout.css
No errors on checking:

<img src="readme_assets/success/checkout_css_no_errors.png" alt="checkout.css no errors" width="75%">


## Validating HTML

<a href=""> Markup Validation Service on w3.org site</a>

### Home page
https://theoldechristmasmarket.projects.andris.jancevskis.com/

Errors.

<img src="readme_assets/errors/home_page_html_errors.png" alt="Home page HTML errors" width="75%">

After fixing:

<img src="readme_assets/errors/home_page_html_errors_2.png" alt="Home page HTML errors" width="75%">

Leaving heading errors is a design decision that does not affect site's functionality or look and feel. 


### Categories page
https://theoldechristmasmarket.projects.andris.jancevskis.com/products/catalogue/toys-gifts/

<img src="readme_assets/errors/categories_page_html_error.png" alt="Categories page HTML errors" width="75%">

Leaving heading error is a design decision that does not affect site's functionality or look and feel. 

### About page
https://theoldechristmasmarket.projects.andris.jancevskis.com/about/

No errors.

<img src="readme_assets/success/about_page_html_no_errors.png" alt="About page HTML no errors" width="75%">

### Contact page
https://theoldechristmasmarket.projects.andris.jancevskis.com/writeme/

No errors.

<img src="readme_assets/success/contact_page_html_no_errors.png" alt="Contact page HTML no errors" width="75%">

### Orders list
Source input.

<img src="readme_assets/errors/orders_list_HTML_errors.png" alt="Orders list HTML errors" width="75%">

After fixing.

<img src="readme_assets/success/orders_list_html_no_errors.png" alt="Orders list HTML no errors" width="75%">


### Order details
Source input.

No errors.

<img src="readme_assets/success/order_details_html_no_errors.png" alt="Orders details HTML no errors" width="75%">

### Cart
Source input.

No errors

<img src="readme_assets/success/cart_html_success.png" alt="Cart HTML check no errors" width="75%">

### Checkout
Source input.

No errors

<img src="readme_assets/success/checkout_page_html_no_errors.png" alt="Checkout page HTML check no errors" width="75%">

### Address list
Source input

Errors with three addresses on the list.

<img src="readme_assets/errors/address_list_html_error.png" alt="Address list HTML check errors" width="75%">

After fixing ids and JavaScript - no errors

<img src="readme_assets/success/address_list_html_no_errors.png" alt="Address list HTML check no errors" width="75%">


### New address
Source input

Errors.

<img src="readme_assets/errors/new_address_html_errors.png" alt="New address HTML check errors" width="75%">

After fixing - no errors

<img src="readme_assets/success/address_list_html_no_errors.png" alt="New address HTML check no errors" width="75%">

### New address
Source input

No errors

<img src="readme_assets/success/address_edit_html_no_errors.png" alt="Address edit HTML check no errors" width="75%">

## JavaScript validation
https://codeshack.io/js-validator/

Checked files:
- cart.js (warnings only)
- checkout.js (warnings only)
- main.js (no errors or warnings)
- main_postload.js (no errors or warnings)
- product_gallery.js (warnings only)
- profile.js (warnings only)
- stripe_elements.js (no errors or warnings)

Warnings types in validation results:
* Missing semicolons (fixed)
* Functions declared within loops referencing an outer scoped variable may lead to confusing semantics.
  * that warning is when the same function is called in a loop for each product and uses sku that is calculated from outer source - HTML DOM.


## Stripe payments
Stripe payments functionality in this shop uses the Stripe Sandbox. Sandbox means that no real payments are taken and is used for testing payment functionality.
The test cards are:
* 4242 4242 4242 4242 for successful authorisation (expiry date: any future date, CVC: any three numbers)
* 4000 0000 0000 0002 for failed payments.
Once the payment attempt is done, all results are collected in Stripe’s transaction log.

Transactions list.

<img src="readme_assets/stripe/transactions_list.png" alt="Transactions list at Stripe" width="75%">

Transaction details.

<img src="readme_assets/stripe/transaction_details.png" alt="Transaction details" width="75%">

## Acceptance test
Testing if user stories are implemented.
The screenshots are provided below the summary table.

| User Story ID | As a/an | Requiremenets                                         | The evidence of completion                                                                                                                                                                                                     |
|---------------|---------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| US1           | Shopper | View a list of products                               | Home page and products by category choise from the main menu.                                                                                                                                                                  |
| US2           | Shopper | View individual product details                       | Click on the product image or title.                                                                                                                                                                                           |
| US3           | Shopper | Easily view the total of my purchases at any time     | On the right side is a cart icon. If theree are items in cart, the number of items is shown next to it. The amount can be seen by navigating to the cart by clicking on the cart icon.                                         |
| US4           | Site User | Easily register for an account                        | Press "Sign Up" on the right side of the main menu and follow instructions.                                                                                                                                                    |
| US5           | Site User | Easily login or logout                                | On the right side of the main menu is menu item "Login". Logout is under "..,your profile" menu on the right side of the main menu.                                                                                            |
| US6           | Site User | Easily recover my password if I forget it             | Password recovery can be accessed by choosing "Login" and following the link "Forgot your password?" on the login screen.                                                                                                      |
| US7           | Site User | Receive verification requests in email                | The user receives verification requests by email on signing up, change password and reset password.                                                                                                                            |
| US8           | Site User | Have a personalized user profile                      | The user profile is accessible by choosing menu item ".., your profile".                                                                                                                                                       |
| US9           | Shopper | Fileter by a specific category of product             | Products by category are accessible from the drop-down menu item "Products"                                                                                                                                                    |
| US10          | Shopper | Search for a product by name or description           | All pages containg products have a search field above the main menu.                                                                                                                                                           |
| US11          | Shopper | Easily select quantity of a product                   | The quantity of the product can be changed in the product detauils page and changed in the cart.                                                                                                                               |
| US12          | Shopper | View items in my bag                                  | Choose cart on the right side of the main menu.                                                                                                                                                                                |
| US13          | Shopper | Adjust the quantity of individual items in my bag     | In the cart are + and - buttons to adjust quantities. There can remove product from cart.                                                                                                                                      |
| US14          | Shopper | Add, delete and edit favourite addresses              | Access to favourite addresses are through Profile/ Addresses.                                                                                                                                                                  |
| US15          | Shopper | Easily enter my payment information                   | Checkout page consists of summary on the right side and the payment information with saved addresses on the left side. Under address fields is the payment block to enter card number, expiry date and CVV code.               |
| US16          | Shopper | Feel my personal and payment information is safe      | Personal information can be accessible only to authorised persons. The payment card data is not saved on system server. Payment authorisation uses the Stripe native authorisation using JavaScript and direct link to Stripe. |
| US17          | Shopper | View an order confirmation after checkout             | Order conirmation is shown to the user after successful card autorisation along with the link to the orders page.                                                                                                              |
| US18          | Shopper | Receive an email confirmation after checking out      | An email with order informati is sent to the users registered email after successful card authorisation.                                                                                                                       |
| US19          | Store Owner | Add a product                                         | Product can be added using Django native admin interface.                                                                                                                                                                      |
| US20          | Store Owner | Edit/update a product                                 | Product can be edited and updated using Django native admin interface.                                                                                                                                                         |
| US21          | Store Owner | Delete a product                                      | Product can be deleted using Django native admin interface.                                                                                                                                                                    |

### The detailed evidence of implemented User Stories
#### US1 View a list of products
<img src="./readme_assets/user_stories/us_1.png" alt="List of products - Home Page" width="75%">

#### US2 View individual product details
<img src="./readme_assets/user_stories/us_2.png" alt="Product details page" width="75%">

#### US3 Easily view the total of my purchases at any time
<img src="./readme_assets/user_stories/us_3_1.png" alt="Items in the cart">

Click on the cart and The system will show the cart. User should be logged in.

<img src="./readme_assets/user_stories/us_3_2.png" alt="Cart summary - cart page" width="75%">

#### US4 Easily register for an account
<img src="./readme_assets/user_stories/us_4.png" alt="Register for an account" width="75%">

A new user will receive an email with a request to confirm email address.

#### US5 Easily login or logout
<img src="./readme_assets/user_stories/us_5_1.png" alt="Login page" width="75%">

<img src="./readme_assets/user_stories/us_5_2.png" alt="Logout page" width="75%">

<img src="./readme_assets/user_stories/us_5_3.png" alt="Logout confirmation page" width="75%">

#### US6 Easily recover my password if I forget it
<img src="./readme_assets/user_stories/us_6_1.png" alt="Forgot password path" width="75%">

<img src="./readme_assets/user_stories/us_6_2.png" alt="Forgot password screen" width="75%">

The system will email you with instructions how to reset the password.

#### US7 Receive verification requests in email
Sign Up screen

<img src="./readme_assets/user_stories/us_7_1.png" alt="Sign Up screen" width="75%">

The received email.

<img src="./readme_assets/user_stories/us_7_2.png" alt="Sign Up next screen" width="75%">

The confirmation email.

<img src="./readme_assets/user_stories/us_7_3.png" alt="The confirmation email" width="75%">

The email confirmation acceptance screen.

<img src="./readme_assets/user_stories/us_7_4.png"  alt="The email confirmation acceptance screen." width="75%">

The email has been confirmed.

<img src="./readme_assets/user_stories/us_7_5.png" alt="The email has been confirmed" width="75%">


#### US8 Have a personalized user profile
<img src="./readme_assets/user_stories/us_8_1.png" alt="Path to user profile" width="75%">

General information screen

<img src="./readme_assets/user_stories/us_8_2.png" alt="General info" width="75%">

Addresses screen (see US14)

<img src="./readme_assets/user_stories/us_8_3.png" alt="General info" width="75%">

Change password

<img src="./readme_assets/user_stories/us_8_4.png" alt="Change password link" width="75%">

<img src="./readme_assets/user_stories/us_8_5.png" alt="Change password screen" width="75%">

#### US9 Fileter by a specific category of product
Choose a product category from the main menu.

<img src="./readme_assets/user_stories/us_9_1.png" alt="Products menu" width="75%">

<img src="./readme_assets/user_stories/us_9_2.png" alt="Chosen 'Toys & gifts' category" width="75%">


#### US10 Search for a product by name or description
Enter search criteria.

<img src="./readme_assets/user_stories/us_10_1.png" alt="Enter the search criteria" width="75%">

The search result. The user can apply filters on the search result.

<img src="./readme_assets/user_stories/us_10_2.png" alt="The search results" width="75%">

The keyword found in the product description.

<img src="./readme_assets/user_stories/us_10_3.png" alt="The keyword in the product description" width="75%">


#### US11 Easily select quantity of a product
Quantity selection on the product page before adding to the cart

<img src="./readme_assets/user_stories/us_11_1.png" alt="Quantity selection on the product page" width="75%">

Quantity selection in the cart.

<img src="./readme_assets/user_stories/us_11_1.png" alt="Quantity selection/ change in the cart" width="75%">

#### US12 View items in my bag
Choose the cart icon.

<img src="./readme_assets/user_stories/us_12_1.png" alt="Cart icon" width="75%">

The cart screen.

<img src="./readme_assets/user_stories/us_12_2.png" alt="The cart contents" width="75%">

#### US13  Adjust the quantity of individual items in my bag
<img src="./readme_assets/user_stories/us_13_1.png" alt="Adjusting quantities" width="75%">

#### US14 Add, delete and edit favourite addresses
An empty address screen

<img src="./readme_assets/user_stories/us_14_1.png" alt="Empty address screen" width="75%">

New address entry screen

<img src="./readme_assets/user_stories/us_14_2.png" alt="New entry address screen" width="75%">

The first address in the list

<img src="./readme_assets/user_stories/us_14_3.png" alt="A list with one address" width="75%">

Added second address in the list.

We can see that button "Delete address" is not sowing by the first address. That is intentionally so system have at 
least one address to send items to. To delete the default address, some other address should be set
to be a default address.

<img src="./readme_assets/user_stories/us_14_4.png" alt="A list with two addresses" width="75%">

The South Pole address is default now and The North Pole address can be deleted.

Edit address.

<img src="./readme_assets/user_stories/us_14_6.png" alt="Edit address" width="75%">

<img src="./readme_assets/user_stories/us_14_7.png" alt="Edited address saved" width="75%">

Trying to delete an address.

<img src="./readme_assets/user_stories/us_14_8.png" alt="Deleting address" width="75%">

The address has been deleted.

<img src="./readme_assets/user_stories/us_14_9.png" alt="Address deleted" width="75%">

#### US15 Easily enter my payment information
Addresses can be chosen from preferred addresses list in the user profile. Even then, address can be changed. 
Defined addresses are templates only.

Name and Surname comes from the user's personal information.

All the user needs is to enter Card number, expiry date and CVC. 

<img src="./readme_assets/user_stories/us_15_1.png" alt="Checkout" width="75%">

#### US16 Feel my personal and payment information is safe
<img src="./readme_assets/user_stories/us_16_1.png" alt="Payments feel safe" width="75%">

#### US17 View an order confirmation after checkout

<img src="./readme_assets/user_stories/us_17_1.png" alt="Payment successful message" width="75%">
<img src="./readme_assets/user_stories/us_17_2.png" alt="The now order in the orders list" width="75%">
<img src="./readme_assets/user_stories/us_17_3.png" alt="Order details" width="75%">

#### US18 Receive an email confirmation after checking out
<img src="./readme_assets/user_stories/us_18_1.png" alt="Received email with order details" width="75%">

#### US19 Add a product
<img src="./readme_assets/user_stories/us_19_1.png" alt="Path to a new product form" width="75%">

<img src="./readme_assets/user_stories/us_19_2.png" alt="New product form" width="75%">

<img src="./readme_assets/user_stories/us_19_3.png" alt="Added product in the list" width="75%">

<img src="./readme_assets/user_stories/us_19_4.png" alt="Added product description" width="75%">

#### US20 Edit/update a product

<img src="./readme_assets/user_stories/us_20_1.png" alt="Error in product description" width="75%">

<img src="./readme_assets/user_stories/us_20_2.png" alt="Path to edit" width="75%">

<img src="./readme_assets/user_stories/us_20_3.png" alt="Product edit screen" width="75%">

<img src="./readme_assets/user_stories/us_20_4.png" alt="Edited product description" width="75%">


#### US21 Delete a product
<img src="./readme_assets/user_stories/us_21_1.png" alt="Set product for deletion" width="75%">

<img src="./readme_assets/user_stories/us_21_2.png" alt="Confirm product deletion" width="75%">

<img src="./readme_assets/user_stories/us_21_3.png" alt="Test product no more" width="75%">

