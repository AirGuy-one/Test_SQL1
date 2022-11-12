from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import TestData, TestDataRelation, Like
from .forms import TestDataForm
from .permissions import IsMayor
from .serializer import TestDataSerializer, TestDataRelationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView, DetailView


class TestDataViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = TestData.objects.all()
    serializer_class = TestDataSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminUser]
    filterset_fields = ['cat']
    search_fields = ['title']
    ordering_fields = ['title', 'created']

    def perform_create(self, serializer):
        serializer.validated_data['mayor'] = self.request.user
        serializer.save()


class TestDataRelationViewSet(ModelViewSet, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TestDataRelation.objects.all()
    serializer_class = TestDataRelationSerializer


class TestDataView(ListView):
    model = TestData


class TestDataDetailView(DetailView):
    model = TestData


def auth(request):
    return render(request, 'oauth.html')


def index(request):
    data = TestData.objects.all()
    user_tmp = request.user
    id_data = list(map(list, TestData.objects.all().values_list('id')))
    likes_data = []
    for i in id_data:
        try:
            likes_data.append(TestDataRelation.objects.filter(city=TestData.objects.get(id=i[0]), like=True).count())
        except:
            likes_data.append(0)
            continue

    context = {
        'data': data,
        'likes': likes_data,
        'tmp': 0,
        'user_tmp': user_tmp
    }

    return render(request, 'index.html', context)


def like(request):
    data = TestData.objects.all()
    user_tmp = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = TestData.objects.get(id=post_id)

        if user_tmp in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

    context = {
        'data': data,
    }

    return render(request, 'like.html', context)


def my(request):
    data = TestData.objects.all()
    return render(request, 'my_cities.html', {'data': data})


def about(request):
    return render(request, 'about.html')


def add(request):
    if request.method == "POST":
        form = TestDataForm(request.POST)
        try:
            f = form.save(commit=False)
            f.mayor = request.user
            f.save()
            return redirect('home')
        except:
            form.add_error(None, 'Adding to database with using form error')

    else:
        form = TestDataForm()

    return render(request, 'add.html', {'form': form})


def some(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f"""
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User-agent: {user_agent}</p>
        """)


def user(request):
    age = request.GET.get("age", 18)
    name = request.GET.get("name", "No_name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get('username', request.user.username)
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response


def users(request):
    users_data = User.objects.all()
    return render(request, 'users.html', {'data': users_data})


def thisis(request):
    return render(request, 'thisis.html')















