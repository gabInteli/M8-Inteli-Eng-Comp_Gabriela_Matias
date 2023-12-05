---
sidebar_position: 4
---

# ChatBot com LLM e Contexto

## 
Utilizando um LLM (local ou API externa), criar um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema deve contar com uma interface gráfica e responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema ainda deve ser capaz de contextualizar suas respostas a partir do seguinte documento:

[Workshop rules and safety considerations](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety)

Para utilizar o documento foi desenvolvido um arquivo: 
```
safety_rules.txt
```


### Repositório de Resolução do Projeto

[✔] [Ponderada 5](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada5)


###  Modo de Execução 

#### 1. Criação de arquivos e pastas: 

Inicialmente basta clonar o repositório contendo o Chat de interação com a interface: 

```
git clone https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias.git
```

Em seguida, acessar a pasta que contem os arquivos de execução da ponderada: 

```
cd src/ponderada5
```

#### 2. Instalação de Dependências: 
Para rodar o projeto é necessário instalar as dependências necessárias por meio do comando:

```
python3 -m pip install -r requirements.txt
```

#### 3. Teste - Chatbot Simples  
Inicialmente precisamos carregar o modelo a ser utilizado, para o nosso caso, Ollama Mistral, por meio do seguinte comando: 

```
ollama run mistral
```

Em seguida vamos executar um chatbot simples que utiliza de um contexto pré definido para buscar a resposta de uma pergunta especifica: 

```
python3 gradio_teste.py
```

Esse chat é construido com uma pergunta ja definida com base em um contexto. Que é: 
"Who is allowed to operate a lathe? What protective gear should be used to do it?" 

#### 4. Iniciando o Servidor da Interface

Por fim, vamos iniciar nosso chat completo que utiliza do contexto para responder as perfunas fornecidas por meio de uma interface, nossa interface é acionada por meio do nosso servidor que aciona o gradio: 

```
python3 chatbot.py
```
E acessar o endereço: http://127.0.0.1:7860/

### Demonstração: 

A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/1wuUclnifS8?si=6jf9sG6-DUH_xmHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>