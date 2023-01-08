@echo off

antlr4 -Dlanguage=Python3 -no-listener -visitor -o gen/ cell.g4
