Jogo 2sem Python

Instale o Python 3, o ambiente de desenvolvimento (recomendado PyCharm) e instale o pacote PyGame para Python3.
---------------------------------------------
Linux:

> Instale PyGame no Python 3:
Para instalar PyGame para Python 3.X no Ubuntu 19.04 e acima, abra o terminal e digite:
  sudo apt install python3-pygame

> Para instalar PyGame no Ubuntu 18.10 abra o terminal e digite:
  sudo nano /etc/apt/sources.list

adicione a seguinte linha:
  deb http://archive.ubuntu.com/ubuntu/ cosmic-proposed universe # for 19.04 replace cosmic with disco 

Salve sources.list com a combinacao de teclas Ctrl+O e pressione Enter, saia com Ctrl+X

Faca update da lista de softwares disponiveis e instale o python3-pygame:
  sudo apt update
  sudo apt install python3-pygame
  
>Etapa adicional: procure na linha 114 aonde um comentario indica a fonte usada no linux.
substitua a linha comentada de 115 para 116.
----------------------------------------------
Windows: Passe o mouse por cima da primeira linha em import pygame e faca o download do pacote Pygame.
----------------------------------------------

Rode.
