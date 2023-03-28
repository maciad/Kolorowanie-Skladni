from enum import Enum


class TokenType(Enum):
    Number = 0
    String = 1
    Identifier = 2
    Keyword = 3
    Operator = 4
    Other = 5

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Token:
    id: int
    value: str
    type: TokenType

    def __init__(self, id_: int, value_: str, type_: TokenType):
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
    operators = ['(', ')', '+', '-', '*', '/', '=', '<', '>']
    keywords = ['for', 'while', 'if', 'return']
    identifiers = ['int', 'float', 'char', 'double', 'void', 'bool', 'string']
    next_id = 1

    def scanner(self, input_string: str, line: int ) -> list[Token]:
        outcome = []
        position = 1

        while len(input_string) > 0:
            while len(input_string) > 0 and input_string[0] == ' ':
                position += 1
                input_string = input_string[1:]
            token = self.scan(input_string, self.next_id, line, position)
            position += len(token.value)
            outcome.append(token)
            input_string = input_string[len(token.value):]
            self.next_id += 1
        return outcome

    def scan(self, input_string: str, next_id: int, line: int, position: int) -> Token:
        if input_string[0] == '"':
            var = '"'
            input_string = input_string[1:]
            while len(input_string) > 0:
                if input_string[0] == '"':
                    break
                var += input_string[0]
                input_string = input_string[1:]
            if len(input_string) == 0:
                raise Exception(f'Unexpected end of line at position {position} on line {line}')
            var += '"'
            return Token(next_id, var, TokenType.String)
        if input_string[0] in self.operators:
            return Token(next_id, input_string[0], TokenType.Operator)
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
                return Token(next_id, var, TokenType.Identifier)
            return Token(next_id, var, TokenType.Other)
        else:
            raise Exception(f'Unexpected character: {input_string[0]} at position {position} on line {line}')
