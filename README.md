# Tech Store

Tech Store is an e-commerce platform built with Django, featuring a messaging system using Pika and SQLite as the database backend.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)

## Features

- **Product Management:** Manage products with CRUD operations.
- **User Authentication:** User registration and authentication system.
- **Shopping Cart:** Add and manage products in the shopping cart.
- **Order Processing:** Complete ordering process including checkout and payment.
- **Messaging System:** Integrated messaging using Pika for communication.
- **Admin Dashboard:** Admin interface for site management.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   cd Tech-Store

2. Install Python dependencies using pip:
   
   ```bash
   pip install -r requirements.txt

3. Apply database migrations:

   ```bash
   python manage.py migrate

4. Create a superuser (admin account) for accessing the admin dashboard:

   ```bash
   python manage.py createsuperuser
   
5. Run the development server:

   ```bash
   python manage.py runserver

6. Access the application at http://localhost:8000.

Browse the store, add products to the cart, and complete orders through the checkout process.

Monitor messages using the integrated messaging system powered by Pika.

## Contributing

Contributions are welcome! Here's how you can contribute to the project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
Please ensure that your pull request adheres to the existing code style and includes unit tests for new features or bug fixes.
