#-*- coding:utf-8 -*-

import webbrowser
import time

__criador__ = 'Helionay Alves'

print('[S2]Oi, este programa vai te ajudar a escolher a sua distro!')
print('[S2]Vamos a algumas perguntinhas...')
print('')
print('[S2]Qual a finalidade?')
print('Quero estudar = 1')
print('Quero conhecer um pouco o mundo linux = 2')
print('Quero programar = 3')
print('Estou estundando vulnerabilidades = 4')
print('Quero usar um pouco = 5')
print('Quero sair, obrigado! == 6')
choice = int(input('Número: '))

if choice == 6:
    print('')
    print('[S2]Então, xau!')
    exit(0)

if choice == 1:
    print('')
    print('[S2]Ótimo, para..?')
    print('Estudar para escola = 1')
    print('Estudar um pouco linux = 2')
    print('Estou pensando em alguns projetos = 3')
    print('Depois eu vejo, tchau! = 4')
    choice1 = int(input('Número: '))

    if choice1 == 1:
        print('')
        print('[S2]Se você deseja estudar um pouco, então vou lhe recomendar o Ubuntu Linux!')
        print('[S2]Deseja abrir uma nova guia no site offcial do Ubuntu?')
        print('OK, claro = 1')
        print('Nhâ, mais tarde = 2')
        print('Nhã, tenho que ir. = 3')
        off = int(input('Número: '))

        if off == 1:
            print('')
            print('[S2]Ok')
            time.sleep(0.1)
            webbrowser.open_new('https://ubuntu.com/')
            exit(0)

        if off = 2:
            print('')
            print('[S2]Ok, quer aprender a como testar o Ubuntu?')
            print('Sim, como? = 1')
            print('Nhââ, tenho que ir. = 2')
            num = int(input('Número: '))

        if num == 2:
            print('')
            print('): OK, então bye bye!!')
            time.sleep(0.1)
            exit(0)

            if num == 1:
                print('')
                print('[S2]Tem duas maneiras simples! Qual?')
                print('Pendrive(8gb, 16gb) = 1')
                print('Virtual Box(programa) = 2')
                print('Tenho que sair, good bye! = 3')
                nu2 = int(input('Número: '))



                if nu2 == 1:
                    print('')
                    print('[S2]OK')
                    time.sleep(0.1)
                    webbrowser.open_new('https://www.youtube.com/results?search_query=Como+instalar+ubuntu+no+pendrive')
                    exit(0)

                if nu2 == 2:
                    print('')
                    print('[S2]OK')
                    time.sleep(0.1)
                    webbrowser.open_new('https://www.youtube.com/results?search_query=Como+instalar+ubuntu+no+pendrive+no+vitural+box')
                    exit(0)

                if nu2 == 3:
                    print('')
                    print('): Tá né, kkk')
                    time.sleep(0.1)
                    exit(0)

        if num == 3:
            print('')
            print('): Ok, kkk')
            time.sleep(0.1)
            exit(0)

    if choice1 == 2:
        print('')
        print('[S2]Ok kkk, aqui vai algumas coisas!')
        print('Entrar em um site explicativo = 1')
        print('Tenho que ir = 2')
        quark = int(input('Num: '))

        if quark == 1:
            print('')
            print('[S2]Ok, só um minutinho...')
            time.sleep(0.1)
            webbrowser.open_new('https://e-tinet.com/linux/aprender-linux-iniciantes/')
            exit(0)

        if quark == 2:
            print('')
            print('): Então tá né...')
            time.sleep(2.0)
            exit(0)

    if choice1 == 3:
        print('')
        print('[S2]Acredito em vocẽ, aqui vai algumas distros!')
        print('Ubunto, simples comum normal para quem não quer muito! = 1')
        print('Kali Linux, um pouco complicado, pentesting... = 2')
        print('Linux Mint, sem algumas coisas do Ubuntu mais continua bem simples = 3')
        print('Tenho que ir... = 4')
        sety = int(input('Num: '))

        if sety == 1:
            print('')
            print('[S2]Ok, só um minutinho...')
            time.sleep(1.0)
            webbrowser.open_new('https://www.youtube.com/results?search_query=Conhecendo+ubuntu')
            exit(0)

        if sety == 2:
            print('')
            print('[S2]Ok, só um minutinho...')
            time.sleep(1.0)
            webbrowser.open_new('https://www.youtube.com/results?search_query=Conhecendo+o+Kali+linux')
            exit(0)

        if sety == 3:
            print('')
            print('[S2]Ok, só um minutinho...')
            time.sleep(1.0)
            webbrowser.open_new('https://www.youtube.com/results?search_query=conhecendo+o+Linux+Mint')
            exit(0)

        if sety == 4:
            print('')
            print('): Ok, então... bay... Xau!')
            time.sleep(0.1)
            exit(0)
