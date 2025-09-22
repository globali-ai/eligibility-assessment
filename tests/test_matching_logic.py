"""
Unit tests for the matching logic of the Eligibility Assessment Agent.
"""
import unittest
from immigration_agent.data_structures import Applicant, Visa
from immigration_agent.matching_logic import is_eligible, find_eligible_visas


class TestMatchingLogic(unittest.TestCase):
    """Test cases for the eligibility matching logic."""

    def setUp(self):
        """Set up some sample applicants and visas for testing."""
        self.applicant1 = Applicant("John Doe", 30, "USA", "Bachelors", 5, True, 50000)
        self.applicant2 = Applicant("Jane Smith", 22, "Canada", "High School", 1, False, 12000)
        self.applicant3 = Applicant("Peter Pan", 17, "Neverland", "None", 0, False, 1000)
        self.applicant4 = Applicant("Dr. Jones", 45, "USA", "PhD", 20, True, 100000)
        self.applicant5 = Applicant("Carlos", 28, "Mexico", "Masters", 3, True, 25000)

        self.student_visa = Visa("Student Visa", "Student", min_age=18, max_age=35, required_education="High School", min_financial_status=10000)
        self.work_visa = Visa("Work Visa", "Work", required_education="Bachelors", required_work_experience=2, requires_job_offer=True)
        self.special_visa = Visa("Special Visa", "Special", allowed_nationalities=["Canada", "Mexico"])
        self.restricted_visa = Visa("Restricted Visa", "Special", blocked_nationalities=["Neverland"])

        self.all_visas = [self.student_visa, self.work_visa, self.special_visa, self.restricted_visa]

    def test_is_eligible_student(self):
        """Test eligibility for a student visa."""
        self.assertTrue(is_eligible(self.applicant2, self.student_visa))
        self.assertFalse(is_eligible(self.applicant1, self.student_visa)) # Fails on education
        self.assertFalse(is_eligible(self.applicant3, self.student_visa)) # Fails on age and financial status

    def test_is_eligible_work(self):
        """Test eligibility for a work visa."""
        self.assertTrue(is_eligible(self.applicant1, self.work_visa))
        self.assertFalse(is_eligible(self.applicant2, self.work_visa)) # Fails on education, experience and job offer

    def test_nationality_restrictions(self):
        """Test eligibility with nationality restrictions."""
        self.assertTrue(is_eligible(self.applicant2, self.special_visa)) # Allowed: Canada
        self.assertTrue(is_eligible(self.applicant5, self.special_visa)) # Allowed: Mexico
        self.assertFalse(is_eligible(self.applicant1, self.special_visa)) # Not in allowed list

        self.assertTrue(is_eligible(self.applicant1, self.restricted_visa)) # Not in blocked list
        self.assertFalse(is_eligible(self.applicant3, self.restricted_visa)) # In blocked list

    def test_find_eligible_visas(self):
        """Test the function that finds all eligible visas for an applicant."""
        # Applicant 1 should be eligible for Work Visa and Restricted Visa
        eligible_for_applicant1 = find_eligible_visas(self.applicant1, self.all_visas)
        self.assertEqual(len(eligible_for_applicant1), 2)
        self.assertIn(self.work_visa, eligible_for_applicant1)
        self.assertIn(self.restricted_visa, eligible_for_applicant1)

        # Applicant 2 should be eligible for Student, Special, and Restricted
        eligible_for_applicant2 = find_eligible_visas(self.applicant2, self.all_visas)
        self.assertEqual(len(eligible_for_applicant2), 3)
        self.assertIn(self.student_visa, eligible_for_applicant2)
        self.assertIn(self.special_visa, eligible_for_applicant2)
        self.assertIn(self.restricted_visa, eligible_for_applicant2)

        # Applicant 3 should not be eligible for any visa
        eligible_for_applicant3 = find_eligible_visas(self.applicant3, self.all_visas)
        self.assertEqual(len(eligible_for_applicant3), 0)


if __name__ == '__main__':
    unittest.main()
