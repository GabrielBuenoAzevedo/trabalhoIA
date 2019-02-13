#biblioteca python
import random

class AlgoritmoGenetico():
    #inicia o objeto com os parâmetros escolhidos
    def __init__(self, parametros_algoritmo, chance_mutacao, qntd_mantida, chance_manter, algoritmo_aplicado):
        self.parametros_algoritmo = parametros_algoritmo
        self.chance_mutacao = chance_mutacao
        self.qntd_mantida = qntd_mantida
        self.algoritmo_aplicado = algoritmo_aplicado
        self.chance_manter = chance_manter

    #cria a populacao inicial com tamanho tamanho_populacao
    def criaPopulacao(self, tamanho_populacao):
        populacao = []
        for individuo in range(0, tamanho_populacao):
            novoIndividuo = self.algoritmo_aplicado(self.parametros_algoritmo)
            populacao.append(novoIndividuo)
        qualidadePopulacao = [ (individuo.fitness() , individuo) for individuo in populacao ]
        populacaoOrdenada = [ x[1] for x in sorted(qualidadePopulacao, key=lambda x: x[0], reverse=True) ]
        return populacaoOrdenada

    #reproducao do pai e da mae para gerar o filho, com aleatoriedade entre os dados dos pais
    def fazFilho(self, mae, pai):
        filho = self.algoritmo_aplicado(self.parametros_algoritmo)

        for parametro in self.parametros_algoritmo:
            filho.parametros[parametro] = random.choice([ mae.parametros[parametro], pai.parametros[parametro] ])
        if self.chance_mutacao > random.random():
            filho = self.mutacao(filho)
        return filho

    #mutacao de um individuo, mudando algum dos seus parâmetros/genes
    def mutacao(self, individuo):
        geneMutado = random.choice( list(self.parametros_algoritmo.keys()) )
        individuo.parametros[geneMutado] = random.choice(self.parametros_algoritmo[geneMutado])
        return individuo

    #verifica a fitness média dos individuos da população
    def mediaPopulacao(self, populacao ):
        mediaPopulacao = 0
        for individuo in populacao:
            mediaPopulacao = mediaPopulacao + individuo.fitness()
        mediaPopulacao =  float( mediaPopulacao/len(populacao) )
        return mediaPopulacao

    #evolue a geração, criando uma população provavelmente mais adaptada
    def evoluiGeracao(self, populacao):
        qntdPopulacaoMantida = int(self.qntd_mantida * len(populacao) )
        novaPopulacao = populacao[:qntdPopulacaoMantida]

        #manter alguns individuos aleatórios
        for individuo in populacao[qntdPopulacaoMantida:]:
            if self.chance_manter > random.random():
                novaPopulacao.append(individuo)

        #talvez mutar os individuos pertencentes à geração anterior
        for individuo in novaPopulacao:
            if self.chance_mutacao > random.random():
                individuo = self.mutacao(individuo)
        qntdFilhos = len(populacao) - len(novaPopulacao)

        #decide os filhos
        filhos = []
        while len(filhos) < qntdFilhos:
            pai = random.randint(0, len(novaPopulacao) - 1 )
            mae = random.randint(0, len(novaPopulacao) - 1 )
            if pai != mae:
                filhos.append( self.fazFilho(novaPopulacao[mae], novaPopulacao[pai]) )
        novaPopulacao.extend(filhos)

        #retorna a nova população ordenada pela qualidade dos individuos
        qualidadePopulacao = [ (individuo.fitness() , individuo) for individuo in novaPopulacao ]
        populacaoOrdenada = [ x[1] for x in sorted(qualidadePopulacao, key=lambda x: x[0], reverse=True) ]
        return populacaoOrdenada
