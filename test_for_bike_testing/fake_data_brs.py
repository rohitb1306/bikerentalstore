import factory
from faker import Faker
import sys
import fake_data_brs
sys.path.insert(0, "/home/dell/Desktop/projects/bikerentalsysytem") 
import customer

f=Faker("en_IN")
class UserFactory(factory.Factory):
    
    class Meta:
        model = customer.entity
    
    name = f.profile()['name']
    mail = f.profile()["mail"]
    id=factory.sequence(lambda n : "00%d"%n)
    password= f.profile()["ssn"]
# rohit = UserFactory()
# harsh= UserFactory()
# print(rohit)
# print(f"name:{rohit.name},mail:{rohit.mail},id:{rohit.id},password:{rohit.password}")
# print(f"name:{harsh.name},mail:{harsh.mail},id:{harsh.id},password:{harsh.password}")