from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url_populacao   = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_homicidio   = "https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"
url_fecundidade = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

# Inicia a class para obter a tabela
wiki_populacao   = Scrapy_Table(url_populacao)
wiki_homicidio   = Scrapy_Table(url_homicidio)
wiki_fecundidade = Scrapy_Table(url_fecundidade)

# Pegando as tabelas
tables_populacao   = wiki_populacao.get_tables(0)
tables_homicidio   = wiki_homicidio.get_tables(1)
tables_fecundidade = wiki_fecundidade.get_tables(1)

for linha in tables_populacao[1:]:
  if int(linha[4])<70000:
    print (linha[2])

