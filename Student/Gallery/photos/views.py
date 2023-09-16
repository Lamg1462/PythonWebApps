from django.views.generic import TemplateView

class PhotoView(TemplateView):
    template_name = 'photo.html'

def get_context_data(self, **kwargs):

    name = kwargs['name']
    image = f'Gallery/static/images/{name}'
    return {'photo': image}


def photo_list():
    photos = Path('static/images').iterdir()
    photos = [f for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())