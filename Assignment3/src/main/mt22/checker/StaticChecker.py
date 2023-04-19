from Visitor import Visitor

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_env = [[]]
        
    # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        for decl in ast.decls:
            o = self.visit(decl, o)
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
                
        o[0] += [Symbol(ast.name, ast.typ, ast.init)]
        return o
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Function(), ast.name)

        o[0] += [Symbol(ast.name, ast.typ, None)]
        
        env = [[]] + o
    
        for decl in ast.params:
            env = self.visit(decl, env)
        for decl in ast.body:
            env = self.visit(decl, env)
            
        return o
    
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
            
        o[0] += [Symbol(ast.name, ast.typ, None)]
        return o
    

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, o):
        pass


    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o):
        pass


    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, o):
        pass


    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        pass


    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        pass

    
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        pass


    def visitBreakStmt(self, ast, o):
        pass


    def visitContinueStmt(self, ast, o):
        pass


    # expr: Expr or None = None
    def visitReturnStmt(self, ast, o):
        pass


    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, o):
        pass

        
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast: BinExpr, o):
       pass

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        pass

    # name: str
    def visitId(self, ast: Id, o):
        pass

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        pass

    # val: int
    def visitIntegerLit(Expr):
        return IntegerType()


    def visitFloatLit(Expr):
        return FloatType()


    def visitStringLit(self, ast, o):
        return StringType()


    def visitBooleanLit(self, ast, o):
        return BooleanType()

    # explist: List[Expr]
    def visitArrayLit(self, ast, o):
        pass

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
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
    def visitArrayType(self, ast, o):
        return ast


    def visitAutoType(self, ast, o):
        return ast


    def visitVoidType(self, ast, o):
        return ast