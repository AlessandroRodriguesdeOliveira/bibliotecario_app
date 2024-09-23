
class Validacoes:
    def __init__(self):
        pass

    def validar_letras(self, entry):
        if entry.get().isalpha() == False:
            entry.delete(0, 'end')

    def validar_numeros(self, entry):
        if entry.get().isalnum() == False:
            entry.delete(0, 'end')

