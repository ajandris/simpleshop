# The Olde Christmas Market

## Overview

**The Olde Christmas Market** is a Django-based e-commerce web application designed to simulate an online Christmas market where users can browse festive products and purchase them through a secure checkout system.

The platform allows customers to explore categories such as decorations, gifts, toys, and festive homeware. Users can add items to a cart, apply discounts, manage shipping details, and complete purchases using **Stripe payment integration**.

The project demonstrates a full-stack web application built with **Django, HTML, CSS, JavaScript, and PostgreSQL**, with automated backend tests for core business logic.

**Live Site:**  
https://theoldechristmasmarket.projects.andris.jancevskis.com/

**GitHub Repository:**  
https://github.com/ajandris/simpleshop

**The intended audience** for the site includes:

## Audience

The **Olde Christmas Market** website is designed for a broad, festive‑minded audience 
who enjoy traditional holiday markets and seasonal browsing:

The site is designed for general public visitors who enjoy traditional Christmas markets, especially those who appreciate:
- Handcrafted, artisan‑style gifts
- Seasonal decorations and festive atmosphere
- A nostalgic, old‑world Christmas aesthetic
- Browsing curated holiday products online
- Light, playful, family‑friendly experiences


The primary groups include:

### Holiday Shoppers  
People looking for unique Christmas gifts, decorations, and handcrafted festive items.

### Families & Casual Visitors  
Users who enjoy exploring cozy, themed seasonal content in a playful, family‑friendly environment.

### Fans of Traditional Christmas Culture  
Visitors who appreciate nostalgic, old‑world Christmas aesthetics, artisan‑style goods, and warm winter themes.

### General Web Users  
Anyone who discovers the site through curiosity, seasonal browsing, or as part of the project’s public demonstration.


1. **Candle Enthusiasts** – Individuals who appreciate candles for their ambience, scent, and decorative appeal.
2. **DIY & Craft Lovers** – Individuals interested in creating their own candles as a hobby or small business.
3. **Home Decor Enthusiasts** – Individuals seeking innovative ways to incorporate candles into their living spaces.
4. **Aromatherapy & Wellness Seekers** – Individuals who utilise candles for relaxation, stress relief, and mood enhancement.
5. **Gift Shoppers** – Those searching for unique and personalised candle gifts.
6. **Eco-Conscious Consumers** – Individuals interested in sustainable, non-toxic, or handmade candles.
7. **Small Business Owners** – Artisans or entrepreneurs in the candle-making industry seeking tips and trends.

The blog will cater to anyone who appreciates the beauty, functionality, and sensory experience of candles.

Anyone is welcome to browse blogs and read comments. Would you like to leave a comment or write a blog yourself? 
Register and go ahead! To have an impact on the site's content, be an editor, also known as a moderator. 
Get in touch by email: andris [at] jancevskis [dot] com.


## Users

There are four categories of users: visitors, registered users, and superusers.

A **visitor** can browse shop and items.

A **registered in user** when logged in can do everything a visitor can, 
plus add items to the basket and checkout - everything what shoppers usually do.

A **superuser** can access admin interface.

## Used technologies, frameworks, services

- HTML
- CSS
- JavaScript
- Python
- Django
- PostgreSQL
- Git
- GitHub
- Grammarly to catch grammar slips and improve the text
- AI generated code snippets adjusted to use in the system

# Development
This part is dedicated to the page's development.
## Development process
The Development of this site includes consequently following the stages described in detail in the following sections:
* Requirements gathering described in Strategy Plane – gathering all requirements to the Site. User Stories belong to this stage.
* Scope definition is described in the Scope Plane, which defines what will be included in the initial release.
* The Structure plane is introduced at the start of the design, where wireframes are used to create sketches of the pages, and Entity-Relationship Diagrams (ERD) show the database structure.
* The result of a Skeleton plane is the Site’s navigation and detailed database description.
* The final stage in development is the Surface plane, where all design is completed for various screen sizes and audiences. This plane includes all JavaScript and CRUD functionality.
* Next comes site testing, which is performed manually using Jigsaw (CSS) and the W3 Validator (HTML). Google’s Lighthouse test is used to test the site’s performance. JavaScript's syntax is tested using Beautify Tools. The database is tested by inserting data using the UI and validating the inserted and updated data using the UI or database tools to read data directly from the database.

