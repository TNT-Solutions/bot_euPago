from gtts import gTTS
from io import BytesIO
from datetime import datetime
import speech_recognition as sr
import webbrowser as wb
import pygame
import pyttsx3


def abrirNavegador(link):
    wb.open_new_tab(link)


def navegador(link):
    wb.open_new_tab(link)


def falar(texto, language='pt'):
    mp3_fo = BytesIO()
    tts = gTTS(texto, lang=language)
    tts.write_to_fp(mp3_fo)
    pygame.mixer.music.load(mp3_fo, 'mp3')
    pygame.mixer.music.play()


def detectarPeriodoDoDia():
    hora = datetime.today().strftime('%H')
    hora = int(hora)
    if hora <= 12:
        return 'Bom dia'
    elif hora <= 17:
        return 'Boa tarde'
    else:
        return 'Boa noite'


def euPago(recon):
    falar('abrindo aplicativo Eu Pago, o que deseja fazer ? comprar, ver historico, ver carteira ou editar perfil')
    abrirNavegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/ce017388')


def menu(recon):
    falar('voltando ao menu, o que deseja fazer ? comprar, ver historico, ver carteira ou editar perfil')
    abrirNavegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/ce017388')


def comprar(recon):
    falar('aqui você pode escolher o cartão, basta dizer cartão e o numero escolhido, voce também pode dizer voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/ba23b50e')


def historico(recon):
    falar('indo para tela de historico, aqui temos o historico de todas as suas compras, qual você deseja consultar, fast shop, sephora, nike ou extra')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/30963375')


def fastShop(recon):
    falar('Compra realizada em 14/04/2022, na Fast Shop, valor de 3.990 reais e 99 centavos, em 5 vezes no cartão de crédito no cartão 2, você pode voltar ao historico ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/70749950')


def sephora(recon):
    falar('Compra realizada em 11/03/2022, na Sephora, valor de 1.499 reais e 99 centavos, em 8 vezes no cartão de crédito no cartão 3, você pode voltar ao historico ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/1bc5ba13')


def nike(recon):
    falar('Compra realizada em 08/02/2022, na Nike, valor de 349 reais e 99 centavos, débito á vista no cartão 1, você pode voltar ao historico ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/69b67d5a')


def extra(recon):
    falar('Compra realizada em 08/02/2022, na Nike, valor de 349 reais e 99 centavos, débito á vista no cartão 1, você pode voltar ao historico ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/22302285')


def carteira(recon):
    falar('aqui você pode adicionar cartão ou removelos, basta dizer adicionar cartão ou remover cartão')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/d04bd22f')


def adicionarCartao(recon):
    falar('para adicionar cartão, basta preencher os dados do cartão e dizer cadastrar cartão, você também pode voltar a carteia ou voltar ao menu ')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/2db42e08')


def cartaoEscolhido(recon):
    falar('aqui você pode aproximar o celular da maquina de cartão e dizer pagar, você pode dizer escolher outro cartão ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/aa807801')


def cartaoCadastrado(recon):
    falar('cartão cadastrado, você pode voltar a carteira ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/c6f21b1e')


def cartaoRemovido(recon):
    falar('cartão removido, você pode dizer voltar a carteira ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/2c6d43ac')


def valores(recon):
    falar('Compra sendo realizada na Fast Shop, no valor de 3.990 reais e 99 centavos em 5 vezes no cartão de crédito, você deseja confirmar ou cancelar ?')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/ae5f6d4e')


def confirmar(recon):
    falar('compra aprovada, você pode dizer voltar ao menu ou ver histórico')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/4d8b134b')


def cancelar(recon):
    falar('compra cancelada, você pode dizer voltar ao menu ou escolher outro cartão')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/1c3e328f')


def perfil(recon):
    falar('para atualizar seu perfil basta preencher os dados e dizer atualizar cadastro ou voltar ao menu')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/042d9b77')


def perfilAtualizado(recon):
    falar('cadastro atualizado, você pode dizer ir a carteira ou voltar ao menu ')
    navegador(
        'https://matheus201737.invisionapp.com/prototype/EuPago2-0-cl211d4g200c4y301pvkxxshm/play/23953039')


def mapearComandos(comando, recon):
    comandos = {
        ('abrir eu pago', 'abrir o aplicativo eu pago', 'eu pago'): euPago,
        ('voltar ao menu', 'menu'): menu,
        ('comprar', 'quero fazer uma compra', 'quero comprar', 'escolher outro cartão'): comprar,
        ('histórico', 'ver histórico', 'voltar ao histórico', 'voltar histórico'): historico,
        ('fast shop', 'ver compra na fast shop'): fastShop,
        ('sephora', 'ver compra na sephora'): sephora,
        ('nike', 'ver compra na nike'): nike,
        ('extra', 'ver compra no extra'): extra,
        ('carteira', 'ver carteira', 'voltar a carteira', 'voltar carteria', 'ir a carteira'): carteira,
        ('adicionar cartão'): adicionarCartao,
        ('cadastrar cartão'): cartaoCadastrado,
        ('remover cartão'): cartaoRemovido,
        ('cartão 1 escolhido', 'cartão 2 escolhido', 'Cartão escolhido', 'cartão escolhido'): cartaoEscolhido,
        ('pagar'): valores,
        ('confirmar compra', 'confirmar'): confirmar,
        ('cancelar', 'cancelar compra'): cancelar,
        ('ver perfil', 'editar perfil', 'perfil'): perfil,
        ('atualizar cadastro'): perfilAtualizado,

    }

    for key, value in comandos.items():
        if comando.lower() in key:
            return value(recon)


def ouvir(recon):
    print('Fale algo...')
    audio = recon.listen(source)
    print('Reconhecendo...')
    comando = recon.recognize_google(audio, language='pt')
    return comando


engine = pyttsx3.init()
recon = sr.Recognizer()
recon.energy_threshold = 50
recon.dynamic_energy_threshold = False
pygame.mixer.init()
with sr.Microphone() as source:
    recon.adjust_for_ambient_noise(source, duration=3)
    while True:
        engine.runAndWait()
        try:
            comando = ouvir(recon)
            mapearComandos(comando, recon)
            print(comando)
            esperar = input('Pressione Enter para continuar...')
            if 'amigo' in comando:
                falar(detectarPeriodoDoDia()+', mestre. Como posso ajudá-lo?')
                comando = ouvir(recon)
                print(comando)
                #esperar = input('Pressione Enter para continuar...')
        except sr.UnknownValueError:
            print('\nTente novamente')
            continue
        except KeyboardInterrupt:
            print('\nEncerrando...')
            break
        except KeyError:
            print('\n Comando não encontrado')
            continue
