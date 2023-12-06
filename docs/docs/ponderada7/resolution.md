---
sidebar_position: 4
---

# Rede Neural Convolucional

Os perceptrons são um conceito fundamental no campo da inteligência artificial, representando um dos primeiros modelos de neurônios artificiais. Desenvolvidos por Frank Rosenblatt nas décadas de 1950 e 1960, os perceptrons foram inspirados nos trabalhos anteriores de Warren McCulloch e Walter Pitts. Eles servem como a base para a compreensão de estruturas mais complexas em redes neurais modernas.

### Objetivo da Entrega: 
Nesta ponderada, desenvolvemos uma rede neural convolucional dedicada à classificação de números com base no conjunto de dados MNIST.

### Repositório de Resolução do Projeto

[✔] [Ponderada 6](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada6)
[✔] [Colab de Desenvolvimento](https://colab.research.google.com/drive/1nVEpS7OEp57fYOMd0OEcgT7SDMr2mtk3?usp=sharing)


## Etapas Realizadas:
1. Carregamento do Conjunto de Dados MNIST: O conjunto de dados MNIST foi carregado para treinar e testar a rede neural.

2. Divisão dos Dados de Treino e Teste: Os dados de entrada e saída foram divididos em conjuntos de treino e teste.

3. Criação do Modelo Sequencial: Um modelo sequencial foi criado para facilitar a configuração da arquitetura da rede.

4. Adição da Camada de Entrada: Uma camada de entrada foi adicionada para receber os dados.

5. Camadas Densas com ReLU: Foram adicionadas camadas densas com 128 neurônios cada, utilizando a função de ativação ReLU.

6. Camada de Saída com Softmax: A camada de saída foi configurada com 10 neurônios e a função de ativação softmax.

7. Compilação do Modelo: O modelo foi compilado com parâmetros escolhidos para otimização, função de perda e métricas.

8. Treinamento do Modelo: O treinamento foi realizado ao longo de 3 épocas, sendo suficiente para alcançar uma acurácia superior a 95%.

9. Avaliação do Modelo: Foram calculados os valores de perda e acurácia para avaliar o desempenho da rede neural.


###  Modo de Execução 

#### Criação de arquivos e pastas: 

Inicialmente basta acessar o Colab do projeto (ou executar localmente com um Jupyter, por exemplo):

```
git clone https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias.git
```

Para verificar a eficácia do modelo, temos: 

```
prediction = classifier.predict([x_test[0]])

```
Para melhor visualização:

```
import numpy as np

print(np.argmax(prediction))
```

### Demonstração: 
A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/pGI2T6ImqJo?si=q9XMoqwusKyraCSP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
