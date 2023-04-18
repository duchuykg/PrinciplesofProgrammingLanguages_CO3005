from Visitor import Visitor


class StaticChecker(Visitor):
    
    def visitProgram(self, ctx: Program, o):
        pass


    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ctx, o):
       pass


    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ctx, o):
        pass



    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ctx, o):
        pass



    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx, o):
        pass


    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ctx, o):
        pass


    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ctx, o):
        pass


    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ctx, o):
        pass


    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ctx, o):
        pass

    
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ctx, o):
        pass


    def visitBreakStmt(self, ctx, o):
        pass


    def visitContinueStmt(self, ctx, o):
        pass


    # expr: Expr or None = None
    def visitReturnStmt(self, ctx, o):
        pass


    # name: str, args: List[Expr]
    def visitCallStmt(self, ctx, o):
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


    def visitBooleanLit(self, ctx, o):
        return (None, None, BooleanType())

    # explist: List[Expr]
    def visitArrayLit(self, ctx, o):
        pass

    # name: str, args: List[Expr]
    def visitFuncCall(self, ctx, o):
        pass



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