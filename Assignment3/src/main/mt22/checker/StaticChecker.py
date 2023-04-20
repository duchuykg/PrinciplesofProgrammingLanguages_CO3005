from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    # len: len(params)
    # flag: isParam
    # parent: name function inherit || inherit param
    def __init__(self, name, mtype, len=0, flag=0, parent=None):
        self.name = name
        self.mtype = mtype
        self.len = len
        self.flag = flag
        self.parent = parent

class Utils:
    def infer(o, name, typ):
        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.mtype = typ
                    return typ
class GetEnv(Visitor):
    # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        o = [[]]
        for decl in ast.decls:
            self.visit(decl, o)
        
        return o
        
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        o[0] += [Symbol(ast.name, ast.typ, 0, 0, None)]
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast: FuncDecl, o):
        o[0] += [Symbol(ast.name, ast.return_type, len(ast.params), 0, ast.inherit)]
        
        # env = [[]] + o  
        # for decl in ast.params:
        #     env = self.visit(decl, env)
                        
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    # def visitParamDecl(self, ast, o):
    #     o[0] += [Symbol(ast.name, ast.typ, 0, 1, ast.inherit)]
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visitProgram(self.ast, [])
        
    # decls: List[Decl]
    # o = (new, local) 
    def visitProgram(self, ast: Program, o):
        o = [[]]
        env = GetEnv().visit(ast, o)
        new = [[]]
        for decl in ast.decls:
            self.visit(decl, (new, env))
        
        for arr in env:
            for symbol in arr:
                if symbol.name == 'main' and type(symbol.mtype) is VoidType and symbol.len == 0:
                    return
                
        raise NoEntryPoint()
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        
        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)
        
        o[0][0] += [Symbol(ast.name, ast.typ, 0, 0, None)]
        return o
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast: FuncDecl, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Function(), ast.name)
            
        o[0][0] += [Symbol(ast.name, ast.return_type, len(ast.params), 0, ast.inherit)]
        
        env = [[]] + o[0]
        curr = (env, o[1])
        for decl in ast.params:
            curr = self.visit(decl, curr)
        
        curr = self.visit(ast.body, curr)
        
        return o
                
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
            
        o[0][0] += [Symbol(ast.name, ast.typ, 0, 1, ast.inherit)]
        return o
    

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, o):
        print(ast.lhs)
        lhs = self.visit(ast.lhs, o)
        print(lhs)
        rhs = self.visit(ast.rhs, o)
        print(rhs)
        if type(lhs) is AutoType and type(rhs) is AutoType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType:
            lhs = Utils.infer(o, ast.lhs.name, rhs)
        if type(rhs) is AutoType:
            rhs = Utils.infer(o, ast.lhs.name, lhs)            
        if type(lhs) is type(rhs):
            return
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return
        raise TypeMismatchInStatement(ast)


    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o): 
        env = o[0]
        for symbol in o[0][0]:
            if symbol.flag != 1:
                env = [[]] + o[0]   
        
        for body in ast.body:
            self.visit(body, (env, o[1]))


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
        for env in o[1]:
            for symbol in env:             
                if symbol.name == ast.name: 
                    return
            
        raise Undeclared(Function(), ast.name)

        
    # op: str, left: Expr, right: Expr ([[]] ([[]])) 
    def visitBinExpr(self, ast: BinExpr, o):
        e1t = self.visit(ast.left, o)
        e2t = self.visit(ast.right, o)
        
        if ast.op in ['+', '-', '*', '/']:
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType())
            if type(e1t) is AutoType and type(e2t) is FloatType :
                e1t = Utils.infer(o[0], ast.left.name, FloatType())
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType())
            if type(e2t) is AutoType and type(e1t) is FloatType:
                e2t =  Utils.infer(o[0], ast.right.name, FloatType())
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType()
            if type(e1t) is FloatType and type(e2t) is FloatType:
                return FloatType()
            if type(e1t) is IntegerType and type(e2t) is FloatType:
                return FloatType()
            if type(e1t) is FloatType and type(e2t) is IntegerType:
                return FloatType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ['%']:
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType())
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType())
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||", "!"]:
            if type(e1t) is AutoType:
                e1t = Utils.infer(o[0], ast.left.name, BooleanType())
            if type(e2t) is AutoType:
                e2t = Utils.infer(o[0], ast.right.name, BooleanType())
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
            
    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        pass

    # name: str
    def visitId(self, ast: Id, o):
        for env in o[0]:
            for symbol in env:             
                if symbol.name == ast.name: 
                    return symbol.mtype
            
        raise Undeclared(Identifier(), ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        for env in o[0]:
            for symbol in env:
                ### Rang buoc E2
                if symbol.name == ast.name and type(symbol.mtype) == ArrayType:
                    return
                    
        raise TypeMismatchInExpression(ast)         
                    

    # val: int
    def visitIntegerLit(self, ast, o):
        return IntegerType()


    def visitFloatLit(self, ast, o):
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
        for env in o[1]:
            for symbol in env:             
                if symbol.name == ast.name:
                    if type(symbol.mtype) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    if len(ast.args) != symbol.len:
                        raise TypeMismatchInExpression(ast)
                    return
        
        raise Undeclared(Function(), ast.name)



    def visitIntegerType(self, ast, o):
        return IntegerType()


    def visitFloatType(self, ast, o):
        return FloatType()


    def visitBooleanType(self, ast, o):
        return BooleanType()


    def visitStringType(self, ast, o):
        return StringType()

    # List[int], typ
    def visitArrayType(self, ast, o):
        return ArrayType()


    def visitAutoType(self, ast, o):
        return AutoType()


    def visitVoidType(self, ast, o):
        return VoidType()