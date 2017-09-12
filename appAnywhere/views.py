from django.shortcuts import render
from django.views.generic import TemplateView
from appAnywhere.globo import get_noticias

from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class HomePageView(TemplateView):

    def get(self, request, **kwargs):

        if request.method == 'GET' and 'data' in request.GET:
            data = request.GET['data']
            data_base = datetime.strptime(data, '%Y-%m-%d').date()
        else:
            data_base = datetime.now()
    
        ano, mes, dia = data_base.year, data_base.month, data_base.day
            
        main, geral, esportes, cotidiano, archive = get_noticias(ano, mes, dia)

        sistema = 'pythonAnywhere'

        mensagem = 'Noticias {0}'.format(archive)

        archive_after = ( archive + relativedelta(days=+1) ).strftime('%Y-%m-%d')
        archive_before = ( archive + relativedelta(days=-1) ).strftime('%Y-%m-%d')

        return render(request, 'index.html', locals())
