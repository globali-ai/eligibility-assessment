"""
A sample database of visa rules for the Eligibility Assessment Agent.
"""
from .data_structures import Visa

# A list of sample visa rules. In a real application, this would be stored
# in a database.
sample_visa_database = [
    Visa(
        name="Student Visa (F-1)",
        type="Student",
        min_age=18,
        max_age=35,
        required_education="High School",
        min_financial_status=10000,
    ),
    Visa(
        name="Work Visa (H-1B)",
        type="Work",
        required_education="Bachelors",
        required_work_experience=2,
        requires_job_offer=True,
    ),
    Visa(
        name="Tourist Visa (B-2)",
        type="Tourist",
        min_financial_status=5000,
    ),
    Visa(
        name="Special Program Visa",
        type="Special",
        allowed_nationalities=["Canada", "Mexico"],
    ),
    Visa(
        name="Restricted Visa",
        type="Special",
        blocked_nationalities=["CountryX"],
    ),
]
