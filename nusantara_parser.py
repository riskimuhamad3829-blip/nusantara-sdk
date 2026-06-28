class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        if self.current_token().type == token_type:
            self.pos += 1
        else:
            raise RuntimeError(f"Diharapkan {token_type} tapi mendapatkan {self.current_token().type}")

    def parse(self):
        statements = []
        while self.current_token().type != 'EOF':
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.current_token()
        
        # Variabel assignment: nama = nilai
        if token.type == 'ID':
            next_tok = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            
            if next_tok and next_tok.type == 'ASSIGN':
                var_name = token.value
                self.eat('ID')
                self.eat('ASSIGN')
                value = self.parse_expression()
                return ('ASSIGN', var_name, value)
            
            elif next_tok and next_tok.type == 'LPAREN':
                # Function call: fungsi(arg)
                func_name = token.value
                self.eat('ID')
                self.eat('LPAREN')
                arg = self.parse_expression()
                self.eat('RPAREN')
                return ('CALL', func_name, arg)
                
            else:
                # Standalone expression / variable evaluation
                return self.parse_expression()
                
        return self.parse_expression()

    def parse_expression(self):
        token = self.current_token()
        if token.type == 'STRING':
            self.eat('STRING')
            return ('STRING', token.value)
        elif token.type == 'NUMBER':
            self.eat('NUMBER')
            return ('NUMBER', token.value)
        elif token.type == 'ID':
            var_name = token.value
            self.eat('ID')
            return ('VAR', var_name)
        else:
            raise RuntimeError(f"Ekspresi tidak valid: {token}")
