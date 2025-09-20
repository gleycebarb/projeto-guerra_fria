def exibir_menu():
    print("\n\n\033[1;45m========== Menu para escolha de temas e/ou exercícios ==========\033[0m\n")
    print("[1]. O que foi a Guerra Fria?")
    print("[2]. Quais foram as causas da Guerra Fria?")
    print("[3]. Quais foram as características da Guerra Fria?")
    print("[4]. Quais foram os principais conflitos da Guerra Fria?")
    print("[5]. Quais foram os países envolvidos na Guerra Fria?")
    print("[6]. Como a Guerra Fria terminou?")
    print("[7]. Informações Extras - IMPORTANTE!!")
    print("[8]. QUIZ - Exercício de Fixação.")
    print("[9]. Sair?\n")

def exibir_conteudo(opcao, nome):
    if opcao == 1:
        print("\n\033[1;33m========== O QUE FOI A GUERRA FRIA? ==========\033[0m\n")
        print("A \033[4;35mGuerra Fria\033[m foi uma luta político-militar entre o socialismo e o capitalismo liderada pela União Soviética e Estados Unidos. Esta guerra teve início após a Segunda Guerra Mundial e durou até a dissolução da União Soviética em 1991. A diferença de ideologia é a chave para entendermos esse conflito. Os Estados Unidos defendiam o capitalismo, enquanto a União Soviética defendia o socialismo, havendo assim, a polarização do mundo entre países capitalistas e países comunistas.")
    elif opcao == 2:
        print("\n\033[1;33m========== CAUSAS DA GUERRA FRIA ==========\033[0m\n")
        print("As \033[4;35mcausas da Guerra Fria\033[m foram a disputa pela hegemonia mundial entre Estados Unidos e União Soviética, os dois países que saíram com status de potência após a Segunda Guerra Mundial. A diferença de ideologia entre os dois países também foi um fator importante para o início da Guerra Fria.\n")
        print("\033[36mOBS: Quando nos tratamos de hegemonia neste contexto, estamos querendo dizer que houve uma disputa pela a superioridade, o poder entre os dois países ganhadores.\nE quando tratamos de ideologia, significa que há uma diferença de concepções, para ficar mais claro, uma diferença de ideias entre os dois países, no caso, Estados Unidos e União Sovética.\033[m ")
    elif opcao == 3:
        print("\n\033[1;33m========== CARACTERÍSTICAS DA GUERRA FRIA ==========\033[0m\n")
        print("\033[4;35mAs características da Guerra Fria\033[m foram a polarização do mundo entre comunismo e capitalismo, a corrida armamentista, a corrida espacial, a interferência estrangeira e a propaganda ideológica.\n"
              "\n-> \033[4;32mPolarização do mundo entre capitalismo e socialismo\033[m se deu a partir da segunda metade do século XX, onde o mundo estava dividido em dois blocos com sistemas políticos, sociais e econômicos opostos: o bloco capitalista, liderado pelos Estados Unidos e o bloco socialista, liderado pela a União Soviética.\n"
              "\n-> \033[4;32mA corrida armamentista\033[m foi a procura pela hegemonia internacional fez com que as duas potências investissem bastante no desenvolvimento de novas tecnologias bélicas. Assim, no período, o número de armas nucleares e termonucleares produzidas disparou.\n"
              "\n-> \033[4;32mA corrida espacial\033[m foi um dos campos de disputa entre americanos e soviéticos e, ao longo da década de 1960, inúmeras expedições espaciais foram realizadas.\n"
              "\n-> \033[4;32mA interferência estrangeira\033[m foi quando os americanos e os soviéticos interferiram em assuntos internos de diferentes países do planeta. Dois exemplos são a interferência americana na política brasileira na década de 1960 e a interferência militar no Afeganistão na década de 1980.\n")
    elif opcao == 4:
        print("\n\033[1;33m========== ALGUNS DOS PRINCIPAIS CONFLITOS OCORRIDOS ==========\033[0m\n")
        print("\033[4;35mAlguns dos principais conflitos da Guerra Fria\033[m foram a Guerra da Coreia, ocorrida no ano de 1950 até 1953, a Guerra do Vietnã, ocorrida no ano de 1959 até 1975, a Guerra do Afeganistão, ocorrida no ano de 1979 e 1989, e a Crise dos Mísseis de Cuba, que foi considerado o momento de maior tensão entre as duas potências da Guerra Fria, ocorrida no ano de 1962.\n"
              "\n -> \033[4;32mA guerra da Coreia\033[m foi o primeiro momento de tensão entre as potências, após a Segunda Guerra Mundial, onde comunistas norte-coreanos, que eram apoiados pelos chineses e soviéticos, resolveram invadir o território sul-coreano, apoiados pelos capitalistas, no caso, Estados Unidos. Contou com o envolvimento direto de soldados americanos, mas ao longo do conflito, nenhum dos dois lados sobressaiu-se e o conflito teve fim, em 1953, com a divisão das Coreias.\n "
              "\n -> \033[4;32mA guerra do Vietnã\033[m foi um conflito travado entre Vietnã do Sul e Vietnã do Norte, onde ambos lados procuravam unificar o país sob seu controle. Acabou que os americanos mandaram milhões de soldados, mas os mesmos não conseguiram cumprir o seu objetivo, fazendo assim com que os comunistas tomassem o controle do país, em 1976, logo após vencerem a guerra.\n"
              "\n -> \033[4;32mA guerra do Afeganistão\033[m quando os soviéticos invadiram o Afeganistão para apoiar o governo comunista daquele país contra rebeldes islâmicos, levando assim, os americanos a financiarem e treinarem os rebeldes islâmicos. O conflito foi extremamente penoso para os soviéticos que se retiraram em 1989.\n"
              "\n -> \033[4;32mA crise dos mísseis em Cuba\033[m foi um confronto de 13 dias entre os Estados Unidos e a União Soviética relacionado com a implantação de mísseis balísticos soviéticos em Cuba. Foi o mais próximo que se chegou ao início de uma guerra nuclear em grande escala durante a Guerra Fria. O governo norte-americano exigiu a retirada dos mísseis de Cuba e impôs um bloqueio ao país caribenho. No final de novembro, Nikita Khrushchov decidiu retirar os mísseis de Cuba em troca de algumas contrapartidas oferecidas pelos Estados Unidos. ")
        print("\033[36mOBS: Um conflito travado se refere a um confronto ou disputa que ocorreu entre duas ou mais partes. Utilizado para descrever qualquer tipo de conflito, desde uma briga entre indivíduos até uma guerra entre países.\n ")
    elif opcao == 5:
        print("\n\033[1;33m========== OS PRINCIPAIS PAÍSES ENVOLVIDOS NA GUERRA ==========\033[0m\n")
        print("\033[4;35mOs principais países envolvidos na Guerra Fria\033[m foram Estados Unidos e União Soviética. Além desses, outros países também se envolveram no conflito, como Alemanha, China, Cuba e Vietnã.")
    elif opcao == 6:
        print("\n\033[1;33m========== QUANDO TERMINOU A GUERRA FRIA? ==========\033[0m\n")
        print("\033[4;35mA Guerra Fria terminou\033[m em dezembro de 1991, com a dissolução da União Soviética. Uma das principais causas do término dessa guerra foi queda do Muro de Berlim, em 1989, havendo assim a reunificação da Alemanha, o acidente Nuclear de Chernobyl, em 1986, onde causou mortes e destruição, além da grande crise econômica e política que atingiu a URSS.")
    elif opcao == 7:
        print("\n\033[1;33m========== INFORMAÇÕES EXTRAS - IMPORTANTE OBSERVAR! ==========\033[0m\n")
        print("\033[4;35mPara finalizarmos esta jornada de explicações e irmos para a parte de exercícios, que por sinal é um super desafio, resolvi adicionar algumas informações extras e/ou pontos importantes que talvez você possa utilizar na hora dos desafios :), mas cuidado, não se perca nas informações.\033[m\n"
              "\n1. \033[4;32mAs principais causas da dissolução da União Soviética é\033[m: Crise econômica, o autoritarismo e a centralização do poder, a opressão da burocracia, a exclusão da população das decisões políticas e a falta de democracia.\n"
              "\n2. \033[4;32mO nome 'Guerra fria' se deve por conta\033[m que foi um período de tensão geopolítica entre a URSS e os EUA e seus respectivos aliados, que não envolveu uma ação militar direta, mas foi exercida principalmente através de ações econômicas e políticas.\n"
              "\n3. \033[4;32mHouve a criação da cooperação política e militar durante a Guerra Fria\033[m, destacando Plano Marshall (Reconstrução dos países aliados da Europa após a II Guerra Mundial) | Comecon (evitar que o Plano Marshall seduzisse as nações do bloco comunista a aliarem-se com os americanos.) | OTAN (Organização do Tratado do Atlântico Norte -> aliança militar de países alinhados aos Estados Unidos visando a impedir uma posição de agressão dos soviéticos.) | Pacto de Varsóvia (A ideia era garantir a segurança das nações do bloco comunista e evitar uma possível agressão realizada pelos estadunidenses).")
    elif opcao == 8:
        exibir_exercicios()
    elif opcao == 9:
        print("\n\033[1;33m========== VOCÊ CHEGOU AO FIM! :) ==========\033[0m\n")
        print(f"\033[31mVocê chegou até o final, pequeno... Quer dizer, grande aprendiz {nome}! Lhe agradeço por ter chegado até aqui e eu espero que você tenha entendido o conteúdo da Guerra Fria! Bom, provavelmente o meu objetivo foi cumprido. Tenha um ótimo dia e não desista dos seus sonhos :), é sério..., não desista, porque se não você não vai ser ninguém nessa vida!!!")
        print("\n\033[1;33m========== FIM :) ==========\033[0m\n")
        exit()
    else:
        print("Opção Inválida.")

