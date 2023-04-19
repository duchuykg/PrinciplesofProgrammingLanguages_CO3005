import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_more_complex_program(self):
        input = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
    ])"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 500))
        
    def test_more_complex_program(self):
        input = """Program([
	    VarDecl(a, StringType, ArrayLit([]))
      VarDecl(a, IntegerType, ArrayLit([]))
    ])"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 501))