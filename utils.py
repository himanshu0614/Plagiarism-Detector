import os
import ast
import networkx as nx
from pygments.lexers import PythonLexer
from pygments.token import Token
from pygments import lex

def read_code(file_path):
    """Reads the Python source code from a file"""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def tokenize_code(code):
    """Tokenizes Python code and returns a list of tokens"""
    tokens = [token_type for token_type, _ in lex(code, PythonLexer()) if token_type not in Token.Text]
    return tokens

def generate_ast(code):
    """Parses code and generates an Abstract Syntax Tree (AST)"""
    return ast.parse(code)

def compare_ast(ast1, ast2):
    """Checks structural similarity between two ASTs"""
    return ast.dump(ast1) == ast.dump(ast2)

def generate_cfg(ast_tree):
    """Creates a control flow graph from AST"""
    cfg = nx.DiGraph()
    for node in ast.walk(ast_tree):
        cfg.add_node(type(node).__name__)
    return cfg
