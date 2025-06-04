# Lof_Bot-SAP

readme_content = """
Automação de Cadastro de Materiais no SAP

## Este projeto tem como objetivo automatizar o processo de cadastro em massa de materiais no SAP a partir de uma planilha Excel (.xlsx), utilizando Python com as bibliotecas `tkinter`, `pandas` e `pyautogui`.

---

## Funcionalidades

- Interface gráfica simples para selecionar o arquivo da planilha
- Leitura automática dos dados do Excel
- Preenchimento automático de campos no SAP
- Automatização de cadastros em lote (vários materiais)
- Execução de comandos como cliques, preenchimento de campos e navegação entre janelas do SAP

---

## Tecnologias Utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- Pandas (leitura de planilhas Excel)
- PyAutoGUI (automação de teclado e mouse)

---

## 📋 Requisitos

- Python instalado (versão 3.8 ou superior recomendada)
- Instalar bibliotecas necessárias:

```bash
pip install pandas pyautogui

## Como Usar
Abra o SAP e acesse a transação desejada

- Execute o script Python

- Clique em "Carregar Planilha" e selecione o arquivo Excel com os dados

- O script iniciará a automação automaticamente, preenchendo os campos no SAP com base na planilha

- Importante: O layout da tela do SAP precisa ser compatível com os pontos de clique definidos no script (x, y). Ajustes podem ser necessários conforme a resolução da tela e interface do SAP.

---

## Estrutura Esperada da Planilha
- O arquivo Excel deve conter as colunas:

- material

- valido_de

- valido_ate

- fornecedor

- orgc

- contrato

- item

- Cada linha representará um material a ser cadastrado.

## Aviso
- Este projeto realiza ações diretamente na interface do SAP com controle total do mouse e teclado. Evite usar o computador durante a execução do script para não interferir no processo.

## Observações
- O projeto foi desenvolvido para uso interno em ambiente controlado

- Pode ser adaptado para outras transações SAP, bastando alterar os campos e posições necessárias

- O tempo de espera (time.sleep() e pyautogui.PAUSE) pode ser ajustado conforme a velocidade da máquina e da rede

## Autor
Desenvolvido por Guilherme Costa Barbosa — Estudante de programação, desenvolvimento web e automação de processos.

## Contato
- E-mail: costabarbosag2@gmail.com
- Linkedin: www.linkedin.com/in/guilherme-costa-barbosa-345178261
- GitHub: GuilhermeCostaBarbosa

Fique à vontade para abrir issues ou contribuir com melhorias!
"""

Salvar em um arquivo
readme_path = "/mnt/data/README.md"
with open(readme_path, "w", encoding="utf-8") as f:
f.write(readme_content)

readme_path


