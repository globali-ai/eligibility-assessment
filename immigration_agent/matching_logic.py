"""
Implements the core eligibility matching logic for the Eligibility Assessment Agent.
"""
from typing import List
from .data_structures import Applicant, Visa


def is_eligible(applicant: Applicant, visa: Visa) -> bool:
    """
    Checks if an applicant is eligible for a single visa.

    Args:
        applicant: The applicant's data.
        visa: The visa's eligibility criteria.

    Returns:
        True if the applicant is eligible, False otherwise.
    """
    if visa.min_age is not None and applicant.age < visa.min_age:
        return False
    if visa.max_age is not None and applicant.age > visa.max_age:
        return False
    if visa.required_education is not None and applicant.education_level != visa.required_education:
        return False
    if visa.required_work_experience is not None and applicant.work_experience_years < visa.required_work_experience:
        return False
    if visa.requires_job_offer is not None and visa.requires_job_offer and not applicant.has_job_offer:
        return False
    if visa.min_financial_status is not None and applicant.financial_status < visa.min_financial_status:
        return False
    if visa.allowed_nationalities is not None and applicant.nationality not in visa.allowed_nationalities:
        return False
    if visa.blocked_nationalities is not None and applicant.nationality in visa.blocked_nationalities:
        return False

    return True


def find_eligible_visas(applicant: Applicant, visas: List[Visa]) -> List[Visa]:
    """
    Finds all visas for which an applicant is eligible.

    Args:
        applicant: The applicant's data.
        visas: A list of all available visas.

    Returns:
        A list of visas for which the applicant is eligible.
    """
    return [visa for visa in visas if is_eligible(applicant, visa)]
