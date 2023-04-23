# 2011286
from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC

class Symbol:
    def __init__(self, name, mtype, flag = 0, parent = None, params = None):
        self.name = name
        self.mtype = mtype
        self.flag = flag
        self.parent = parent
        self.params = params

class Utils:
    def infer(o, name, typ, o1):
        flag = 0
        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.mtype = typ
                    flag = 1
                    break
        if flag == 1:
            for symbol_list in o1:
                for symbol in symbol_list:
                    if symbol.name == name:
                        symbol.mtype = typ
                        break
            return typ    

class GetEnv(Visitor):
    # decls: List[Decl]
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])
    def visitProgram(self, ast: Program, o):
        o = [[]]
        o[0] += [Symbol("readInteger", IntegerType(), 2, None, None)]
        o[0] += [Symbol("readFloat", FloatType(), 2, None, None)]
        o[0] += [Symbol("readBoolean", BooleanType(), 2, None, None)]
        o[0] += [Symbol("readString", StringType(), 2, None, None)]
        o[0] += [Symbol("printInteger", VoidType(), 2, None, None)]
        o[0] += [Symbol("writeFloat", VoidType(), 2, None, None)]
        o[0] += [Symbol("printBoolean", VoidType(), 2, None, None)]
        o[0] += [Symbol("printString", VoidType(), 2, None, None)]
        for decl in ast.decls:
            self.visit(decl, o)
        return o
        
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        o[0] += [Symbol(ast.name, ast.typ, 0, None, None)]
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: List[Stmt or VarDecl]
    def visitFuncDecl(self, ast: FuncDecl, o):
        o[0] += [Symbol(ast.name, ast.return_type, 2, ast.inherit, ast.params)]
        
