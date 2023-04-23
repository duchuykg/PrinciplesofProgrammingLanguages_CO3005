import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckerSuite(unittest.TestCase):
    
    def test_0(self):
        input = """
            b: integer = 1; 
            foo: function void () {} 
            too: function void (a: integer, b: integer) {}
            a: float = 1; 
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_1(self):
        input = """
            b: integer = 1; 
            main: function void () {} 
            b: float = 1; 
            main: function void() {}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_2(self):
        input = """
            b: integer = 1; 
            main: function void () {} 
            b: function void (a: integer, b: integer) {}
            t: float = 1; 
            main: function void() {}
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test_3(self):
        input = """
            b: integer = 1; 
            foo: function void () {} 
            main: function void (a: integer, a: integer) {}
            t: float = 1; 
            main: function void() {}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 503))
    
    def  test_4(self):
        input = """
            b: auto;
            main: function void() {}
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 504))

    def  test_5(self):
        input = """
            b: auto = true;
            a: integer;
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 505))
    
    def  test_6(self):
        input = """
            a: integer;
            t: float;
            a: auto;
            main: function void() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 506))
    
    def  test_7(self):
        input = """
            t: integer = 2;
            main: function void ( a: integer, a: integer) inherit bar {}
            bar: function void (inherit c: integer, b: integer) {}
            main: function void() {}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 507))
    
    def  test_8(self):
        input = """ 
            main: function void () {
            
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 508))

    def  test_9(self):
        input = """
            t: integer = 2;
            main: function void (a: integer, b: integer) inherit bar {
                super(2,3);
                b: float;
            }
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 509))

    def  test_10(self):
        input = """
            t: integer = 2;
            main: function void (a: integer, b: integer) inherit bar {
                super(2,3);
                c: float;
            }
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 510))
    
    def  test_11(self):
        input = """
            t: integer = 2;
            too: function void (a: integer, b: integer) inherit bar {
                super(2,3);
                t: float;
                {
                    a: float;
                    c: integer;
                }
            }
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))

    def  test_12(self):
        input = """
            t: integer = 2;
            main: function void (a: integer, b: integer) inherit goo {}
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 512))
    
    def test_13(self):
        input = """
            t: integer = 2;
            main: function void (a: integer, b: integer) inherit goo {}
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 513))

    def test_14(self):
        input = """
            t: integer = 2;
            main: function void (a: integer, b: integer) inherit bar{
                super(2,3);
                goo();
            }
            bar: function void (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 514))

    def test_15(self):
        input = """
            t: integer = 2;
            bar: function void (b: integer, inherit c: integer) {}
            main: function void (a: integer, b: integer) inherit bar{
                super(2,3);
                t: integer = bar;
            }
            main: function void() {}
        """
        expect = "Undeclared Identifier: bar"
        self.assertTrue(TestChecker.test(input, expect, 515))

    ## TODO: TYPE_MISMATCH_IN_EXPRESSION 
    def test_16(self):
        input = """
            t: auto = 1.5 + 2;
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 516))

    def test_17(self):
        input = """
            t: float = 1 + 2;
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 517))

    def test_18(self):
        input = """
            t: float = true + 2;
            main: function void() {}
        """
        expect = "Type mismatch in expression: BinExpr(+, BooleanLit(True), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 518))

    def test_19(self):
        input = """
            t: integer = 1.5 + 2;
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(t, IntegerType, BinExpr(+, FloatLit(1.5), IntegerLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 519))

    def test_20(self):
        input = """
            a: auto = 1.4 + 2;
            b: integer = a + 5;
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), IntegerLit(5)))"
        self.assertTrue(TestChecker.test(input, expect, 520))

    def test_21(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                t: integer;
            }
            a: auto = too(2,3) + 2.5;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521))

    def test_22(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                t: integer;
            }
            a: auto = 2.5 - too(2,3);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 522))

    def test_23(self):
        input = """
            too: function auto (a: integer, b: integer){
                t: integer;
                too(2,3);
            }
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 523))

    def test_24(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                t: integer;
            }
            a: integer = too(2,3);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524))

    def test_25(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: float = too(1,3) % true;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: BinExpr(%, FuncCall(too, [IntegerLit(1), IntegerLit(3)]), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 525))

    def test_26(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = m % 3;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 526))

    def test_27(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = m && too(2,4);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 527))

    def test_28(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = "hello";
            n: string = ""::m;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 528))

    def test_29(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                d: boolean = true;
                n: auto = c == d;
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 529))

    def test_30(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            d: float = 25;
            n: auto = 12 >= d;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 530))

    def test_31(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = 6;
            n: auto = !m;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: UnExpr(!, Id(m))"
        self.assertTrue(TestChecker.test(input, expect, 531))

    def test_32(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            n: auto = !n;
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 532))

    def test_33(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            n: auto = !too(3,6);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 533))

    def test_34(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = 2;
            n: float = -too(3,4);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 534))
    
    def test_35(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
            }
            m: auto = 2;
            n: float = main(3);
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: FuncCall(main, [IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 535))

    def test_36(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                m = 5;
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 536))

    def test_37(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                m = bar(3,4);
                t: integer = bar(2,3);
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(t, IntegerType, FuncCall(bar, [IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 537))

    def test_38(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                if (m) {
                    t: string = "hello";
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: IfStmt(Id(m), BlockStmt([VarDecl(t, StringType, StringLit(hello))]))"
        self.assertTrue(TestChecker.test(input, expect, 538))

    def test_39(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                if (bar(2,5)) {
                    t: string = "hello";
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 539))

    def test_40(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                if (true) {
                    t: string = "hello";
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 540))

    def test_41(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                if (true) {
                    t: string = "hello";
                } else {
                    n: auto;
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Invalid Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 541))

    def test_42(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                while (true) {
                    t: auto;
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Invalid Variable: t"
        self.assertTrue(TestChecker.test(input, expect, 542))

    def test_43(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                while (m) {
                    t: auto;
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: WhileStmt(Id(m), BlockStmt([VarDecl(t, AutoType)]))"
        self.assertTrue(TestChecker.test(input, expect, 543))

    def test_44(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                while (bar(3,2)) {
                    t: auto;
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Invalid Variable: t"
        self.assertTrue(TestChecker.test(input, expect, 544))

    def test_45(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                m: auto = 3.5;
                s = 4;
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Undeclared Identifier: s"
        self.assertTrue(TestChecker.test(input, expect, 545))

    def test_45(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2.5;
                for (i = 1, i <= 5, i + 1){}
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 545))

    def test_46(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2;
                for (i = 3+3.5, i <= 5, i + 1){}
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(i), BinExpr(+, IntegerLit(3), FloatLit(3.5)))"
        self.assertTrue(TestChecker.test(input, expect, 546))

    def test_47(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2;
                for (i = bar(2,4) + 5, i <= 5, i + 1){}
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 547))

    def test_48(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2;
                for (i = bar(2,4) + 5, i + 7, i + 1){}
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), BinExpr(+, FuncCall(bar, [IntegerLit(2), IntegerLit(4)]), IntegerLit(5))), BinExpr(+, Id(i), IntegerLit(7)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 548))

    def test_49(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2;
                for (i = bar(2,4) + 5, i < 5, i + 1.4){}
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), BinExpr(+, FuncCall(bar, [IntegerLit(2), IntegerLit(4)]), IntegerLit(5))), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), FloatLit(1.4)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 549))

    def test_50(self):
        input = """
            too: function auto (a: integer, b: integer) inherit bar{
                super(2,3);
                i: auto = 2;
                for (i = 1, i < 5, i + 1){
                    m: auto;
                }
            }
            bar: function auto (b: integer, inherit c: integer) {}
            main: function void() {}
        """
        expect = "Invalid Variable: m"
        self.assertTrue(TestChecker.test(input, expect, 550))

    def test_51(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                while (true) {
                    a2: auto = 5;
                    {
                        a3: auto = b+a1;
                    }
                }
            }
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 551))

    ## TODO: MUST_IN_LOOP
    def test_52(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                continue;
                while (true) {
                    a2: auto = 5;
                    {
                        a3: auto = b+a1;
                    }
                }
            }
            main: function void() {}
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 552))

    def test_53(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                while (true) {
                    break;
                    a2: auto = 5;
                    {
                        a3: auto = b+a1;
                    }
                }
            }
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 553))

    def test_54(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                while (true) {
                    a2: auto = 5;
                    {
                        break;
                        a3: auto = b+a1;
                    }
                }
            }
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 554))

    def test_55(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                do {
                    break;
                } while (true);
            }
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 555))

    def test_56(self):
        input = """
            too: function auto (a: integer, b: integer) {
                a1: auto = 2;
                break;
                do {
                } while (true);
            }
            main: function void() {}
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test_56(self):
        input = """
            foo: function auto (a: integer, b: integer) {}
            main: function auto () {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test_57(self):
        input = """
            foo: function auto (a: integer, b: integer) {}
            main: function void (a: float) {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 557))

    def test_58(self):
        input = """
            foo: function auto (a: integer, b: integer) {}
            main: function void () {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 558))

    def test_59(self):
        input = """
            foo: function auto (a: integer, b: integer) {
                main();
            }
            main: function auto () {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 559))

    ## TODO: ARRAY
    def test_60(self):
        input = """
            a: array [4] of integer ={1, 2, 3, 4}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 560))

    def test_61(self):
        input = """
            a: array [4] of integer ={1, 2, 3.4, 4}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.4), IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 561))

    def test_62(self):
        input = """
            a: array [2,2] of integer = {{1,2}, {3, 4}}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 562))

    def test_63(self):
        input = """
            a: array [2,2] of integer = {{1, 3.4}, {3, 4}}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(3.4)])"
        self.assertTrue(TestChecker.test(input, expect, 563))

    def test_64(self):
        input = """
            a: array [2,2] of integer = {{1, 2}, {3, 4, 5}}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)])])"
        self.assertTrue(TestChecker.test(input, expect, 564))

    def test_65(self):
        input = """
            a: array [2,2] of integer = {{1.2, 2.3}, {3, 4}}; 
            main: function void() {
            }
            too: function auto ( a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 565))

    def test_66(self):
        input = """
            a: array [2,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}, {9}}}; 
            main: function void() {
            }
            too: function auto (a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8)]), ArrayLit([IntegerLit(9)])])"
        self.assertTrue(TestChecker.test(input, expect, 566))

    def test_67(self):
        input = """
            a: array [2,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, {{1.3, 2.4}, {3.2, 5.6}}}; 
            main: function void() {
            }
            too: function auto (a: integer, b: integer) {  }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]), ArrayLit([ArrayLit([IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8)])]), ArrayLit([ArrayLit([FloatLit(1.3), FloatLit(2.4)]), ArrayLit([FloatLit(3.2), FloatLit(5.6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 567))

    ## TODO: CHECK VARDECL WITH ARRAYLIT
    def test_68(self):
        input = """
            a: array [2,3] of integer = {{1,2}, {3,4}};
            main: function void() {
            }
            too: function void (a: auto, b: integer, inherit c: auto) {
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))"
        self.assertTrue(TestChecker.test(input, expect, 568))

    def test_69(self):
        input = """
            a: array [2] of integer = {foo(), goo()};
            main: function void() {
                m: string = foo();
            }
            foo: function auto () {}
            goo: function auto () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, StringType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 569))

    ## TODO: CHECK_FUNC_PARAMS
    def test_70(self):
        input = """
            b: integer = 1; 
            too: function auto (a: auto, b: integer, c: auto) {}
            a: float = 1; 
            main: function void() {
                c: string = "hello";
                d: integer = too(a,b,c);
                e: float = too(2.4, 2.5, "bye");
            }
        """
        expect = "Type mismatch in expression: FuncCall(too, [FloatLit(2.4), FloatLit(2.5), StringLit(bye)])"
        self.assertTrue(TestChecker.test(input, expect, 570))

    def test_71(self):
        input = """
            a: float = 1; 
            b: integer = 1; 
            main: function void() {
                c: string = "hello";
                d: string = goo(a,b,c);
            }
            foo: function auto (m: integer) inherit goo {
                preventDefault();
                t: integer = a;
            }
            goo: function auto (a: auto, inherit b: integer, inherit c: auto) {
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(t, IntegerType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 571))
    
    def test_72(self):
        input = """
            b: integer = 1; 
            too: function auto (a: auto, b: integer, c: auto) {}
            a: float = 1; 
            main: function void() {
                c: string = "hello";
                d: integer = too(a,b);
            }
        """
        expect = "Type mismatch in expression: FuncCall(too, [Id(a), Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 572))
    
    def test_73(self):
        input = """
            too: function auto (a: array [3] of float, b: integer) {}
            main: function void() {
                arr: array [2] of float = {4.2,6.2};
                res: auto = too(arr, 1) + 10;
            }
        """
        expect = "Type mismatch in expression: FuncCall(too, [Id(arr), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 573))

    def test_74(self):
        input = """
            too: function auto (a: auto, b: integer) {}
            main: function void() {
                arr: array [2] of float = {4.2,6.2};
                too(arr, 1);
                i: auto = too(arr, 2);
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 574))

    ## TODO: CHECK ARRAY CELL
    def test_75(self):
        input = """
            too: function auto (a: auto, b: integer) {}
            main: function void() {
                arr: array [2] of float = {4.2,6.2};
                t: float = arr[1,2];
            }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 575))

    def test_76(self):
        input = """
            too: function string (a: auto, b: integer) {}
            main: function void() {
                arr: array [2] of float = {4.2,6.2};
                t: float = arr[too(2,4)];
            }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [FuncCall(too, [IntegerLit(2), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 576))

    def test_77(self):
        input = """
            too: function string (a: auto, b: integer) {}
            main: function void() {
                arr: array [3,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, {{9,10}, {11,12}}}; 
                arr2: auto = arr[2];
                arr3: array [2,2] of integer = arr2;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 577))

    def test_78(self):
        input = """
            too: function string (a: auto, b: integer) {}
            main: function void() {
                arr: array [3,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, {{9,10}, {11,12}}}; 
                arr2: auto = arr[2];
                arr2 = arr[1,2];
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(arr2), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 578))

    def test_79(self):
        input = """
            too: function string (a: auto, b: integer) {}
            main: function void() {
                arr: array [3,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, {{9,10}, {11,12}}}; 
                t: float = arr[2,1,1];
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 579))

    def test_80(self):
        input = """
            too: function string (a: auto, b: integer) {}
            main: function void() {
                arr: array [3,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, {{9,10}, {11,12}}}; 
                arr[2,1,1] = 2.3;
            }
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(arr, [IntegerLit(2), IntegerLit(1), IntegerLit(1)]), FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 580))

    def test_81(self):
        input = """
            foo: function auto ()  {
                preventDefault();
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 581))

    def test_82(self):
        input = """
            foo: function auto ()  {
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 582))

    def test_83(self):
        input = """
            foo: function auto () inherit too  {
                a: auto = 2;
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 583))

    def test_84(self):
        input = """
            foo: function auto () inherit too  {
                a: auto = 2;
            } 
            too: function auto () {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 584))

    def test_85(self):
        input = """
            foo: function auto () inherit too  {
                super();
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 585))

    def test_86(self):
        input = """
            foo: function auto () inherit too  {
                super(2,3,4+5);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(4), IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 586))

    def test_87(self):
        input = """
            foo: function auto () inherit too  {
                super(2);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 587))

    def test_88(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                preventDefault();
                b = a + 5;
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 588))

    def test_89(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                t: auto;
            } 
            too: function auto (a: integer, inherit a: integer) {}
            main: function void() {}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 589))

    def test_90(self):
        input = """
            foo: function auto (b: integer) inherit too  {
                super(2, 3);
                
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 590))

    def test_91(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                b = a + 3.4;
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(b), BinExpr(+, Id(a), FloatLit(3.4)))"
        self.assertTrue(TestChecker.test(input, expect, 591))

    def test_92(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                while (true) {
                    a = a + 2;
                }
                break;
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 592))

    def test_93(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                m: float = -too(2,3);
                n: integer = too(2,3);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(n, IntegerType, FuncCall(too, [IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 593))

    def test_94(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                m: float = -too(2,3);
                n: integer = too(2,3);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(n, IntegerType, FuncCall(too, [IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 594))

    def test_95(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                if (true) {
                    if (false) {
                        return "b";
                    } else {
                        return "eojoaf";
                    }
                    return 2;
                } else {
                    return 1.2;
                }
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 595))

    def test_96(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                if (true) {
                    return 2;
                } else {
                    return 1.2;
                }
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 596))

    def test_97(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                if (true) {
                    return 2.5;
                } else {
                    return 1.2;
                }
                return "abc";
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 597))

    def test_98(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                return 2;
                return 2.5;
                return "abc";
                m: string = foo(2);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, StringType, FuncCall(foo, [IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 598))

    def test_99(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                if (true) {
                    return 2.5;
                    return "a1";
                } else {
                    return 1;
                    return "a2";
                }
                return "a3";
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(a3))"
        self.assertTrue(TestChecker.test(input, expect, 599))

    def test_100(self):
        input = """
            foo: function auto (a: integer) inherit too  {
                super(2, 3);
                return "a3";
                if (true) {
                    return 2.5;
                } else {
                    return 1;
                }
                a = foo(2);
            } 
            too: function auto (a: integer, inherit b: integer) {}
            main: function void() {}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 600))

    def test_101(self):
        input = """
            inc : function void (out n : integer, a:float) inherit foo{}
            foo : function auto (inherit m: float, n: integer){}
            main: function void() {}
        """
        expect = "Invalid statement in function: inc"
        self.assertTrue(TestChecker.test(input, expect, 601))

    def test_102(self):
        input = """
            foo: function auto (a: auto, b: auto) {
                s: string = a + b;
            }
            main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(s, StringType, BinExpr(+, Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 602))

    def test_103(self):
        input = """
            foo: function auto (a: auto) inherit goo {}
            goo: function auto () {}
            main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 603))

    def test_104(self):
        input = """
            goo: function void(a: auto, a: auto) inherit foo {}
            main: function void() {}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 604))

    def test_105(self):
        input = """
            foo: function auto (a: auto) inherit goo {
                super(2,3, true);
            }
            goo: function auto (a: integer, inherit b: auto) {}
            main: function void() {}
        """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 605))

    def test_106(self):
        input = """
            foo: function auto () {}
            main: function void() {
                arr: array [3] of integer = {3, foo(), 2};
                t: integer = !foo();
            }
        """
        expect = "Type mismatch in expression: UnExpr(!, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 606))

    def test_107(self):
        input = """
            foo: function auto () {}
            main: function void() {
                arr: array [2,2] of integer = {foo(), {3, 2}};
                arr2: array [2] of integer = foo();
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 607))

    def test_108(self):
        input = """
            a: array [2,2] of integer = {foo(), goo()};
            main: function void() {
                m: string = foo();
            }
            foo: function auto () {}
            goo: function auto () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, StringType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 608))

    def test_109(self):
        input = """
            a: array [3,2,2] of integer = {{{1,2}, {3,4}}, {{5,6}, {7,8}}, foo()};
            main: function void() {
                m: array [2,2] of integer = foo();
            }
            foo: function auto () {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 609))

    def test_110(self):
        input = """
            a: array [3,2,2] of integer = {too(), goo(), foo()};
            main: function void() {
                m: array [2,2] of integer = foo();
                m[1, 1] = 1.4;
            }
            foo: function auto () {}
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(m, [IntegerLit(1), IntegerLit(1)]), FloatLit(1.4))"
        self.assertTrue(TestChecker.test(input, expect, 610))

    def test_111(self):
        input = """
            a: array [3,2,2] of integer = {too(), {{1,2}, goo()}, {{4,3}, {5, foo()}}};
            main: function void() {
                m: array [2,2] of integer = too();
                n: array [2] of integer = goo();
                n[1] = foo();
                m[1] = n;
            }
            foo: function auto () {}
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(m, [IntegerLit(1)]), Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 611))

    def test_112(self):
        input = """
            a: array [3,2,2] of integer = {too(), {{1,2}, goo()}, {{4,3}, {5, foo()}}};
            main: function void() {
                printString(foo());
            }
            foo: function auto () {}
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in statement: CallStmt(printString, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 612))

    def test_113(self):
        input = """
            a: array [3,2,2] of integer = {too(), {{1,2}, goo()}, {{4,3}, {5, foo()}}};
            main: function void() {
                printString(foo());
            }
            foo: function auto () {}
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in statement: CallStmt(printString, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 613))

    def test_114(self):
        input = """
            main: function void() {
                m: integer = readInteger();
                n: auto;
            }
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Invalid Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 614))

    def test_114(self):
        input = """
            main: function void() {
                m: integer = readFloat();
                n: auto;
            }
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, IntegerType, FuncCall(readFloat, []))"
        self.assertTrue(TestChecker.test(input, expect, 614))

    def test_115(self):
        input = """
            main: function void() {
                m: integer = readFloat();
                n: auto;
            }
            goo: function auto () {}
            too: function auto () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(m, IntegerType, FuncCall(readFloat, []))"
        self.assertTrue(TestChecker.test(input, expect, 615))

    def test_116(self):
        input = """
            main: function void() {
                m: integer = goo({too(), 3}, 5);
                i: float = !too();
            }
            goo: function auto (a: array [2] of integer, b: auto) {}
            too: function auto () {}
        """
        expect = "Type mismatch in expression: UnExpr(!, FuncCall(too, []))"
        self.assertTrue(TestChecker.test(input, expect, 616))