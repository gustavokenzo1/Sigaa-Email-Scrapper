# Sigaa E-mail Scrapper

Programa simples feito em Python durante a aula de Cálculo 2 mesmo, que lê todos os e-mails da página de participantes de uma determinada disciplina no Sigaa (já que um amigo meu disse que fazia tudo no CTRL+C CTRL+V um por um, o que demora muito), a fim de facilitar o envio do link do grupo da turma. O programa ignora o e-mail da UnB e do professor (mas é sempre bom checar).

## Requisitos

- Python 3 ou superior
- Beautiful Soup 

Para instalar o Beautiful Soup, utilize o seguinte comando: pip install beautifulsoup4

## Uso

- Baixe o .zip do projeto ou faça um git clone
- Crie um arquivo .html vazio com qualquer nome dentro da pasta do projeto
- Faça login no Sigaa e vá para a página de participantes da disciplina que você quer pegar os e-mails
- Aperte CTRL+U para abrir o código fonte da página
- Aperte CTRL+A para selecionar tudo e copie e cole dentro do .html em que você criou
- Se você estiver usando alguma IDE como o Visual Studio Code, ele pode apontar algum erro no html do Sigaa, mas você pode ignorar e salvar o arquivo mesmo assim
- Agora, basta abrir o CMD, PowerShell ou outro terminal na pasta do projeto e rodar "python scrapper.py nome_do_arquivo", subsituindo nome_do_arquivo pelo nome do arquivo, obviamente kkkkkkk, se ele não reconhecer, basta adicionar .html ao final do nome do arquivo ou vice-versa
- O programa irá imprimir todos os e-mails separado por espaços, pronto para copiar e colar no g-mail

## Disclaimer

E-mails são informações sensíveis, mas quem vai usar esse programa já tem acesso a esses e-mails de qualquer forma. Cheque sempre vizualmente se deu tudo certo, eu não me responsabilizo se algum e-mail tiver ficado de fora.