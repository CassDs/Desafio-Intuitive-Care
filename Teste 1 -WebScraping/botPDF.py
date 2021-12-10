import requests
from PyPDF2 import PdfFileMerger, PdfFileReader

#Nome do arquivo mais recente
nome_Arquivo = "padrao-tiss_componente-organizacional_202111.pdf"
#Diretorio para download do arquivo
diretorio = "C:\\Users\\Caio\\Desktop\\Teste\\"

url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/{}'.format(nome_Arquivo)
resp = requests.get(url)
#Condiçõs par download do PDF
if (resp.status_code == 200) and ("Warning" not in str(resp.content)):
  print("Acessando pagina Gov.br/n")
  print("Buscando arquivo mais recente do Padrão TISS...")
  #br a pasta
  with open("{}{}".format(diretorio,nome_Arquivo), "wb") as f:
    f.write(resp.content)
    print('Arquivo baixando com sucesso!')
else:
  print("Erro ao baixar pdf")

