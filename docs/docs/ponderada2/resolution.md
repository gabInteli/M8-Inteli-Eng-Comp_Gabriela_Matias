---
sidebar_position: 2
---

# Mapeamento e Navegação com Ros2 e Nav2 - Launch Files

## Sistema de launch files para mapeamento e navegação
O objetivo dessa atividade ponderada é criar e executar um sistema de mapeamento e de navegação no framework ros2 utilizando o sistema de simulação Gazebo.

### Repositório de Resolução do Projeto

[✔] [Ponderada 2](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada2)

###  Modo de Execução 

Caso o pacote seja baixado diretamente do repositório, ela já estará buildado e pronto para execução, **para evitar erros, recomendamos adicionar o source do pacote ao seu interpretador de terminal preferido**(**.bashrc**, **.zshrc**, etc.). 

Caso opte por não realizar isso, você terá que digitar o seguinte source em seu terminal dentro da pasta do pacote na hora de executar:
```
source install/local_setup.bash #Caso você tenha zsh, troque o bash por .zsh
```

Após isso, o pacote estará pronto para uso! 
Com ele, você terá acesso a três nós e a três launch files:

- **Nós**
  - **initial_pose** - Seta a posição inicial do robô.
  - **go_to** - Vai até pontos definidos no RVIz. 

**Para iniciar os nós, é necessário utilizar o seguinte comando:**
```
ros2 run my_package <nome_do_nó>
```

- **Launch Files**
  - **mapping.launch.py** - Inicia o mapeamento utilizando o mapa base do gazebo.
  - **mapping-save.launch.py** - Salva o mapa que foi mapeado e apresentado no RVIz para a pasta atual(do terminal).
  - **navigation.launch.py** - Inicia a navegação no mapa criado a partir do mapeamento no RVIz com pontos já pré-definidos.
 
**Para iniciar os launch files, é necessário utilizar o seguinte comando:**
```
ros2 launch my_package <nome_do_launch_file>
```

(Importante ressaltar que nenhum dos comandos citados vão funcionar caso você não tenha iniciado o pacote com o comando de source)


### Demonstração: 

Para poder executar os pacotes corretamente, basta seguir a ordem: 
1. Mapeamento: 
    - [Repositório](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada1/launch)
    - Arquivo: "mapping.launch.py"
2. Salvamento:
    - [Repositório](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada1/launch)
    - Arquivo: "mapping-save.launch.py"
3. Navegação: 
    - [Repositório](https://github.com/gabInteli/M8-Inteli-Eng-Comp_Gabriela_Matias/tree/main/src/ponderada1/launch)
    - Arquivo: "navigation.launch.py"

A demonstração pode ser verificada no vídeo abaixo:  
<iframe width="560" height="315" src="https://www.youtube.com/embed/cLMVFRKlTdw?si=0Cqt396I1O_f_6Kp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

