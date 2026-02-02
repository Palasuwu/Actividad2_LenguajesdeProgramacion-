from token_data import Token, TokenType, KEYWORDS
from symbol_table import SymbolTable

class Scanner:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.symbol_table = SymbolTable()

    def current_char(self):
        return self.source[self.pos] if self.pos < len(self.source) else None

    def advance(self):
        char = self.current_char()
        self.pos += 1
        if char == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return char

    def peek(self):
        next_pos = self.pos + 1
        return self.source[next_pos] if next_pos < len(self.source) else None

    def skip_comment(self):
        self.advance() # Consumir '/'
        next_c = self.advance()
        if next_c == '/': # Comentario de lnea //
            while self.current_char() and self.current_char() != '\n':
                self.advance()
        elif next_c == '*': # Comentario de bloque /* */
            while self.current_char():
                if self.current_char() == '*' and self.peek() == '/':
                    self.advance(); self.advance()
                    break
                self.advance()

    def scan_tokens(self):
        tokens = []
        while self.pos < len(self.source):
            char = self.current_char()
            if char is None: break
            if char.isspace():
                self.advance(); continue

            # Manejo de Comentarios
            if char == '/' and (self.peek() == '/' or self.peek() == '*'):
                self.skip_comment(); continue

            start_line, start_col = self.line, self.col

            # Identificadores 
            if char.isalpha() or char == '_':
                value = ""
                while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
                    value += self.advance()
                t_type = TokenType.KEYWORD if value in KEYWORDS else TokenType.IDENTIFIER
                if t_type == TokenType.IDENTIFIER:
                    self.symbol_table.add(value)
                tokens.append(Token(t_type, value, start_line, start_col))

            # Numeros (Enteros y Decimales)
            elif char.isdigit():
                value = ""
                while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
                    value += self.advance()
                tokens.append(Token(TokenType.NUMBER, value, start_line, start_col))

            # Cadenas de strings
            elif char == '"':
                value = self.advance()
                while self.current_char() and self.current_char() != '"':
                    value += self.advance()
                if self.current_char() == '"': value += self.advance()
                tokens.append(Token(TokenType.STRING, value, start_line, start_col))

            # Operadores 
            elif char in "+-*/=<>!":
                value = self.advance()
                if self.current_char() == '=': # Para <=, -=, etc.
                    value += self.advance()
                tokens.append(Token(TokenType.OPERATOR, value, start_line, start_col))
            
            # Delimitadores
            elif char in "(){}[];,.":
                value = self.advance()
                tokens.append(Token(TokenType.DELIMITER, value, start_line, start_col))
            
            else:
                self.advance() # Ignorar caracteres no reconocidos

        tokens.append(Token(TokenType.EOF, "EOF", self.line, self.col))
        return tokens