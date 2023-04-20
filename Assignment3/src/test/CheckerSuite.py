# import unittest
# from TestUtils import TestChecker
# from AST import *
 
# class CheckerSuite(unittest.TestCase):

#     def test_35(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{}
#             m: auto = 2;
#             n: float = main(3);
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in expression: FuncCall(main, [IntegerLit(3)])"
#         self.assertTrue(TestChecker.test(input, expect, 535))

#     def test_36(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 m = 5;
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 536))

#     def test_37(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 m = bar(3,4);
#                 t: integer = bar(2,3);
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(t, IntegerType, FuncCall(bar, [IntegerLit(2), IntegerLit(3)]))"
#         self.assertTrue(TestChecker.test(input, expect, 537))

#     def test_38(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 if (m) {
#                     t: string = "hello";
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in statement: IfStmt(Id(m), BlockStmt([VarDecl(t, StringType, StringLit(hello))]))"
#         self.assertTrue(TestChecker.test(input, expect, 538))

#     def test_39(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 if (bar(2,5)) {
#                     t: string = "hello";
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 539))

#     def test_40(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 if (true) {
#                     t: string = "hello";
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 540))

#     def test_41(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 if (true) {
#                     t: string = "hello";
#                 } else {
#                     n: auto;
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Invalid Variable: n"
#         self.assertTrue(TestChecker.test(input, expect, 541))

#     def test_42(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 while (true) {
#                     t: auto;
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Invalid Variable: t"
#         self.assertTrue(TestChecker.test(input, expect, 542))

#     def test_43(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 while (m) {
#                     t: auto;
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in statement: WhileStmt(Id(m), BlockStmt([VarDecl(t, AutoType)]))"
#         self.assertTrue(TestChecker.test(input, expect, 543))

#     def test_44(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 while (bar(3,2)) {
#                     t: auto;
#                 }
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Invalid Variable: t"
#         self.assertTrue(TestChecker.test(input, expect, 544))

#     def test_45(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 m: auto = 3.5;
#                 s = 4;
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Undeclared Identifier: s"q    
#         self.assertTrue(TestChecker.test(input, expect, 545))

#     def test_45(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 i: auto = 2.5;
#                 for (i = 1, i <= 5, i + 1){}
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
#         self.assertTrue(TestChecker.test(input, expect, 545))
    
