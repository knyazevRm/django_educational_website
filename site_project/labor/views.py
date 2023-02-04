from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.utils.translation import gettext_lazy as _

from .forms import RegisterUserForm, LoginUserForm
from .models import *
from datetime import datetime

def index(request):
    return HttpResponse('index.html')


class Base(ListView):
    template_name = 'index.html'
    model = Vacancy
    paginate_by = 2
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    #def get(self, request, *args, **kwargs):
    #    return HttpResponse('Hello World!')


class Resume(ListView):
    template_name = 'children/resume.html'
    paginate_by = 5
    model = Candidate
    context_object_name = 'posts'

    # queryset = Employer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return dict(list(context.items()))

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search is None:
            return super().get_queryset()

        queryset = Candidate.objects.filter(
            Q(sex=search)
        )

        return queryset

    #def get(self, request, *args, **kwargs):
    #    return HttpResponse('Hello World!')


class Position(ListView):
    template_name = 'children/position.html'
    paginate_by = 3
    model = Vacancy
    context_object_name = 'posts'

    # queryset = Employer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_queryset(self):
        search = self.request.GET.get('search')

        po = self.request.GET.get('po')
        add = self.request.GET.get('add')

        if po is None and add is None and search is None:
            return super().get_queryset()

        if search is not None:
            queryset = Vacancy.objects.filter(
                Q(salary__gte=search)
            ).distinct()

        query = Q()

        if po is not None:
            id_p = Post.objects.filter(
                Q(title=po)
            )

            query = Q(post__in=id_p)

            queryset = Vacancy.objects.filter(
                query
            ).distinct()

        if add is not None:
            id_i = Employer.objects.filter(
                Q(address=add)
            )

            query = Q(employer__in=id_i)

            queryset = Vacancy.objects.filter(
                query
            ).distinct()


        return queryset

    #def get(self, request, *args, **kwargs):
    #    return HttpResponse('Hello World!')


class Company(ListView):
    paginate_by = 3
    model = Employer
    template_name = 'children/company.html'
    context_object_name = 'posts'
    #queryset = Employer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return dict(list(context.items()))

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search is None:
            return super().get_queryset()

        queryset = Employer.objects.filter(
            Q(title=search)
        ).distinct()

        return queryset

    #def get(self, request, *args, **kwargs):
    #    return HttpResponse('Hello World!')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'children/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('base')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'children/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('base')


def logout_user(request):
    logout(request)
    return redirect('login')


