from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)
from blog.models import Post, Comment

class AboutView(TemplateView):

    template_name = 'about.html'


class PostListView(ListView):

    model = Post

    def get_queryset(self):
        """
        The __lte is related to the SQL search:
        
        field__lookup_type

        e.g. 

        published_date__lte='2009-10-10' means:

        SELECT * FROM blog_entry WHERE pub_date <= '2009-10-10'
        """

        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
        
        

