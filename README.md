# Assignment 3: Cash Register using Django-ORM

This assignment implements key functionalities of a cash register application using the **Django Object-Relational Management (ORM)** feature.

## Group 5 Contribution Summary

**Members:** Eesha Razia, Sayyeda Faruqui

| Member | Contribution |
| :--- | :--- |
| **Eesha Razia** | Q1 Code Implementation, README.MD Organization and Formatting |
| **Sayyeda Faruqui** | Repository Organization (File Uploads), README.MD Organization and Formatting, Q2 Completion and Submission on Canvas |

*Both members reviewed each other's work and supported each other throughout the assignment.*

---

## 1. Repository Organization and Django-ORM Use (Q1-Code)

This section addresses the Q1-Code Organization and Django ORM rubric criterion. The project is based on the provided Django-ORM startup code, modified for a complete web application structure to demonstrate ORM functionality via a simple UI.

### Key Files and Directory Structure

The following files show the structure and implementation of the required cash register functionality:

| File/Directory | Description | Django-ORM Use |
| :--- | :--- | :--- |
| **`register/models.py`** | Defines the Product model, which maps the product UPC, Name, and Price to the database table. | **Model Definition** |
| **`register/views.py`** | Contains the logic for populating the database and handling the product "scan" (lookup) request from the UI. | **Query Execution** |
| **`register/scan.html`** | The UI template containing the input box for the UPC and the display area for the resulting product details. | **Presentation** |
| **`products.json`** | Source file used to populate the initial product data into the database (Fixture). | **Data Source** |
| **`manage.py` & `settings.py` & `urls.py`** | Core Django files configured to recognize the register app and handle routing to the scan.html view. | **Framework Configuration** |

<img width="1302" height="554" alt="image" src="https://github.com/user-attachments/assets/f5907869-d988-46f6-ac6a-4107446a8b02" />


---

## 2. Setup and Execution Instructions

To run and test the application, follow these steps:

### A. Environment Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-5-crn-43510.git](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-5-crn-43510.git)
    cd assignment-3-django-and-energy-group-5-crn-43510
    ```
2.  **Set Up Virtual Environment:**
    ```bash
    python -m venv venv
    ```
    *Activate:*
    ```bash
    # Windows: venv\Scripts\activate
    # Linux/macOS: source venv/bin/activate
    ```
3.  **Install Django:**
    ```bash
    pip install django
    ```

### B. Running the Application

4.  **Database Migration & Population:**
    The `register` app uses a migration file (e.g., `register/migrations/0001_initial.py`) to create the Product database table. The database is populated with initial product data from the `products.json` file, which is formatted as a Django fixture.

    Run the standard Django setup and then the fixture load command:
    ```bash
    # 1. Apply migrations to create the Product table
    python manage.py migrate

    # 2. Load the initial data from the fixture file
    python manage.py loaddata products.json
    ```
5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Access the application at the root URL: `http://127.0.0.1:8000/`

---

## 3. Demonstration of Functionality (Q1-Demonstration)

This section addresses the Q1-Demonstration rubric criterion and includes the submission of screen dumps/images. The implementation covers two aspects of the cash register application using Django-ORM:

### A. Populating the Database

The database is populated with product UPC codes, Names, and prices.

**Evidence (views.py code snippet):**

<img width="1279" height="465" alt="image" src="https://github.com/user-attachments/assets/9da6a0f8-0ac6-408b-8011-b5d9e8d24bc9" />


### B. Scanning a Product and Displaying Details

The web interface simulates the scanning of a product (via an input box) and displays the product name and price. This demonstrates a read operation using the ORM.

**Evidence:**

1.  **Initial View:** Screenshot of the `scan.html` interface showing the UPC input box and an empty result display before a scan.
     <img width="1324" height="355" alt="image" src="https://github.com/user-attachments/assets/a2581c30-fe59-4ede-8606-f3130a27b0c7" />


2.  **Successful Scan:** Screenshot showing a valid UPC entered into the input box and the resulting Product Name and Price displayed clearly after submission.
    <img width="1313" height="438" alt="image" src="https://github.com/user-attachments/assets/7e669e9b-2964-4ef6-852d-0e1f813ff9dc" />


3.  **Error Handling:** Screenshot showing an invalid UPC entered and the application's appropriate response ("Product Not Found").
    <img width="1341" height="364" alt="image" src="https://github.com/user-attachments/assets/db2f7ffa-1cf7-40f9-994d-fe998a6dc8ca" />

---

## 4. Q2: Energy Efficiency Scenario (Canvas Submission Reference)

This section is a placeholder to acknowledge the second part of the assignment. **Q2 is submitted via the Canvas drop box.**

* A concrete energy efficiency scenario for a smartphone app (e.g., a health monitoring app) was created based on the Energy Efficiency General Scenario table in the Appendix.
* Two architectural/design tactics were identified, and their application and contribution to better energy efficiency were briefly explained.
