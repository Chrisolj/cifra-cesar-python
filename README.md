# Cifra de César com camadas numéricas

Projeto em Python criado para praticar funções, listas, validação de entradas, sequências numéricas e gravação de arquivos. O programa cifra uma mensagem com a Cifra de César e, se a pessoa quiser, aplica uma segunda camada baseada em uma sequência.

> **Aviso:** este projeto é didático. As cifras implementadas são simples e não devem ser usadas para proteger senhas, dados pessoais ou informações importantes.

## O que o programa faz

- Aceita mensagens de 1 a 15 caracteres.
- Usa um alfabeto com letras maiúsculas, letras minúsculas e dígitos, nessa ordem: `A-Z`, `a-z`, `0-9`.
- Aplica a Cifra de César com um deslocamento inteiro entre `-1.000.000.000` e `1.000.000.000`.
- Deixa espaços, pontuação e caracteres fora do alfabeto sem alteração.
- Opcionalmente aplica uma segunda camada usando uma das sequências abaixo:
  1. Fibonacci: `1, 1, 2, 3, 5...`
  2. Progressão aritmética: começa em `1` e soma a razão informada.
  3. Progressão geométrica: começa em `1` e multiplica pela razão informada.
  4. Números primos: começa em `2`.
  5. Incremento em progressão: `1, 2, 4, 7...`.
- Grava o resultado em `resultado_criptografia.txt`, incluindo o texto codificado, o deslocamento, o método e o tamanho da mensagem.

As razões das progressões aritmética e geométrica devem ser inteiros entre `1` e `1.000`.

## Como executar no computador

1. Salve o código do programa em um arquivo chamado `criptografia.py`.
2. Abra um terminal na pasta onde salvou o arquivo.
3. Execute:

   ```bash
   python criptografia.py
   ```

   No Windows, se `python` não funcionar, tente:

   ```powershell
   py criptografia.py
   ```

4. Responda às perguntas no terminal. Ao terminar, procure `resultado_criptografia.txt` na pasta de execução.

## Como testar no OnlineGDB

1. Abra o OnlineGDB e selecione **Python 3** como linguagem.
2. Cole o código de `criptografia.py` no editor.
3. Clique em **Run** e responda às perguntas pela área de entrada/console.
4. O programa tenta criar `resultado_criptografia.txt` no ambiente do OnlineGDB. Para guardar esse arquivo no computador, baixe-o pelo painel de arquivos, se essa opção estiver disponível, ou execute o programa localmente.

## Como funciona a cifra

Cada caractere que pertence ao alfabeto recebe uma posição de `0` a `61`. A Cifra de César soma o deslocamento a essa posição e usa o resto da divisão por `62` para voltar ao começo do alfabeto quando necessário. Por isso, deslocamentos positivos ou negativos podem ultrapassar os limites sem sair da faixa válida.

Na segunda camada, o programa soma também o número correspondente da sequência escolhida. Caracteres que não fazem parte do alfabeto são mantidos.

## Organização do código

| Parte | Responsabilidade |
| --- | --- |
| `ler_inteiro` | Lê um inteiro e repete a pergunta quando a entrada está fora dos limites. |
| `cifra_cesar` | Aplica o primeiro deslocamento à mensagem. |
| Funções de sequência | Geram Fibonacci, PA, PG, primos ou incremento em progressão. |
| `segunda_camada_*` | Aplica a sequência escolhida ao resultado da primeira cifra. |
| Sistema principal | Valida respostas, conduz o menu, exibe resultados e grava o arquivo. |

## Comentários no código

Os comentários explicam a intenção das funções e ajudam quem está aprendendo. Alguns blocos, porém, repetem em parágrafos longos o que o nome da função e as linhas seguintes já mostram. Para facilitar futuras mudanças, prefira comentários curtos para as etapas principais e docstrings de poucas linhas nas funções, explicando o propósito, os parâmetros e o retorno.

## Limitações

- O programa processa apenas até 15 caracteres por mensagem.
- A segunda camada é opcional; se for escolhida, é aplicada depois da Cifra de César.
- Este projeto não implementa descriptografia.
- O nome e o local do arquivo de resultado dependem da pasta em que o programa é executado.

## Ideias para evoluir

- Criar uma opção para descriptografar.
- Separar o menu em uma função `main()`.
- Reduzir a repetição entre as cinco funções de segunda camada.
- Adicionar testes automatizados para cada cifra e para as entradas inválidas.
