Eligibility Assessment Agent
This project is an Eligibility Assessment Agent designed to assess an applicant's eligibility for various immigration services. It processes personal information and key details about the applicant's background, matches them against a set of rules, and provides feedback about which immigration options are available to them.

Features
Data Structures: Clear and defined data classes for Applicant and Visa criteria.
Matching Logic: A core engine to match applicant profiles against visa requirements.
Sample Visa Database: An in-memory database with a variety of visa types for testing and demonstration.
Command-Line Interface (CLI): An interactive CLI to input applicant data and receive an eligibility assessment.
Unit Tests: A comprehensive test suite to ensure the reliability of the matching logic.
Getting Started
Prerequisites
Python 3.6 or higher
Installation
Clone the repository.
Navigate to the project directory.
Usage
To run the Eligibility Assessment Agent, execute the main.py script from the root directory:

python main.py
The application will then prompt you to enter the applicant's details. After you provide the information, it will display a list of eligible visas.

Example
Welcome to the Immigration Eligibility Assessment Agent!
Please enter your details below.
Name: Jane Doe
Age: 28
Nationality: Canada
Education Level: Bachelors
Years of Work Experience: 3
Do you have a job offer? (yes/no): yes
Financial Status (in USD): 60000

--- Assessment Complete ---
Congratulations, Jane Doe! You may be eligible for the following visas:
- Work Visa (H-1B) (Work)
- Tourist Visa (B-2) (Tourist)
- Special Program Visa (Special)
Running Tests
To run the unit tests, use Python's built-in unittest module from the root directory:

python -m unittest discover
This command will automatically discover and run the tests located in the tests/ directory.

