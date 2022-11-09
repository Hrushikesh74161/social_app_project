from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms, models


class ImageUploadView(LoginRequiredMixin, CreateView):
    form_class = forms.ImageForm
    template_name = 'images/image_upload.html'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class ImageDetailView(DetailView):
    model = models.Image
    template_name = 'images/image_detail_view.html'
    context_object_name: str = 'image'


