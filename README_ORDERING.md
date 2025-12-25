ORDERING
=================

# Introduction
Ordering selected items is a crucial part of every e-commerce system. 
This README part enlightens all aspects of the ordering and payment card processing implemented into this application.

# Starting position
Before starting the ordering part, the system has:
* implemented shop main framework functionality (all-auth, products, categories, cart);
* created three apps without user interfaces:
  * orders for order management;
  * payments for general payments handling from many payments processors and logging;
  * payments_stripe for stripe specific functionality;
  * created initial models for orders (Order, OrderItem).

# Ordering process
During order fulfillment, there are certain stages the order goes through.

The full order statuses are given in the table below.
# Order Statuses

| Status            | Description |
|-------------------|-------------|
| **Pending**       | The order has been created but payment has not yet been completed or confirmed. |
| **Payment Failed**| An attempt to process payment was unsuccessful. The order remains unpaid. |
| **Paid**          | Payment has been successfully received and confirmed. |
| **Confirmed**     | The order has been reviewed and accepted for fulfillment. |
| **Processing**   | The order is being prepared for shipment (e.g., picking, packing, or manufacturing). |
| **On Hold**       | The order is temporarily paused due to an issue such as stock unavailability, verification, or customer inquiry. |
| **Partially Fulfilled** | Some items in the order have been shipped or delivered, while others are still pending. |
| **Shipped**       | The order has been dispatched to the carrier but not yet delivered. |
| **In Transit**    | The shipment is currently moving through the carrier’s logistics network. |
| **Out for Delivery** | The shipment is with the courier and expected to be delivered soon. |
| **Delivered**     | The order has been successfully delivered to the customer. |
| **Completed**    | The order lifecycle is fully finished, including delivery and any post-delivery checks. |
| **Cancelled**    | The order was cancelled before fulfillment was completed. |
| **Returned**     | The customer has sent the order back after delivery. |
| **Refund Pending** | A refund has been initiated but not yet processed. |
| **Refunded**     | The payment has been fully or partially refunded to the customer. |
| **Failed**       | The order could not be completed due to a system, payment, or fulfillment error. |

The Shop implements statuses: Pending, Paid, Payment Failed, Confirmed and Completed.

# Workflows
After Checkout page is filled and Pay button pressed.

The implemented Orders workflows are:
1. Order Pending -> Paid -> Confirmed -> Completed
2. Order Pending -> Payment Failed -> Pending -> Retry -> Paid -> Confirmed -> Completed

What is not included:
1. Order processing
2. Order cancellation
3. Refunds
2. Delivery and order tracking


## Workflow 1
Create order from the shopping cart:
* check if products in required quantities are still available. 
If not available, adjust cart with items and available quantities in cart and show checkout page.
* copy data from Cart to Orders.
* set order status to Pending.
* log action

Payment:

+ Payment attempt returns Payment Successful.
  + Log Payment action.

The next steps are created automatically (for future use):

* Order status change to Paid.
  + Log Order action.


* Order status change to Confirmed.
  + Log Order action.

* Order status change to Completed.
  + Log Order action.

# Testing
The ordering process testing is performed by implementing the Test Driven Development (TDD).
At its core, TDD is a "test-first" approach. Instead of writing code and then testing it, you flip the script. 
The developer follow a tight loop known as the Red-Green-Refactor cycle.

_**Red**_: Write a small test for a specific piece of functionality. 
Run it and watch it fail (because the code doesn't exist yet).

_**Green**_: Write the bare minimum code required to make that test pass.

_**Refactor**_: Clean up the code that was just written, ensuring it follows good design principles 
while keeping the test "Green."

