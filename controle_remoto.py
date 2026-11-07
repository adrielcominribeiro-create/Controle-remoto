from rich import print
from rich.panel import Panel

class Contole_remoto():
    # quantidades de canal
    canal_max:int = 6
    canal_min:int = 1

    # quantidades de volume
    volume_max:int = 6
    volume_min:int = 1

    # Valores padrão da TV
    def __init__(self , canal = 1 , volume = 1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    # Vai ligar e desligar 
    def ligadesliga(self):
        self.ligado = not self.ligado

    # Verfica se não for canal maximo
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.canal_max:

                # volta para o canal minimo
                self.canal_atual = self.canal_min
            else:

                # avança um canal
                self.canal_atual += 1

    # Verifica um canal se nao for canal minimo
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.canal_min:
                
                # Volta para canal máximo
                self.canal_atual = self.canal_max
            else:

                # volta um canal
                self.canal_atual -= 1

    # Verifica o aumento de volume
    def volume_mais(self):
        if self.ligado:
            if self.volume_atual == self.volume_max:

                # volta para o volume minimo
                self.volume_atual = self.volume_min
            else:
                # aumenta volume
                self.volume_atual += 1

    # Verifica quando diminui o volume
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == self.volume_min:

                # Volta paara o volume máximo
                self.volume_atual == self.volume_max
            else:

                # diminui volume
                self.volume_atual -= 1

    # Mostra todas as funções da TV funcionarem
    def mostrar_tv(self):
        conteudo = ''

        # Verifica se ligou a TV
        if not self.ligado:
            conteudo = ':prohibited: [red]Não está ligada[/]'
        else:
            
            # Funcionamento visual da TV

            # Mostrando a sequencia dos canais 
            conteudo = f'CANAL = '
            for canal in range(Contole_remoto.canal_min , Contole_remoto.canal_max +1):
                if canal == self.canal_atual:
                    # adiciona cor no canal escolhido
                    conteudo += f'[black on yellow] {canal} [/] '
                else:
                    # Continua a cor padrão se nao for escolido a posição
                    conteudo += f'{canal} '

            # Mostrar sequências dos volumes
            conteudo += '\nVolume = '
            for volume in range(Contole_remoto.volume_min , Contole_remoto.volume_max + 1):
                if volume <= self.volume_atual:
                        
                        #Adiciona cor verde no indice selecionado
                        volume = '[on green]  [/]'
                else:
                    # Cor padrão dos volumes não selecionados
                    volume = '[on blue]  [/]'
                # adiciona as cores
                conteudo += f'{volume} '

        # Organiza o espaço , escopo do conteúdo
        tv = Panel(conteudo , title='[ TV ]' , width= 30)
        print(tv)


c = Contole_remoto()
while True:
    # Sempre vai mostrar as atualizações do controle
    c.mostrar_tv()
    # Onde os dados serão inseridos
    comando = str(input(f'<CAL{c.canal_atual}> | -VOL{c.volume_atual}+ '))
    match comando:
        case '@':
            c.ligadesliga()
        case '>':
           c.canal_mais()
        case '<':
          c.canal_menos()
        case '-':
          c.volume_menos()
        case '+':
            c.volume_mais()