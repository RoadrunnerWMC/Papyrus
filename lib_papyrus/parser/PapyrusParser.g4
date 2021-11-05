parser grammar PapyrusParser;

options { tokenVocab=PapyrusLexer; }


papyrusFile : statements ;
statements : statement* ;


// NOTE about antlr-denter: it puts EITHER a `NL` OR a sequence of DEDENT/INDENT between two lines, but not both.
// I'm not convinced this is a good design, but regardless, that's why some of the rules below might look a bit odd.


// Types of statements
statement : singleLineStatement | blockStatement;
singleLineStatement : standaloneLine NL ;
blockStatement : blockStartingLine (blockLines | NL) ;

blockLines : INDENT (standaloneLine NL)+ DEDENT;


// Categories of lines
blockStartingLine : addLine | updateLine ;
standaloneLine : setLine | deleteLine | runLine | blankLine ;


// Specific types of lines
setLine : VERB_SET HWS+ attributeName HWS+ setLineValue lineEndingJunk ;
addLine : VERB_ADD HWS+ typeName (HWS+ objectName)? HWS* COLON (HWS* bytesLiteral)? lineEndingJunk ;
deleteLine : VERB_DELETE HWS+ typeName HWS+ objectNameSearchable lineEndingJunk ;
updateLine : VERB_UPDATE HWS+ typeName HWS+ objectNameSearchable HWS* COLON lineEndingJunk ;
runLine : VERB_RUN HWS+ macro lineEndingJunk ;
blankLine : lineEndingJunk ;

setLineValue : anyLiteral | objectAttribute | macro ;


// Helper for optional junk at the end of a line (whitespace and/or comment)
lineEndingJunk : HWS* LINE_COMMENT_POUND? ;


// A name of an object for lookup purposes (either an explicit name, or a macro returning a name)
objectNameSearchable : (objectName | macro) ;


// Macros (look like function calls in most other languages)
// NOTE: the "all positional-only must precede all keyword-only arguments" policy should be enforced
// at the semantic level -- otherwise this gets way too complicated and unreadable/undebuggable
macro : macroName HWS* L_PAREN HWS* args R_PAREN ;
args : arg HWS* (COMMA HWS* arg HWS*)* ;
arg : positionalArg | keywordArg ;
positionalArg : anyLiteral ;
keywordArg : macroKeywordArgName HWS* EQUAL HWS* anyLiteral ;


// Attribute on an object ("object.attribute")
objectAttribute : objectName HWS* DOT HWS* attributeName ;


// Some aliases for `name` so the rules above are more readable
// (and also to help with walking the tree)
typeName : name ;
objectName : name ;
attributeName : name ;
macroName : name ;
macroKeywordArgName : name ;


// Stand-in for any literal value
// "name" is here for constant literals
anyLiteral : boolLiteral | intLiteral | stringLiteral | bytesLiteral | name ;


boolLiteral : BOOL_LITERAL ;
intLiteral : INT_LITERAL ;
stringLiteral : STRING_LITERAL ;
bytesLiteral : BYTES_LITERAL ;
name : NAME ;
