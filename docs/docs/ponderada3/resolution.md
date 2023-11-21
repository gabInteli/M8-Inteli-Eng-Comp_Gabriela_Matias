---
sidebar_position: 3
---

# Navegação por Meio de Chatbot Simples

## Sistema de launch files para navegação com interação via terminal 
O objetivo desse repositório demonstrar o desenvolvimento e a execução de um chatbot utilizando expressões regulares para se movimentar até pontos específicos. 

### Repositório de Resolução do Projeto

[✔] [Ponderada 3](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada3)

###  Modo de Execução 

Caso o pacote seja baixado diretamente do repositório, ela já estará buildado e pronto para execução, **para evitar erros, recomendamos adicionar o source do pacote ao seu interpretador de terminal preferido**(**.bashrc**, **.zshrc**, etc.). 

Caso opte por não realizar isso, você terá que digitar o seguinte source em seu terminal dentro da pasta do pacote na hora de executar:
```
source install/local_setup.bash #Caso você tenha zsh, troque o bash por .zsh
```

Após isso, é necessário inicialmente acionar o pacote de execução da navegação no mapa definido. 
Já explicado anteriormente na [Ponderada 2](https://gabinteli.github.io/M8-Inteli-Eng-Comp_Gabriela_Matias/docs/ponderada2/resolution). 


### Demonstração: 

Para poder executar os pacotes corretamente, basta seguir a ordem: 
1. Navegação: 
    - [Repositório](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada2/launch)
    - Arquivo: "navigation.launch.py"
2. Entrada de Pontos:
    - [Repositório](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada3/chatbot)
    - Dir: '/chatbot'
    - Execução: 
    ```
    ros2 run chatbot controller
    ```

A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/wWz3obQjfUM?si=2cKyr9Lhowud7-lA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>