## Strategy plane



## E‑Commerce User Stories

### Viewing and Navigation

| User Story ID | As a/an | I want to be able to…                             | So that I can…                                                                     |
|---------------|---------|---------------------------------------------------|------------------------------------------------------------------------------------|
| US1           | Shopper | View a list of products                           | Select some to purchase                                                            |
| US2           | Shopper | View individual product details                   | Identify the price, description, product rating, product image and available sizes |
| US3           | Shopper | Easily view the total of my purchases at any time | Avoid spending too much                                                            |

### Registration and User Accounts

| User Story ID | As a/an   | I want to be able to…                      | So that I can…                                                                  |
|---------------|-----------|---------------------------------------------|----------------------------------------------------------------------------------|
| US4           | Site User | Easily register for an account             | Have a personal account and be able to view my profile                           |
| US5           | Site User | Easily login or logout                     | Access my personal account information                                           |
| US6           | Site User | Easily recover my password if I forget it  | Recover access to my account                                                     |
| US7           | Site User | Receive an email confirmation after registering | Verify that my account registration was successful                           |
| US8           | Site User | Have a personalized user profile           | View my personal order history, order confirmations, and save payment information |

### Searching and Filtering

| User Story ID | As a/an | I want to be able to…                                       | So that I can…                                                                 |
|---------------|---------|-------------------------------------------------------------|---------------------------------------------------------------------------------|
| US9           | Shopper | Sort a specific category of product                         | Find the best-priced in a specific category |
| US10          | Shopper | Filter multiple categories of products simultaneously       | Find the best-priced or best-rated products across broad categories (e.g., clothing, homeware) |
| US11          | Shopper | Search for a product by name or description                 | Find a specific product I'd like to purchase                                   |

### Purchasing and Checkout

| User Story ID | As a/an | I want to be able to…                             | So that I can…                                                            |
|---------------|---------|---------------------------------------------------|---------------------------------------------------------------------------|
| US12          | Shopper | Easily select quantity of a product               | Ensure I don't accidentally select the wrong product, quantity, or size   |
| US13          | Shopper | View items in my bag                              | Identify the total cost and all items I will receive                      |
| US14          | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout                        |
| US15          | Shopper | Add, delete and edit favourite addresses          | Save time by just selecting delivery and billing addrress before checkout |
| US16          | Shopper | Easily enter my payment information               | Check out quickly and with no hassles                                     |
| US17          | Shopper | Feel my personal and payment information is safe  | Confidently provide the needed information to make a purchase             |
| US18          | Shopper | View an order confirmation after checkout         | Verify that I haven't made any mistakes                                   |
| US19          | Shopper | Receive an email confirmation after checking out  | Keep the confirmation of what I've purchased for my records               |

### Admin and Store Management

| User Story ID | As a/an     | I want to be able to…        | So that I can…                                           |
|---------------|-------------|-------------------------------|-----------------------------------------------------------|
| US20          | Store Owner | Add a product                 | Add new items to my store                                 |
| US21          | Store Owner | Edit/update a product         | Change product prices, descriptions, images, and criteria |
| US22          | Store Owner | Delete a product              | Remove items that are no longer for sale                  |

  
Site development is performed using JetBrains PyCharm IDE, Python version 3.12 and Django version 5.1.4. 
The site utilises PostgreSQL version 16 for data storage. Git and GitHub are used for storing code and version control.

## Scope plane
The user stories above show the full functionality of the site. However, due to unavoidable circumstances, 
the user permission functionality may be reduced for registered users.

At the end of development will be delivered:
* Implemented User Stories
* README.md file
* Development documentation in README.md file.
* Deployment to cPanel hosting.
* Code and version control using Git and GitHub


