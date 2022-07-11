import sys
from fake_data_brs import UserFactory
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 

import customer,rentalsore,unittest,faker

class test_returnbike(unittest.TestCase):
    
    def test_case1(self):
        user=UserFactory()
        user.rent_bike(3,"week")
        self.assertEqual(user.return_bike(2),f"returned {2} left to return {user.quanti}")

    def test_case2(self):
        user=UserFactory()
        user.rent_bike(3,"week")
        self.assertEqual(user.return_bike(3),"all bikes returned")

    def test_case3(self):
        user=UserFactory()
        rentalsore.admin.add_no_of_bikes(10)
        user.rent_bike(4,"day")
        user.return_bike(3)
        self.assertEqual(user.return_bike(2),f"only {user.quanti} bikes were left to return you are trying to return more then left")

unittest.main()