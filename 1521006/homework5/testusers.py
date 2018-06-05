import unittest
from hello import db,User

class TestCalcCase(unittest.TestCase):
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()
        
    def test_one(self):
        user=User("wangyiping")
        db.session.add(user)
        db.session.commit()
        test = db.session.query(User).all()[0]
        self.assertEqual(user.username,test.username)
    
    def test_two(self):
        user=User("wangyiping")
        self.assertEqual(user.age, 20)

    def test_three(self):
        user=User("wangyiping")
        user.age=24
        self.assertEqual(user.age,24)

if __name__ == '__main__':
    unittest.main()
