<h1 align="center">converter-images-dcm-to-png</h1>
 
<p align="center">
  Conversor de imagens médicas <strong>DICOM (.dcm)</strong> para <strong>PNG</strong> em Python.
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.5_|_3.7-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
  <img src="https://img.shields.io/badge/pydicom-1A1A2E?style=for-the-badge" alt="pydicom" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pillow-5C3EE8?style=for-the-badge" alt="Pillow" />
</p>

 
## Sobre
 
Script que percorre uma pasta de imagens **DICOM** (`.dcm`) e converte cada arquivo para **PNG**, salvando o resultado em uma pasta de saída. Útil para visualizar ou reaproveitar exames fora de softwares de imagem médica.
 
## Versões disponíveis
 
O repositório traz o mesmo conversor em duas versões, conforme o Python instalado:
 
| Script | Python |
| --- | --- |
| `converter_dcm_png.py` | Python 3.5 |
| `converter_dcm_png_37.py` | Python 3.7 |

 
## Requisitos
 
- Python 3.5 ou 3.7
- Bibliotecas: `pydicom`, `numpy`, `Pillow`
## Instalação
 
```bash
pip install pydicom numpy Pillow
```
 
## Como usar
 
**Opção 1: passando as pastas por argumento**
 
```bash
python converter_dcm_png.py caminho/entrada caminho/saida
```
 
**Opção 2: sem argumentos** (usa as pastas padrão `imagens_dcm` e `imagens_png`)
 
```bash
python converter_dcm_png.py
```
 
## Estrutura
 
```text
converter-images-dcm-to-png/
├── converter_dcm_png.py        # versão Python 3.5
├── converter_dcm_png_37.py     # versão Python 3.7
├── imagens_dcm/                # entrada padrão (coloque os .dcm aqui)
└── imagens_png/                # saída padrão (os .png aparecem aqui)
```
 
## Notas
 
- Os arquivos `.dcm` devem estar na pasta de entrada antes de rodar o script.
- A pasta de saída é criada/usada automaticamente conforme os caminhos informados.
