
#tipos de tokens y clase token
class TokenType:
    KEYWORD = "Palabra Reservada"
    IDENTIFIER = "Identificador"
    NUMBER = "Numero"
    STRING = "Cadena de Texto"
    OPERATOR = "Operador"
    DELIMITER = "Delimitador"
    EOF = "Fin de Archivo"

# Palabras reservadas en java 
KEYWORDS = {
    "public", "class", "static", "final", "double", "int", 
    "String", "void", "new", "if", "else", "this", "private"
}

class Token:
    def __init__(self, t_type, value, line, col):
        self.type = t_type
        self.value = value
        self.line = line
        self.col = col

    def __str__(self):
        #Linea:Col | Tipo | Valor
        return f"Linea {self.line:2}:{self.col:<3} | {self.type:<18} | {self.value}"
        print("="*50)
