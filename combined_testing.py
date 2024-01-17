import unittest
from backend_testing import BackEndTests
from frontend_testing import FrontEndTests


class CombinedTests(unittest.TestCase):
    id = 6
    name = 'aba'
    """Combines backend and frontend tests for comprehensive coverage."""
    backend = BackEndTests(id, name)

    def test_backend_functionality(self):
        """Tests backend operations for posting, retrieving users, and data integrity."""
        self.backend.check_post()
        self.backend.get_user()
        self.backend.check_data()

    def test_frontend_display(self):
        """Tests frontend display of user names."""
        frontend = FrontEndTests(self.id)
        frontend.check_name()

    def tearDown(self):
        """Performs cleanup after each test."""
        self.backend.cleanup()


if __name__ == "__main__":
    unittest.main()
