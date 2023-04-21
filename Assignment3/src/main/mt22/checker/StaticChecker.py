from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    # flag: isParam
    # parent: name function inherit || inherit param
    def __init__(self, name, mtype, flag = 0, parent = None, params = None):
        self.name = name
        self.mtype = mtype
        self.flag = flag
        self.parent = parent
        self.params = params

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
        o[0] += [Symbol(ast.name, ast.typ, 0, None, None)]
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast: FuncDecl, o):
        o[0] += [Symbol(ast.name, ast.return_type, 2, ast.inherit, ast.params)]
        
        # env = [[]] + o  
        # for decl in ast.params:
        #     env = self.visit(decl, env)
                        
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    # def visitParamDecl(self, ast, o):
    #     o[0] += [Symbol(ast.name, ast.typ, 0, 1, ast.inherit)]
class StaticChecker(Visitor):
    def __init__(self, ast, flag = 0):
        self.ast = ast
        self.flag = flag
    
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
                if symbol.name == 'main' and type(symbol.mtype) is VoidType and len(symbol.params) == 0:
                    return
                
        raise NoEntryPoint()
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        
        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)

        o[0][0] += [Symbol(ast.name, ast.typ, 0, None, None)] 
        if ast.init is not None:
            rhs = self.visit(ast.init, o)           
            lhs = ast.typ
            if type(lhs) is AutoType and type (rhs) is AutoType:
                raise TypeMismatchInVarDecl(ast)
            if type(lhs) is AutoType:
                lhs = rhs
            # Duyet qua toan bo
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.init.name, lhs)
                rhs = Utils.infer(o[1], ast.init.name, lhs)
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                return o
            if type(rhs) is not type(lhs):
                raise TypeMismatchInVarDecl(ast)
        
        return o
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast: FuncDecl, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Function(), ast.name)
            
        o[0][0] += [Symbol(ast.name, ast.return_type, 2, ast.inherit, ast.params)]
        
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
            
        o[0][0] += [Symbol(ast.name, ast.typ, 1, ast.inherit, None)]
        return o
    

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        # if type(lhs) is AutoType and type(rhs) is AutoType:
        #     raise TypeMismatchInStatement(ast)
        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType:
            lhs = Utils.infer(o[0], ast.lhs.name, rhs)
        if type(rhs) is AutoType:
            rhs = Utils.infer(o[0], ast.rhs.name, lhs)
        if type(lhs) is type(rhs):
            return type(lhs)
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return type(lhs)
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
        cond = self.visit(ast.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, o)
        if ast.fstmt is not None:
            self.visit(ast.fstmt, o)


    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        self.flag += 1
        init = self.visit(ast.init, o)
        if init is not IntegerType: 
            raise TypeMismatchInStatement(ast)
        upd = self.visit(ast.upd, o)
        if type(upd) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        self.flag -= 1

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        self.flag += 1
        cond = self.visit(ast.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.flag -= 1
    
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        self.flag += 1
        cond = self.visit(ast.cond, o)
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.flag -= 1
    def visitBreakStmt(self, ast, o):
        if self.flag == 0:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        if self.flag == 0:
            raise MustInLoop(ast)

    # expr: Expr or None = None
    def visitReturnStmt(self, ast, o):
        pass


    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, o):
        flag = False
        params = None
        typ = None
        for env in o[1]:
            for symbol in env:
                if symbol.name == ast.name and symbol.flag == 2:
                    flag = True
                    params = symbol.params
                    typ = symbol.mtype
                    break
        if not flag: raise Undeclared(Function(), ast.name)
        if len(ast.args) != len(symbol.params):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            lhs = self.visit(ast.args[i], o)
            rhs = params[i].typ
            if type(lhs) is VoidType or type(rhs) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                raise TypeMismatchInStatement(ast)
            if type(lhs) is AutoType:
                lhs = Utils.infer(o[0], ast.args[i].name, rhs)
            if type(rhs) is AutoType:
                rhs = lhs      
            if type(lhs) is type(rhs):
                continue
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                continue
            
            raise TypeMismatchInStatement(ast)
        if type(typ) is not AutoType and type(typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        
        
    # op: str, left: Expr, right: Expr ([[]] ([[]])) 
    def visitBinExpr(self, ast: BinExpr, o):
        e1t = self.visit(ast.left, o)
        e2t = self.visit(ast.right, o)
        
        if ast.op in ['+', '-', '*', '/']:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
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
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType())
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType())
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||"]:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is BooleanType:
                e1t = Utils.infer(o[0], ast.left.name, BooleanType())
            if type(e2t) is AutoType and type(e1t) is BooleanType:
                e2t = Utils.infer(o[0], ast.right.name, BooleanType())
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["::"]:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is StringType:
                e1t = Utils.infer(o[0], ast.left.name, StringType())
            if type(e2t) is AutoType and type(e1t) is StringType:
                e2t = Utils.infer(o[0], ast.right.name, StringType())
            if type(e1t) is StringType and type(e2t) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==', '!=']:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType())
            if type(e1t) is AutoType and type(e2t) is BooleanType :
                e1t = Utils.infer(o[0], ast.left.name, BooleanType())
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType())
            if type(e2t) is AutoType and type(e1t) is BooleanType:
                e2t =  Utils.infer(o[0], ast.right.name, BooleanType())
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return BooleanType()
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType()
            if type(e1t) is IntegerType and type(e2t) is BooleanType:
                return BooleanType()
            if type(e1t) is BooleanType and type(e2t) is IntegerType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['<', '>', '<=', '>=']:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType())
            if type(e1t) is AutoType and type(e2t) is FloatType :
                e1t = Utils.infer(o[0], ast.left.name, FloatType())
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType())
            if type(e2t) is AutoType and type(e1t) is FloatType:
                e2t =  Utils.infer(o[0], ast.right.name, FloatType())
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return BooleanType()
            if type(e1t) is FloatType and type(e2t) is FloatType:
                return BooleanType()
            if type(e1t) is IntegerType and type(e2t) is FloatType:
                return BooleanType()
            if type(e1t) is FloatType and type(e2t) is IntegerType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
    
    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        e1t = self.visit(ast.val, o)
        if ast.op in ['-']:
            if type(e1t) is AutoType:
                e1t = Utils.infer(o[0], ast.value.name, FloatType())
            if type(e1t) is FloatType:
                return FloatType()
            if type(e1t) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['!']:
            if type(e1t) is AutoType:
                e1t = Utils.infer(o[0], ast.value.name, BooleanType())
            if type(e1t) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

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
                if symbol.name == ast.name and type(symbol.mtype) == ArrayType:
                     ### Rang buoc E2
                    for expr in ast.cell:
                        typ = self.visit(expr, o)
                        if type(typ) is not IntegerType:
                            raise TypeMismatchInExpression(ast)         
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
        typ = None
        if len(ast.explist) > 0:
            typ = self.visit(ast.explist[0], o)
        for expr in ast.explist:
            rhs = self.visit(expr, o)
            if type(typ) is not type(rhs):
                raise IllegalArrayLiteral(ast)
                # { {1 , 2}, { 1,1.5} } ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1),, FloatLit(1.5)])])

        return ArrayType(ast.explist, typ)

    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        flag = False
        params = None
        func_type = None
        for env in o[1]:
            for symbol in env:
                if symbol.name == ast.name and symbol.flag == 2:
                    flag = True
                    params = symbol.params
                    func_type = symbol.mtype
                    break
        if not flag: raise Undeclared(Function(), ast.name)
        if len(ast.args) != len(symbol.params):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.args)):
            lhs = self.visit(ast.args[i], o)
            rhs = params[i].typ
            if type(lhs) is VoidType or type(rhs) is VoidType:
                raise TypeMismatchInExpression(ast)
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                raise TypeMismatchInExpression(ast)
            if type(lhs) is AutoType:
                lhs = Utils.infer(o[0], ast.args[i].name, rhs)
            if type(rhs) is AutoType:
                rhs = lhs      
            if type(lhs) is type(rhs):
                continue
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                continue
            raise TypeMismatchInExpression(ast)
        
        return func_type

    def visitIntegerType(self, ast, o):
        return IntegerType()


    def visitFloatType(self, ast, o):
        return FloatType()


    def visitBooleanType(self, ast, o):
        return BooleanType()


    def visitStringType(self, ast, o):
        return StringType()

    # dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast, o):
        return ArrayType()


    def visitAutoType(self, ast, o):
        return AutoType()


    def visitVoidType(self, ast, o):
        return VoidType()