# Python Practice and Student Management System

This repository contains my Python learning programs and my Student Management System project.

## Student Management System

A menu-driven application built using Python to manage student records.

### Features

* Add student records
* View all students
* Search students by roll number
* Update student details
* Delete student records
* Validate user inputs
* Prevent duplicate roll numbers
* Save and load records using JSON

### Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON file handling

### How to Run

1. Install Python.

2. Open the terminal in the project folder.

3. Run:

   `py student_management.py`

4. Choose an option from the menu.

## Learning Goals

Practising Python programming, classes and objects, input validation, file handling, and project development.

## 💰 Expense Tracker Dashboard

A Python-based expense tracking application built with Streamlit. It helps users record daily expenses, monitor monthly spending, visualize spending patterns, and manage a monthly budget.

### Features
- Add expenses with amount, category, description, and date.
- Automatically save expenses in a local JSON file.
- View total spending, current-month spending, transaction count, and average expense.
- Visualize category-wise spending with a donut chart.
- View monthly spending trends with a bar chart.
- Delete recorded expenses.
- Set a monthly budget and receive spending alerts.
- View recent expenses and all transactions.

### Technologies Used
- Python
- Streamlit
- Pandas
- JSON

### How to Run

1. Install Python 3.12 or a compatible Python version.
2. Install the required libraries:

   `py -m pip install streamlit pandas`

3. Open the project folder in your terminal.
4. Run the application:

   `py -m streamlit run expense_tracker.py`

5. Open the local URL displayed in your terminal.

### Project Files
- `expense_tracker.py` — Main dashboard application.
- `expenses.json` — Local expense data created when expenses are saved. This file is excluded from Git using `.gitignore`.

### Future Improvements
- Export expenses to CSV.
- Add date-range filters.
- Add monthly category comparisons.
- Improve the dashboard's visual design.
