import random

class testeAdicao():

    def __init__(self, parametros=None):
        vetorAdicao = {}
        if parametros != None:
            for i in parametros:
                vetorAdicao[i] = random.randint(0, parametros[i])
        self.medidas = vetorAdicao
        self.parametros = parametros

    def fitness(self):
        qualidade = 0
        for i in self.medidas:
            qualidade = qualidade + self.medidas[i]
        return qualidade

    def printSelf(self):
        for parametro in self.medidas:
            print(self.medidas[parametro])
        # print('fitness: ' + str(self.fitness()))
        print('----------------------')
