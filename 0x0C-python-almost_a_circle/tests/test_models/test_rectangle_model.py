#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

'''
    Runs test cases for the Rectangle module
'''


class test_rectangle(unittest.TestCase):
    '''
        Testing rectangle
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_width(self):
        '''
            Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''
            Testing the Rectangle height getter
        '''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''
            Testing Rectangle x getter and setter
        '''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        '''
            Testing Rectangle y getter and setter
        '''

        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_arectangle_id(self):
        '''
            Test the id for Rectangle
        '''
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 5)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

    def test_height_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "5")

    def test_height_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, True)

    def test_height_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, "46")

    def test_x_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_y_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

    def test_height_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 0)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1.07, 5)

    def test_height_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.07)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 8, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 5, 8, 1.07)

    def test_area(self):
        '''
            Testing the area of the rectangle
        '''
        self.assertEqual(self.r.area(), 5 * 10)
        rect = Rectangle(3, 9, 8, 8, 2)
        self.assertEqual(rect.area(), 3 * 9)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        '''
            Testing the update method
        '''
        self.r.update(54)
        self.assertEqual(54, self.r.id)

    def test_update_width(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30)
        self.assertEqual(30, self.r.width)

    def test_update_height(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10)
        self.assertEqual(10, self.r.height)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10, 6)
        self.assertEqual(6, self.r.x)

    def test_update_y(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10, 6, 2)
        self.assertEqual(2, self.r.y)
