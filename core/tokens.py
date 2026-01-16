from enum import Enum

class TokenType(Enum):
    INT = 'INT'
    FLOAT = 'FLOAT'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'  
    POW = '^'
    EQ = '='
    EE = '=='
    NE = '!='
    LT = '<'
    GT = '>'
    LTE = '<='
    GTE = '>='
    LPAREN = '('
    RPAREN = ')'
    LSQUARE = '['
    RSQUARE = ']'
    LCURLY = '{'
    RCURLY = '}'
    COMMA = ','
    ARROW = '->'
    NEWLINE = 'NEWLINE'
    EOF = 'EOF'
class Keyword(Enum):
    VAR = 'ცვლადი'
    AND = 'და'
    OR = 'ან'
    NOT = 'არა'
    IF = 'თუ'
    ELIF = 'სხვა'
    ELSE = 'სხვაშემთხვევაში'
    FOR = 'ციკლი'
    FROM = 'დან'
    TO = 'მდე'
    FUN = 'ფუნქცია'
    RETURN = 'დააბრუნე'
    CONTINUE = 'გააგრძელე'
    BREAK = 'შეწყვიტე'
    TRUE = 'ჭეშმარიტი'
    FALSE = 'მცდარი'


class BuiltInFunction(Enum):
    PRINT = 'დაბეჭდვა'
    PRINT_ALT = 'დაბეჭვდა'
    APPEND = 'დაამატე'
    POP = 'ამოიღე'
    EXTEND = 'გააფართოვე'
    LEN = 'სიგრძე'
    RUN = 'გაუშვი'
    
def get_keyword_values():
    return [k.value for k in Keyword]

def get_builtin_values():
    return [f.value for f in BuiltInFunction]



class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
