import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """
            b: integer = 1; 
            main: function void () {} 
            foo: function void (a: integer, b: integer) {}
            a: float = 1; 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_1(self):
        input = """
            b: integer = 1; 
            main: function void () {
            } 
            b: float = 1; 
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_2(self):
        input = """
            b: integer = 1; 
            main: function void () {} 
            b: function void (a: integer, b: integer) {}
            t: float = 1; 
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test_3(self):
        input = """
            b: integer = 1; 
            main: function void () {} 
            foo: function void (a: auto, a: integer) {
                t: float = 1; 
            }
            t: float = 1; 
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 503))
    
    # def  test_4(self):
    #     input = """
    #         b: auto;
    #     """
    #     expect = "Invalid Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 504))

    # def  test_5(self):
    #     input = """
    #         b: auto = 2;
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 505))