## Structure plane

The structure plane is concerned with design elements on pages.

The Olde Christmas Market site has a very intentional visual identity built around warmth, 
nostalgia, and a handcrafted Christmas‑market atmosphere. Here are the key design elements 
that define the experience:

### Overall Theme
- A **traditional Christmas aesthetic** with warm, cozy tones.
- Visuals evoke an **old‑world market** rather than a modern e‑commerce store.
- The design leans into **storytelling and atmosphere**, not just functionality.

### Color Palette
- Warm reds, deep greens, and gold accents.
- Soft, muted backgrounds that feel rustic and handcrafted.
- High contrast between text and background for readability.

### Imagery & Decorative Elements
- Seasonal illustrations and textures that resemble:
  - wooden stalls  
  - vintage signage  
  - festive ornaments  
- Imagery supports the theme without overwhelming usability.

### Layout & Structure
- Clean, centered layout with clear spacing.
- Sections feel like “stalls” or “market booths,” reinforcing the theme.
- Product cards and content blocks are simple and readable.

### Typography
- A mix of:
  - **Decorative serif fonts** for titles (evoking tradition and warmth)
  - **Clean sans‑serif fonts** for body text (ensuring clarity)
- Typography supports the festive theme without sacrificing usability.

### Navigation & UX
- Straightforward, intuitive navigation.
- Clear calls to action with festive styling.
- User flows feel familiar to standard e‑commerce but wrapped in a seasonal aesthetic.

### Emotional Tone
- Friendly, inviting, and nostalgic.
- Designed to feel like browsing a real Christmas market rather than a generic shop.
- Encourages exploration and delight.


## Site Content Structure

The Olde Christmas Market site follows a clear, intuitive content structure designed to 
guide visitors through a festive shopping experience while keeping navigation simple and 
predictable. Here’s how the content is organized:

### 1. Homepage
- Introduces the Christmas‑market theme with warm visuals and seasonal messaging  
- Highlights featured products or categories  
- Acts as the entry point into the shopping experience  

### 2. Product Listings (Category Pages)
- Displays a grid of available products  
- Includes sorting options (price, rating, category)  
- Allows quick scanning of items through images, names, and prices  

### 3. Product Detail Pages
- Shows full product information:
  - description  
  - price  
  - rating  
  - available sizes  
  - product imagery  
- Includes size/quantity selectors and an “Add to Bag” action  

### 4. Shopping Bag / Cart
- Lists selected items with:
  - product name  
  - size  
  - quantity  
  - subtotal
- Allows quantity adjustments and item removal  
- Shows running total to support budgeting  
- Choose shipping method to see total amount payable

### 5. Checkout Flow
- Collects customer details:
  - payment information  
- Emphasizes clarity and trust (secure checkout cues)
- Ends with:
  - an order confirmation screen  
  - order confirmation email  

### 6. User Account
- Registration and login pages
- Password recovery  
- Profile dashboard with:
  - order history  
  - saved details  
  - confirmation records  

### 7. Search & Filter Tools
- Search bar for product names/descriptions  
- Filtering controls for:
  - price 
  - category
- Search results page showing query + number of matches  

### 8. Navigation & Footer
- Top navigation links to major sections  
- Footer with:
  - contact info  
  - policies  
  - additional links 

### 9. Contact form
- simple contact form
- Captcha SPAM protection


## Skeleton plane
Skeleton Plane is concerned about the site's functionality, including its database structure.

**Entity-relationship diagrams (ERDs)** show the relationships between data entities. 
It serves as the starting point of a database design, and it impacts the site's navigation and layout.

The final Entity-Relationship diagram and database table description is located in the 
file [Structure](structure.md).

**Navigation:** The site features two menus, the Main menu and a Command bar.

The main menu is a bar of links which belong to the page's header. 
It is static and is shown on each site's page.

The site has two submenu:
- products with category choices,
- profile with personal information and logout.

**Authorisation and authentication**

