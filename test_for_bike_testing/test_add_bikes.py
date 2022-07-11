import sys
from fake_data_brs import UserFactory
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 

import customer,rentalsore,unittest,faker

class test_showentity(unittest.TestCase):
    
    def test_add_bikes(self):
        self.assertEqual(rentalsore.admin.add_no_of_bikes(10),f"{10} bikes added sucessfully")


unittest.main()
