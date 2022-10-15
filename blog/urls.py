from django.urls import path, include
from .views import BlogView, BlogTagView, BlogCommentView, FeaturedBlog, TopBlog, SimilarBlogs
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blogs", BlogView, "blogs")
router.register("blog-tags", BlogTagView, "blog-tags")
router.register("blog-comments", BlogCommentView, "blog-comments")
router.register("top-blogs", TopBlog, "top-blogs")
router.register("featured-blogs", FeaturedBlog, "featured-blogs")
# router.register("similar-blogs", SimilarBlogs, "similar-blogs")

urlpatterns = [
    path("", include(router.urls)),
    # path("top-blogs/", TopBlog.as_view()),
    # path("featured-blogs/", FeaturedBlog.as_view()),
    path("similar-blogs/<int:blog_id>/", SimilarBlogs.as_view())
]
