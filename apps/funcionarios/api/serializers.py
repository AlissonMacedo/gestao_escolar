from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.views import HoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = HoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = (
        'id','nome', 'segundonome', 'departamento',
        'total_horas_extra', 'registrohoraextra_set')
