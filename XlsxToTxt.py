import openpyxl
import threading
import time

def ler_planilha_e_copiar_para_txt(caminho_xlsx, caminho_txt):
    while True:
        # Carrega a planilha
        workbook = openpyxl.load_workbook(caminho_xlsx)
        folha = workbook.active
        
        # Abre o arquivo de texto em modo de escrita
        with open(caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
            for linha in folha.iter_rows(values_only=True):
                linha_texto = ';'.join([str(celula) for celula in linha])
                arquivo_txt.write(linha_texto + '\n')
        
        print("Conteúdo da planilha copiado para o arquivo de texto com sucesso.")
        
        # Tempo de espera para rodar a função
        time.sleep(60)

# coloque o caminho dos seus arquivos
caminho_xlsx = "C:/Documents/AAAA.xlsx"
caminho_txt = "C:/Documents/BBBB.txt"

# Usa threading para rodar a função de salvar em segundo plano, podendo finalizar o comando pelo gerenciador de tarefas
threading.Thread(target=ler_planilha_e_copiar_para_txt, args=(caminho_xlsx, caminho_txt)).start()