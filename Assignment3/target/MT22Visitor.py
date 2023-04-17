# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varlist.
    def visitVarlist(self, ctx:MT22Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var1.
    def visitVar1(self, ctx:MT22Parser.Var1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ap_inherit.
    def visitAp_inherit(self, ctx:MT22Parser.Ap_inheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ap_out.
    def visitAp_out(self, ctx:MT22Parser.Ap_outContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inher_func.
    def visitInher_func(self, ctx:MT22Parser.Inher_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_part.
    def visitElse_part(self, ctx:MT22Parser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list1.
    def visitList1(self, ctx:MT22Parser.List1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blocklist.
    def visitBlocklist(self, ctx:MT22Parser.BlocklistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_func.
    def visitType_func(self, ctx:MT22Parser.Type_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_element.
    def visitType_element(self, ctx:MT22Parser.Type_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_array.
    def visitType_array(self, ctx:MT22Parser.Type_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#integerlist.
    def visitIntegerlist(self, ctx:MT22Parser.IntegerlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_primelist.
    def visitExpr_primelist(self, ctx:MT22Parser.Expr_primelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_arg.
    def visitList_arg(self, ctx:MT22Parser.List_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_argprime.
    def visitList_argprime(self, ctx:MT22Parser.List_argprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_func.
    def visitSpecial_func(self, ctx:MT22Parser.Special_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readi.
    def visitReadi(self, ctx:MT22Parser.ReadiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readf.
    def visitReadf(self, ctx:MT22Parser.ReadfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readb.
    def visitReadb(self, ctx:MT22Parser.ReadbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#reads.
    def visitReads(self, ctx:MT22Parser.ReadsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printi.
    def visitPrinti(self, ctx:MT22Parser.PrintiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printb.
    def visitPrintb(self, ctx:MT22Parser.PrintbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prints.
    def visitPrints(self, ctx:MT22Parser.PrintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writef.
    def visitWritef(self, ctx:MT22Parser.WritefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_func.
    def visitSuper_func(self, ctx:MT22Parser.Super_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventdefault.
    def visitPreventdefault(self, ctx:MT22Parser.PreventdefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)



del MT22Parser