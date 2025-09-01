import os
import time

PASTA = "C:/Sischef/comandas"

def excluir_pares():
    arquivos = [f for f in os.listdir(PASTA) if f.endswith(".xml")]
    grupos = {}

    for arq in arquivos:
        nome, ext = os.path.splitext(arq)
        sufixo = nome[-5:]
        chave = sufixo[:-2] 
        tipo = sufixo[-1]    

        if chave not in grupos:
            grupos[chave] = {}
        grupos[chave][tipo] = arq

    for chave, itens in grupos.items():
        if "C" in itens and "L" in itens:
            for arq in [itens["C"], itens["L"]]:
                caminho = os.path.join(PASTA, arq)
                try:
                    os.remove(caminho)
                    print(f"Excluído: {caminho}")
                except Exception as e:
                    print(f"Erro ao excluir {caminho}: {e}")

        elif "L" in itens and "C" not in itens:
            caminho = os.path.join(PASTA, itens["L"])
            try:
                os.remove(caminho)
                print(f"Excluído: {caminho}")
            except Exception as e:
                print(f"Erro ao excluir {caminho}: {e}")

if __name__ == "__main__":
    print("Monitorando a pasta...")
    while True:
        excluir_pares()
        time.sleep(120)
