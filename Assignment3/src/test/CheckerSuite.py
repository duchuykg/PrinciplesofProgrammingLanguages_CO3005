import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckerSuite(unittest.TestCase):
    # def test_0(self):
    #     input = """
    #         b: integer = 1; 
    #         main: function void () {} 
    #         foo: function void (a: integer, b: integer) {}
    #         a: float = 1; 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 500))

    # def test_1(self):
    #     input = """
    #         b: integer = 1; 
    #         main: function void () {
    #         } 
    #         b: float = 1; 
    #     """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 501))

    # def test_2(self):
    #     input = """
    #         b: integer = 1; 
    #         main: function void () {} 
    #         b: function void (a: integer, b: integer) {}
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Function: b"
    #     self.assertTrue(TestChecker.test(input, expect, 502))

    # def test_3(self):
    #     input = """
    #         b: integer = 1; 
    #         main: function void () {} 
    #         foo: function void (a: auto, a: integer) {
    #             t: float = 1; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 503))
    
    # # def  test_4(self):
    # #     input = """
    # #         b: auto;
    # #     """
    # #     expect = "Invalid Variable: b"
    # #     self.assertTrue(TestChecker.test(input, expect, 504))

    # # def  test_5(self):
    # #     input = """
    # #         b: auto = 2;
    # #     """
    # #     expect = ""
    # #     self.assertTrue(TestChecker.test(input, expect, 505))
    
    # def test_6(self):
    #     input = """
    #         b : integer = 1;
    #         main: function void () {} 
            
    #         foo: function void (b: auto, c: integer) {
    #             a : integer = 1;
    #             {
    #                 d: integer = 1;
    #             }
    #             {
    #                 d: integer = 1;
    #             }
    #             d : integer = 1;
    #             a : integer = 1;
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 506))
        
    def test_7(self):
        input = """     
            foo: function void (a: auto, c: integer) {
                c = a; 
            }
            t: float = 1; 
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 507))
        
    def test_8(self):
        input = """     
            main: function void () {} 
            foo: function void (a: auto, c: integer) {
                d = a; 
            }
            t: float = 1; 
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 508))
    
    def test_9(self):
        input = """     
            foo: function void () {} 
            foo: function void (a: auto, c: integer) {
                d = a; 
            }
            t: float = 1; 
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 509))
    
    def test_10(self):
        input = """     
            a : auto;
            main: function void () {} 
            foo: function void (a: auto, c: integer) {
                c = a; 
            }
            t: float = 1; 
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 510))

    def test_11(self):
        input = """  
        main: function void () {}    
            foo: function void (a: auto, c: integer) {
                c = a; 
            }
            t: float = 1; 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))
    
    def test_12(self):
        input = """  
        main: function void () {}    
            foo: function void (a: array [1] of integer, c: integer) {
                a[4] = c; 
            }
            t: float = 1; 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 512))