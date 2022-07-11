import sys
from fake_data_brs import UserFactory
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 

import customer,rentalsore,unittest,faker

class test_showentity(unittest.TestCase):
    
    def test_case1(self):
        rentalsore.admin.add_no_of_bikes(10)
        self.assertEqual(rentalsore.admin.no_of_bike_nprice(),
        f"number of bikes available\t: {rentalsore.admin.no_of_bikes}\nprice={rentalsore.admin.price}\noffer= Group Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price")

unittest.main()
    