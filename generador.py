class Generador:

    generador = None

    def getInstance(self):
        if Generador.generador is None:
            Generador.generador = Generador()
        return Generador.generador
        
    def addExpresion(self, n1, n2, tipo):
        return f'({n1} {tipo} {n2})'
    
    def addRaiz(self, n1, n2):
        return f'{n1}^(1/{n2})'

    def addReverse(self, n1):
        return f'( {n1}^(-1) )'