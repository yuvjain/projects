
# Seed Management System

This is a DBMS project developed as a Seed Management System using Python, Tkinter, and MySQL. The system allows users to manage seeds, suppliers, and customers, including functionalities for adding, updating, deleting, and viewing records.

## Project Overview

The Seed Management System is designed to help manage various aspects of seed distribution, including tracking customer orders, maintaining supplier information, and managing seed inventory. It provides an intuitive interface for users to interact with the system and perform CRUD (Create, Read, Update, Delete) operations.

### Key Features

- **Customer Management:** Add, update, delete, and search for customer records.
- **Supplier Management:** Manage supplier details including contact information and address.
- **Seed Inventory:** Maintain a list of available seeds, their categories, prices, and supplier information.
- **Sales Management:** Track sales transactions and maintain records for future reference.
- **Database Integration:** Uses MySQL for backend data storage with a well-structured database schema.

## Project Structure

- `main.py`: The main Python script that contains the logic for the GUI using Tkinter and the database interactions using MySQL.
- `db/`: Contains the SQL scripts or database-related files (if applicable).
- `static/`: Holds any static resources like images or stylesheets (if applicable).
- `templates/`: Contains template files for the GUI layout (if applicable).

## How to Run the Project

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/yuvjain/projects/tree/main/dbms/seed%20management%20system>
    cd <dbms/seed management system>
    ```

2. **Install the required dependencies:**
    Ensure you have Python and the necessary libraries installed. You can install the required libraries using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL Database:**
    - Create a MySQL database for the project.
    - Run the SQL script provided in the `db/` folder (if available) to create the necessary tables.
    - Update the database connection details in the `main.py` file.

4. **Run the Application:**
    ```bash
    python main.py
    ```

5. **Interact with the GUI:**
    Use the graphical interface to manage customers, suppliers, seeds, and sales transactions.

## Dependencies

- Python 3.x
- Tkinter (for GUI)
- MySQL Connector (for database interaction)


## Database Schema
The project uses a MySQL database with tables for customers, suppliers, seeds, and transactions. The schema includes:

- Customer Table: Stores customer details like name, contact number, and address.
- Supplier Table: Stores supplier information including supplier name, contact details, and address.
- Seed Table: Maintains seed information such as category, price, and supplier ID.
- Sales Table: Tracks sales transactions, linking customers and seed products.

## Future Improvements
- Enhanced Reporting: Add features to generate sales reports and inventory status reports.
- User Authentication: Implement a login system to manage access control.
- Data Analytics: Integrate data analytics to gain insights into seed sales and customer trends.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed by Yuv Jain.  
For more projects, visit my [GitHub profile](https://github.com/yuvjain).
