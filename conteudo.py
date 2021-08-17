import requests;
class Conteudo:
    
    listaValoresInvalidos = [];
    valoresValidos = 0;
    linhas = [];
    
    def testarEndPoints(self):        
        for x in range(-10000, 10001):
            request = requests.get("http://challengeqa.staging.devmuch.io/" + str(x));
            if (request.status_code == 400):
                self.listaValoresInvalidos.append(x);
            elif (request.status_code == 200):                
                self.valoresValidos = self.valoresValidos + 1;

    def preencherConteudo(self):
        total = len(self.listaValoresInvalidos) + self.valoresValidos;
        taxaSucesso = "{:.2f}".format((self.valoresValidos / total) * 100);        
        taxaFalha = "{:.2f}".format((len(self.listaValoresInvalidos) / total) * 100);        
        self.linhas.append("Resultado:");
        self.linhas.append("Válidos = " + str(self.valoresValidos));
        self.linhas.append("Inválidos = " + str(len(self.listaValoresInvalidos)));
        self.linhas.append("Taxa de sucesso = " + taxaSucesso + "%");
        self.linhas.append("Taxa de falha = " + taxaFalha + "%");
        self.linhas.append("Endpoints com erro:");
        self.linhas.append(self.listaValoresInvalidos);  
