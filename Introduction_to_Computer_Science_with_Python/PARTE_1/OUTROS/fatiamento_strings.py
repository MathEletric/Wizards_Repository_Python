frase = 'Hello, World'
indices = "\t".join(str(i) for i in range(len(frase)))
print("String original:\t" + "\t".join(frase))
print("Índices:\t\t" + indices)

print(f" FRASE: {frase} -> Método .count(' '): {frase.count(' ')}")
print(f" FRASE: {frase} -> Método .count('h'): {frase.count('h')}", end="\n\n")

print(f" FRASE: {frase} -> Método .upper(): {frase.upper()}", end="\n\n")

print(f" FRASE: {frase} -> Método .lower(): {frase.lower()}", end="\n\n")


print(f" FRASE: {frase} -> Método .find(' '): {frase.find(' ')}")
print(f" FRASE: {frase} -> Método .find('w'): {frase.find('w')}", end="\n\n")

print(f" FRASE: {frase} -> Método .capitalize(): {frase.capitalize()}", end='\n\n')

print(f" FRASE: {frase} -> Método .title(): {frase.title()}", end='\n\n')

print(f"'Hello' in frase: {'Hello' in frase}", end="\n\n")


frase = '    Hello, World  '
def tabular_string(string, spacing=2):
    return ' ' * spacing + (' ' * spacing).join(string)
indices = ' '.join(f"{i}" for i in range(len(frase)))
indices_alinhados = '  '.join(f"{i}" for i in range(len(frase)))
print("String original:" + tabular_string(frase))
print("Índices:       " + indices_alinhados, end='\n\n')

print(f" FRASE: {frase} -> Método .strip(): {frase.strip()}")
print("(Existe o .rstrip() e lstrip)", end='\n\n')

print(f" FRASE: {frase} -> Método .split(): {frase.split()}")
