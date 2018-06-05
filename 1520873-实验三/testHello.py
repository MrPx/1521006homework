import unittest
from hello import User
from hello import db

class TestHello(unittest.TestCase):
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()
        
    def test_creatUser(self):
        a=User('shenqianqian')
        self.assertEqual(a.username,'shenqianqian')
    
    def test_userAge(self):
        b=User('shenqianqian')
        self.assertEqual(b.age,20)
	
    def test_userAgeInput(self):
        c=User('shenqianqiann',24)
        self.assertEqual(c.age,24)
		
if __name__ == '__main__':
    unittest.main()
