from os import write
import tabula
import csv
from shutil import make_archive

#Lendo PDF Extraindo tabelas
tables = tabula.read_pdf("padrao-tiss_componente-organizacional_202111.pdf",  pages="114-120")

cont = 1
#Convertndo Tabelas em csv
for i in range(len(tables)):
  if((i == 0) or (i == 7)):
    tables[i].to_csv(f'testes\\test{cont}.csv', encoding='ISO-8859-1')
    cont += 2     
del(tables[7])
del(tables[0])
#Unificando tabelas
f = open('testes\\test2.csv', 'w')
for table in tables:
  write = csv.writer(f)
  write.writerow(table)
f.close()  
#zipando os arquvos csv
make_archive('Teste_Cassio', 'zip', 'testes')



