grammar cell;


/*

TODO :
    - add imports
    - add break & continue keywords
    - add Object-Oriented-Programming (OOP)

*/


/* Lexer Rules */

/// Symbol
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LLIST : '[';
RLIST : ']';

EQUALS : '=';
DOT : '.';
COMMA : ',';
SEMI : ';';
COLON : ':';
DOUBLECOLONS : '::';
QUESTION : '?';
AMPERSAND : '&';
EXCLAM : '!';
LARROW : '->';
RARROW : '<-';
ARROWASSIGN : '=>';
AT : '@';


/// Operators
OPERATORS : '+' | '-' | '*' | '/' | '%' | '**' | '==' | '!=' | '>' | '<' | '<=' | '>=';
ASSIGNOPS : '+=' | '-=' | '*=' | '/=' | '%=' | '**=';
INCR : '++';
DECR : '--';


/// Keywords
FUNC : 'func' | 'fn';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
IMPORT : 'import';
FROM : 'from';
CLASS : 'class';
NEW : 'new';
OVERRIDE : 'override';
PUBLIC : 'public';
PRIVATE : 'private';
TASK : 'task';

TASK_RESUME : 'resume';


/// Skipped
COMMENT : '//' ~[\r\n]* -> skip;
WS : [ \t\r\n] -> skip;

/// Data Types
BOOL : ('true' | 'false');
NULL : 'null';

ID : [a-zA-Z_] [a-zA-Z_0-9]*;
INT : '-'? [0-9]+;
FLOAT : '-'? [0-9]+? '.' [0-9]*;
STRING : '"' (~["\r\n] | '""')* '"';

/// All
TYPE : 'int' | 'float' | 'string' | 'bool';

/* Parser Rules */

parse : stmt* EOF;

stmts: stmt*;

stmt
    : if_stmt SEMI?
    | while_stmt SEMI?
    | for_stmt SEMI?
    | varassignment SEMI?
    | funcassignment SEMI?
    | expr SEMI?
    | call SEMI?
    ;


/// Stmts
if_stmt : IF conditional_block stmt_block (ELSE IF conditional_block stmt_block)* (ELSE stmt_block)?;
while_stmt : WHILE conditional_block stmt_block;
for_stmt : FOR ID SEMI conditional_block SEMI ID (INCR | DECR) stmt_block;


/// Assignments
varassignment
    : ID? QUESTION? ID atype=EQUALS expr
    | ID? QUESTION? ID atype=ASSIGNOPS expr
    ;

funcassignment
    : (PUBLIC | PRIVATE)? OVERRIDE? (FUNC | ID) ID LPAREN params? RPAREN stmt_block
    | ID? ID EQUALS LPAREN params? RPAREN (PUBLIC | PRIVATE)? OVERRIDE? ARROWASSIGN stmt_block
    ;


/// Blocks
conditional_block
    : LPAREN expr RPAREN
    | expr
    ;

stmt_block: LBRACE stmts RBRACE;


/// Functions
call : ID LPAREN args? RPAREN;

args : expr (COMMA expr)*;
params : ID? ID (COMMA ID? ID)*;


/// Other
type_conversion : LPAREN ID RPAREN (ID | STRING | BOOL | INT | FLOAT);

mem_addr : AMPERSAND ID;

getattribs : (ID | STRING | BOOL | INT | FLOAT) DOT ID (LPAREN args? RPAREN)?;

task_usage : AT TASK DOT (NEW | TASK_RESUME) LPAREN args? RPAREN;

// More datatypes
array : LLIST args? RLIST;


// Expression
expr
    : ID
    | STRING
    | INT
    | FLOAT
    | BOOL
    | NULL
    | expr op=OPERATORS expr
    | EXCLAM BOOL
    | type_conversion
    | task_usage
    | getattribs
    | mem_addr
    | array
    | call
    ;
