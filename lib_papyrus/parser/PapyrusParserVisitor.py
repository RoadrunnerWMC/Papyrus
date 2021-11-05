# Generated from PapyrusParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapyrusParser import PapyrusParser
else:
    from PapyrusParser import PapyrusParser

# This class defines a complete generic visitor for a parse tree produced by PapyrusParser.

class PapyrusParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PapyrusParser#papyrusFile.
    def visitPapyrusFile(self, ctx:PapyrusParser.PapyrusFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#statements.
    def visitStatements(self, ctx:PapyrusParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#statement.
    def visitStatement(self, ctx:PapyrusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#singleLineStatement.
    def visitSingleLineStatement(self, ctx:PapyrusParser.SingleLineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#blockStatement.
    def visitBlockStatement(self, ctx:PapyrusParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#blockLines.
    def visitBlockLines(self, ctx:PapyrusParser.BlockLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#blockStartingLine.
    def visitBlockStartingLine(self, ctx:PapyrusParser.BlockStartingLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#standaloneLine.
    def visitStandaloneLine(self, ctx:PapyrusParser.StandaloneLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#setLine.
    def visitSetLine(self, ctx:PapyrusParser.SetLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#addLine.
    def visitAddLine(self, ctx:PapyrusParser.AddLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#deleteLine.
    def visitDeleteLine(self, ctx:PapyrusParser.DeleteLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#updateLine.
    def visitUpdateLine(self, ctx:PapyrusParser.UpdateLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#runLine.
    def visitRunLine(self, ctx:PapyrusParser.RunLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#blankLine.
    def visitBlankLine(self, ctx:PapyrusParser.BlankLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#setLineValue.
    def visitSetLineValue(self, ctx:PapyrusParser.SetLineValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#lineEndingJunk.
    def visitLineEndingJunk(self, ctx:PapyrusParser.LineEndingJunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#objectNameSearchable.
    def visitObjectNameSearchable(self, ctx:PapyrusParser.ObjectNameSearchableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#macro.
    def visitMacro(self, ctx:PapyrusParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#args.
    def visitArgs(self, ctx:PapyrusParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#arg.
    def visitArg(self, ctx:PapyrusParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#positionalArg.
    def visitPositionalArg(self, ctx:PapyrusParser.PositionalArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#keywordArg.
    def visitKeywordArg(self, ctx:PapyrusParser.KeywordArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#objectAttribute.
    def visitObjectAttribute(self, ctx:PapyrusParser.ObjectAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#typeName.
    def visitTypeName(self, ctx:PapyrusParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#objectName.
    def visitObjectName(self, ctx:PapyrusParser.ObjectNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#attributeName.
    def visitAttributeName(self, ctx:PapyrusParser.AttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#macroName.
    def visitMacroName(self, ctx:PapyrusParser.MacroNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#macroKeywordArgName.
    def visitMacroKeywordArgName(self, ctx:PapyrusParser.MacroKeywordArgNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#anyLiteral.
    def visitAnyLiteral(self, ctx:PapyrusParser.AnyLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#boolLiteral.
    def visitBoolLiteral(self, ctx:PapyrusParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#intLiteral.
    def visitIntLiteral(self, ctx:PapyrusParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#stringLiteral.
    def visitStringLiteral(self, ctx:PapyrusParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#bytesLiteral.
    def visitBytesLiteral(self, ctx:PapyrusParser.BytesLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapyrusParser#name.
    def visitName(self, ctx:PapyrusParser.NameContext):
        return self.visitChildren(ctx)



del PapyrusParser