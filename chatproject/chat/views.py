from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CreateRoomForm, MessageForm
from .models import Room

class HomeView(generic.TemplateView):
    template_name = "home.html"


class RoomCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "room/create.html"
    form_class = CreateRoomForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class RoomListView(generic.ListView):
    model = Room
    template_name = "room/list.html"


class RoomDetailView(generic.DetailView):
    template_name = "room/detail.html"
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.all()
        context["form"] = MessageForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.instance.room = self.get_object()
            form.instance.posted_by = request.user
            form.save()
            return redirect("room.detail", pk=self.get_object().pk)
        return super().get(request, *args, **kwargs)