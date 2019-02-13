import random
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

class KNN():
    #inicia o objeto com os parâmetros escolhidos
    def __init__(self, parametros=None):
        self.parametros = {}
        self.entrada = parametros['entrada']
        self.resultado = parametros['resultado']
        if parametros != None:
            for parametro in parametros:
                self.parametros[parametro] = random.choice(parametros[parametro])

    #função de fitness, usando a acurácia
    def fitness(self):
        entrada_treinamento, entrada_teste, resultado_treinamento, resultado_teste = train_test_split(self.entrada, self.resultado, test_size=self.parametros['test_size'], random_state=4)
        instanciaKNN = KNeighborsClassifier(n_neighbors = self.parametros['n_neighbors'],
                                            weights = self.parametros['weights'],
                                            algorithm = self.parametros['algorithm'],
                                            leaf_size = self.parametros['leaf_size']
                                            )
        instanciaKNN.fit(entrada_treinamento, resultado_treinamento)
        resultadosKNN = instanciaKNN.predict(entrada_teste)
        score = metrics.accuracy_score(resultado_teste, resultadosKNN)
        return score

    #função que o objeto usa para se printar
    def printSelf(self):
        for parametro in self.parametros:
            print("        Parametro: " + str(parametro) + ' -- ' + str(self.parametros[parametro]))
