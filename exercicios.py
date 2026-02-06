print('---Sistema de Notas do Sensei---')

# Função para ler o arquivo antes de começar (Dando "memória" ao programa)
def carregar_mural():
    try:
        with open('mural_de_honra.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print("\n📜 ALUNOS QUE JÁ ESTÃO NO MURAL DE HONRA:")
                print(conteudo)
                print("-" * 30)
    except FileNotFoundError:
        pass

#lista honra 
lista_honra = []

#Função para pedir a nota e Validar
def obter_nota(nome):
    """
    Solicita a nota do aluno via teclado e valida o dado.
    Trata erros de digitação (letras) e valores fora do intervalo 0-10.
    """
    try:
        nota = float(input(f'Qual a nota do {nome}? '))
    except ValueError:
        print('Ops! Você precisa digitar um número válido para a nota.')
        return None
    if nota < 0 or nota > 10:
        print('Erro: A nota deve estar entre 0 e 10.')        
        return None
    return nota 

# Função para Avaliar Resultado
def avaliar_aluno(nome, nota):
    """
    Avalia a nota do aluno, e retorna True se tirou nota máxima.
    """
    if nota == 10:
        print(f'Resultado: {nome}, Parabéns tirou nota Máxima! 🏆')
        return True
    elif nota >= 7:
        print(f'Resultado: {nome}, Está Aprovado! ✅')
    elif 5 <= nota < 7:
        print(f'Resultado: {nome}, Está de Recuperação ✍️')
    else:
        print(f'Resultado: {nome}, Infelizmente está Reprovado ❌')
    return False    

# --- Início do Programa Principal ---

carregar_mural() # Mostra quem já estava salvo

while True:
    nome = input('\nQual o seu nome? (ou digite "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break
    
    nota = obter_nota(nome)

    if nota is None:
        continue

    e_nota_maxima = avaliar_aluno(nome, nota)
    
    if e_nota_maxima:
        lista_honra.append(nome)

print('\n--- Encerrando o sistema; Até logo! ---')

if lista_honra:
    print('MURAL DE HONRA DESTA SESSÃO (NOTAS 10):')
    with open('mural_de_honra.txt', 'a', encoding='utf-8') as arquivo:
        for aluno in lista_honra:
            print(f'⭐ {aluno}')
            # Agora alinhado certinho:
            arquivo.write(f'Aluno Nota 10: {aluno}\n')
    print('\n✅ Os novos nomes foram salvos em "mural_de_honra.txt"!')   