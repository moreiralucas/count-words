from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from core.forms import TextForm


class TextFormView(FormView):
    template_name = "core/text_form.html"
    form_class = TextForm
    success_url = reverse_lazy("text_form")

    def form_valid(self, form) -> HttpResponse:
        content = form.cleaned_data["text"]
        total_words = len(content.split())
        return self.render_to_response(self.get_context_data(form=form, total_words=total_words))
