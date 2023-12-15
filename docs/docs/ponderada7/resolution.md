---
sidebar_position: 4
---

# Rede Neural Convolucional

Uma Rede Neural Convolucional (CNN), também conhecida como ConvNet, é um tipo de modelo de aprendizado profundo projetado especialmente para processar dados em grade, como imagens. Essa arquitetura é amplamente utilizada em tarefas de visão computacional, como reconhecimento de imagem e classificação.

A estrutura fundamental de uma CNN consiste em camadas de convolução, camadas de pooling e camadas totalmente conectadas. 

### Objetivo da Entrega: 
Nesta ponderada, desenvolvemos uma rede neural convolucional dedicada à classificação de números com base no conjunto de dados MNIST.

### Repositório de Resolução do Projeto

[✔] [Ponderada 7](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada7)
[✔] [Colab de Desenvolvimento](https://colab.research.google.com/drive/1nVEpS7OEp57fYOMd0OEcgT7SDMr2mtk3?usp=sharing)


## Etapas Realizadas:

1. Carregamento dos Dados MNIST:
Os dados do MNIST foram carregados para treinar e testar a rede neural.

2. Divisão em Conjuntos de Treino e Teste:
Os dados de entrada e saída foram divididos em conjuntos de treino e teste.

3. Criação do Modelo Sequencial:
Um modelo sequencial foi criado para definir a arquitetura da rede de forma simples.

4. Configuração da Camada de Entrada:
Foi adicionada uma camada de entrada para receber os dados.

5. Camadas Densas e de Saída:
Adicionaram-se camadas densas com 128 neurônios e ativação ReLU. A camada de saída possui 10 neurônios com ativação softmax.

6. Compilação e Treinamento do Modelo:
O modelo foi compilado com parâmetros otimizados, incluindo função de perda e métricas. O treinamento ocorreu por 3 épocas, resultando em acurácia superior a 95%.

7. Avaliação do Desempenho do Modelo:
Os valores de perda e acurácia foram calculados para avaliar o desempenho da rede neural.

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
<iframe width="560" height="315" src="https://www.youtube.com/embed/-nO_kh_DhNs?si=VKjfvHSlwi1ECGHW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>