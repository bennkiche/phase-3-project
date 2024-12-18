Labaratory Managament CLI App
The Lab Management System provides functionalities for creating, updating, and deleting labs and tests, as well as searching for them based on various criteria.

The application utilizes Object-Relational Mapping (ORM) techniques to interact with a SQLite database, ensuring data persistence and integrity.

Features
1.Manage labs: Create, update, delete, and search for labs by name, section, or ID.

2.Manage tests: Create, update, delete, and search for tests by name or ID.

3.One-to-many relationship:  a one to many relationship between the models where a lab can have many tests and a tests is specific to a given lab
A user will be able to:.

4.Command Line Interface (CLI): User-friendly interface for interacting with the application.

5.Input validation: Ensure data integrity by validating user input for lab and test creation/update.

6. Lists the the available labs and tests

7. Assign tests to a specific lab and view the tests to a specific lab

Usage
Ensure the database is initialized and populated with sample data: python3 debug.py

Run the CLI application: python3 cli.py

Follow the prompts to interact with the application:
Choose options to manage labs and tests. Create, update, delete, or search for labs and tests as needed. Use input validation to ensure data integrity.