#bibliotecas feitas por mim
from algoritmoGenetico import AlgoritmoGenetico
from teste import testeAdicao
from knn import KNN

#bibliotecas do sklearn e python
from sklearn.datasets import load_iris
import numpy as np

def main():
    #carrega o dataset iris, de classificação de flores por tamanho de sépala e de pétala
    dataset = load_iris()

    #divisão do dataset entre entrada e resultado esperado
    entrada = dataset.data
    resultado = dataset.target

    #definição dos parametros que o algoritmo genético receberá para decidir no KNN
    parametros = {
        'n_neighbors' : range(1,30),
        'weights' : ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree'],
        'leaf_size' : range(25,75),
        'test_size' : np.arange(0.1,0.52,0.02),
        'entrada': entrada,
        'resultado': resultado,
    }

    #criação do algoritmo genético e da população inicial
    tamanho_populacao = 100
    num_geracoes = 50
    algoritmo = AlgoritmoGenetico(parametros, 0.2, 0.4, 0.1, KNN)
    populacao = algoritmo.criaPopulacao(tamanho_populacao)

    #evoluções/gerações do knn
    for i in range(0, num_geracoes):
        print("Geração: " + str(i+1))
        print("Fitness: " + str(algoritmo.mediaPopulacao(populacao) ))
        populacao[0].printSelf()
        populacao = algoritmo.evoluiGeracao(populacao)
        print('---------\n')

    #print da população final
    for i in range(0, len(populacao)):
        print('Printando a %d populacao: ', i)
        print(populacao[i].fitness())
        populacao[i].printSelf()

if __name__ == '__main__':
    main()
