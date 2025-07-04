from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from .models import BlogPost
from .forms import BlogPostForm


# Список опубликованных статей только с фильтрацией по is_published=True
class BlogListView(ListView):
    model = BlogPost

    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


# Детальный просмотр с увеличением счетчика просмотров (переопределяем get_object)
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost

    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.increment_views()
        return obj


# Создание нового поста
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:blog_list")


# Обновление поста с перенаправлением на страницу просмотра этого поста после успешного редактирования.
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        # После редактирования перенаправляем на страницу просмотра статьи.
        return reverse("blog:post_detail", kwargs={"pk": self.object.pk})


# Удаление поста (после удаления возвращаемся к списку)
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
