from django.db import models

# Cada classe abaixo vira uma TABELA no banco de dados.
# Cada atributo da classe vira uma COLUNA da tabela.


class Aluno(models.Model):
    '''
    Estudante da PUC-Rio cadastrado no UniRide.
    Quem tem carro e oferece trajeto atua como motorista;
    quem pede carona atua como passageiro.
    '''
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome completo')
    email = models.EmailField(max_length=254, unique=True, help_text='E-mail institucional (@puc-rio.br)')
    matricula = models.CharField(max_length=10, unique=True, help_text='Número de matrícula na PUC-Rio')
    curso = models.CharField(max_length=100, help_text='Curso de graduação')
    membro_desde = models.DateField(auto_now_add=True, verbose_name='Membro desde')

    class Meta:
        managed = True
        db_table = 'Aluno'
        ordering = ['nome']
        verbose_name_plural = 'Alunos'

    def __str__(self):
        '''
        Como o aluno aparece nas listas da página de administração.
        '''
        return "Aluno: " + self.nome


class Veiculo(models.Model):
    '''
    Veículo de um aluno que oferece carona.
    Cada aluno tem no máximo um veículo, e cada veículo pertence a um só aluno.
    '''
    id = models.AutoField(primary_key=True)
    motorista = models.OneToOneField(
        Aluno,
        on_delete=models.CASCADE,
        related_name='veiculo',
        help_text='Aluno proprietário do veículo',
    )
    placa = models.CharField(max_length=8, unique=True, help_text='Placa no formato ABC1D23')
    modelo = models.CharField(max_length=50, help_text='Modelo do carro (ex.: Onix)')
    cor = models.CharField(max_length=30, help_text='Cor do carro')

    class Meta:
        managed = True
        db_table = 'Veiculo'
        ordering = ['placa']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        '''
        Como o veículo aparece nas listas da página de administração.
        '''
        return "Veículo: " + self.modelo + " (" + self.placa + ")"


class Trajeto(models.Model):
    '''
    Trajeto cadastrado na tela "Meu trajeto".
    O aluno escolhe se oferece ou procura carona, a origem, os dias da semana,
    o horário de saída e, no caso de oferta, quantas vagas tem no carro.
    '''
    OFERECE = 'OFERECE'
    PROCURA = 'PROCURA'
    TIPOS = [
        (OFERECE, 'Oferece carona'),
        (PROCURA, 'Procura carona'),
    ]

    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='trajetos',
        help_text='Aluno dono do trajeto',
    )
    tipo = models.CharField(max_length=7, choices=TIPOS, help_text='Oferece ou procura carona')
    origem = models.CharField(max_length=100, help_text='Bairro de partida (ex.: Botafogo)')
    destino = models.CharField(max_length=100, default='PUC-Rio', help_text='Destino da carona')
    horario = models.TimeField(help_text='Horário de saída no formato HH:MM', verbose_name='Horário de saída')
    vagas = models.PositiveSmallIntegerField(
        default=0,
        help_text='Vagas oferecidas no carro (1 a 4). Use 0 quando o aluno procura carona.',
    )
    # Dias da semana em que o trajeto acontece
    dom = models.BooleanField(default=False, verbose_name='Domingo')
    seg = models.BooleanField(default=False, verbose_name='Segunda')
    ter = models.BooleanField(default=False, verbose_name='Terça')
    qua = models.BooleanField(default=False, verbose_name='Quarta')
    qui = models.BooleanField(default=False, verbose_name='Quinta')
    sex = models.BooleanField(default=False, verbose_name='Sexta')
    sab = models.BooleanField(default=False, verbose_name='Sábado')
    ativo = models.BooleanField(default=True, help_text='Desmarque para esconder o trajeto da busca')

    class Meta:
        managed = True
        db_table = 'Trajeto'
        ordering = ['horario']
        verbose_name_plural = 'Trajetos'

    def __str__(self):
        '''
        Como o trajeto aparece nas listas da página de administração.
        '''
        return "Trajeto: " + self.origem + " → " + self.destino + " (" + self.aluno.nome + ")"

