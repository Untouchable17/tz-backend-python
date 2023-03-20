from django.views.generic import TemplateView

from src.menu import models


class IndexViewPage(TemplateView):

	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
