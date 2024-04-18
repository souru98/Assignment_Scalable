# Product Service

## Overview
This repository contains the code for the Product Service, a part of a microservices architecture application. The Product Service is responsible for managing the inventory of books in a book rental system.

## Features
- Search for a book by name
- Check the availability of a book
- Fetch all books
- Add a new book
- Decrease the count of a book when it is rented
- Increase the count of a book when it is returned

## Technologies Used
- Flask: A lightweight WSGI web application framework.
- SQLAlchemy: The Python SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Docker: A platform to develop, ship, and run applications inside containers.
- PostgreSQL: An open-source relational database management system (RDBMS).

## Getting Started

### Prerequisites
- Docker
- Python 3.x
- PostgreSQL

### Steps to Configure and Use
1. **Clone the repository**
   git clone https://github.com/souru98/Assignment_Scalable_Product.git
2. **Create a virtual environment**
   python3 -m venv env source env/bin/activate
3. **Install the packages listed in the requirements.txt file**
   pip install -r requirements.txt
4. **Build and run the Docker container**
   docker compose up --build flask_product_service_app


## API Endpoints
- `/book/search/<name>`: Search for a book by name
- `/book/availability/<id>`: Check the availability of a book
- `/books`: Fetch all books
- `/book`: Add a new book
- `/books/<book_id>/decrease`: Decrease the count of a book
- `/books/<book_id>/increase`: Increase the count of a book

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

