lexer grammar PapyrusLexer;

import LexBasic;


// ################################################################
// ################# Boilerplate for antlr-denter #################
// ########### (https://github.com/yshavit/antlr-denter) ##########
// ################################################################

// ****************************************************************
// ********************* Python implementation ********************
// ****************************************************************

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
}
@lexer::members {
class PapyrusDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: PapyrusLexer = lexer

    def pull_token(self):
        return super(PapyrusLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.PapyrusDenter(self, self.NL, PapyrusLexer.INDENT, PapyrusLexer.DEDENT, False)
    return self.denter.next_token()
 
}

NL: ('\r'? '\n' ' '*);

// ****************************************************************
// ********************** Java implementation *********************
// ****************************************************************

// tokens { INDENT, DEDENT }
//
// @lexer::header {
//   import com.yuvalshavit.antlr4.DenterHelper;
// }
// @lexer::members {
//   private final DenterHelper denter = new DenterHelper(NL, PapyrusLexer.INDENT, PapyrusLexer.DEDENT) {
//     @Override
//     public Token pullToken() {
//       return PapyrusLexer.super.nextToken();
//     }
//   };
//
//   @Override
//   public Token nextToken() {
//     return denter.nextToken();
//   }
// }
//
// NL: ('\r'? '\n' ' '*);

// ################################################################
// ############################# (end) ############################
// ################################################################


// "Verbs" that can begin lines
VERB_SET : 'set' ;
VERB_ADD : 'add' ;
VERB_DELETE : 'delete' ;
VERB_UPDATE : 'update' ;
VERB_RUN : 'run' ;


// Types of literals
BOOL_LITERAL : BoolLiteral ;
INT_LITERAL : (MINUS HWS*)? (DecimalNumeral | HexNumeral) ;
fragment HexNumeral : ('0x' | '0X') HexDigit+ ;
STRING_LITERAL : SQuoteLiteral | DQuoteLiteral ;
BYTES_LITERAL : LBrack (HexDigit | Hws)* RBrack ;


// NOTE: this has to be below BOOL_LITERAL so that "true"/"false" resolve to that and not to this
NAME : NameStartChar NameChar* ;


// Exposing some LexBasic fragments to the parser
HWS : Hws ;
VWS : Vws ;
COLON : Colon ;
COMMA : Comma ;
DOT : Dot ;
EQUAL : Equal ;
L_PAREN : LParen ;
MINUS : '-' ;  // why is this not in LexBasic, anyway?
R_PAREN : RParen ;


// LexBasic's LineComment uses "//" and not "#", so we ignore it and redefine it with "#"
LINE_COMMENT_POUND : Pound ~ [\r\n]* ;