The site uses an allauth module for authorisation and authentication. In the top right corner, there are links for 
registration and authorisation. Only the user's self-registration, sign-in, and sign-out functionality is supported. 
The registered user is promoted to an editor using the admin interface, and the Editor role can be added to the user's 
role list. Currently, no other roles are supported.

**Search**

On top of every product page's header features an input field and a Search button, 
allowing users to search products by title and content. 
The product pages have a filter by price form.
It is possible to filter from search result.

Searched and filtered product count is on the bottom of the filters form.

The result is displayed in a grid list.

**Paginator** appears when there is more than one page (12 items) in the list, displaying a bar of numbers and arrows. 
Arrows are shown when there is at least one page to navigate to the arrow's direction (left or right).

## Surface plane

All pages are designed to adapt seamlessly to various screen sizes and resolutions. Whether it's a desktop, tablet, 
or mobile screen, the user experience remains consistent and optimal.

**The menu** collapses at mobile sizes.

Due to the small project size, there is no design mock-up, and all elements will be built during development using the try-and-fix method.

### Page Colours

Page base colours are:
* page background: #fafafa
* header area above menu: #f3e0d1
* Menu background: amber
* Footer background: #f3e0d1
* Fonts: black

**Behavioural colours**

* Active menu item: bold, opacity 25% 
* Delete button hover: red, other buttons hover: green

**Information bar colours**

Information bar colours depend on what kind of information is to be shown:
* debug: background #6c757d, font white,
* info: background #17a2b8, font black,
* success: background #28a745, font black,
* warning: background #FFA500, font black,
* debug: background #FF0000, font black.

# Testing
Software testing, a crucial step in software development, is the process of evaluating and verifying whether 
a software application meets its expected requirements and functions correctly, ensuring the end product is 
of high quality and meets user expectations.

It aims to identify defects, bugs, or missing features in contrast to the specified requirements.

Essentially, it answers two critical questions:

Is the software built correctly? (does the software correctly implement specific functions?) Is it the right product? 
(does the software align with customer requirements or user stories?) This project uses manual testing and 
acceptance testing.

During manual testing, the test operator manually checks if the system works as expected by going through all 
screens and simulating end-user behaviour. The user interface is also checked for look and feel during this test. 

In web development, web pages are tested against different screen sizes, browsers, and operational systems.

The system's functionality can be automated using test scripts. For that purpose, automated tests are used. 
Automated tests are helpful for large projects to ensure that new functionality does not alter existing behaviour. 
They increase testing speed but add extra work for writing them. One of the testing frameworks for JavaScript is Jest. 

Automated tests are not used for this project because they lack continuity, and writing tests would add extra work.

Acceptance tests ensure that all user requirements are met. In this project, they are user stories.

The complete test results are in a [separate file](/TESTING.md).

# Deployment

## Creating database and granting privileges

To create a database and a database user using SQL statements, connect to the database server using a command-line 
tool with the user having administrative privileges. Change the `user`, `database` and `mypassword` in 
scripts with your preferred names.

**Creating database:**
```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
```
**Privileges to database user:**
```
GRANT CONNECT ON DATABASE mydatabase TO myuser;
```

Change superuser's default database with command:
```
\c mydatabase
```
Continue with granting privileges:
```
GRANT ALL PRIVILEGES ON SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

Detailed database and user creation instructions are not included in this document, as they would reveal sensitive server-side information. 
Overall, creating a database with cPanel is a straightforward task.

## Environment variables
Environment variables for development are set in the env.py file. For the production environment, 
those should be put on the web server during deployment. The development environment is set on a 
local computer with PostgreSQL installed.

**The list of environment variables:**
```
# security
SECRET_KEY: <THE KEY FROM INITIAL SETTINGS.PY FILE>
DEBUG: False
ALLOWED_HOSTS: localhost, 127.0.0.1  # a list of allowed hosts separated by coma

