class ProcessamentoDoArquivoCSVDaFaturaAWS: 
    def __init__(self, nomeDicionario, linhaArquivo):
        self.dicionario = nomeDicionario
        self.coluna = linhaArquivo
        self.valor = linhaArquivo[23]
        self.quantidade = linhaArquivo[18]
        self.periodo = str(self.coluna[7])[0:10] + " | " + str(self.coluna[7])[11:19] + " --> " + str(self.coluna[8])[0:10] + " | " + str(self.coluna[8])[11:19]
        self.tipoDaInstancia = self.coluna[97] + " | " + self.coluna[125]
        self.tipoDoVolume = self.coluna[187]
        self.tipoDeOperacao = self.coluna[14]

    def verificaSeContaDePagamentoExiste(self):
        if self.coluna[6] not in self.dicionario['CONTA_DE_PAGAMENTO']:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]] = {'Valor_Total_Conta_de_Pagamento': 0, 'PERIODO': {}}

    def atualizaValorTotalContaPagamento(self):
        self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['Valor_Total_Conta_de_Pagamento'] += float(self.valor)

    def verificaSeIdPeriodoExiste(self):
        if self.periodo not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO']:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo] = {'Valor_Total_do_Periodo': 0, 'USUARIO': {}}

    def atualizaValorTotalDoPeriodo(self):
        self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['Valor_Total_do_Periodo'] += float(self.valor)

    def verificaSeIdUsuarioExiste(self):
        if self.coluna[9] not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO']:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]] = {'Valor_Total_do_Usuario': 0, 'PRODUTO': {}, 'INSTANCIA': {}, 'VOLUME': {}, 'OPERACAO': {}}

    def atualizaValorTotalDoUsuario(self):
        self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['Valor_Total_do_Usuario'] += float(self.valor)

    def verificaSeProdutoExiste(self):
        if self.coluna[13] not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['PRODUTO']:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['PRODUTO'][self.coluna[13]] = float(self.valor)
    
    def atualizaValorTotalDoProduto(self):
        self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['PRODUTO'][self.coluna[13]] += float(self.valor)

    def verificaSeTipoDeInstanciaExiste(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            if self.tipoDaInstancia not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA']:
                self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia] = {'Valor_Total_do_Tipo_de_Instancia': 0, 'Id_da_Instancia': {}}

    def atualizaValorTotalDoTipoDeInstancia(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Valor_Total_do_Tipo_de_Instancia'] += float(self.valor)

    def verificaSeOIdDaInstanciaExiste(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            if self.coluna[17] not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Id_da_Instancia']:
                self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Id_da_Instancia'][self.coluna[17]] = {'Quantidade_Usada': 0, 'Valor_Total': 0}

    def regiaoOndeEstaAInstancia(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Id_da_Instancia'][self.coluna[17]]['Regiao'] = self.coluna[149]

    def atualizaQuantidadeUsadaInstancia(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Id_da_Instancia'][self.coluna[17]]['Quantidade_Usada'] += float(self.quantidade)

    def atualizaValorTotalDaInstancia(self):
        if self.coluna[17][0] == 'i' and self.coluna[17][1] == '-' and 'BoxUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['INSTANCIA'][self.tipoDaInstancia]['Id_da_Instancia'][self.coluna[17]]['Valor_Total'] += float(self.valor)

    def verificaSeTipoDeVolumeExiste(self):
        if self.coluna[17][0] == 'v' and self.coluna[17][1] == 'o' and self.coluna[17][2] == 'l' and self.coluna[17][3] == '-' and 'VolumeUsage' in self.coluna[14]:
            if self.tipoDoVolume not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME']:
                self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume] = {'Valor_Total_do_Volume': 0, 'Id_do_Volume': {}}

    def atualizaValorTotalDoTipoDeVolume(self):
        if self.coluna[17][0] == 'v' and self.coluna[17][1] == 'o' and self.coluna[17][2] == 'l' and self.coluna[17][3] == '-' and 'VolumeUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume]['Valor_Total_do_Volume'] += float(self.valor)

    def verificaSeIdDoVolumeExiste(self):
        if self.coluna[17][0] == 'v' and self.coluna[17][1] == 'o' and self.coluna[17][2] == 'l' and self.coluna[17][3] == '-' and 'VolumeUsage' in self.coluna[14]:
            if self.coluna[17] not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume]['Id_do_Volume']:
                self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume]['Id_do_Volume'][self.coluna[17]] = {'Quantidade_Usada': 0, 'Valor_Total': 0}

    def atualizaQuantidadeUsadaDoVolume(self):
        if self.coluna[17][0] == 'v' and self.coluna[17][1] == 'o' and self.coluna[17][2] == 'l' and self.coluna[17][3] == '-' and 'VolumeUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume]['Id_do_Volume'][self.coluna[17]]['Quantidade_Usada'] += float(self.quantidade)

    def atualizaValorTotalDoVolume(self):
        if self.coluna[17][0] == 'v' and self.coluna[17][1] == 'o' and self.coluna[17][2] == 'l' and self.coluna[17][3] == '-' and 'VolumeUsage' in self.coluna[14]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['VOLUME'][self.tipoDoVolume]['Id_do_Volume'][self.coluna[17]]['Valor_Total'] += float(self.valor)

    def verificaSeOperacaoExiste(self):
        if self.tipoDeOperacao not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO'] and 'BoxUsage' not in self.coluna[14] and 'VolumeUsage' not in self.coluna[14] and self.coluna[23] != '0.0' and 'Tax' not in self.coluna[10]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO'][self.tipoDeOperacao] = 0

    def atualizaValorTotalDaOperacao(self):
        if 'BoxUsage' not in self.coluna[14] and 'VolumeUsage' not in self.coluna[14] and self.coluna[23] != '0.0' and 'Tax' not in self.coluna[10]:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO'][self.tipoDeOperacao] += float(self.valor)

    def calculaImpostos(self):
        if 'Impostos e Taxas' not in self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO']:
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO']['Impostos e Taxas'] = 0
    
    def atualizaValorImpostos(self):
        if self.coluna[10] == 'Tax':
            self.dicionario['CONTA_DE_PAGAMENTO'][self.coluna[6]]['PERIODO'][self.periodo]['USUARIO'][self.coluna[9]]['OPERACAO']['Impostos e Taxas'] += float(self.valor)


