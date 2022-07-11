import sys
from fake_data_brs import UserFactory
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 

import customer,rentalsore,unittest,faker

class test_showentity(unittest.TestCase):
    
    def test_case1(self):
        user=UserFactory()
        self.assertEqual(user.show_entity(),({"Name":user.name,"contact":user.contact,"your id":user.id,"number of bikes rented":user.quanti,"ttal balance remaining":user.balance}))


unittest.main()