# database
POSTGRES_USER: <myuser>
POSTGRES_PASSWORD: <mypassword>
POSTGRES_HOST: localhost
POSTGRES_PORT: 5432  # default is 5432
POSTGRES_DATABASE_NAME: <mydatabase>
```

The secret key is copied from the initial settings.py file. If you don't have it, create a temporary Django project, 
copy the key, and then destroy that Django project.

## The very first installation
### Environment

### Pre-installation procedures

1. create a database and a database user with permission described above (how to configure PostgreSQL, see database documentation)
2. Enabling environment variables named above. Look at the image below, under "Deploying Application".

### Installation
1. copying files

* Download the project files from GitHub as a single zip file.

![download source code from github image](/readme_assets/deployment/download_files_from_git.png)

* For copying files with cPanel's File Manager: create a folder for candlemania files. Let's call it a &lt;project root&gt;

* Upload dowloaded project's code zip into &lt;project root&gt;
* Unzip candlemania files into &lt;project root&gt; (see image)

![image of project code into <project root>](/readme_assets/deployment/copied_and_extracted_files_in_project_root.png)

* create a domain/subdomain pointing to the &lt;project root&gt;/candlemania-main directory

2. deploying application
* in cPanel Software section choose Setup Python App.
* on the next screen, cPanel will show a list of installed applications. Press the button "Create Application".

![image of create application screen](/readme_assets/deployment/create_application_screen.png)
Choose Python version 3.12, write the directory name where project code resides, choose the domain name for the application 
and press the "Create" button.

Additional configuration information is added to the application screen.
![image of generated configuration info](/readme_assets/deployment/generated_config_info.png)

Environment variables can be added before or during application creation.

After successful app installation, the site shows the default web server response.
![image of default python app response](/readme_assets/deployment/it_works.png)


2. installing dependencies

* From a terminal as a user (not root), activate virtual environment and change directory to the &lt;project root&gt;.
* in virtual environment execute '''pip install -r requirements.txt'''. That will install 
all packages. If there is a problem with psycopg2 installation, in requirements.txt file change psycopg2
to psycopg2-binary. That will avoid errors.

3. building a database

PostgreSQL database server should be installed and available in cPanel. This is a high level 
guide as these tasks are not project specific.
* Create a database by pressing the "Databases" section button in the PostgreSQL Database Wizard or PostgreSQL Databases.
* Create a database user from PostgreSQL databases interface.
* Grant database user access rights (see above) using phpPgAdmin application's web interface.

**Note** that button names can be different but still meaningful.

* Finalise environment variable's setup in Python application interface.
* in terminal issue command '''python manage.py makemigrations'''. If there are errors, they are most likely fue to the 
database user having insufficient privileges to the database and/or schema PUBLIC.
* in terminal issue command '''python manage.py migrate'''
* Once migration is finished create administrative 
account with a command '''python manage.py createsuperuser''' and enter all required information.
* restart application.
* Now, the application should work and have no blogs and no comments.

### Post installation procedures

***Adding the role "Editor"*** 

* open site's admin page (SITE_URL/admin/) and enter superuser's credentials.
* add Group "Editor" and press Save
![adding group "Editor"](/readme_assets/deployment/create_editor_group.png)
* Log out from administration screen.

***Granting role "Editor" to a registered user*** 

* On the site's main screen's top right corner, click "Register" and fill all the required information. That way, a registered user is created.
* Log into admin screen, select the user, and enter the edit screen.
* Locate the "Add group" section
* on the left box, select "Editor"
* press arrow pointing to the right.
* Press Save
![User as an "Editor"](/readme_assets/deployment/make_user_editor.png)

# Acknowledgement
I would like to extend my gratitude to my tutor, Rachel Furlong, and the Code Institute.

# Bibliography
W3 Schools (https://www.w3schools.com/)

# Next steps
While this is a fictional blog site, it can become real. The possible next steps for the site's idea to evolve 
and possibly "go live" could be:
* add contact form,
* allow using images in blogs,
* add a candle shop,
* change name to more unique,
* explore Django CMS like "django CMS" or Wagtail.

