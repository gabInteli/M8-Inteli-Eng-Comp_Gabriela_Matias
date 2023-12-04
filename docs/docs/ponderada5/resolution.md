---
sidebar_position: 4
---

# ChatBot com LLM e Contexto

## 
Utilizando um LLM (local ou API externa), criar um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema ainda deve ser capaz de contextualizar suas respostas a partir do seguinte documento:

[Workshop rules and safety considerations](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety)

### Repositório de Resolução do Projeto

[✔] [Ponderada 4](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada4)


###  Modo de Execução 

#### 1. Criação de arquivos e pastas: 

Inicialmente basta clonar o repositório contendo o Modelfile e o Chat de interação com a interface: 

```
git clone https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias.git
```

Em seguida, acessar a pasta que contem os arquivos de execução da ponderada: 

```
cd src/ponderada4
```

#### 2. Instalação de Dependências: 
Para rodar o projeto é necessário instalar as dependências necessárias por meio do comando:

```
python3 -m pip install -r requirements.txt
```

#### 3. Criando o Modelo 
Para usar o Modelfile de referência para a criação do nosso modelo que segue o seguinte promp de instrução: 
```
From now on, you are Grace Hopper, a safety professional in the engineering field, you understand equipment, tools and PPE for the areas of Civil, Mechanical, Mechatronics, Electrical, Electronic and Computer Engineering. Furthermore, he likes to answer things in a humorous way, so at the end of his answers he always includes a funny joke.
``` 

Basta rodar o seguinte comando:

```
ollama create safety_guard -f Modelfile
```

#### 4. Iniciando o Servidor da Interface

Por fim, basta iniciar o nosso servidor que aciona o gradio: 

```
python3 main.py
```
E acessar o endereço: http://127.0.0.1:7860/

### Demonstração: 

A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/1wuUclnifS8?si=6jf9sG6-DUH_xmHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>