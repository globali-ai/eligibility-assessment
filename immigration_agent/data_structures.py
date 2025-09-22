"""
Defines the data structures for the Eligibility Assessment Agent.
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Applicant:
    """Represents an applicant for a visa."""
    name: str
    age: int
    nationality: str
    education_level: str
    work_experience_years: int
    has_job_offer: bool
    financial_status: float


@dataclass
class Visa:
    """Represents the eligibility criteria for a visa."""
    name: str
    type: str
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    required_education: Optional[str] = None
    required_work_experience: Optional[int] = None
    requires_job_offer: Optional[bool] = None
    min_financial_status: Optional[float] = None
    allowed_nationalities: Optional[List[str]] = None
    blocked_nationalities: Optional[List[str]] = None