def exibir_exercicios():
    print("\033[34mVOCÊ CHEGOU NA PARTE DE EXERCÍCIOS! Top, então vamos dar continuidade, certo?\033[m")
    print("\033[34mAgora, para finalizarmos a nossa busca pela a aprendizagem, vamos realizar um pequeno exercício de fixação. Boa sorte e desde já agradeço por ter chegado aqui! Tamo junto :)\033[m")

    perguntas_1 = [
        "1. Qual foi a diferença de ideologia entre Estados Unidos e União Soviética durante a Guerra Fria?",
        "2. Qual foi o principal evento da Guerra Fria?",
        "3. Quais foram os países envolvidos na Guerra Fria?"
    ]
    opcoes_1 = [
        ["a) Comunismo e facismo", "b) Capitalismo e socialismo", "c) Democracia e ditadura"],
        ["a) A  Construção do Muro de Berlim", "b) A Guerra do Vietnã", "c) A Crise dos Mísseis em Cuba"],
        ["a) Estados Unidos, União Soviética, Alemanha, China, Cuba e Vietnã", "b) Estados Unidos, França, Reino Unido, Alemanha, Japão e Coreia do Sul", "c) União Soviética, China, Cuba, Vietnã, Coreia do Norte e Irã"]
    ]
    respostas_corretas1 = ["b", "c", "a"]

    perguntas_2 = [
        "1. Qual as principais causas da dissolução da União Soviética?",
        "2. Porque o nome “Guerra Fria”? Porque este período histórico ganhou este nome?",
        "3. Em que ano foi ocorreu a queda do muro de Berlim?",
        "4. Em que ano iniciou e acabou a Guerra Fria?"
    ]
    opcoes_2 = [
        ["a) Por conta que eles tiveram que se render para os países que estavam aliados aos EUA, por medo","b) Por conta da irresponsabilidade da própria URSS, causando sua queda", "c) Por conta de diversas crises que eles tiveram, tanto por conta do autoritarismo, quanto por conta de crises econômicas"],
        ["a) Nunca houve um conflito direto entre a URSS e os EUA", "b) Houve um conflito direto entre a URSS e os EUA", "c) Houve muitas mortes e destrução, então esse período passo a ser chamado desse jeito por conta do sangue frio dos militares."],
        ["a) Ocorreu no ano de 1956 ", "b) Ocorreu no ano de 1989", "c) Ocorreu no ano de 1990"],
        ["a) Início (1998) / Fim (2000)", "b) Início (1946) Fim / (1991)", "c) Início (1947) / Fim (1991)"]
    ]
    respostas_corretas2 = ["c", "a", "b", "c"]

    perguntas_3 = [
        "1. Qual o principal objetivo da Doutrina Truman?",
        "2. O que significa a sigla OTAN?",
        "3. Qual das opções corresponde ao Plano Marshall?",
        "4. Em que ano acabou a Guerra do Afeganistão?.",
        "5. Quem saiu ganhadora da Guerra Fria?"
    ]
    opcoes_3 = [
        ["a) A Doutrina Truman tinha como principal objetivo ajudar os soviéticos, a partir do combate ao avanço do capitalismo","b) A Doutrina Truman tinha como objetivo combater o avanço do Comunismo", "c) A Doutrina Truman tinha como objetivo fornencer alimentos em meio a Guerra Fria, ajudando principalmente as pessoas refugiadas."],
        ["a) Organização das Nações Unidas", "b) Organização do Tratamento do Atlântico ", "c) Organização do Tratado do Atlântico Norte"],
        ["a) Reconstrução dos países aliados da Europa após a II Guerra Mundial ", "b) Um plano que tinha como objetivo eliminar todos os judeus", "c) Um plano para acabar com todos os comunistas"],
        ["a) Acabou no ano de 1986", "b) Acabou no ano de 1989", "c) Acabou no ano de 1991"],
        ["a) Estados Unidos", "b) Rússia", "c) União Soviética"]
    ]
    respostas_corretas3 = ["b", "c", "a", "b", "a"]

    # Exercício fácil
    while exercicio_fixacao(opcoes_1, perguntas_1, respostas_corretas1) == -1:
        d = input("Que pena, suas vidas acabaram! Quer tentar de novo? S/s para SIM ou N/n para NÃO: ")
        if d.lower() == 's':
            continue
        else:
            print("Certo, boa sorte na próxima!")
            return

    nivel = input("Pequeno aprendiz, gostaria de aumentar a dificuldade do exercício? S/s para SIM ou N/n para NÃO: ")
    if nivel.lower() == 's':
        print("Ok, então vamos aumentar o nível de dificuldade para vermos se você realmente está preparado!!\n")
        escolha = int(input("Digite 2 para perguntas de médio nível, ou 3 para perguntas difíceis : "))
        if escolha == 2:
            while exercicio_fixacao(opcoes_2, perguntas_2, respostas_corretas2) == -1:
                d = input("Que pena, suas vidas acabaram! Quer tentar de novo? S/s para SIM ou N/n para NÃO: ")
                if d.lower() == 's':
                    continue
                else:
                    print("Certo, boa sorte na próxima!")
                    return
        else:
            while exercicio_fixacao(opcoes_3, perguntas_3, respostas_corretas3) == -1:
                d = input("Que pena, suas vidas acabaram! Quer tentar de novo? S/s para SIM ou N/n para NÃO: ")
                if d.lower() == 's':
                    continue
                else:
                    print("Certo, boa sorte na próxima!")
                    return
    elif nivel.lower() == 'n':
        print("Tudo bem, você jogou bem. :)")
    else:
        print("Opa, opção inválida. :(")

