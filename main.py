from utils import read_code, tokenize_code, generate_ast, compare_ast, generate_cfg

# File paths for student submissions
file1 = "submissions/student1.py"
file2 = "submissions/student2.py"

# Read the code from both student files
code1 = read_code(file1)
code2 = read_code(file2)

# Check if both files were found
if not code1 or not code2:
    print("Error: One or both files could not be read. Exiting...")
    exit()

# Tokenization check
tokens1 = tokenize_code(code1)
tokens2 = tokenize_code(code2)
token_similarity = tokens1 == tokens2

print("\nToken Similarity:", token_similarity)

# AST Comparison
ast1 = generate_ast(code1)
ast2 = generate_ast(code2)
ast_similarity = compare_ast(ast1, ast2)

print("\nAST Similarity:", ast_similarity)

# Generate Control Flow Graphs (CFG)
cfg1 = generate_cfg(ast1)
cfg2 = generate_cfg(ast2)

print("\nControl Flow Graph Nodes (Student 1):", cfg1.nodes)
print("Control Flow Graph Nodes (Student 2):", cfg2.nodes)

# Final verdict
if ast_similarity or token_similarity:
    print("\n⚠️ Potential Plagiarism Detected!")
else:
    print("\n✅ The codes are significantly different.")