def elaboraAsEstatisticasDosCustosEmUmaFaturaAWS(dicionario, linhaDoCSV):
    processaCSV = ProcessamentoDoArquivoCSVDaFaturaAWS(dicionario, linhaDoCSV)
    processaCSV.verificaSeContaDePagamentoExiste()
    processaCSV.atualizaValorTotalContaPagamento()
    processaCSV.verificaSeIdPeriodoExiste()
    processaCSV.atualizaValorTotalDoPeriodo()
    processaCSV.verificaSeIdUsuarioExiste()
    processaCSV.atualizaValorTotalDoUsuario()
    processaCSV.verificaSeProdutoExiste()
    processaCSV.atualizaValorTotalDoProduto()
    processaCSV.verificaSeTipoDeInstanciaExiste()
    processaCSV.atualizaValorTotalDoTipoDeInstancia()
    processaCSV.verificaSeOIdDaInstanciaExiste()
    processaCSV.regiaoOndeEstaAInstancia()
    processaCSV.atualizaQuantidadeUsadaInstancia()
    processaCSV.atualizaValorTotalDaInstancia()
    processaCSV.verificaSeTipoDeVolumeExiste()
    processaCSV.atualizaValorTotalDoTipoDeVolume()
    processaCSV.verificaSeIdDoVolumeExiste()
    processaCSV.atualizaQuantidadeUsadaDoVolume()
    processaCSV.atualizaValorTotalDoVolume()
    processaCSV.verificaSeOperacaoExiste()
    processaCSV.atualizaValorTotalDaOperacao()
    processaCSV.calculaImpostos()
    processaCSV.atualizaValorImpostos()
