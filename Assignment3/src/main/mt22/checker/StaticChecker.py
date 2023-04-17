from Visitor import Visitor


class StaticChecker(Visitor):
    
    def visitProgram(self, ctx: Program, o):
        pass
    
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ctx: BinExpr, o):
       pass

    # op: str, val: Expr
    def visitUnExpr(self, ctx: UnExpr, o):
        pass

    # name: str
    def visitId(self, ctx: Id, o):
        pass

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ctx, o):
        pass

    # val: int
    def visitIntegerLit(Expr):
        return (None, None, IntegerType())


    def visitFloatLit(Expr):
        return (None, None, FloatType())


    def visitStringLit(self, ctx, o):
        return (None, None, StringType())


    class BooleanLit(Expr):
        def __init__(self, val: bool):
            self.val = val

        def __str__(self):
            return "BooleanLit({})".format("True" if self.val else "False")


    class ArrayLit(Expr):
        def __init__(self, explist: List[Expr]):
            self.explist = explist

        def __str__(self):
            return "ArrayLit([{}])".format(", ".join([str(exp) for exp in self.explist]))


    class FuncCall(Expr):
        def __init__(self, name: str, args: List[Expr]):
            self.name = name
            self.args = args

        def __str__(self):
            return "FuncCall({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.args]))


    # Statements

    class AssignStmt(Stmt):
        def __init__(self, lhs: LHS, rhs: Expr):
            self.lhs = lhs
            self.rhs = rhs

        def __str__(self):
            return "AssignStmt({}, {})".format(str(self.lhs), self.rhs)


    class BlockStmt(Stmt):
        def __init__(self, body: List[Stmt or VarDecl]):
            self.body = body

        def __str__(self):
            return "BlockStmt([{}])".format(", ".join([str(body) for body in self.body]))


    class IfStmt(Stmt):
        def __init__(self, cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None):
            self.cond = cond
            self.tstmt = tstmt
            self.fstmt = fstmt

        def __str__(self):
            return "IfStmt({}, {}{})".format(str(self.cond), str(self.tstmt), ", " + str(self.fstmt) if self.fstmt else "")


    class ForStmt(Stmt):
        def __init__(self, init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt):
            self.init = init
            self.cond = cond
            self.upd = upd
            self.stmt = stmt

        def __str__(self):
            return "ForStmt({}, {}, {}, {})".format(str(self.init), str(self.cond), str(self.upd), str(self.stmt))


    class WhileStmt(Stmt):
        def __init__(self, cond: Expr, stmt: Stmt):
            self.cond = cond
            self.stmt = stmt

        def __str__(self):
            return "WhileStmt({}, {})".format(str(self.cond), str(self.stmt))


    class DoWhileStmt(Stmt):
        def __init__(self, cond: Expr, stmt: BlockStmt):
            self.cond = cond
            self.stmt = stmt

        def __str__(self):
            return "DoWhileStmt({}, {})".format(str(self.cond), str(self.stmt))


    class BreakStmt(Stmt):
        def __str__(self):
            return "BreakStmt()"


    class ContinueStmt(Stmt):
        def __str__(self):
            return "ContinueStmt()"


    class ReturnStmt(Stmt):
        def __init__(self, expr: Expr or None = None):
            self.expr = expr

        def __str__(self):
            return "ReturnStmt({})".format(str(self.expr) if self.expr else "")


    class CallStmt(Stmt):
        def __init__(self, name: str, args: List[Expr]):
            self.name = name
            self.args = args

        def __str__(self):
            return "CallStmt({}, {})".format(self.name, ", ".join([str(expr) for expr in self.args]))


    # Declarations


    class VarDecl(Decl):
        def __init__(self, name: str, typ: Type, init: Expr or None = None):
            self.name = name
            self.typ = typ
            self.init = init

        def __str__(self):
            return "VarDecl({}, {}{})".format(self.name, str(self.typ), ", " + str(self.init) if self.init else "")


    class ParamDecl(Decl):
        def __init__(self, name: str, typ: Type, out: bool = False, inherit: bool = False):
            self.name = name
            self.typ = typ
            self.out = out
            self.inherit = inherit

        def __str__(self):
            return "{}{}Param({}, {})".format("Inherit" if self.inherit else "", "Out" if self.out else "", self.name, str(self.typ))


    class FuncDecl(Decl):
        def __init__(self, name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt):
            self.name = name
            self.return_type = return_type
            self.params = params
            self.inherit = inherit
            self.body = body

        def __str__(self):
            return "FuncDecl({}, {}, [{}], {}, {})".format(self.name, str(self.return_type), ", ".join([str(param) for param in self.params]), self.inherit if self.inherit else "None", str(self.body))

    # Program

    def visitIntegerType(self):
        return IntegerType()


    def visitFloatType(self):
        return FloatType()


    def visitBooleanType(self):
        return BooleanType()


    def visitStringType(self):
        return StringType()

    # List[int], typ
    def visitArrayType(self, ctx, o):
        return ctx


    def visitAutoType(self, ctx, o):
        return ctx


    def visitVoidType(self, ctx, o):
        return ctx