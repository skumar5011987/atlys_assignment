# atlys_assignment
# Scraping Tool
This project is a web scraping tool built using Python and the FastAPI framework. It scrapes product information from the target website and stores it in a local database. The tool also provides APIs for interacting with the scraped data.

# Features
    Scrapes product names, prices, and images from a specified number of pages.
    Stores scraped data in a local SQLite database.
    Supports proxy settings for scraping.
    Caches scraping results to avoid redundant updates.
    Provides a simple retry mechanism for robust scraping.
    Offers authentication for API endpoints using a static token.

# Prerequisites
    Python 3.8+
    FastAPI
    SQLAlchemy
    Requests
    Redis
    BeautifulSoup4
    Tenacity

# Installation
1. Clone the repository:
    git clone <repository-url>
    cd <repository-directory>

2. Create and activate a virtual environment:
    conda create -n venv python==3.9 # make sure conda is installed to your sistem
    conda activate venv
    or
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
    pip install -r requirements.txt


# Running the Application
1. Initialize the database:
    python -c 'from app.database import init_db; init_db()'

2. Start the FastAPI server:
    uvicorn app.main:app --reload

3. Access the application at 'http://localhost:8000'

# API Endpoints
1. Welcome Endpoint
    GET /
    Description: Welcome message with available APIs and authentication details.
    Example Response:
    {"message": "Welcome to Atlys, Lets starts!!"}

2. Get All Products
    GET /products
    Description: Retrieve all scraped products.
    Authentication: Requires Authorization header with the API key.
    Example Response:[
        {
            "title": "Product 1",
            "price": 10.99,
            "image_url": "http://example.com/image1.jpg",
            "path_to_image": "images/Product 1.jpg"
        },
        {
            "title": "Product 2",
            "price": 20.99,
            "image_url": "http://example.com/image2.jpg",
            "path_to_image": "images/Product 2.jpg"
        }
    ]

3. Start Scraping
    POST /scrape
    Description: Start the scraping process in the background.
    Authentication: Requires Authorization header with the API key.
    Parameters:
        page_limit (query parameter): Number of pages to scrape.
        proxy (query parameter, optional): Proxy string to use for scraping.
    
    Example Response:{
        "message": "Scraping started in background !!!"
    }

4. Clear Cache
    POST /clear_cache
    Description: Clear the cached scraping results.
    Authentication: Requires Authorization header with the API key.
    Example Response:{
        "message": "ok"
    }

# Authentication
The API endpoints require a static token for authentication. Include the following header in your requests:

Header Name: Authorization
Header Value: 'U2FpbGVzaEt1bWFy'

# Author Sailesh Kumar
# SoftwareEngineer at Subtlabs Software Solutions Pvt ltd
