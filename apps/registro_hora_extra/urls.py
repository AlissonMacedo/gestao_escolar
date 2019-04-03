from django.urls import path
from .views import (
        HoraExtraList,
        HoraExtraEdit,
        HoraExtraDelete,
        HoraExtraNovo,
        HoraExtraEditBase,
        utilizouHoraExtra,
        naoutilizouHoraExtra,
        ExportarParaCSV,
        ExportarParaExcel
)


urlpatterns = [
        path('', HoraExtraList.as_view(), name='list_hora_extra'),
        path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
        path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
        path('utilizou-hora-extra/<int:pk>/', utilizouHoraExtra.as_view(), name='utilizouHoraExtra'),
        path('naoutilizou-hora-extra/<int:pk>/', naoutilizouHoraExtra.as_view(), name='naoutilizouHoraExtra'),
        path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
        path('novo/<int:pk>/', HoraExtraNovo.as_view(), name='create_hora_extra'),
        path('exportar-csv/', ExportarParaCSV.as_view(), name='exportar_csv'),
        path('exportar-excel/', ExportarParaExcel.as_view(), name='exportar_excel'),
]
