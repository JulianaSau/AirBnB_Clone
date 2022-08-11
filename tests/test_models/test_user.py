#!/usr/bin/python3
'''
Contains all tests for the base_model class
'''
from models.base_model import BaseModel
from models.user import User
import unittest
import os


class TestUser(unittest.TestCase):
    '''
    Tests that the BaseModel works okay
    '''
    def setUp(self):
        '''
        Set up method
        Renames the file_storage file to avoid iterfering with data
        '''
        if os.path.isfile("file.json"):
            os.rename("file.json", "backup_file.json")

        self.model_1 = User()
        self.model_2 = User()

    def tearDown(self):
        '''
        Tear down method
        Does clean up
        '''
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("backup_file.json"):
            os.rename("backup_file.json", "file.json")

        del self.model_1
        del self.model_2

    def test_attributes_types(self):
        '''
        Test that all attributes are of the correct type
        '''
        self.assertTrue(type(self.model_1), BaseModel)

    def test_attributes_exist(self):
        '''
        Test that class User has the required attributes and methods
        '''
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_attribute_types(self):
        """Test whether the class attributes are of the right type"""
        user_1 = User()
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)

    def test_isinstance(self):
        '''
        Check that the created instance is an instance of the BaseModel class
        '''
        self.assertIsInstance(self.model_1, BaseModel)

    def test_is_subclass(self):
        '''
        Check whethe User is a subclass of basemodel
        '''
        self.assertTrue(issubclass(self.model_1.__class__, BaseModel))

    def test_inherited_attributes(self):
        '''
        Confirm that all the required attributes were imported from BaseModel
        Also confirm that User's attributes are present
        '''
        self.assertTrue('id' in self.model_1.__dict__)
        self.assertTrue('created_at' in self.model_1.__dict__)
        self.assertTrue('updated_at' in self.model_1.__dict__)

if __name__ == "__main__":
    unittest.main()
