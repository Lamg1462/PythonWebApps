from django.shortcuts import render



class SuperheroListView(TemplateView):
    template_name = 'superhero.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Superhero.objects.all()
        }


class SuperheroDetailView(TemplateView):
    template_name = 'superhero.html'

    def get_context_data(self, **kwargs):
        return {
            'hero': Superhero.objects.get(pk=kwargs['pk'])
        }
