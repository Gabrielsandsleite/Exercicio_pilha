class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0


def reverter_string(texto):
    pilha = Pilha()
    
    
    for caractere in texto:
        pilha.push(caractere)

   
    resultado = ""
    while not pilha.esta_vazia():
        resultado += pilha.pop()
    
    return resultado



if __name__ == '__main__':
    exemplos = [
        "Python",
        "12345",
        "Olá, mundo!",
        "A man a plan a canal Panama"
    ]

    for s in exemplos:
        print(f"Original: {s} | Reversa: {reverter_string(s)}")
