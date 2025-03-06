# Code Plagiarism Detector

## Overview
This project detects plagiarism in Python code by analyzing syntax, structure, and logic using tokenization, AST (Abstract Syntax Tree), and Control Flow Graph (CFG).

## Features
- **Token-Based Comparison**: Uses lexical analysis to compare token sequences.
- **AST Comparison**: Checks structural similarity between two codes.
- **Control Flow Graph (CFG) Analysis**: Examines code execution flow.
- **Multi-File Support**: Compare multiple Python scripts.

## Installation
### Prerequisites
Ensure you have Python installed. Install dependencies using:
```bash
pip install pygments networkx
```

## Usage
1. Place student Python files in the directory (e.g., `student1.py`, `student2.py`).
2. Run the program:
```bash
python main.py
```
3. The output will indicate similarity based on tokenization, AST, and CFG.

## File Structure
```
|-- project-directory/
    |-- main.py  # Main script to run plagiarism check
    |-- utils.py  # Helper functions for tokenization, AST, and CFG
    |-- student1.py  # Sample student file 1
    |-- student2.py  # Sample student file 2
    |-- README.md  # Documentation
```

## GitHub Setup & Deployment
To push this project to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

## License
This project is licensed under the MIT License.
