from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ('motivo', 'funcionario', 'horas','ultilizada')