class StaticChecker(Visitor):
    def __init__(self, ast, flag = 0, flag1 = 0, flag2 = 0, flag3 = 0, inp = 0):
        self.ast = ast
        # Break, continue
        self.flag = flag
        # Invalid param
        self.flag1 = flag1
        # If
        self.flag2 = flag2
        # Return
        self.flag3 = flag3
        # If Return
        self.inp = inp

    def check(self):
        return self.visitProgram(self.ast, [])
        
    # decls: List[Decl]
    def visitProgram(self, ast: Program, o):
        env = GetEnv(self.ast).visit(ast, o)
        new = [[]]
        new[0] += [Symbol("readInteger", IntegerType(), 2, None, None)]
        new[0] += [Symbol("readFloat", FloatType(), 2, None, None)]
        new[0] += [Symbol("readBoolean", BooleanType(), 2, None, None)]
        new[0] += [Symbol("readString", StringType(), 2, None, None)]
        new[0] += [Symbol("printInteger", VoidType(), 2, None, None)]
        new[0] += [Symbol("writeFloat", VoidType(), 2, None, None)]
        new[0] += [Symbol("printBoolean", VoidType(), 2, None, None)]
        new[0] += [Symbol("printString", VoidType(), 2, None, None)]
        for decl in ast.decls:
            self.visit(decl, (new, env))
        
        for arr in env:
            for symbol in arr:
                if symbol.name == "main" and type(symbol.mtype) is VoidType and len(symbol.params) == 0:
                    return
                
        raise NoEntryPoint()
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        
        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)
        if ast.init is not None:
            rhs = self.visit(ast.init, o)  
            lhs = ast.typ

            if type(rhs) == ArrayType and type(lhs) == ArrayType:   
                flag = 0
                if (rhs.dimensions != lhs.dimensions):
                    raise TypeMismatchInVarDecl(ast)
                if type(rhs.typ) is ArrayType:
                    flag = 1
                    for i in range(len(rhs.dimensions)):                  
                        rhs = self.visit(rhs.typ, o)
                    if type(rhs) is AutoType:
                        rhs = lhs.typ
                        
                    if type(rhs) is not type(lhs.typ):
                            raise TypeMismatchInVarDecl(ast)    

                    o[0][0] += [Symbol(ast.name, lhs, 0, None, None)] 
                    return o
                    
                if flag == 0:        
                
                    if type(rhs.typ) is AutoType:
                        for a in ast.init.explist:
                            rhs.typ = Utils.infer(o[0], a.name, lhs.typ, o[1])
                            if rhs.typ is None:
                                rhs.typ = Utils.infer(o[1], a.name, lhs.typ, o[1])                                
                    if type(rhs.typ) is not type(lhs.typ):
                        raise TypeMismatchInVarDecl(ast)

            if type(lhs) is AutoType and type (rhs) is AutoType:
                raise TypeMismatchInVarDecl(ast)
            if type(lhs) is AutoType:
                lhs = rhs
                o[0][0] += [Symbol(ast.name, lhs, 0, None, None)] 
                return o
            # Duyet qua toan bo
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.init.name, lhs, o[1])
                if rhs is None:
                    rhs = Utils.infer(o[1], ast.init.name, lhs, o[1])      
            
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                o[0][0] += [Symbol(ast.name, ast.typ, 0, None, None)] 
                return o
                
            if type(rhs) is not type(lhs):
                raise TypeMismatchInVarDecl(ast)

        o[0][0] += [Symbol(ast.name, ast.typ, 0, None, None)] 
        return o
    
    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast: FuncDecl, o):
        ### for symbol in o[1]:
        for symbol in o[0][0]:
            if symbol.name == ast.name:
                raise Redeclared(Function(), ast.name)
        
        o[0][0] += [Symbol(ast.name, ast.return_type, 2, ast.inherit, ast.params)]
        if ast.inherit is not None:
            flag = 0;
            param_parent = None
            for symbol in o[1][0]:
                if ast.inherit == symbol.name:
                    flag = 1;
                    param_parent = symbol.params
                    break
            if not flag: raise Undeclared(Function(), ast.inherit)
                
            env = [[]] + o[0]
            curr = (env, o[1])
            for decl in ast.params:
                curr = self.visit(decl, curr)
                
                
            stmt1 = self.visit(ast.body, [[]])
            if len(param_parent) == 0:
                if stmt1 is None:
                    curr = self.visit(ast.body, curr)
                else:
                    if stmt1[0] == "preventDefault":
                        curr = self.visit(ast.body, curr)
                    if stmt1[0] == "super":
                        if len(stmt1[1]) == 0:
                            curr = self.visit(ast.body, curr)
                        else:
                            raise TypeMismatchInExpression(stmt1[1][0])
            else:   
                if stmt1 is None or len(stmt1) == 0:
                    raise InvalidStatementInFunction(ast.name)
                    # raise InvalidStatementInFunction(ast.inherit)
                if stmt1[0] == "preventDefault":
                    curr = self.visit(ast.body, curr)
                if stmt1[0] == "super":
                    # Goi ham cha voi tham so truyen vao
                    if len(stmt1[1]) < len(param_parent):
                        raise TypeMismatchInExpression([])
                    if len(stmt1[1]) > len(param_parent):
                        raise TypeMismatchInExpression(stmt1[1][len(param_parent)])   
                    if len(stmt1[1]) == len(param_parent):
                        for i in range(len(stmt1[1])):   
                            rhs = self.visit(stmt1[1][i], curr)
                            lhs = param_parent[i].typ 
                            if type(lhs) is AutoType:
                                lhs = Utils.infer(o[0], param_parent[i].name, rhs, o[1])
                            if type(rhs) is AutoType:
                                rhs = Utils.infer(o[0], stmt1[1][i].name, lhs, o[1])
                                
                            if type(lhs) is FloatType and type(rhs) is IntegerType:
                                continue
                            if type(lhs) is not type(rhs):
                                raise TypeMismatchInExpression(stmt1[1][i])
                            
                        c = [[]] + o[0]
                        curr_parent = (c, o[1])
                        for decl in param_parent:
                            curr_parent = self.visit(decl, curr_parent)
                        self.flag1 = 1
                        for i in param_parent:
                            if i.inherit == True:
                                curr = self.visit(i, curr)
                            # else: 
                            #     self.visit(i, curr)         
                        self.flag1 = 0
                        curr = self.visit(ast.body, curr)
        if ast.inherit is None:
            stmt1 = self.visit(ast.body, [[]])
            if stmt1 is None:
                env = [[]] + o[0]
                curr = (env, o[1])
                for decl in ast.params:
                    curr = self.visit(decl, curr)
                curr = self.visit(ast.body, curr)    
                return o
            else:
                if stmt1[0] == "preventDefault":
                    raise InvalidStatementInFunction(ast.name)
                if stmt1[0] == "super":
                    raise InvalidStatementInFunction(ast.name)
                env = [[]] + o[0]
                curr = (env, o[1])
                for decl in ast.params:
                    curr = self.visit(decl, curr)
                curr = self.visit(ast.body, curr)    
                return o
                
    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, o):
        for symbol in o[0][0]:
            if symbol.name == ast.name and self.flag1 == 0:
                raise Redeclared(Parameter(), ast.name)
            if symbol.name == ast.name and self.flag1 == 1:
                raise Invalid(Parameter(), ast.name)
            
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
        # if type(lhs) is ArrayType and type(rhs) is ArrayType:
        #     if lhs.dimensions !=  rhs.dimensions:
        #         raise TypeMismatchInExpression(ast)
        #     if lhs.typ is not rhs.typ:
        #         raise TypeMismatchInExpression(ast)
        #     return lhs.typ
        if type(lhs) is AutoType:
            lhs = Utils.infer(o[0], ast.lhs.name, rhs, o[1])
            if lhs is None:
                lhs = Utils.infer(o[1], ast.lhs.name, rhs, o[1])
        if type(rhs) is AutoType:
            rhs = Utils.infer(o[0], ast.rhs.name, lhs, o[1])
            if rhs is None:
                rhs = Utils.infer(o[1], ast.rhs.name, lhs, o[1])
        if type(lhs) is type(rhs):
            return type(lhs)
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return type(lhs)
        raise TypeMismatchInStatement(ast)

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, o): 
        if len(ast.body) == 0 or o is None:
            return None
        if type(ast.body[0]) is CallStmt and o == [[]]:
            return (ast.body[0].name, ast.body[0].args)
        if o == [[]]:
            return None
    
        env = o[0]
        for symbol in o[0][0]:
            if symbol.flag != 1:
                env = [[]] + o[0]   
        
        for body in ast.body:
            self.visit(body, (env, o[1]))
        
    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, o):
        self.flag2 += 1
        self.inp = 0
        cond = self.visit(ast.cond, o)
        if type(cond) is AutoType:
            cond = Utils.infer(o[0], ast.cond.name, BooleanType(), o[1])
            if cond is None:
                cond = Utils.infer(o[1], ast.cond.name, BooleanType(), o[1])
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, o)
        if ast.fstmt is not None:
            self.inp = 0
            self.visit(ast.fstmt, o)

        self.flag2 -= 1
        self.inp = 0
    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, o):
        self.flag += 1
        init = self.visit(ast.init, o)
        if init is not IntegerType: 
            raise TypeMismatchInStatement(ast)
        upd = self.visit(ast.upd, o)
        if type(upd) is AutoType:
            upd = Utils.infer(o[0], ast.upd.name, BooleanType(), o[1])
            if upd is None:
                upd = Utils.infer(o[1], ast.upd.name, BooleanType(), o[1])
        if type(upd) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, o)
        self.flag -= 1

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, o):
        self.flag += 1
        cond = self.visit(ast.cond, o)
        if type(cond) is AutoType:
            cond = Utils.infer(o[0], ast.cond.name, BooleanType(), o[1])
            if cond is None:
                cond = Utils.infer(o[1], ast.cond.name, BooleanType(), o[1])
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, o)
        self.flag -= 1
    
    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, o):
        self.flag += 1
        cond = self.visit(ast.cond, o)
        if type(cond) is AutoType:
            cond = Utils.infer(o[0], ast.cond.name, BooleanType(), o[1])
            if cond is None:
                cond = Utils.infer(o[1], ast.cond.name, BooleanType(), o[1])
        if type(cond) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, o)
        self.flag -= 1
        
    def visitBreakStmt(self, ast, o):
        if self.flag == 0:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast, o):
        if self.flag == 0:
            raise MustInLoop(ast)

    # expr: Expr or None = None
    def visitReturnStmt(self, ast, o):
        if self.flag3 == 0 and self.flag2 == 0:
            if len(o) > 0:
                if len(o[0]) > 0:
                    if len(o[0][-1]) > 0:
                        symbol = o[0][-1][-1]
                        lhs = symbol.mtype
                        if ast.expr is None:
                            if type(lhs) is VoidType:
                                self.flag3 = 1
                                return
                            raise TypeMismatchInStatement(ast)     
                        rhs = self.visit(ast.expr, o)
                        
                        if type(lhs) is AutoType:
                            self.flag3 = 1
                            lhs = Utils.infer(o[0], symbol.name, rhs, o[1])
                        if type(rhs) is AutoType:
                            self.flag3 = 1
                            rhs = Utils.infer(o[0], symbol.name, lhs, o[1])
                            if rhs is None:
                                rhs = Utils.infer(o[1], symbol.name, lhs, o[1])
                        
                        if type(lhs) is FloatType and type(rhs) is IntegerType:
                            self.flag3 = 1
                            return
                        if type(lhs) is not type(rhs):
                            raise TypeMismatchInStatement(ast)
            self.flag3 = 1
            
        if self.flag2 > 0 and self.inp == 0:
            if len(o) > 0:
                if len(o[0]) > 0:
                    if len(o[0][-1]) > 0:
                        self.inp += 1
                        symbol = o[0][-1][-1]
                        lhs = symbol.mtype
                        if ast.expr is None:
                            if type(lhs) is VoidType:
                                return
                            raise TypeMismatchInStatement(ast)     
                        rhs = self.visit(ast.expr, o)
                        
                        if type(lhs) is AutoType:
                            lhs = Utils.infer(o[0], symbol.name, rhs, o[1])
                            if lhs is None:
                                lhs = Utils.infer(o[1], symbol.name, rhs, o[1])
                        if type(rhs) is AutoType:
                            rhs = Utils.infer(o[0], symbol.name, lhs, o[1])
                            if rhs is None:
                                rhs = Utils.infer(o[1], symbol.name, lhs, o[1])
                            
                        if type(lhs) is FloatType and type(rhs) is IntegerType:
                            return
                        if type(lhs) is not type(rhs):
                            raise TypeMismatchInStatement(ast)
    # name: str, args: List[Expr]
    def visitCallStmt(self, ast, o):
        flag = False
        params = None
        typ = None
        if ast.name == "preventDefault":
            return ast.name
        if ast.name == "super":
            return ast.name
        if ast.name == "printInteger":
            if ast.args is None or len(ast.args) != 1:
                raise TypeMismatchInStatement(ast)
            rhs = self.visit(ast.args[0], o)
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, IntegerType(), o[1])
            if type(rhs) is not IntegerType:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "writeFloat":
            if ast.args is None or len(ast.args) != 1:
                raise TypeMismatchInStatement(ast)
            rhs = self.visit(ast.args[0], o)
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, FloatType(), o[1])
            if type(rhs) is not FloatType or type(rhs) is not IntegerType:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "printBoolean":
            if ast.args is None or len(ast.args) != 1:
                raise TypeMismatchInStatement(ast)
            rhs = self.visit(ast.args[0], o)
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, BooleanType(), o[1])
            if type(rhs) is not BooleanType:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "printString":
            if ast.args is None or len(ast.args) != 1:
                raise TypeMismatchInStatement(ast)
            rhs = self.visit(ast.args[0], o)
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, StringType(), o[1])
            if type(rhs) is not StringType:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "readInteger":
            if ast.args is None or len(ast.args) != 0:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "readFloat":
            if ast.args is None or len(ast.args) != 0:
                raise TypeMismatchInStatement(ast)
            return
        if ast.name == "readBoolean":
            if ast.args is None or len(ast.args) != 0:
                raise TypeMismatchInStatement(ast)
            return 
        if ast.name == "readString":
            if ast.args is None or len(ast.args) != 0:
                raise TypeMismatchInStatement(ast)
            return 
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
            lhs = params[i].typ
            rhs = self.visit(ast.args[i], o)
            
            if type(lhs) is VoidType or type(rhs) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                if lhs.dimensions !=  rhs.dimensions:
                    raise TypeMismatchInExpression(ast)
                if lhs.typ is not rhs.typ:
                    raise TypeMismatchInExpression(ast)
                return 
            if type(lhs) is AutoType:
                lhs = Utils.infer(o[0], params[i].name, rhs, o[1])
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, lhs, o[1])
            if type(lhs) is type(rhs):
                continue
            if type(lhs) is FloatType and type(rhs) is IntegerType:
                continue
        
            raise TypeMismatchInStatement(ast)
        # if type(typ) is not AutoType and type(typ) is not VoidType:
        #     raise TypeMismatchInStatement(ast) 
        return 
    # op: str, left: Expr, right: Expr ([[]] ([[]])) 
    def visitBinExpr(self, ast: BinExpr, o):
        e1t = self.visit(ast.left, o)
        e2t = self.visit(ast.right, o)
        
        if ast.op in ['+', '-', '*', '/']:
            if type(e1t) is AutoType and type(e2t) is AutoType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType(), o[1])
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType(), o[1])
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType(), o[1])
            if type(e1t) is AutoType and type(e2t) is FloatType :
                e1t = Utils.infer(o[0], ast.left.name, FloatType(), o[1])
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType(), o[1])
            if type(e2t) is AutoType and type(e1t) is FloatType:
                e2t =  Utils.infer(o[0], ast.right.name, FloatType(), o[1])
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
                e1t = Utils.infer(o[0], ast.left.name, IntegerType(), o[1])
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType(), o[1])
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||"]:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is BooleanType:
                e1t = Utils.infer(o[0], ast.left.name, BooleanType(), o[1])
            if type(e2t) is AutoType and type(e1t) is BooleanType:
                e2t = Utils.infer(o[0], ast.right.name, BooleanType(), o[1])
            if type(e1t) is BooleanType and type(e2t) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["::"]:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is StringType:
                e1t = Utils.infer(o[0], ast.left.name, StringType(), o[1])
            if type(e2t) is AutoType and type(e1t) is StringType:
                e2t = Utils.infer(o[0], ast.right.name, StringType(), o[1])
            if type(e1t) is StringType and type(e2t) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==', '!=']:
            # if type(e1t) is AutoType and type(e2t) is AutoType:
            #     raise TypeMismatchInExpression(ast)
            if type(e1t) is AutoType and type(e2t) is IntegerType:
                e1t = Utils.infer(o[0], ast.left.name, IntegerType(), o[1])
            if type(e1t) is AutoType and type(e2t) is BooleanType :
                e1t = Utils.infer(o[0], ast.left.name, BooleanType(), o[1])
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType(), o[1])
            if type(e2t) is AutoType and type(e1t) is BooleanType:
                e2t =  Utils.infer(o[0], ast.right.name, BooleanType(), o[1])
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
                e1t = Utils.infer(o[0], ast.left.name, IntegerType(), o[1])
            if type(e1t) is AutoType and type(e2t) is FloatType :
                e1t = Utils.infer(o[0], ast.left.name, FloatType(), o[1])
            if type(e2t) is AutoType and type(e1t) is IntegerType:
                e2t =  Utils.infer(o[0], ast.right.name, IntegerType, o[1]())
            if type(e2t) is AutoType and type(e1t) is FloatType:
                e2t =  Utils.infer(o[0], ast.right.name, FloatType(), o[1])
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
                e1t = Utils.infer(o[0], ast.val.name, FloatType(), o[1])
                if e1t is None:
                    e1t = Utils.infer(o[1], ast.val.name, FloatType(), o[1])
                return e1t
            if type(e1t) is FloatType:
                return FloatType()
            if type(e1t) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        if ast.op in ['!']:
            if type(e1t) is AutoType:
                e1t = Utils.infer(o[0], ast.val.name, BooleanType(), o[1])
                return e1t
            if type(e1t) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)

    # name: str
    def visitId(self, ast: Id, o):
        for env in o[0]:
            for symbol in env:            
                if symbol.name == ast.name and symbol.flag != 2: 
                    return symbol.mtype
            
        raise Undeclared(Identifier(), ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast, o):
        typ = None
        for env in o[0]:
            for symbol in env:
                if symbol.name == ast.name and type(symbol.mtype) is ArrayType:
                    dimensions = symbol.mtype.dimensions
                    if len(dimensions) < len(ast.cell):
                        raise TypeMismatchInExpression(ast)
                        
                    for expr in ast.cell:
                        typ = self.visit(expr, o)
                        if type(typ) is not IntegerType:
                            raise TypeMismatchInExpression(ast)        
                    
                    if len(dimensions) == len(ast.cell):
                        return typ
                    if len(dimensions) > len(ast.cell):
                        # dim = symbol.mtype.dimensions
                        return ArrayType(dimensions[len(ast.cell):], typ)
                        
                if symbol.name == ast.name and type(symbol.mtype) is not ArrayType:
                    raise TypeMismatchInExpression(ast)       
        raise Undeclared(Identifier(), ast.name)   

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
        if len(ast.explist) == 0:
            raise IllegalArrayLiteral(ast)
        typ = self.visit(ast.explist[0], o)
        dim = []
        if type(typ) is AutoType:
            for i in range(1, len(ast.explist)):
                curr = self.visit(ast.explist[i], o)
                if type(curr) is ArrayType:
                    typ = Utils.infer(o[0], ast.explist[i].name, curr.typ, o[1]) 
                    if typ is None:
                        typ = Utils.infer(o[1], ast.explist[i].name, curr.typ, o[1])   
                    if type(curr.typ) is not type(typ):
                        raise IllegalArrayLiteral(ast)
                else: 
                    typ = Utils.infer(o[0], ast.explist[0].name, curr, o[1]) 
                    if typ is None:
                        typ = Utils.infer(o[1], ast.explist[0].name, curr, o[1])   
                    
        if type(typ) is not AutoType:
            if type(typ) is ArrayType:
                dim = typ.dimensions
            for i in range(1, len(ast.explist)):
                curr = self.visit(ast.explist[i], o)
                if type(typ) is ArrayType:	
                    if type(curr.typ) is not type(typ.typ) or curr.dimensions != typ.dimensions:
                        raise IllegalArrayLiteral(ast)
                else:
                    if type(curr) is AutoType:
                        curr = Utils.infer(o[0], ast.explist[i].name, typ, o[1])   
                        if curr is None:
                            curr = Utils.infer(o[1], ast.explist[i].name, typ, o[1])   
                    if type(curr) is not type(typ):
                        raise IllegalArrayLiteral(ast)
        
        dims = [len(ast.explist)] + dim     
        return ArrayType(dims, typ)
    # name: str, args: List[Expr]
    def visitFuncCall(self, ast, o):
        if ast.name == "printInteger":
            raise TypeMismatchInExpression(ast) 
        if ast.name == "writeFloat":
            raise TypeMismatchInExpression(ast)
        if ast.name == "printBoolean":
            raise TypeMismatchInExpression(ast)
        if ast.name == "printString":
            raise TypeMismatchInExpression(ast)
        if ast.name == "readInteger":
            if len(ast.args) != 0:
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        if ast.name == "readFloat":
            if len(ast.args) != 0:
                raise TypeMismatchInExpression(ast)
            return FloatType()
        if ast.name == "readBoolean":
            if len(ast.args) != 0:
                raise TypeMismatchInExpression(ast)
            return  BooleanType()
        if ast.name == "readString":
            if len(ast.args) != 0:
                raise TypeMismatchInExpression(ast)
            return StringType()
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
            lhs = params[i].typ
            rhs = self.visit(ast.args[i], o)
            
            if type(lhs) is VoidType or type(rhs) is VoidType:
                raise TypeMismatchInExpression(ast)
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                if lhs.dimensions !=  rhs.dimensions:
                    raise TypeMismatchInExpression(ast)
                if lhs.typ is not rhs.typ:
                    raise TypeMismatchInExpression(ast)
                return func_type
               
            if type(lhs) is AutoType:
                lhs = Utils.infer(o[0], params[i].name, rhs, o[1])
            if type(rhs) is AutoType:
                rhs = Utils.infer(o[0], ast.args[i].name, lhs, o[1])
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
        return ArrayType(ast.dimensions, ast.typ)


    def visitAutoType(self, ast, o):
        return AutoType()


    def visitVoidType(self, ast, o):
        return VoidType()