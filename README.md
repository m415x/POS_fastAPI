# Point of Sale (POS) System

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Built With](#built-with)
  - [FastAPI](#fastapi)
  - [Reflex](#reflex)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## Description

The Point of Sale (POS) System is a comprehensive software solution designed to streamline and optimize retail and sales operations. It provides a user-friendly interface for managing various aspects of a business, from handling sales transactions and managing inventory to tracking customer interactions.

## Features

- **Product Management:** Easily add, update, and remove products from the inventory. Track details such as product name, price, and quantity on hand.

- **Sales and Transactions:** Efficiently process sales transactions, calculate totals, generate invoices, and provide receipts. Keep a detailed record of all transactions.

- **Inventory Management:** Monitor and manage inventory levels in real-time. Receive notifications for low stock to avoid stockouts and streamline reordering processes.

- **Customer and Vendor Management:** Maintain a database of customers and vendors, allowing easy access to contact information and purchase history.

- **User Authentication:** Implement a secure user authentication system to control access to POS functionalities, ensuring data privacy and system security.

- **Reporting and Analytics:** Generate insightful reports on sales performance, popular products, and customer preferences. Use analytics to make informed business decisions.

- **Customizable UI:** Tailor the POS interface to match your brand with customizable themes and branding options.

## Built With

This Point of Sale (POS) System is built using the following Python frameworks:

### [FastAPI](https://fastapi.tiangolo.com/)

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and efficient, making it an excellent choice for developing the backend of this POS system.

#### Why FastAPI?

- **Fast Development:** FastAPI allows for rapid development with automatic interactive documentation, data validation, and serialization.

- **High Performance:** It is built on top of Starlette and Pydantic, making it one of the fastest web frameworks available.

- **Async Support:** FastAPI fully supports asynchronous programming, enabling efficient handling of concurrent operations.

### [Reflex](https://reflex.dev/)

Reflex is an open-source, full-stack Python framework that makes it easy to build and deploy web apps in minutes. It offers the ease of use and accessibility of low-code frameworks, combined with the flexibility, performance, and customizability of traditional web development. Reflex is designed to be easy to get started with for those with no previous web development experience.

#### Why Reflex?

- **Ease of use and accessibility:** Reflex is designed to be easy to use for developers with no previous web development experience. It offers a low-code approach that allows you to build web applications with simple configuration files and declarative components. This makes it a great choice for beginners or for teams that want to quickly build prototypes or MVPs.

- **Flexibility, performance, and customizability:** Reflex is built on top of the FastAPI framework, which provides a high-performance and scalable foundation for your web applications. It also offers a variety of features and customization options that allow you to build complex and sophisticated applications.

- **Full-stack development:** Reflex is a full-stack framework, which means that it provides tools for both the front-end and back-end development of your web applications. This can save you time and effort, as you don't need to learn and integrate multiple frameworks and tools.

## Getting Started

### Prerequisites

Before setting up the POS system, ensure that you have the following prerequisites installed:

- **Python:** The POS system is developed using Python 3.10 or later. Install Python by visiting [python.org](https://www.python.org/) and following the installation instructions for your operating system.

- **PostgreSQL Database:** The POS system uses PostgreSQL 15.5 or later as its backend database. Install and configure PostgreSQL on your server or local machine. You can download PostgreSQL from [postgresql.org](https://www.postgresql.org/).

- **Git:** Version control is essential for collaborative development. Install Git 2.34.1 o later by visiting [git-scm.com](https://git-scm.com/) and following the installation instructions.

### Installation

1. Clone the Repository

   > ```bash
   > git clone https://github.com/m415x/POS_with_Reflex_and_FastAPI.git
   > ```

2. Set Up Virtual Environment

   > ```bash
   > cd POS_with_Reflex_and_FastAPI
   > python -m venv .venv
   > ```

3. Activate Virtual Environment

   > _Linux / macOS_
   >
   > ```bash
   > source .venv/bin/activate
   > ```
   >
   > _Windows_
   >
   > ```bash
   > .venv\Scripts\activate
   > ```

4. Install Dependencies

   > ```bash
   > pip install -r requirements.txt
   > ```

5. Database Setup:

   1. Open pgAdmin and right-click on "Databases".
   2. Select "Create" and then "Database".
   3. Enter the name of the database and select the owner.

6. Create the '.env' file in the root with the following variables

   > ```text
   > DB_URL="postgresql://<user>:<password>@localhost:5432/my_db"
   > ```

7. Start the Application

   > ```bash
   > reflex run
   > reflex run --loglevel debug
   > ```

8. In your browser, access http://localhost:3000/
