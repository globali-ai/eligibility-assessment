"""
A simple command-line interface for the Eligibility Assessment Agent.
"""
from immigration_agent.data_structures import Applicant
from immigration_agent.matching_logic import find_eligible_visas
from immigration_agent.visa_database import sample_visa_database


def main():
    """
    The main function for the CLI.
    """
    print("Welcome to the Immigration Eligibility Assessment Agent!")
    print("Please enter your details below.")

    name = input("Name: ")
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")
    nationality = input("Nationality: ")
    education_level = input("Education Level (e.g., High School, Bachelors, Masters): ")
    while True:
        try:
            work_experience_years = int(input("Years of Work Experience: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for work experience.")
    has_job_offer_str = input("Do you have a job offer? (yes/no): ").lower()
    has_job_offer = has_job_offer_str == 'yes'
    while True:
        try:
            financial_status = float(input("Financial Status (in USD): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for financial status.")

    applicant = Applicant(
        name=name,
        age=age,
        nationality=nationality,
        education_level=education_level,
        work_experience_years=work_experience_years,
        has_job_offer=has_job_offer,
        financial_status=financial_status,
    )

    eligible_visas = find_eligible_visas(applicant, sample_visa_database)

    print("\n--- Assessment Complete ---")
    if eligible_visas:
        print(f"Congratulations, {applicant.name}! You may be eligible for the following visas:")
        for visa in eligible_visas:
            print(f"- {visa.name} ({visa.type})")
    else:
        print(f"Sorry, {applicant.name}. Based on the information provided, we could not find any suitable visas for you at this time.")


if __name__ == "__main__":
    main()
