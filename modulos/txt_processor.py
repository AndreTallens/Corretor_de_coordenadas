import pandas as pd
import os

def processar_txt_coletora(caminho_arquivo):
    """
    Lê o arquivo TXT bruto da coletora e mapeia as colunas específicas.
    """
    try:
        print(f"Lendo o arquivo: {caminho_arquivo}...")
        
        # O Pandas lê o arquivo considerando ',' como separador de colunas 
        # e '.' como separador decimal.
        # header=None indica que a primeira linha já é dado (não tem cabeçalho).
        df = pd.read_csv(caminho_arquivo, sep=',', decimal='.', header=None)
        
        # Criamos uma tabela vazia para organizar exatamente como você precisa
        df_organizado = pd.DataFrame()
        
        # Mapeando as colunas conforme sua regra (lembre-se: no Python a contagem começa do 0)
        # A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8
        
        df_organizado['Ponto']        = df[0]  # Coluna A
        df_organizado['Coordenada X'] = df[2]  # Coluna C
        df_organizado['Coordenada Y'] = df[1]  # Coluna B
        df_organizado['Coordenada Z'] = df[3]  # Coluna D
        df_organizado['Limite']       = df[4]  # Coluna E
        df_organizado['Sigma Y']      = df[5]  # Coluna F
        df_organizado['Sigma X']      = df[7]  # Coluna H
        df_organizado['Sigma Z']      = df[8]  # Coluna I
        
        return df_organizado

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar o TXT: {e}")
        return None

# ==============================================================================
# BLOCO DE TESTE
# Tudo que está aqui dentro só executa se você rodar ESTE arquivo diretamente.
# ==============================================================================
if __name__ == "__main__":
    # Vamos criar um arquivo TXT de mentira só para você testar o código agora mesmo
    caminho_teste = 'teste_coletora_mock.txt'
    
    if not os.path.exists(caminho_teste):
        with open(caminho_teste, 'w', encoding='utf-8') as f:
            # Simulando colunas A, B, C, D, E, F, G(inútil), H, I
            f.write("P01,7000000.123,500000.456,100.12,MURO,0.012,G_LIXO,0.015,0.020\n")
            f.write("P02,7000000.124,500000.457,100.15,CERCA,0.010,G_LIXO,0.011,0.018\n")
            f.write("BASE,7000000.000,500000.000,100.00,BASE,0.001,G_LIXO,0.001,0.002\n")
        print(f"[*] Arquivo '{caminho_teste}' criado para o teste.\n")

    # Executando a nossa função
    dados = processar_txt_coletora(caminho_teste)
    
    if dados is not None:
        print("\nSucesso! Veja como a tabela ficou perfeitamente organizada:")
        print("-" * 60)
        print(dados)
        print("-" * 60)
        print("\nEssa é a tabela exata que será enviada para a aba RTK do Excel no futuro!")