#     def test_46(self):
#         input = """
#             main: function auto (a: integer, b: integer) inherit bar{
#                 i: auto = 2;
#                 for (i = bar(2,4), i <= 5, i + 1){}
#             }
#             bar: function auto (b: integer, inherit c: integer) {}
#         """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
#         self.assertTrue(TestChecker.test(input, expect, 546))

    # def test_0(self):
    #     input = """
    #         b: integer = 1; 
    #         foo: function void () {} 
    #         main: function void (a: integer, b: integer) {}
    #         a: float = 1; 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 500))

    # def test_1(self):
    #     input = """
    #         b: integer = 1; 
    #         main: function void () {} 
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
    #         foo: function void () {} 
    #         main: function void (a: integer, a: integer) {}
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 503))
    
    # def  test_4(self):
    #     input = """
    #         b: auto;
    #     """
    #     expect = "Invalid Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 504))

    # def  test_5(self):
    #     input = """
    #         b: auto = true;
    #         a: integer;
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 505))
    
    # def  test_6(self):
    #     input = """
    #         a: integer;
    #         t: float;
    #         a: auto;
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 506))
    
    # def  test_7(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void ( a: integer, a: integer) inherit bar {}
    #         bar: function void (inherit c: integer, b: integer) {}
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 507))
    
    # def  test_8(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, inherit c: integer, b:float) inherit bar {}
    #         bar: function void (inherit c: integer, b: integer) {}
    #     """
    #     expect = "Invalid Parameter: c"
    #     self.assertTrue(TestChecker.test(input, expect, 508))

    # def  test_9(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit bar {
    #             b: float;
    #         }
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 509))

    # def  test_10(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit bar {
    #             c: float;
    #         }
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 510))
    
    # def  test_11(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit bar {
    #             t: float;
    #             {
    #                 a: float;
    #                 c: integer;
    #             }
    #         }
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 511))

    # def  test_12(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit goo {}
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Undeclared Function: goo"
    #     self.assertTrue(TestChecker.test(input, expect, 512))
    
    # def test_13(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit goo {}
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Undeclared Function: goo"
    #     self.assertTrue(TestChecker.test(input, expect, 513))

    # def test_14(self):
    #     input = """
    #         t: integer = 2;
    #         main: function void (a: integer, b: integer) inherit bar{
    #             goo();
    #         }
    #         bar: function void (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Undeclared Function: goo"
    #     self.assertTrue(TestChecker.test(input, expect, 514))

    # def test_15(self):
    #     input = """
    #         t: integer = 2;
    #         bar: function void (b: integer, inherit c: integer) {}
    #         main: function void (a: integer, b: integer) inherit bar{
    #             t: integer = bar;
    #         }
    #     """
    #     expect = "Undeclared Identifier: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 515))

    # # =================================================================
    # # TYPE_MISMATCH_IN_EXPRESSION 
    # def test_16(self):
    #     input = """
    #         t: auto = 1.5 + 2;
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 516))

    # def test_17(self):
    #     input = """
    #         t: float = 1 + 2;
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 517))

    # def test_18(self):
    #     input = """
    #         t: float = true + 2;
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, BooleanLit(True), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 518))

    # def test_19(self):
    #     input = """
    #         t: integer = 1.5 + 2;
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(t, IntegerType, BinExpr(+, FloatLit(1.5), IntegerLit(2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 519))

    # def test_20(self):
    #     input = """
    #         a: auto = 1.4 + 2;
    #         b: integer = a + 5;
    #     """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(5)))"
    #     self.assertTrue(TestChecker.test(input, expect, 520))

    # def test_21(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{
    #             t: integer;
    #         }
    #         a: auto = main(2,3) + 2.5;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 521))

    # def test_22(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{
    #             t: integer;
    #         }
    #         a: auto = 2.5 - main(2,3);
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 522))

    # def test_23(self):
    #     input = """
    #         main: function auto (a: integer, b: integer){
    #             t: integer;
    #             main(2,3);
    #         }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 523))

    # def test_24(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{
    #             t: integer;
    #         }
    #         a: integer = main(2,3);
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 524))

    # def test_25(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         m: float = main(1,3) % true;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Type mismatch in expression: BinExpr(%, FuncCall(main, [IntegerLit(1), IntegerLit(3)]), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 525))

    # def test_26(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         m: auto = m % 3;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 526))

    # def test_27(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         m: auto = m && main(2,4);
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 527))

    # def test_28(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         m: auto = "hello";
    #         n: string = ""::m;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 528))

    # def test_29(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{
    #             d: boolean = true;
    #             n: auto = c == d;
    #         }
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 529))

    # def test_30(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         d: float = 25;
    #         n: auto = 12 >= d;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 530))

    # def test_31(self):
    #     input = """
    #         main: function auto (a: integer, b: integer) inherit bar{}
    #         m: auto = 6;
    #         n: auto = !m;
    #         bar: function auto (b: integer, inherit c: integer) {}
    #     """
    #     expect = "Type mismatch in expression: UnExpr(!, Id(m))"
    #     self.assertTrue(TestChecker.test(input, expect, 531))

    



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
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 505))
    
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
    #             d : integer = 1 + true;
    #             a : integer = 1;
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 506))
        
    # def test_7(self):
    #     input = """     
    #         foo: function void (a: auto, c: integer) {
    #             c = a; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 507))
        
    # def test_8(self):
    #     input = """     
    #         main: function void () {} 
    #         foo: function void (a: auto, c: integer) {
    #             d = a; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Undeclared Identifier: d"
    #     self.assertTrue(TestChecker.test(input, expect, 508))
    
    # def test_9(self):
    #     input = """     
    #         foo: function void () {} 
    #         foo: function void (a: auto, c: integer) {
    #             d = a; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 509))
    
    # def test_10(self):
    #     input = """     
    #         a : auto;
    #         main: function void () {} 
    #         foo: function void (a: auto, c: integer) {
    #             c = a; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 510))

    # def test_11(self):
    #     input = """  
    #     main: function void () {}    
    #         foo: function void (a: auto, c: integer) {
    #             c = a; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 511))
    
    # def test_12(self):
    #     input = """  
    #     main: function void () {}    
    #         foo: function void (a: array [1] of integer, c: integer) {
    #             c[4] = c; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(4)])"
    #     self.assertTrue(TestChecker.test(input, expect, 512))
    
    # def test_13(self):
    #     input = """  
    #     main: function void () {}    
    #         foo: function void (a: array [1] of integer, c: integer) {
    #             d[4] = c; 
    #         }
    #         t: float = 1; 
    #     """
    #     expect = "Type mismatch in expression: ArrayCell(d, [IntegerLit(4)])"
    #     self.assertTrue(TestChecker.test(input, expect, 513))
    
    
    # def test_14(self):
    #     input = """       
    #         t: float = 1;      
    #         foo: function void (a: array [1] of integer, c: integer) {
    #             a[4] = c; 
    #         }
    #         main: function void () {
    #             t = foo();
    #         }  
    #     """
    #     expect = "Type mismatch in expression: FuncCall(foo, [])"
    #     self.assertTrue(TestChecker.test(input, expect, 514))
        
    # def test_15(self):
    #     input = """       
    #         t: float = 1;      
    #         foo: function integer (a: array [1] of integer, c: integer) {
    #             a[4] = c; 
    #         }
    #         main: function void () {
    #             t = foo();
    #         }  
    #     """
    #     expect = "Type mismatch in expression: FuncCall(foo, [])"
    #     self.assertTrue(TestChecker.test(input, expect, 515))
    
    # def test_15(self):
    #     input = """       
    #         t: float = 1;      
    #         foo: function void (a: array [1] of integer, c: integer) {
    #             a[4] = c; 
    #         }
    #         main: function void () {
    #             t = foo();
    #         }  
    #     """
    #     expect = "Type mismatch in expression: FuncCall(foo, [])"
    #     self.assertTrue(TestChecker.test(input, expect, 515))
        
    # def test_16(self):
    #     input = """     
    #         main: function void () {} 
    #         i : integer = foo1();
    #         foo: function void (a: auto, c: integer) {
    #             c = a; 
    #             foo1();
    #         }
    #         foo1: function float () {}
    #         t: float = 1; 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 516))
    
    def test_17(self):
        input = """     
            main: function void () {} 
            i : integer = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                a[1,2] = 3;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 517))
        
    def test_18(self):
        input = """     
            main: function void () {} 
            i : integer = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                if (i > 2) return;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 518))
        
    def test_19(self):
        input = """     
            main: function void () {} 
            i : string = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                if (i > 2) return;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in expression: BinExpr(>, Id(i), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 519))
        
    def test_20(self):
        input = """     
            main: function void () {} 
            i : string = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                if ("1" :: " ") return;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: IfStmt(BinExpr(::, StringLit(1), StringLit( )), ReturnStmt())"
        self.assertTrue(TestChecker.test(input, expect, 520))
        
    def test_21(self):
        input = """     
            main: function void () {} 
            i : string = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                do {return 1;} while (a > 1);
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in expression: BinExpr(>, Id(a), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 521))
        
    def test_22(self):
        input = """     
            main: function void () {} 
            i : string = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                if ("1" :: " ") return;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: IfStmt(BinExpr(::, StringLit(1), StringLit( )), ReturnStmt())"
        self.assertTrue(TestChecker.test(input, expect, 522))
        
    def test_23(self):
        input = """     
            main: function void () {} 
            i : string = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                for (i = 1, i < 10, i + 1)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 523))
        
    def test_24(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo: function void (a: array [1] of integer, c: integer) {
                foo1();
                for (c = 1, c < 10, c + i)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(1)), BinExpr(<, Id(c), IntegerLit(10)), BinExpr(+, Id(c), Id(i)), ReturnStmt(IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 524))
        
    def test_25(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo: function void (a: array [1] of integer, c: float) {
                foo1();
                for (c = 1, c < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(1)), BinExpr(<, Id(c), IntegerLit(10)), BinExpr(+, IntegerLit(1), IntegerLit(2)), ReturnStmt(IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 525))
        
    def test_26(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo2: function integer (d: integer, e: integer){}
            foo: function integer (a: array [1] of integer, c: integer) {
                foo2(c, c, c);
                for (c = 1, c < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: CallStmt(foo2, Id(c), Id(c), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 526))
        
    def test_27(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo2: function integer (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: integer) {
                foo2(c, c);
                for (c = 1, c < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: CallStmt(foo2, Id(c), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 527))
        
    def test_27(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo2: function integer (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                foo2(c, c);
                for (c = 1, c < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: CallStmt(foo2, Id(c), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 527))
        
    def test_28(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo2: function integer (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                for (c = 1, c < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = "Type mismatch in statement: AssignStmt(Id(c), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 528))
    
    def test_29(self):
        input = """     
            main: function void () {} 
            i : float = 1 + true;
            foo2: function integer (d: integer, e: string){}
            foo: function integer (a: array [1] of integer, c: auto) {
                d : integer;
                foo2(d, c);
                break;
                for (d = 1, d < 10, 1 + 2)
                    return 1;
            }
            foo1: function float () {}
            t: float = 1; 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 529))
        
    def test_32(self):
        input = """
            main: function auto (a: integer, b: integer) inherit bar{}
            n: auto = !n;
            foo: function auto (b: integer) {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 532))

    # def test_34(self):
    #     input = """
    #         foo: function auto (a: integer, b: integer) inherit bar{}
    #         m: auto = 2;
    #         n: float = - foo(3,4);
    #         bar: function auto (b: integer, inherit c: integer) {}
    #         main: function void () {}
    #     """
    #     expect = "Type mismatch in expression: UnExpr(-, FuncCall(main, [IntegerLit(3), IntegerLit(4)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 534))