from django.shortcuts import render

from pages.models import Quote


def quotes(request):
	quotes = Quote.objects.filter(make_public=True)

	return render(request, 'pages/index.html', {'quotes': quotes})