from bs4 import BeautifulSoup
import sys

# Abrir o arquivo e ler com o BS

if len(sys.argv) != 2:
    print('Uso: python scrapper.py nome_do_arquivo')
    sys.exit()

file = open(sys.argv[1], encoding="utf8")
bs = BeautifulSoup(file, 'html.parser')

# Pegar todo o conteúdo entre as tags <em></em>
lines = bs.find_all('em')
emails = []

for line in lines:
    line = str(line)
    
    # Formatar para ficar bonitinho
    line = line.replace('<em>', '').replace('</em>', '').replace(' ', '')

    if '@' in line:
        emails.append(line)

# Os dois primeiros emails sempra são da unb e do professor, então podemos remover hehehe
# Atenção em remover sempre o segundo primeiro, visto que se fosse ao contrário, causaria uma alteração nos índices
emails.remove(emails[1])
emails.remove(emails[0])

simplified_emails = ''

# Remover as aspas e transformar apenas em uma string gigante para poder copiar e colar no gmail
for email in emails:
    simplified_emails += email 
    simplified_emails += ' '

print(simplified_emails)