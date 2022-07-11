import sys
from fake_data_brs import UserFactory
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 

import customer,rentalsore,unittest,faker

class test_rentbike(unittest.TestCase):
    
    def test_case1(self):
        user=UserFactory()
        self.assertEqual(user.rent_bike(3,"week"),"bikes rented")

    def test_case2(self):
        user=UserFactory()
        self.assertEqual(user.rent_bike(6,"day"),"we dont allow more that 5 bikes to a single customer")

    def test_case3(self):
        user=UserFactory()
        self.assertEqual(user.rent_bike(4,"day"),f"Not enough bikes for rent\n{rentalsore.admin.no_of_bikes} bikes left")

    def test_case4(self):
        user=UserFactory()
        rentalsore.admin.add_no_of_bikes(10)
        self.assertEqual(user.rent_bike(4,"week"),"bikes rented")

    def test_case5(self):
        user=UserFactory()
        self.assertEqual(user.rent_bike(1,"weeks"),"wrong time length selected")


unittest.main()