from .serializer import (Blog, BlogComment, BlogTag,
                         BlogSerializer, BlogCommentSerializer, BlogTagSerializer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Count


class PaginationInterface(PageNumberPagination):
    page_size = 6


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PaginationInterface
    lookup_field = "slug"


class BlogTagView(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer


class BlogCommentView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()
        return self.queryset.filter(**query)


class FeaturedBlog(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        blogs =  self.queryset.filter(featured=True).order_by("-created_at")[:4]
        return blogs

class TopBlog(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = self.queryset.annotate(comment_count=Count(
            "comments")).order_by("-comment_count")[:4]
        return blogs

class SimilarBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        blog_id = self.kwargs.get("blog_id")
        try:
            blog_tag = self.queryset.get(id=blog_id).tags.all()
        except Exception:
           return [] 
        blogs = self.queryset.filter(tags__id__in=[tag.id for tag in blog_tag]).exclude(id=blog_id)
        blog = blogs[1]
        return blogs