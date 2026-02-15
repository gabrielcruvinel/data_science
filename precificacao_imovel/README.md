# Precificação de Imoveis
Esse projeto consiste em criar um modelo de precificação de imoveis dado um dataset disponibilizado.

Para utilizar o modelo sem precisar executar o notebook toda vez, foi criado uma API que realiza o deploy do modelo localmente, onde basta seguir os seguintes passos para a utilização da mesma.

Primeiro é necessario instalar as dependencias do projeto, devido o flask utilizar uma versão antiga de uma lib em suas dependencias, realizaremos um downgrade nessa lib nesse projeto, bastando executar a seguinte linha de comando

pip install -r requirements.txt

Após a instalação dos requisitos, rodar o comando:

 python main.py

 Com a API rodando localmente no terminal, utilizar um software como o Postman ou o Insomnia para enviar uma requisição para o endereço
    http://127.0.0.1:5000/submit-data com os parametros do modelo


Exemplo de requisição:
{
	"Qualidade": 6,
	"AnoConstrucao":1976,
	"Banheiros":2,
	"Comodos": 6,
	"Garagem": 2
}

Output:
{
  "Preco_estimado": 163530
}
