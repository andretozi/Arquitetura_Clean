# Atividade Pratica 4 - Clean Architecture e Inversao de Dependencia

Este repositorio contem a versao final do MVP da livraria virtual, desenvolvido para a disciplina de Engenharia de Software. O projeto consolida a evolucao arquitetural do software, passando de um modelo Multicamadas para a **Clean Architecture**, com foco na separacao estrita de conceitos e na aplicacao do Principio da Inversao de Dependencia (DIP - Dependency Inversion Principle).

## 1. Clean Architecture e DIP

A Clean Architecture visa manter o nucleo da aplicacao (regras de negocio e casos de uso) totalmente isolado de detalhes externos, como banco de dados, frameworks web (Flask) ou interfaces de usuario. 

Nesta implementacao, o foco principal foi a aplicacao do **DIP**:
* **Domain (Dominio):** Criamos uma interface abstrata (`ICarrinhoRepository`) que define o contrato do que o repositorio deve fazer (adicionar, remover, obter_todos, esvaziar), sem implementar como isso e feito.
* **Use Cases (Casos de Uso):** O `CarrinhoUseCase` dita as acoes do usuario. Ele depende exclusivamente da interface abstrata do dominio, sendo completamente cego em relacao a existencia de um arquivo TXT ou de um banco SQL.
* **Infrastructure (Infraestrutura):** A classe `CarrinhoTXTRepository` implementa os metodos exigidos pela interface, lidando com a complexidade de baixo nivel (abrir, ler, escrever e apagar dados do arquivo `carrinho.txt`).
* A injecao de dependencia ocorre no Controller, unindo a infraestrutura real ao caso de uso.

## 2. Persistencia de Dados (TXT)

A fim de simular um ambiente real onde os dados do usuario nao sao perdidos ao fechar a aplicacao, a camada de infraestrutura gerencia um arquivo fisico (`carrinho.txt`). Sempre que o usuario adiciona ou remove um item, o arquivo e lido e reescrito em tempo real, garantindo a persistencia da sessao.

## 3. Funcionalidades do MVP Final

O ciclo completo da jornada do cliente foi fechado com a adicao e consolidacao das seguintes features:

* **Filtro Rapido por Categoria:** Botoes de acesso rapido na interface principal (View) que repassam parametros ao Controller para filtrar a base de dados em memoria por categorias especificas (ex: Fantasia, Romance, Terror).
* **Gerenciamento de Carrinho:** O usuario pode nao apenas adicionar itens ao carrinho, mas tambem remove-los individualmente. O Controller aciona o Use Case que, por sua vez, atualiza a persistencia no TXT.
* **Finalizar Compra (Checkout):** O fluxo de compra nao e mais uma simulacao de interface. O usuario e direcionado para uma rota especifica de checkout, onde pode selecionar o metodo de pagamento (Cartao, Pix ou Boleto).
* **Confirmacao e Sucesso:** Apos submeter o formulario de pagamento, o sistema encaminha o usuario para uma tela de sucesso, apresentando o metodo escolhido. Em background, o caso de uso aciona a exclusao completa dos dados do arquivo TXT, liberando o carrinho para a proxima sessao.

## 4. Estrutura de Pastas

A organizacao do projeto segue estritamente a separacao por dominios e responsabilidades da Clean Architecture:

```text
Arquitetura_Clean/
|
|-- domain/                  # Nucleo estavel e interfaces abstratas
|   └── interfaces.py
|
|-- use_cases/               # Regras de orquestracao da aplicacao
|   └── carrinho_use_case.py
|
|-- infrastructure/          # Detalhes tecnicos e conexoes externas (BD/TXT)
|   |-- biblioteca_db.py
|   └── txt_repository.py
|
|-- presentation/            # Entrega de dados e interacao com usuario
|   |-- controllers/
|   |   └── livro_controller.py
|   └── views/
|       |-- index.html
|       |-- carrinho.html
|       |-- checkout.html
|       └── sucesso.html
|
|-- app.py                   # Ponto de entrada e injecao de dependencias

```

<img width="555" height="546" alt="image" src="https://github.com/user-attachments/assets/b4f79848-12b0-4b6e-8da3-dcdaf9fb9300" /></br>

## FRONTEND : 

<img width="1859" height="903" alt="image" src="https://github.com/user-attachments/assets/9b2a4ab4-a6dd-4ba8-8454-83685018c096" />/br>

<img width="1872" height="862" alt="image" src="https://github.com/user-attachments/assets/89745d4a-f118-4e02-9055-5f21e63bfb27" />/br>

<img width="1894" height="884" alt="image" src="https://github.com/user-attachments/assets/2f54cbc4-762f-41b3-a39c-b55dd7aeb4c1" />/br>

<img width="1337" height="718" alt="image" src="https://github.com/user-attachments/assets/e9b3fd64-abd4-4a5e-a4f4-368d02aac04f" />/br>



