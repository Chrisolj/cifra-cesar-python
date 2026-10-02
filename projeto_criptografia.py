# Alfabeto utilizado para criptografia
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Função para ler um número inteiro do usuário, com validação de entrada. 
def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("\nDigite apenas um número inteiro.")
            continue

        if minimo is not None and valor < minimo:
            print(f"\nDigite um número maior ou igual a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"\nDigite um número menor ou igual a {maximo}.")
            continue
        return valor

# Cifra de César
#
# Aplica o deslocamento e mantém caracteres fora do alfabeto.
def cifra_cesar(mensagem, deslocamento):
    msg_cript = ""
    for caractere in mensagem:
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            nova_posicao = (posicao + deslocamento) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_cript = msg_cript + novo_caractere
        else:
            msg_cript = msg_cript + caractere
    return msg_cript

# Geração da sequência de Fibonacci para a segunda camada.
# 
#   Esta função gera a sequência de Fibonacci que será utilizada
# na segunda camada de criptografia. A função recebe como parâmetro
# o tamanho da mensagem e retorna uma lista com os números da
# sequência de Fibonacci até atingir esse tamanho.
def fibonacci_base(tamanho):
    if tamanho == 1:
        return [1]
    sequencia = [1, 1]
    while len(sequencia) < tamanho:
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
    return sequencia

# Segunda camada de criptografia - Fibonacci.
#
#   Esta função recebe como parâmetros a mensagem criptografada
# pela primeira camada, a sequência de Fibonacci e o deslocamento
# utilizado na primeira camada.
#   A função percorre cada caractere da mensagem e, caso o caractere
# esteja presente no alfabeto, calcula sua nova posição utilizando
# o deslocamento da primeira camada somado ao número correspondente
# da sequência de Fibonacci.
#   Em seguida, adiciona o novo caractere à mensagem criptografada final.
# Caso o caractere não esteja no alfabeto, ele é adicionado à mensagem
# final sem alterações.
def segunda_camada_fib(mensagem, sequencia, deslocamento):
    msg_fib = ""
    for i in range(len(mensagem)):
        caractere = mensagem[i]
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            deslocamento_fib = deslocamento + sequencia[i]
            nova_posicao = (posicao + deslocamento_fib) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_fib = msg_fib + novo_caractere
        else:
            msg_fib = msg_fib + caractere
    return msg_fib

# Geração da sequência de PA para a segunda camada.
# 
# Essa função recebe o tamanho da mensagem e a razão da progressão aritmética, definida pelo usuário no sistema principal, como parâmetros e retorna qual será a sequência de números da progressão aritmética até atingir o tamanho da mensagem.
def progressao_aritmetica(tamanho, razao):
    sequencia = [1]
    while len(sequencia) < tamanho:
        proximo_numero = sequencia[-1] + razao
        sequencia.append(proximo_numero)
    return sequencia

# Segunda camada de criptografia - Progressão Aritmética.
#
# Essa função recebe como parâmetros a mensagem criptografada em Cifra de césar, a sequencia de números da PA e o deslocamento utilizado na Cifra de César. A função percorre cada caractere da mensagem e, caso o caractere esteja presente no alfabeto, calcula sua nova posição utilizando o deslocamento da primeira camada somado ao número correspondente da sequência de PA. Em seguida, adiciona o novo caractere à mensagem criptografada final. Caso o caractere não esteja no alfabeto, ele é adicionado à mensagem final sem alterações.
def segunda_camada_pa(mensagem, sequencia, deslocamento):
    msg_pa = ""
    for i in range(len(mensagem)):
        caractere = mensagem[i]
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            deslocamento_pa = deslocamento + sequencia[i]
            nova_posicao = (posicao + deslocamento_pa) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_pa = msg_pa + novo_caractere
        else:
            msg_pa = msg_pa + caractere
    return msg_pa

# Geração da sequência de PG para a segunda camada.
#
# Essa função recebe o tamanho da mensagem e a razão da progressão geométrica, definida pelo usuário no sistema principal, como parâmetros e retorna qual será a sequência de números da progressão geométrica até atingir o tamanho da mensagem.
def progressao_geometrica(tamanho, razao):
    sequencia = [1]
    while len(sequencia) < tamanho:
        proximo_numero = sequencia[-1] * razao
        sequencia.append(proximo_numero)
    return sequencia

# Segunda camada de criptografia - Progressão Geométrica.
#
# Essa função recebe como parâmetros a mensagem criptografada em Cifra de césar, a sequencia de números da PG e o deslocamento utilizado na Cifra de César. A função percorre cada caractere da mensagem e, caso o caractere esteja presente no alfabeto, calcula sua nova posição utilizando o deslocamento da primeira camada somado ao número correspondente da sequência de PG. Em seguida, adiciona o novo caractere à mensagem criptografada final. Caso o caractere não esteja no alfabeto, ele é adicionado à mensagem final sem alterações.
def segunda_camada_pg(mensagem, sequencia, deslocamento):
    msg_pg = ""
    for i in range(len(mensagem)):
        caractere = mensagem[i]
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            deslocamento_pg = deslocamento + sequencia[i]
            nova_posicao = (posicao + deslocamento_pg) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_pg = msg_pg + novo_caractere
        else:
            msg_pg = msg_pg + caractere
    return msg_pg

# Verificação de números primos.
#
# Esta função recebe um número como parâmetro e verifica se ele é primo. Caso seja primo, a função retorna True; caso contrário, retorna False.
def eh_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

# Geração da sequência de Números primos para a segunda camada.
#
# Essa função recebe o tamanho da mensagem como parâmetro e retorna uma lista com os números primos até atingir esse tamanho.
def numeros_primos(tamanho):
    sequencia = []
    numero = 2
    while len(sequencia) < tamanho:
        if eh_primo(numero):
            sequencia.append(numero)
        numero = numero + 1
    return sequencia

# Segunda camada de criptografia - Números Primos.
#
# Essa função recebe como parâmetros a mensagem criptografada em Cifra de césar, a sequencia de números primos e o deslocamento utilizado na Cifra de César. A função percorre cada caractere da mensagem e, caso o caractere esteja presente no alfabeto, calcula sua nova posição utilizando o deslocamento da primeira camada somado ao número correspondente da sequência de números primos. Em seguida, adiciona o novo caractere à mensagem criptografada final. Caso o caractere não esteja no alfabeto, ele é adicionado à mensagem final sem alterações.
def segunda_camada_primos(mensagem, sequencia, deslocamento):
    msg_primos = ""
    for i in range(len(mensagem)):
        caractere = mensagem[i]
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            deslocamento_primos = deslocamento + sequencia[i]
            nova_posicao = (posicao + deslocamento_primos) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_primos = msg_primos + novo_caractere
        else:
            msg_primos = msg_primos + caractere
    return msg_primos

# Geração da sequência de Incremento em Progressão para a segunda camada.
#
# Essa função recebe o tamanho da mensagem como parâmetro e retorna uma lista com os números em incremento de progressão até atingir esse tamanho.
def incremento_progressao(tamanho):
    sequencia = [1]
    incremento = 1
    while len(sequencia) < tamanho:
        proximo_numero = sequencia[-1] + incremento
        sequencia.append(proximo_numero)
        incremento = incremento + 1
    return sequencia

# Segunda camada de criptografia - Incremento em Progressão.
#
# Essa função recebe como parâmetros a mensagem criptografada em Cifra de césar, a sequencia de números da sequência de incremento em progressão e o deslocamento utilizado na Cifra de César. A função percorre cada caractere da mensagem e, caso o caractere esteja presente no alfabeto, calcula sua nova posição utilizando o deslocamento da primeira camada somado ao número correspondente da sequência de incremento em progressão. Em seguida, adiciona o novo caractere à mensagem criptografada final. Caso o caractere não esteja no alfabeto, ele é adicionado à mensagem final sem alterações.
def segunda_camada_incremento(mensagem, sequencia, deslocamento):
    msg_incremento = ""
    for i in range(len(mensagem)):
        caractere = mensagem[i]
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            deslocamento_incremento = deslocamento + sequencia[i]
            nova_posicao = (posicao + deslocamento_incremento) % len(alfabeto)
            novo_caractere = alfabeto[nova_posicao]
            msg_incremento = msg_incremento + novo_caractere
        else:
            msg_incremento = msg_incremento + caractere
    return msg_incremento


# SISTEMA PRINCIPAL
mensagem = input(f"----- BEM-VINDO -----\nDigite a mensagem a ser criptografada: ")
while mensagem == "" or len(mensagem) > 15:
    if mensagem == "":
        print(f"\nA mensagem não pode estar vazia.")
    else:
        print(f"\nA mensagem deve ter no máximo 15 caracteres.")
    mensagem = input("Digite a mensagem a ser criptografada: ")
confirmar = input(f"\nMensagem escolhida: {mensagem}\n\nDeseja confirmar? (sim/não)\n").strip().lower()
while confirmar not in ["sim","não"]:
    print(f"\nResposta inválida")
    confirmar = input(f"\nVocê digitou: {mensagem}\n\nDeseja confirmar? (sim/não)\n").strip().lower()

while confirmar == "não":
    mensagem = input(f"\n----- BEM-VINDO -----\nDigite a mensagem a ser criptografada: ")
    while mensagem == "" or len(mensagem) > 15:
        if mensagem == "":
            print(f"\nA mensagem não pode estar vazia.")
        else:
            print(f"\nA mensagem deve ter no máximo 15 caracteres.")
        mensagem = input("Digite a mensagem a ser criptografada: ")
    confirmar = input(f"\nVocê digitou: {mensagem}\n\nDeseja confirmar? (sim/não)\n").strip().lower()
    while confirmar not in ["sim", "não"]:
        print(f"\nResposta inválida")
        confirmar = input(f"\nVocê digitou: {mensagem}\n\nDeseja confirmar? (sim/não)\n").strip().lower()
if confirmar == "sim":
    tamanho = len(mensagem)
    print(f"\nMensagem: {mensagem}\n")

    # Validação do deslocamento para evitar que o programa quebre caso o usuário não digite um número inteiro.
    deslocamento = ler_inteiro(f"===== CIFRA DE CÉSAR =====\n\nDigite o deslocamento desejado: ", maximo=1000000000, minimo=-1000000000)
    resultado = cifra_cesar(mensagem, deslocamento)
    print(f"\n-------------------------------------------------------------------\nAlfabeto utilizado:\n{', '.join(alfabeto)}\n")
    print(f"\nMensagem criptografada: {resultado}\n-------------------------------------------------------------------")

#Segunda camada de criptografia, definida pela opção selecionada pelo usuário. Caso o usuário escolha uma opção inválida, o sistema solicitará que ele escolha novamente.
segundo_criptografia = input(f"\nDeseja utilizar uma segunda forma de criptografia? (sim/não)\n\nResposta: ").strip().casefold()
while segundo_criptografia not in ["sim", "não"]:
    print(f"\nResposta inválida")
    segundo_criptografia = input("\nDeseja utilizar uma segunda forma de criptografia? (sim/não)\n\nResposta: ").strip().casefold()
if segundo_criptografia == "sim":
    opção = input(f"\n-------------------------------------------------------------------\nEscolha a segunda forma de criptografia:\n1 - Fibonacci\n2 - Progressão Aritmética\n3 - Progressão Geométrica\n4 - Números Primos\n5 - Incremento em Progressão\n\nResposta: ").strip()
    while opção not in ["1", "2", "3", "4", "5"]:
        print(f"\nOpção inválida")
        opção = input(f"\n-------------------------------------------------------------------\nEscolha a segunda forma de criptografia:\n1 - Fibonacci\n2 - Progressão Aritmética\n3 - Progressão Geométrica\n4 - Números Primos\n5 - Incremento em Progressão\n\nResposta: ").strip()

    if opção == "1":
        sequencia = fibonacci_base(tamanho)
        print(f"\n-------------------------------------------------------------------")
        print(f"\nSequência de Fibonacci gerada:\n{sequencia}\n")
        resultado_final = segunda_camada_fib(resultado, sequencia, deslocamento)
        print(f"\nMensagem após segunda criptografia: {resultado_final}")
        print(f"\n-------------------------------------------------------------------")
        try:
            with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Palavra codificada: {resultado_final}\n")
                arquivo.write(f"SHIFT: {deslocamento}\n")
                arquivo.write(f"Tipo: Fibonacci\n")
                arquivo.write(f"Letras: {tamanho}\n")
        except OSError as erro:
            print(f"Não foi possível salvar o arquivo: {erro}")

    elif opção == "2":
        razao = ler_inteiro(f"\n-------------------------------------------------------------------\nDigite a razão da progressão aritmética: ",minimo=1,maximo=1000)
        sequencia = progressao_aritmetica(tamanho, razao)
        print(f"\n-------------------------------------------------------------------")
        print(f"\nSequência de Progressão Aritmética gerada:\n{sequencia}\n")
        resultado_final = segunda_camada_pa(resultado, sequencia, deslocamento)
        print(f"\nMensagem após segunda criptografia: {resultado_final}")
        print(f"\n-------------------------------------------------------------------")
        try:
            with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Palavra codificada: {resultado_final}\n")
                arquivo.write(f"SHIFT: {deslocamento}\n")
                arquivo.write(f"Tipo: Progressao Aritmetica\n")
                arquivo.write(f"Letras: {tamanho}\n")
        except OSError as erro:
            print(f"Não foi possível salvar o arquivo: {erro}")

    elif opção == "3":
        razao = ler_inteiro(f"\n-------------------------------------------------------------------\nDigite a razão da progressão geométrica: ",minimo=1,maximo=1000)
        sequencia = progressao_geometrica(tamanho, razao)
        print(f"\n-------------------------------------------------------------------")
        print(f"\nSequência de Progressão Geométrica gerada:\n{sequencia}\n")
        resultado_final = segunda_camada_pg(resultado, sequencia, deslocamento)
        print(f"\nMensagem após segunda criptografia: {resultado_final}")
        print(f"\n-------------------------------------------------------------------")
        try:
            with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Palavra codificada: {resultado_final}\n")
                arquivo.write(f"SHIFT: {deslocamento}\n")
                arquivo.write(f"Tipo: Progressao Geometrica\n")
                arquivo.write(f"Letras: {tamanho}\n")
        except OSError as erro:
            print(f"Não foi possível salvar o arquivo: {erro}")

    elif opção == "4":
        sequencia = numeros_primos(tamanho)
        print(f"\n-------------------------------------------------------------------")
        print(f"\nSequência de números primos gerada:\n{sequencia}\n")
        resultado_final = segunda_camada_primos(resultado, sequencia, deslocamento)
        print(f"Mensagem após segunda criptografia: {resultado_final}")
        print(f"\n-------------------------------------------------------------------")
        try:
            with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Palavra codificada: {resultado_final}\n")
                arquivo.write(f"SHIFT: {deslocamento}\n")
                arquivo.write(f"Tipo: Numeros Primos\n")
                arquivo.write(f"Letras: {tamanho}\n")
        except OSError as erro:
            print(f"Não foi possível salvar o arquivo: {erro}")

    elif opção == "5":
        sequencia = incremento_progressao(tamanho)
        print(f"\n-------------------------------------------------------------------")
        print(f"\nSequência de incremento em progressão gerada:\n{sequencia}\n")
        resultado_final = segunda_camada_incremento(resultado, sequencia, deslocamento)
        print(f"Mensagem após segunda criptografia: {resultado_final}")
        print(f"\n-------------------------------------------------------------------")
        try:
            with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Palavra codificada: {resultado_final}\n")
                arquivo.write(f"SHIFT: {deslocamento}\n")
                arquivo.write(f"Tipo: Incremento Progressao\n")
                arquivo.write(f"Letras: {tamanho}\n")
        except OSError as erro:
            print(f"Não foi possível salvar o arquivo: {erro}")
else:
    try:
        with open("resultado_criptografia.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Palavra codificada: {resultado}\n")
            arquivo.write(f"SHIFT: {deslocamento}\n")
            arquivo.write("Tipo: Cifra de César\n")
            arquivo.write(f"Letras: {tamanho}\n")
    except OSError as erro:
        print(f"Não foi possível salvar o arquivo: {erro}")