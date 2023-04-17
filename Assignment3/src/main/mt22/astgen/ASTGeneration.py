from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from functools import *
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl+ EOF ; 12
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(list(reduce(lambda prev, curr: prev + self.visit(curr), ctx.decl(), [])))


    # decl: vardecl | funcdecl ; 15
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())


    # vardecl: varlist SEMI; 19 
    # varlist: ID var1 expr | idlist COLON typ; 20
    # var1: COMMA ID var1 expr COMMA | COLON typ ASSIGN; 21
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        ctx = ctx.varlist()
        
        if ctx.idlist():
            name = self.visit(ctx.idlist())
            typ = self.visit(ctx.typ())
            return list(map(lambda x: VarDecl(x, typ, None), name))
   
        name = [ctx.ID().getText()]
        
        expr = [self.visit(ctx.expr())]
        
        ctx = ctx.var1()
        while ctx.typ() is None:
            name += [ctx.ID().getText()]
            expr += [self.visit(ctx.expr())]
            ctx = ctx.var1()
        
        typ = self.visit(ctx.typ())
        expr = expr[::-1]
        
        return list(map(lambda x, y: VarDecl(x, typ, y), name, expr))

    
    # idlist: ID COMMA idlist | ID; 22
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.idlist(): 
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]


    # param: ap_inherit ap_out ID COLON typ; 25
    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.typ())
        out = self.visit(ctx.ap_out())
        inherit = self.visit(ctx.ap_inherit())
        return ParamDecl(name, typ, out, inherit)


    # ap_inherit: INHERIT | ; 26
    def visitAp_inherit(self, ctx:MT22Parser.Ap_inheritContext):
        if ctx.getChildCount() == 0:
            return False
        return True


    # ap_out: OUT | ; 27
    def visitAp_out(self, ctx:MT22Parser.Ap_outContext):
        if ctx.getChildCount() == 0:
            return False
        return True


    # funcdecl: ID COLON FUNCTION type_func LB paramlist RB inher_func blockstmt; 30
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        name = ctx.ID().getText()
        return_type = self.visit(ctx.type_func())
        params = self.visit(ctx.paramlist())
        inherit = self.visit(ctx.inher_func())
        body = self.visit(ctx.blockstmt())
        return [FuncDecl(name, return_type, params, inherit, body)]


    # paramlist: paramprime |  ;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())


    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())


    # inher_func: INHERIT ID | ;
    def visitInher_func(self, ctx:MT22Parser.Inher_funcContext):
        if ctx.getChildCount() == 2: 
            return ctx.ID().getText()
        return None


    # stmt: ... 36
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))


    # assignstmt: scalar_var ASSIGN expr SEMI; 48
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        lhs = self.visit(ctx.scalar_var())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)


    # scalar_var: ID | index_operator; 49
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.index_operator())


    # ifstmt: IF LB expr RB stmt else_part; 52
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt())
        fstmt = self.visit(ctx.else_part())
        return IfStmt(cond, tstmt, fstmt)


    # else_part: ELSE stmt | ; 53
    def visitElse_part(self, ctx:MT22Parser.Else_partContext):
        if ctx.getChildCount() == 0: 
            return None
        return self.visit(ctx.stmt())


    # forstmt: FOR LB scalar_var ASSIGN INTLIT COMMA condition_expr COMMA update_expr RB stmt; 56
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        lhs = self.visit(ctx.scalar_var())
        rhs = IntegerLit(int(ctx.INTLIT().getText()))
        init = AssignStmt(lhs, rhs)
        cond = self.visit(ctx.condition_expr())
        upd = self.visit(ctx.update_expr())
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)


    # condition_expr: expr; 57
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visit(ctx.expr())


    # update_expr: expr; 58
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visit(ctx.expr())


    # whilestmt: WHILE LB expr RB stmt; 61
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)


    # dowhilestmt: DO blockstmt WHILE LB expr RB SEMI; 64
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        blockstmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, blockstmt)


    # breakstmt: BREAK SEMI; 67
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()


    # continuestmt: CONTINUE SEMI; 70
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()


    # returnstmt: RETURN list1 SEMI; 73
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        expr = self.visit(ctx.list1())
        return ReturnStmt(expr)


    # list1: expr | ; 74
    def visitList1(self, ctx:MT22Parser.List1Context):
        if ctx.getChildCount() == 0: 
            return None
        return self.visit(ctx.expr())


    # callstmt: special_func SEMI | func_call SEMI; 77
    # func_call: ID LB list_arg RB; 123
    # super_func: SUPER LB expr_primelist RB; 147
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        if ctx.special_func():
            ctx = ctx.special_func()
            ctx = ctx.getChild(0)
            name = ctx.getChild(0).getText()
            args = []
            if name == "printInteger" or name == "printBoolean" or name == "printString" or name == "writeFloat":
                args += [self.visit(ctx.expr())]
            elif name == "super":
                args += self.visit(ctx.expr_primelist())
            return CallStmt(name, args)
        ctx = ctx.func_call()
        name = ctx.ID().getText()
        args = self.visit(ctx.list_arg())
        return CallStmt(name, args)


    # blockstmt: LP blocklist RP; 80
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.blocklist()))


    # blocklist: stmt blocklist | vardecl blocklist | ; 81
    def visitBlocklist(self, ctx:MT22Parser.BlocklistContext):
        if ctx.getChildCount() == 0: 
            return []
        elif ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.blocklist())
        return self.visit(ctx.vardecl()) + self.visit(ctx.blocklist())            


    # typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | type_array; 84
    def visitTyp(self, ctx:MT22Parser.TypContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        return self.visit(ctx.type_array())


    # type_func: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID | type_array; 85
    def visitType_func(self, ctx:MT22Parser.Type_funcContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        return self.visit(ctx.type_array())


    # type_element: BOOLEAN | INTEGER | FLOAT | STRING; 86
    def visitType_element(self, ctx:MT22Parser.Type_elementContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        return StringType()


    # type_array: ARRAY LS integerlist RS OF type_element; 89
    def visitType_array(self, ctx:MT22Parser.Type_arrayContext):
        dimensions = self.visit(ctx.integerlist())
        typ = self.visit(ctx.type_element())
        return ArrayType(dimensions, typ)


    # integerlist: INTLIT COMMA integerlist | INTLIT; 90
    def visitIntegerlist(self, ctx:MT22Parser.IntegerlistContext):
        if ctx.getChildCount() == 1: 
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.integerlist())


    # literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit; 93
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        return self.visit(ctx.arraylit())

    # arraylit: LP expr_primelist RP; 114
    # expr_primelist: expr_list | ; 115
    # expr_list: expr COMMA expr_list| expr; 116
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        explist = self.visit(ctx.expr_primelist())
        return ArrayLit(explist)

    # expr_primelist: expr_list | ; 115
    def visitExpr_primelist(self, ctx:MT22Parser.Expr_primelistContext):
        if ctx.getChildCount() == 0: 
            return []
        return self.visit(ctx.expr_list())


    # expr_list: expr COMMA expr_list| expr; 116
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        if ctx.getChildCount() == 1: 
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())

    # index_operator: ID LS expr_list RS; 119  a[1,2]
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        name = ctx.ID().getText()
        cell = self.visit(ctx.expr_list())
        return ArrayCell(name, cell)


    # func_call: ID LB list_arg RB; 123
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.list_arg())
        return FuncCall(name, args)


    # list_arg: list_argprime | ; 124
    def visitList_arg(self, ctx:MT22Parser.List_argContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_argprime())

    # list_argprime: expr COMMA list_argprime | expr; 125
    def visitList_argprime(self, ctx:MT22Parser.List_argprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.list_argprime())


    # special_func: ... 128
    def visitSpecial_func(self, ctx:MT22Parser.Special_funcContext):
        return self.visit(ctx.getChild(0))


    # readi: READI LB RB;
    def visitReadi(self, ctx:MT22Parser.ReadiContext):
        name = ctx.READI().getText()
        args = []
        return FuncCall(name, args)

    # readf: READF LB RB;
    def visitReadf(self, ctx:MT22Parser.ReadfContext):
        name = ctx.READF().getText()
        args = []
        return FuncCall(name, args)


    # readb: READB LB RB;
    def visitReadb(self, ctx:MT22Parser.ReadbContext):
        name = ctx.READB().getText()
        args = []
        return FuncCall(name, args)


    # reads: READS LB RB;
    def visitReads(self, ctx:MT22Parser.ReadsContext):
        name = ctx.READS().getText()
        args = []
        return FuncCall(name, args)


    # printi: PRINTI LB expr RB; 143
    def visitPrinti(self, ctx:MT22Parser.PrintiContext):
        name = ctx.PRINTI().getText()
        args = [self.visit(ctx.expr())]
        return FuncCall(name, args)


    # printb: PRINTB LB expr RB; 144
    def visitPrintb(self, ctx:MT22Parser.PrintbContext):
        name = ctx.PRINTB().getText()
        args = [self.visit(ctx.expr())]
        return FuncCall(name, args)


    # prints: PRINTS LB expr RB; 145
    def visitPrints(self, ctx:MT22Parser.PrintsContext):
        name = ctx.PRINTS().getText()
        args = [self.visit(ctx.expr())]
        return FuncCall(name, args)


    # writef: WRITEF LB expr RB; 146
    def visitWritef(self, ctx:MT22Parser.WritefContext):
        name = ctx.WRITEF().getText()
        args = [self.visit(ctx.expr())]
        return FuncCall(name, args)


    # super_func: SUPER LB expr_primelist RB; 147
    def visitSuper_func(self, ctx:MT22Parser.Super_funcContext):
        name = ctx.SUPER().getText()
        args = self.visit(ctx.expr_primelist())
        return FuncCall(name, args)


    # preventdefault: PREVENTDEFAULT LB RB;
    def visitPreventdefault(self, ctx:MT22Parser.PreventdefaultContext):
        name = ctx.PREVENTDEFAULT().getText()
        args = []
        return FuncCall(name, args)


    # operand: literal | ID | func_call | special_func;
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.special_func():
            return self.visit(ctx.special_func())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.literal())

    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinExpr(op, left, right)


    # expr1: expr2 (EQUAL | NOT_EQUAL | SMALLER | GREATER | SMALLER_EQUAL | GREATER_EQUAL) expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinExpr(op, left, right)


    # expr2: expr2 (AND | OR) expr3 | expr3; 155
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinExpr(op, left, right)


    # expr3: expr3 (ADD | SUB) expr4 | expr4; 156
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinExpr(op, left, right)


    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5; 157
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinExpr(op, left, right)

    # expr5: NOT expr5 | expr6; 158
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        val = self.visit(ctx.expr5())
        return UnExpr(op, val)


    # expr6: SUB expr6 | expr7; 159
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        op = ctx.SUB().getText()
        val = self.visit(ctx.expr6())
        return UnExpr(op, val)

    # expr7: index_operator | expr8; 160
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.expr8():
            return self.visit(ctx.expr8())
        return self.visit(ctx.index_operator())

    # expr8: operand | LB expr RB; 161
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        return self.visit(ctx.expr())