# Generated from PapyrusParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapyrusParser import PapyrusParser
else:
    from PapyrusParser import PapyrusParser

# This class defines a complete listener for a parse tree produced by PapyrusParser.
class PapyrusParserListener(ParseTreeListener):

    # Enter a parse tree produced by PapyrusParser#papyrusFile.
    def enterPapyrusFile(self, ctx:PapyrusParser.PapyrusFileContext):
        pass

    # Exit a parse tree produced by PapyrusParser#papyrusFile.
    def exitPapyrusFile(self, ctx:PapyrusParser.PapyrusFileContext):
        pass


    # Enter a parse tree produced by PapyrusParser#statements.
    def enterStatements(self, ctx:PapyrusParser.StatementsContext):
        pass

    # Exit a parse tree produced by PapyrusParser#statements.
    def exitStatements(self, ctx:PapyrusParser.StatementsContext):
        pass


    # Enter a parse tree produced by PapyrusParser#statement.
    def enterStatement(self, ctx:PapyrusParser.StatementContext):
        pass

    # Exit a parse tree produced by PapyrusParser#statement.
    def exitStatement(self, ctx:PapyrusParser.StatementContext):
        pass


    # Enter a parse tree produced by PapyrusParser#singleLineStatement.
    def enterSingleLineStatement(self, ctx:PapyrusParser.SingleLineStatementContext):
        pass

    # Exit a parse tree produced by PapyrusParser#singleLineStatement.
    def exitSingleLineStatement(self, ctx:PapyrusParser.SingleLineStatementContext):
        pass


    # Enter a parse tree produced by PapyrusParser#blockStatement.
    def enterBlockStatement(self, ctx:PapyrusParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PapyrusParser#blockStatement.
    def exitBlockStatement(self, ctx:PapyrusParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by PapyrusParser#blockLines.
    def enterBlockLines(self, ctx:PapyrusParser.BlockLinesContext):
        pass

    # Exit a parse tree produced by PapyrusParser#blockLines.
    def exitBlockLines(self, ctx:PapyrusParser.BlockLinesContext):
        pass


    # Enter a parse tree produced by PapyrusParser#blockStartingLine.
    def enterBlockStartingLine(self, ctx:PapyrusParser.BlockStartingLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#blockStartingLine.
    def exitBlockStartingLine(self, ctx:PapyrusParser.BlockStartingLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#standaloneLine.
    def enterStandaloneLine(self, ctx:PapyrusParser.StandaloneLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#standaloneLine.
    def exitStandaloneLine(self, ctx:PapyrusParser.StandaloneLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#setLine.
    def enterSetLine(self, ctx:PapyrusParser.SetLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#setLine.
    def exitSetLine(self, ctx:PapyrusParser.SetLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#addLine.
    def enterAddLine(self, ctx:PapyrusParser.AddLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#addLine.
    def exitAddLine(self, ctx:PapyrusParser.AddLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#deleteLine.
    def enterDeleteLine(self, ctx:PapyrusParser.DeleteLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#deleteLine.
    def exitDeleteLine(self, ctx:PapyrusParser.DeleteLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#updateLine.
    def enterUpdateLine(self, ctx:PapyrusParser.UpdateLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#updateLine.
    def exitUpdateLine(self, ctx:PapyrusParser.UpdateLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#runLine.
    def enterRunLine(self, ctx:PapyrusParser.RunLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#runLine.
    def exitRunLine(self, ctx:PapyrusParser.RunLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#blankLine.
    def enterBlankLine(self, ctx:PapyrusParser.BlankLineContext):
        pass

    # Exit a parse tree produced by PapyrusParser#blankLine.
    def exitBlankLine(self, ctx:PapyrusParser.BlankLineContext):
        pass


    # Enter a parse tree produced by PapyrusParser#lineEndingJunk.
    def enterLineEndingJunk(self, ctx:PapyrusParser.LineEndingJunkContext):
        pass

    # Exit a parse tree produced by PapyrusParser#lineEndingJunk.
    def exitLineEndingJunk(self, ctx:PapyrusParser.LineEndingJunkContext):
        pass


    # Enter a parse tree produced by PapyrusParser#objectNameSearchable.
    def enterObjectNameSearchable(self, ctx:PapyrusParser.ObjectNameSearchableContext):
        pass

    # Exit a parse tree produced by PapyrusParser#objectNameSearchable.
    def exitObjectNameSearchable(self, ctx:PapyrusParser.ObjectNameSearchableContext):
        pass


    # Enter a parse tree produced by PapyrusParser#macro.
    def enterMacro(self, ctx:PapyrusParser.MacroContext):
        pass

    # Exit a parse tree produced by PapyrusParser#macro.
    def exitMacro(self, ctx:PapyrusParser.MacroContext):
        pass


    # Enter a parse tree produced by PapyrusParser#args.
    def enterArgs(self, ctx:PapyrusParser.ArgsContext):
        pass

    # Exit a parse tree produced by PapyrusParser#args.
    def exitArgs(self, ctx:PapyrusParser.ArgsContext):
        pass


    # Enter a parse tree produced by PapyrusParser#arg.
    def enterArg(self, ctx:PapyrusParser.ArgContext):
        pass

    # Exit a parse tree produced by PapyrusParser#arg.
    def exitArg(self, ctx:PapyrusParser.ArgContext):
        pass


    # Enter a parse tree produced by PapyrusParser#positionalArg.
    def enterPositionalArg(self, ctx:PapyrusParser.PositionalArgContext):
        pass

    # Exit a parse tree produced by PapyrusParser#positionalArg.
    def exitPositionalArg(self, ctx:PapyrusParser.PositionalArgContext):
        pass


    # Enter a parse tree produced by PapyrusParser#keywordArg.
    def enterKeywordArg(self, ctx:PapyrusParser.KeywordArgContext):
        pass

    # Exit a parse tree produced by PapyrusParser#keywordArg.
    def exitKeywordArg(self, ctx:PapyrusParser.KeywordArgContext):
        pass


    # Enter a parse tree produced by PapyrusParser#objectAttribute.
    def enterObjectAttribute(self, ctx:PapyrusParser.ObjectAttributeContext):
        pass

    # Exit a parse tree produced by PapyrusParser#objectAttribute.
    def exitObjectAttribute(self, ctx:PapyrusParser.ObjectAttributeContext):
        pass


    # Enter a parse tree produced by PapyrusParser#typeName.
    def enterTypeName(self, ctx:PapyrusParser.TypeNameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#typeName.
    def exitTypeName(self, ctx:PapyrusParser.TypeNameContext):
        pass


    # Enter a parse tree produced by PapyrusParser#objectName.
    def enterObjectName(self, ctx:PapyrusParser.ObjectNameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#objectName.
    def exitObjectName(self, ctx:PapyrusParser.ObjectNameContext):
        pass


    # Enter a parse tree produced by PapyrusParser#attributeName.
    def enterAttributeName(self, ctx:PapyrusParser.AttributeNameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#attributeName.
    def exitAttributeName(self, ctx:PapyrusParser.AttributeNameContext):
        pass


    # Enter a parse tree produced by PapyrusParser#macroName.
    def enterMacroName(self, ctx:PapyrusParser.MacroNameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#macroName.
    def exitMacroName(self, ctx:PapyrusParser.MacroNameContext):
        pass


    # Enter a parse tree produced by PapyrusParser#macroKeywordArgName.
    def enterMacroKeywordArgName(self, ctx:PapyrusParser.MacroKeywordArgNameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#macroKeywordArgName.
    def exitMacroKeywordArgName(self, ctx:PapyrusParser.MacroKeywordArgNameContext):
        pass


    # Enter a parse tree produced by PapyrusParser#anyLiteral.
    def enterAnyLiteral(self, ctx:PapyrusParser.AnyLiteralContext):
        pass

    # Exit a parse tree produced by PapyrusParser#anyLiteral.
    def exitAnyLiteral(self, ctx:PapyrusParser.AnyLiteralContext):
        pass


    # Enter a parse tree produced by PapyrusParser#name.
    def enterName(self, ctx:PapyrusParser.NameContext):
        pass

    # Exit a parse tree produced by PapyrusParser#name.
    def exitName(self, ctx:PapyrusParser.NameContext):
        pass



del PapyrusParser