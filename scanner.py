import re
import sys

class MiniLangScanner:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.source_code = file.read()
        self.tokens = []
        self.keywords = {'if', 'else', 'print', 'true', 'false'}

    def scan(self):
        lines = self.source_code.split('\n')
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if line.startswith('//'):
                continue

            tokens = re.findall(r'\b(?:\d+|true|false|[a-zA-Z][a-zA-Z0-9]*|\S)\b|==|!=|[+\-*/=()]', line)
            for token in tokens:
                if token in self.keywords:
                    self.tokens.append(('KEYWORD', token))
                elif token.isdigit():
                    self.tokens.append(('INTEGER_LITERAL', int(token)))
                elif token in {'true', 'false'}:
                    self.tokens.append(('BOOLEAN_LITERAL', token == 'true'))
                elif token.isalpha():
                    self.tokens.append(('IDENTIFIER', token))
                elif token in {'+', '-', '*', '/', '=', '==', '!=', '(', ')'}:
                    self.tokens.append(('OPERATOR', token))
                else:
                    print(f"Lexical Error: Line {line_num}, unrecognized token '{token}'")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python minilang_scanner.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    scanner = MiniLangScanner(file_path)
    scanner.scan()

    print("Tokens:")
    for token_type, lexeme in scanner.tokens:
        print(f"{token_type}: {lexeme}")
