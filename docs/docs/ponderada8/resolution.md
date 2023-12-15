---
sidebar_position: 4
---

# Tradutor Utilizando STT-TTS

## STT
STT é uma tecnologia que converte fala humana em texto escrito. Também é conhecida como reconhecimento de fala. Os sistemas STT são frequentemente utilizados em aplicativos de transcrição, assistentes virtuais, legendagem automática de vídeos, entre outros. Eles processam os sinais de áudio da fala e tentam extrair o conteúdo textual correspondente.

# TTS
TTS é uma tecnologia que converte texto em discurso audível. Em outras palavras, transforma palavras escritas em uma representação de áudio da fala. Os sistemas TTS são usados em uma variedade de aplicações, como assistentes virtuais, leitores de tela, sistemas de navegação por voz e muito mais. Esses sistemas podem gerar uma voz sintética que soa o mais natural possível.

### Objetivo da Entrega: 
Nesta ponderada utilizaremos reconhecimento de Fala (STT) e Síntese de Fala (TTS) da OpenAI para realizar as seguintes etapas: transcrição de um áudio, tradução para o inglês e subsequente reprodução do conteúdo.
Estou te ouvindo !


### Repositório de Resolução do Projeto

[✔] [Ponderada 8](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada8)


###  Modo de Execução 

1. Instalação de Dependências
```
pip install -r requirements.txt
``` 
2. Criação de Variáveis de Ambiente:
```
touch .env
```
Como estamos utilizando uma biblioteca da OpenAI, se torna necessário adicionar a API_KEY que é a chave de acesso para a API da OpenAI em nossa env, como uma variável de ambiente. Portanto adicione o valor para a seguinte variável: 

```
OPENAI_API_KEY= (insira o valor aqui) 
```

3. Executando o Tradutor: 
Para iniciar, basta executar o seguinte comando: 
```
python3 main.py
```
Ele apresentará a seguinte mensagem: 
```
Estou iniciando sua gravação, então cuidadi, estou te ouvindo !
```

Após finalizar a gravação ele apresentará a seguinte mensagem: 
```
Fim da Gravação, ja pode fofocar sem perigo !
```

4. Acessando as Informações: 
Ao final da gravação são gerados dois arquivos na pasta principal do projeto: 
- input.mp3 = Arquivo gravado 
- output.mp3 = Arquivo de Tradução

### Demonstração: 
A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/_VuiBnVMTho?si=5_-m0qxaE2eaWZtO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>