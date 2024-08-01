# 📄 ExtractPDFPages

Um utilitário simples para extrair páginas de arquivos PDF usando Python e Tkinter, especificamente para boletos do Banco Caixa.

## Como Usar 🚀

1. **Instalação:**

   - Clone o repositório: `git clone https://github.com/seu-usuario/ExtractPDFPages.git`
   - Instale as dependências: `pip install -r requirements.txt`

2. **Execução:**

   - Execute o programa: `python main.py`

3. **Interface Gráfica:**
   - Selecione a pasta com os boletos PDF.
   - Insira o número da parcela desejada.
   - Selecione a pasta de destino.
   - Clique no botão "Extrair parcela" para iniciar o processo.

## Requisitos 🛠️

- Python 3.x
- PyPDF2
- Tkinter

## Funcionalidades

- Extrai páginas de arquivos PDF contendo uma determinada parcela de um boleto do Banco Caixa.
- Busca pelo padrão "RECBTO\. PAR \[número da parcela]/\[total de parcelas]" para identificar a parcela correta.
- Permite selecionar a pasta de origem, a parcela desejada e a pasta de destino.
- Desabilita o botão "Extrair parcela" até que todas as opções necessárias sejam selecionadas.
- Exibe mensagens de status para informar o usuário sobre o progresso da extração.

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença 📝

Este projeto é licenciado sob a [Licença MIT](LICENSE).
