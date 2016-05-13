### Bem vindo ao projeto *Cleaner Pool*

## O Projeto
O projeto visa o desenvolvimento de um sistema embarcado que forneça as
capacidades necessárias para que o *Clean Pool Robot* faça o que se propõe. Dentre as
funcionalidades a serem disponibilizadas estão: movimentação do robô, leitura
do *output* dos sensores, tratamento de obstáculos e correção do percurso.

O projeto está dividido em três repositórios: o [_Cleaner Pool Environment_][env], [_Cleaner Pool Source_][src] e o [_Cleaner Pool Arduino_][ard].

Toda a documentação do _Cleaner Pool_ está na wiki do _Cleaner Pool Environment_, pois optou-se por centralizar as informações em um único repositório.

<dl>
  <dt><i>Cleaner Pool Environment</i></dt>
  <dd>
    Esse subprojeto tem por intuito produzir ferramentas que facilitem o levantamento do ambiente de desenvolvimento. Este consiste de uma VM (<i>Virtual Machine</i>) já configurada e pronta para uso no desenvolvimento do código-fonte. Para isso, faz-se uso de <i>scripts</i> para a automatização da instalação e <i>download</i> de ferramentas para a execução da VM.
  <dd>

  <dt><i>Cleaner Pool Source</i></dt>
  <dd>
    Esse subprojeto mantém o código-fonte do <i>Cleaner Pool</i>. É escrito em C/C++, fazendo-se uso de bibliotecas externas que auxiliam no desenvolvimento, entre elas, a bcm2835.h, para ter-se acesso a GPIO e outros recursos da <i>Raspberry Pi</i>.
  </dd>

 <dt><i>Cleaner Pool Arduino</i></dt>
  <dd>
    Esse subprojeto mantém o código-fonte de operações realizados no Arduino necessárias para o <i>Cleaner Pool</i> . É escrito em C/C++ com algumas modificações necessárias para o desenvolvimento de projetos no Arduino</i>.
  </dd>
<
</dl>

***

## Licença
O projeto está sob a licença GPLv3, como afirma o [documento][license].

## Como Contribuir
Para entender como contribuir com o projeto e o que é necessário para isso,
leia o seguinte [documento][how-contribute].

## Contribuidores
A listagem dos contribuidores do projeto encontra-se aqui.

[license]: https://github.com/CleanPoolRobot/cleaner-pool-src/blob/master/LICENSE.txt
[how-contribute]: https://github.com/CleanPoolRobot/cleaner-pool-env/wiki/Como-Contribuir
[env]: https://github.com/CleanPoolRobot/cleaner-pool-env
[src]: https://github.com/CleanPoolRobot/cleaner-pool-src
[ard]: https://github.com/CleanPoolRobot/cleaner-pool-arduino
