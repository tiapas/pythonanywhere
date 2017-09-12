from django.shortcuts import render
from django.views.generic import TemplateView
from appAnywhere.globo import get_noticias


class HomePageView(TemplateView):

    def get(self, request, **kwargs):

        if request.method == 'GET' and 'data' in request.GET:
            data = request.GET['data']
        else:
            data = ''

        sistema = 'pythonAnywhere'

        mensagem = 'Noticias {0}'.format(data)

        noticias = get_noticias()

        return render(request, 'index.html', locals())
