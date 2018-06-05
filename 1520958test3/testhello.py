import unittest
from hello import Users
from hello import db

class TestHello(unittest.TestCase):
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()
        
    def test_add1(self):
        user1 = Users(username='1520958傅琦')
        self.assertEqual(user1.username, '1520958傅琦')
    
    def test_add2(self):
        user2 = Users(username='1520958傅琦')
        self.assertEqual(user2.age, 20)
		
    def test_add3(self):
        user3 = Users(username='1520958傅琦')
        user3.age = 24
        self.assertEqual(user3.age, 24)

if __name__ == '__main__':
    unittest.main()