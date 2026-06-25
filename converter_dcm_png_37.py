import os
import sys
import pydicom
import numpy as np
from PIL import Image


def normalizar_pixels(array_pixels: np.ndarray) -> np.ndarray:
    valor_minimo = array_pixels.min()
    valor_maximo = array_pixels.max()
    if valor_maximo == valor_minimo:
        return np.zeros_like(array_pixels, dtype=np.uint8)
    array_normalizado = (array_pixels - valor_minimo) / (valor_maximo - valor_minimo) * 255
    return array_normalizado.astype(np.uint8)


def converter_dcm_para_png(caminho_entrada: str, caminho_saida: str) -> None:
    arquivo_dicom = pydicom.dcmread(caminho_entrada)
    array_pixels = arquivo_dicom.pixel_array.astype(np.float32)

    if array_pixels.ndim == 3:
        array_pixels = array_pixels[0]

    array_normalizado = normalizar_pixels(array_pixels)
    imagem = Image.fromarray(array_normalizado)
    imagem.save(caminho_saida)
    print(f"Convertido: {caminho_entrada} -> {caminho_saida}")


def converter_pasta(pasta_entrada: str, pasta_saida: str) -> None:
    os.makedirs(pasta_saida, exist_ok=True)

    arquivos_dcm = [
        nome for nome in os.listdir(pasta_entrada)
        if nome.lower().endswith('.dcm')
    ]

    if not arquivos_dcm:
        print(f"Nenhum arquivo .dcm encontrado em: {pasta_entrada}")
        return

    total = len(arquivos_dcm)
    print(f"Encontrados {total} arquivo(s) .dcm para converter.")

    for nome_arquivo in arquivos_dcm:
        caminho_dcm = os.path.join(pasta_entrada, nome_arquivo)
        nome_png = os.path.splitext(nome_arquivo)[0] + '.png'
        caminho_png = os.path.join(pasta_saida, nome_png)
        try:
            converter_dcm_para_png(caminho_dcm, caminho_png)
        except Exception as erro:
            print(f"Erro ao converter {nome_arquivo}: {erro}")

    print(f"Conversao concluida: {total}/{total} arquivo(s).")


if __name__ == '__main__':
    pasta_entrada, pasta_saida = (sys.argv[1], sys.argv[2]) if len(sys.argv) == 3 else ('imagens_dcm', 'imagens_png')
    converter_pasta(pasta_entrada, pasta_saida)
