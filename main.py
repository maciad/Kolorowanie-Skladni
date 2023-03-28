import Scanner

if __name__ == '__main__':

    word_colors = {
        'number': 'blue',
        'string': 'green',
        'keyword': 'red',
        'operator': 'orange',
        'identifier': 'pink',
        'other': 'black'
    }

    scanner = Scanner.Scanner()

    with open('asd.txt', 'r') as fin, open('out.html', 'w') as out:
        out.write('<html><body>\n')
        for i, line in enumerate(fin):
            tokens = scanner.scanner(line.strip(), i + 1)
            for token in tokens:
                color = word_colors['other']
                if token.type == Scanner.TokenType.Number:
                    color = word_colors['number']
                elif token.type == Scanner.TokenType.Operator:
                    color = word_colors['operator']
                elif token.type == Scanner.TokenType.String:
                    color = word_colors['string']
                elif token.type == Scanner.TokenType.Keyword:
                    color = word_colors['keyword']
                elif token.type == Scanner.TokenType.Identifier:
                    color = word_colors['identifier']
                out.write(f'<span style="color: {color}">{token.value}</span> ')
            out.write('<br>\n')
        out.write('</body></html>')
