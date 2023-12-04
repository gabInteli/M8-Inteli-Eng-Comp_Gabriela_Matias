---
sidebar_position: 4
---

# Perceptron

Os perceptrons são um conceito fundamental no campo da inteligência artificial, representando um dos primeiros modelos de neurônios artificiais. Desenvolvidos por Frank Rosenblatt nas décadas de 1950 e 1960, os perceptrons foram inspirados nos trabalhos anteriores de Warren McCulloch e Walter Pitts. Eles servem como a base para a compreensão de estruturas mais complexas em redes neurais modernas.

## Criação de um Perceptron Simples 
Suponha que o fim de semana esteja chegando e você tenha ouvido falar que vai acontecer um festival de queijos na sua cidade. Você gosta de queijo e está tentando decidir se vai ou não ao festival. Você pode tomar sua decisão ponderando três fatores:

1. O tempo está bom?
2. Seu namorado ou namorada quer te acompanhar?
3. O festival é próximo ao transporte público? (Você não possui carro).

Podemos representar esses três fatores pelas variáveis ​​binárias correspondentes x1,x2 e x3. Por exemplo, teríamos x1=1 se o tempo estiver bom e x1=0 se o tempo estiver ruim. Da mesma forma, x2=1 se o seu namorado ou namorada quiser ir, e x2=0 se não. E da mesma forma novamente para x3 e transporte público.


## Implementação de Perceptron em Portas Lógicas 
O objetivo da atividade é a implementação de um perceptron capaz de ser treinado para reproduzir o comportamento das seguintes portas lógicas:
1. AND
2. OR
3. NAND
4. XOR


### Repositório de Resolução do Projeto

[✔] [Ponderada 6](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada6)


###  Modo de Execução 

#### Criação de arquivos e pastas: 

Inicialmente basta clonar o repositório contendo o perceptron desenvolvido: 

```
git clone https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias.git
```

Em seguida, acessar a pasta que contem os arquivos de execução da ponderada: 

```
cd src/ponderada6
```

### Execução do Arquivo e Teste: 

#### Perceptron Simples: 
Para executar o arquivo basta abrir um terminal e executar o seguinte comando: 
```
python3 main.py
```

#### Perceptron Portas Lógicas
Para executar o arquivo basta abrir um terminal e executar o seguinte comando: 
```
python3 perceptron.py
```

### Demonstração: 
A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/1wuUclnifS8?si=6jf9sG6-DUH_xmHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Análise e Conclusão:
A estrutura do nosso perceptron é definida por meio de 3 funções principais e alguns parâmetros relevantes que são definidos no nosso método principal: 

1. Método Principal: 
- Definição de parâmetros do perceptron, como taxa de aprendizado (learning_rate), número de iterações de treinamento (n_iterations), e o limiar de ativação (threshold). Também inicializa os pesos e o viés.

2. Método activation_function:
- Implementa a função de ativação degrau. Retorna 1 se a entrada x for maior ou igual ao limiar (threshold), caso contrário, retorna 0.

3. Método predict:
- Realiza a previsão do perceptron para um conjunto de entradas inputs.

4. Método train:
- Realiza o treinamento do perceptron. Itera sobre o conjunto de dados X e rótulos y por um número especificado de iterações (n_iterations).

### Objetivo da Atividade: Porta XOR

A estrutura basica de um perceptron pensando em expressar a porta XOR esta aplicada. Porém devido a essa porta não se comportar como as portas básicas não é possível encontrar os valores corretos de peso e bias para seu funcionamento. O

Isso ocorre pois só usamos um perceptron, o que serve para resolvermos problemas lineares, enquanto o XOR, é um problema não linear. Para funcionar, precisariamos criar um segundo perceptron(nesse caso, uma camada oculta entre o input e o resultado) e trocar a função linear por uma função sigmoide.