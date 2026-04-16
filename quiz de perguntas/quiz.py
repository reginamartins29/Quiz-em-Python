print("Seja muito bem vindo ao Quiz da Regina!")
comecar = input("Vamos começar? (S/N) ")
print(comecar)

score = 0 # score é uma variável que armazena a pontuação do usuário. Inicialmente, ela é definida como 0, indicando que o usuário ainda não acertou nenhuma pergunta. À medida que o usuário responde corretamente às perguntas do quiz, o valor de "score" será incrementado para refletir o número de acertos. No final do quiz, a pontuação total será exibida ao usuário.

if comecar != "S": # != é o operador de desigualdade, ou seja, ele verifica se a variável "comecar" é diferente de "S". Se for diferente, o programa executará o bloco de código dentro do if.
    print("Que pena, até a próxima!")
    quit() # O comando quit() é usado para encerrar o programa imediatamente. Se o usuário escolher "N" ou qualquer outra resposta diferente de "S", o programa exibirá a mensagem de desped


print("Vamos começar com a primeira pergunta!")
print("Qual é a capital do Brasil?" "\n" "A) Rio de Janeiro" "\n" "B) São Paulo" "\n" "C) Brasília" "\n" "D) Salvador")
resposta1 = input("Digite a letra da resposta correta: ")

if resposta1 == "C": # == é o operador de igualdade, ou seja, ele verifica se a variável "resposta1" é igual a "C". Se for igual, o programa executará o bloco de código dentro do if.
    print("Parabéns, você acertou!")  
    score = score + 1 # A expressão "score = score + 1" é usada para incrementar a pontuação do usuário em 1 ponto toda vez que ele acerta uma pergunta. Isso significa que, se o usuário acertar a primeira pergunta, o valor de "score" passará de 0 para 1. Se ele acertar a segunda pergunta, o valor de "score" passará de 1 para 2, e assim por diante. No final do quiz, a pontuação total será exibida ao usuário, indicando quantas perguntas ele acertou.
else:
    print("Resposta incorreta. A resposta correta é C) Brasília.")

print("Qual é a capital da França?" "\n" "A) Paris" "\n" "B) Lyon" "\n" "C) Marseille" "\n" "D) Bordeaux")
resposta2 = input("Digite a letra da resposta correta: ")   

if resposta2 == "A":
    print("Parabéns, você acertou!")   
    score + score + 1

else:
    print("Resposta incorreta. A resposta correta é A) Paris.")     

print("Qual é a capital do Japão?" "\n" "A) Osaka" "\n" "B) Kyoto" "\n" "C) Hiroshima" "\n" "D) Tóquio")
resposta3 = input("Digite a letra da resposta correta: ")

if resposta3 == "D":
    print("Parabéns, você acertou!")   
    score = score + 1   

else:
    print("Resposta incorreta. A resposta correta é D) Tóquio.")    

print(f"Quiz acabou! Você acertou {score} de 3 perguntas.") # A função f-string é usada para formatar a string de saída, permitindo que a variável "score" seja inserida diretamente na mensagem exibida ao usuário. O resultado final mostrará quantas perguntas o usuário acertou em relação ao total de perguntas do quiz.