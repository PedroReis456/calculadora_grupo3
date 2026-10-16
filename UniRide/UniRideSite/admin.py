from django.contrib import admin

from UniRideSite.models import Aluno, Veiculo, Trajeto, Solicitacao, Avaliacao

admin.site.register(Aluno)
admin.site.register(Veiculo)
admin.site.register(Trajeto)
admin.site.register(Solicitacao)
admin.site.register(Avaliacao)