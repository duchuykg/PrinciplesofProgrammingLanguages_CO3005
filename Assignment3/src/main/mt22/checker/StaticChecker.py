from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    # flag: Main and params scope
    def __init__(self, name, mtype, flag=0):
        self.name = name
        self.mtype = mtype
        self.flag = flag

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visitProgram(self.ast, [])
        
    # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        o = [[]]
        for decl in ast.decls:
            o = self.visit(decl, o)
        
        for env in o:
            for symbol in env:
                if symbol.name == 'main' and type(symbol.mtype) is VoidType and symbol.flag == 1:
                    return
                
        raise NoEntryPoint()
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        
        if type(ast.typ) is AutoType and ast.init == None:
                raise Invalid(Variable(), ast.name)
            
        o[0] += [Symbol(ast.name, ast.typ, 0)]
        return o
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast, o):
        flag = 0
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Function(), ast.name)
            
        if ast.name == 'main' and type(ast.return_type) is VoidType and len(ast.params) == 0:
            flag = 1
            
        o[0] += [Symbol(ast.name, ast.return_type, flag)]
        
        env = [[]] + o  
        for decl in ast.params:
            env = self.visit(decl, env)
        
        env = self.visit(ast.body, env)
        
        return o
                
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
            
        o[0] += [Symbol(ast.name, ast.typ, 1)]
        return o
    

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)


    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o): 
        env = o    
        for symbol in o[0]:
            if symbol.flag == 0:
                env = [[]] + o
        for body in ast.body:
            self.visit(body, env)


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
        for env in o:
            for symbol in env:             
                if symbol.name == ast.name: 
                    return
            
        raise Undeclared(Function(), ast.name)

        
    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast: BinExpr, o):
       pass

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        pass

    # name: str
    def visitId(self, ast: Id, o):
        for env in o:
            for symbol in env:             
                if symbol.name == ast.name: 
                    return
            
        raise Undeclared(Identifier(), ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        for env in o:
            for symbol in env:
                ### Rang buoc E2
                if symbol.name == ast.name and type(symbol.mtype) == ArrayType:
                    return
                    
        raise TypeMismatchInExpression(ast)         
                    

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
        return ArrayType()

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        for env in o:
            for symbol in env:             
                if symbol.name == ast.name: 
                    return
            
        raise Undeclared(Function(), ast.name)



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