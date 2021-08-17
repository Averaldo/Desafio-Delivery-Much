from conteudo import Conteudo
        
arquivo = open("relatorio.txt", 'w');

conteudo = Conteudo();
conteudo.testarEndPoints();
conteudo.preencherConteudo();

for x in conteudo.linhas:    
    arquivo.writelines(str(x)+"\n");
arquivo.close();