import os
import sys
import pydicom
import numpy as np
from PIL import Image

def normalizar_pixels(array_pixels):
    valor_minimo = array_pixels.min()
    valor_maximo = array_pixels.max()
    if valor_maximo == valor_minimo:
        return np.zeros_like(array_pixels, dtype=np.uint8)
    array_normalizado = (array_pixels - valor_minimo) / (valor_maximo - valor_minimo) * 255
    return array_normalizado.astype(np.uint8)


def converter_dcm_para_png(caminho_entrada, caminho_saida):
    arquivo_dicom = pydicom.dcmread(caminho_entrada)
    array_pixels = arquivo_dicom.pixel_array.astype(np.float32)

    if array_pixels.ndim == 3:
        array_pixels = array_pixels[0]

    array_normalizado = normalizar_pixels(array_pixels)
    imagem = Image.fromarray(array_normalizado)
    imagem.save(caminho_saida)
    print("Convertido: {} -> {}".format(caminho_entrada, caminho_saida))


def converter_pasta(pasta_entrada, pasta_saida):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    arquivos_dcm = [
        nome for nome in os.listdir(pasta_entrada)
        if nome.lower().endswith('.dcm')
    ]

    if not arquivos_dcm:
        print("Nenhum arquivo .dcm encontrado em: {}".format(pasta_entrada))
        return

    total = len(arquivos_dcm)
    print("Encontrados {} arquivo(s) .dcm para converter.".format(total))

    for indice, nome_arquivo in enumerate(arquivos_dcm, start=1):
        caminho_dcm = os.path.join(pasta_entrada, nome_arquivo)
        nome_png = os.path.splitext(nome_arquivo)[0] + '.png'
        caminho_png = os.path.join(pasta_saida, nome_png)
        try:
            converter_dcm_para_png(caminho_dcm, caminho_png)
        except Exception as erro:
            print("Erro ao converter {}: {}".format(nome_arquivo, erro))

    print("Conversao concluida: {}/{} arquivo(s).".format(total, total))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        pasta_entrada = sys.argv[1]
        pasta_saida = sys.argv[2]
    else:
        pasta_entrada = 'imagens_dcm'
        pasta_saida = 'imagens_png'

    converter_pasta(pasta_entrada, pasta_saida)
