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
- MiniKube
- Python 3.x
- PostgreSQL

### Steps to Configure and Use
1. **Clone the repository**
   ```
   git clone https://github.com/souru98/Assignment_Scalable_Product.git
2. **Create a virtual environment**
   ```
   python3 -m venv env source env/bin/activate
3. **Install the packages listed in the requirements.txt file**
   ```
   pip install -r requirements.txt
4. **Build and run the Docker container**
   ```
   docker compose up --build flask_product_service_app

## Deploying to MiniKube

Follow these steps to deploy your application to MiniKube:

1. **Navigate to Project Directory**: 
   Open Windows PowerShell and navigate to your project directory using the `cd` command.

2. ** change MiniKube Driver to Docker**
   ```
   minikube config set driver docker

3. **Start MiniKube**: 
   Start your MiniKube cluster with the command 
   ```
   minikube start`.

4. ** Initialize MiniKube Env**
   ```
   minikube docker-env

5. **Set Docker Environment**: 
   Set up the Docker environment inside MiniKube. Run the following command in PowerShell:
   ```powershell
   minikube -p minikube docker-env --shell powershell | Invoke-Expression
   
6. **Build Docker Image**
   ```powershell
   docker build -t product_service/flask_api:1.0 .
   
7. **Create Kubernetes Deployment**
   ```powershell
   kubectl run product-service-mk --image=product_service/flask_api:1.0 --image-pull-policy=Never --port=4000
   
8. **Port Forwarding**
   ```powershell
   kubectl port-forward product-service-mk 4000


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

