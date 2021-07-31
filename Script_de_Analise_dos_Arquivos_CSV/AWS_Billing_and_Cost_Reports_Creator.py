import csv
import json
import awsbillsstatistics
arquivosCSV = {'arquivo1': r"..\Arquivos_CSV\file_hackaton1.csv", 'arquivo2': r"..\Arquivos_CSV\file_hackaton2.csv", 'arquivo3': r"..\Arquivos_CSV\file_hackaton3.csv", 'arquivo4': r"..\Arquivos_CSV\file_hackaton4.csv"}

faturaConsolidada = {'CONTA_DE_PAGAMENTO': {}, 'EBS': {}}
for i,num in enumerate(arquivosCSV):
    with open(arquivosCSV[num]) as arquivoFatura:
        fatura = csv.reader(arquivoFatura)
        for linha in fatura:
            if linha[0] == "":
                continue
            else:
                awsbillsstatistics.elaboraAsEstatisticasDosCustosEmUmaFaturaAWS(faturaConsolidada, linha)

with open ('faturaConsolidada.json', 'w') as arquivoJSON:
    json.dump(faturaConsolidada, arquivoJSON, indent=3)