def exercicio_fixacao(opcoes, perguntas, gabarito):
    vidas = 3
    print("Você tem 3 vidas! A cada erro, você perderá 1 vida. Cuidado...")
    for i in range(len(perguntas)):
        print(perguntas[i])
        for j in range(len(opcoes[i])):
            print(opcoes[i][j])
        while True:
            resposta = input("Escolha a opção que corresponde com a pergunta: ")
            if resposta.lower() in ['a', 'b', 'c']:
                break
            else:
                print("Resposta inválida.")
        if resposta.lower() == gabarito[i]:
            print("\033[32mE a resposta está... correta! Uau, você realemente está estudado! Meus parabéns :)\n\033[m")
        else:
            vidas -= 1
            if vidas <= 0:
                return -1
            print(f"\033[31mAh, que pena! Resposta incorreta, aliás, você perdeu uma vida. Você está com {vidas}/3 vida(s)\n\033[m")
    print(f"O seu total de vidas resulta: {vidas}/{len(perguntas)} ")

def main():
    print("Para iniciarmos essa jornada de aprendizagem, gostaria de conhecê-lo(a) primeiro!")
    nome = input("Qual é o seu nome? Ou por qual nome gostaria de ser identificado?: ")
    print(f"Olá pequeno(a) aprendiz(a) \033[34m{nome}\033[m, tudo bem? Espero que sim! Criei este projeto com o intuito de ajudar pessoas, como você, que gostariam de aprender mais sobre a 'Guerra Fria'. Aqui estarei abordando um pouquinho de tudo o que pode ser visto sobre o tema da Guerra Fria.\nPor onde gostaria de começar? Aqui estão algumas opções para você!")

    while True:
        exibir_menu()
        try:
            opcao = int(input("Insira o número da opção que você se interessou mais e/ou que você gostaria de entender, pequeno aprendiz: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        exibir_conteudo(opcao, nome)

if __name__ == "__main__":
    main()