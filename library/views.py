# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Books


def homepage(request):

	latest_book_list = Books.objects.order_by('-pub_date')
	context = {'latest_book_list': latest_book_list}
	return render(request, 'library/homepage.html', context)


def book_search(request):
	search_param = request.POST['search']

	if search_param != '':
		get_books = Books.objects.filter(name=search_param)
	else:
		get_books = Books.objects.all()

	context = {'searched_books': get_books}

	return render(request, 'library/search.html', context)