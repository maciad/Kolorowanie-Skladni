import Scanner

if __name__ == '__main__':

    word_colors = {
        'number': 'blue',
        'string': 'green',
        'keyword': 'red',
        'other': 'black'
    }

    scanner = Scanner.Scanner()
    line = input("dawaj: ")
    print("asd")
    tokens = scanner.scanner(line)
    for token in tokens:
        print(token)
