import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        # Definisikan pola regex untuk masing-masing token
        token_specification = [
            ('STRING',   r'"[^"]*"'),           # String literal
            ('NUMBER',   r'\d+(\.\d*)?'),       # Integer or decimal number
            ('ASSIGN',   r'='),                 # Assignment operator
            ('ID',       r'[A-Za-z_]\w*'),      # Identifiers
            ('LPAREN',   r'\('),                # Left parenthesis
            ('RPAREN',   r'\)'),                # Right parenthesis
            ('SKIP',     r'[ \t\n]+'),          # Skip spaces and tabs
            ('MISMATCH', r'.'),                 # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        
        for mo in re.finditer(tok_regex, self.text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'STRING':
                value = value[1:-1] # Remove quotes
                self.tokens.append(Token(kind, value))
            elif kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
                self.tokens.append(Token(kind, value))
            elif kind == 'ID':
                self.tokens.append(Token(kind, value))
            elif kind in ('ASSIGN', 'LPAREN', 'RPAREN'):
                self.tokens.append(Token(kind, value))
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Syntax salah pada karakter: {value!r}')
        self.tokens.append(Token('EOF', ''))

    def get_tokens(self):
        return self.tokens
