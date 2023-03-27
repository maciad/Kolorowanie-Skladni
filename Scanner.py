from enum import Enum


class TokenType(Enum):
    Number = 0
    String = 1
    Keyword = 3
    Other = 4


class Token:
    id: int
    value: str
    type: TokenType

    def __init__(self, id_, value_, type_):
        self.id = id_
        self.value = value_
        self.type = type_

    def __str__(self):
        return f"id:{self.id}, val:'{self.value}', type:'{self.type}'"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id and self.value == other.value and self.type == other.type


class Scanner:
    operators: list = ['(', ')', '+', '-', '*', '/']
    keywords: list = ['for', 'while', 'if', 'return']
    identifiers: list = ['int', 'float', 'char', 'double', 'void', 'bool', 'string']

    def scanner(self, input_string: str) -> list[Token]:
        outcome = []
        next_id = 0
        line = 1
        position = 0

        while len(input_string) > 0:
            while len(input_string) > 0 and input_string[0] in [' ', '\t']:
                if input_string[0] == '\t':
                    position += 4
                else:
                    position += 1
            if input_string == '\n':
                break
            token = self.scan(input_string, next_id, line, position)
            position += len(token.value)
            outcome.append(token)
            input_string = input_string[len(token.value):]
            next_id += 1
        return outcome

    def scan(self, input_string: str, next_id: int, line: int, position: int) -> Token:
        if input_string[0] in self.operators:
            return Token(next_id, input_string[0], TokenType.Other)
        if input_string[0].isnumeric():
            var = ''
            while len(input_string) > 0 and input_string[0].isnumeric():
                var += input_string[0]
                input_string = input_string[1:]
            return Token(next_id, var, TokenType.Number)
        if input_string[0].isalpha():
            var = ''
            while len(input_string) > 0 and input_string[0].isalnum():
                var += input_string[0]
                input_string = input_string[1:]
            if var in self.keywords:
                return Token(next_id, var, TokenType.Keyword)
            if var in self.identifiers:
                return Token(next_id, var, TokenType.Other)
            return Token(next_id, var, TokenType.Other)
        else:
            raise Exception(f'Unexpected character: {input_string[0]} at position {position} on line {line}')