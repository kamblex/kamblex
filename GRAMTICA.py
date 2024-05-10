from collections import defaultdict

def derive_string(grammar, start_symbol, string, terminals, non_terminals):
    """
    Deriva la cadena dada utilizando las producciones de la gramática.
    """
    productions = defaultdict(list)

    # Analizar la gramática
    for production in grammar:
        head, body = production.split('->')
        head = head.strip()
        body = body.strip()
        for symbol in body:
            if symbol not in terminals and symbol not in non_terminals:
                raise ValueError(f"Símbolo '{symbol}' no está definido en los conjuntos de terminales y no terminales.")
        productions[head].extend(body.split('|'))

    # Derivar la cadena
    derivation = [start_symbol]
    current_string = start_symbol
    while any(symbol in non_terminals for symbol in current_string):
        for i, symbol in enumerate(current_string):
            if symbol in non_terminals:
                for production in productions[symbol]:
                    new_string = current_string[:i] + production + current_string[i+1:]
                    print(f"{' ⇒ '.join(derivation)} ⇒ {new_string}")
                    derivation.append(new_string)
                    current_string = new_string
                break

    return ' '.join(derivation)

# Ejemplo de uso
terminals = input("Ingrese el conjunto de símbolos terminales separados por comas: ").split(',')
terminals = [symbol.strip() for symbol in terminals]

non_terminals = input("Ingrese el conjunto de símbolos no terminales separados por comas: ").split(',')
non_terminals = [symbol.strip() for symbol in non_terminals]

grammar = []
print("Ingrese las producciones de la gramática (escriba 'fin' para terminar):")
while True:
    production = input()
    if production.lower() == 'fin':
        break
    grammar.append(production)

start_symbol = input("Ingrese el símbolo inicial: ").strip()
string = input("Ingrese la cadena a derivar: ").strip()

print(f"Derivación de la cadena '{string}' según la gramática ingresada:")
derivation = derive_string(grammar, start_symbol, string, terminals, non_terminals)
print(derivation)