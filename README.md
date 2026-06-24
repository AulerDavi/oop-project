# Sistema de Análise de Solos

Projeto 100% em Python com interface gráfica para análise de solos agrícolas, utilizando **PySide6** para a interface e **PyInstaller** para empacotamento.

## Funcionalidades

- Cadastro de técnicos responsáveis (nome, CPF, registro, empresa, e-mail, telefone)
- Entrada de dados do solo (tipo, coordenadas geográficas)
- Configuração de análise (pH, umidade, nutrientes, temperatura)
- Geração de relatórios com classificação automatizada do solo
- Validação de CPF e e-mail

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Como empacotar com PyInstaller

```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." main.py
```

## Estrutura do projeto

```
main.py      — ponto de entrada da aplicação
gui.py       — interface gráfica (PySide6/Qt)
models.py    — lógica de negócio e modelos de dados
utils.py     — utilitários (caminho de recursos)
icon.ico     — ícone da aplicação
requirements.txt — dependências