#!/usr/bin/env bash

antlr4 -Dlanguage=Python3 -no-listener -visitor PapyrusLexer.g4
antlr4 -Dlanguage=Python3 -no-listener -visitor PapyrusParser.g4
