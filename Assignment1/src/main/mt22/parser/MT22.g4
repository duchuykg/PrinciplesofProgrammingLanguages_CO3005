// ID: 2011286
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF ;

decl: vardecl | funcdecl ;

//5.1
//5.1.1
vardecl: varlist SEMI;
varlist: ID var1 expr | idlist COLON typ;
var1: COMMA ID var1 expr COMMA | COLON typ ASSIGN;
idlist: ID COMMA idlist | ID;

//5.1.2
param: ap_inherit ap_out ID COLON typ;
ap_inherit: INHERIT | ;
ap_out: OUT | ;

//5.2
funcdecl: ID COLON FUNCTION type_func LB paramlist RB inher_func blockstmt;
paramlist: paramprime |  ;
paramprime: param COMMA paramprime | param;
inher_func: INHERIT ID | ;

//7.Statements
stmt: assignstmt
    | ifstmt
    | forstmt
    | whilestmt
    | dowhilestmt
    | breakstmt
    | continuestmt
    | returnstmt
    | callstmt
    | blockstmt;

//7.1
assignstmt: scalar_var ASSIGN expr SEMI;
scalar_var: ID | index_operator;

//7.2
ifstmt: IF LB expr RB stmt else_part;
else_part: ELSE stmt | ;

//7.3
forstmt: FOR LB scalar_var ASSIGN INTLIT COMMA condition_expr COMMA update_expr RB stmt;
condition_expr: expr;
update_expr: expr;

//7.4
whilestmt: WHILE LB expr RB stmt;

//7.5
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;

//7.6
breakstmt: BREAK SEMI;

//7.7
continuestmt: CONTINUE SEMI;

//7.8
returnstmt: RETURN list1 SEMI;
list1: expr | ;

//7.9
callstmt: special_func SEMI | func_call SEMI;

//7.10
blockstmt: LP blocklist RP;
blocklist: stmt blocklist | vardecl blocklist | ;

//4.1
typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | type_array;
type_func: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID | type_array;
type_element: BOOLEAN | INTEGER | FLOAT | STRING;

//4.2
type_array: ARRAY LS integerlist RS OF type_element;
integerlist: INTLIT COMMA integerlist | INTLIT;

//3.7
literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;

//3.7.1
INTLIT: '0' | [1-9][0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_","")};

//3.7.2
FLOATLIT: INTPART DECPART EXPPART* {self.text = self.text.replace("_","")}
        | INTPART EXPPART {self.text = self.text.replace("_","")}
        | DECPART EXPPART {self.text = '0' + self.text.replace("_","")};
fragment INTPART: INTLIT;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE][+-]? [0-9]+;

//3.7.3
BOOLLIT: 'true' | 'false';

//3.7.4
STRINGLIT: '"' (STRING_DB | ESCAPE)* '"' {self.text = self.text[1:-1]};
fragment STRING_DB: ~[\n\\"];
fragment ESCAPE:  '\\"' | '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\';
fragment ILL_ESCAPE: '\\' ~[bfrnt'\\] | '\'' ~'"';

//3.7.5
arraylit: LP expr_primelist RP;
expr_primelist: expr_list | ;
expr_list: expr COMMA expr_list| expr;

//6.5
index_operator: ID LS expr_list RS;
index_op: LS expr_list RS;

//6.6
func_call: ID LB list_arg RB;
list_arg: list_argprime | ;
list_argprime: expr COMMA list_argprime | expr;

//8
special_func: readi
            | readf
            | readb
            | reads
            | printi
            | printb
            | prints
            | writef
            | super_func
            | preventdefault;

readi: READI LB RB;
readf: READF LB RB;
readb: READB LB RB;
reads: READS LB RB;
printi: PRINTI LB expr RB;
printb: PRINTB LB expr RB;
prints: PRINTS LB expr RB;
writef: WRITEF LB expr RB;
super_func: SUPER LB expr_primelist RB;
preventdefault: PREVENTDEFAULT LB RB;

//6.Expression
operand: literal | ID | func_call | special_func;

expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL | SMALLER | GREATER | SMALLER_EQUAL | GREATER_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: index_operator | expr8; //De sua: khong co tinh ket hop
expr8: operand | LB expr RB;

//3.4
AUTO: 'auto';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

//3.2
COMMENT: (COMMENT_C | COMMENT_C2plus) -> skip;
fragment COMMENT_C: '/*' .*? '*/';
fragment COMMENT_C2plus: '//' ~[\r\n]*;

//3.5
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
SMALLER: '<';
SMALLER_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
CONCAT: '::';

//3.6
LB: '(' ;
RB: ')' ;
LS: '[';
RS: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LP: '{';
RP: '}';
ASSIGN: '=';

//8.Special
READI: 'readInteger';
READF: 'readFloat';
READB: 'readBoolean';
READS: 'readString';
PRINTI: 'printInteger';
PRINTB: 'printBoolean';
PRINTS: 'printString';
WRITEF: 'writeFloat';
SUPER: 'super';
PREVENTDEFAULT: 'preventDefault';

//3.3
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' (STRING_DB | ESCAPE)* (EOF | '\n'){
	esc = '\n'
	if self.text[-1] in esc:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' (STRING_DB | ESCAPE)* ILL_ESCAPE {
	raise IllegalEscape(self.text[1:])
};