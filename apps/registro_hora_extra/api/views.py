from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import HoraExtraSerializer
from apps.registro_hora_extra.models import RegistroHoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = HoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
