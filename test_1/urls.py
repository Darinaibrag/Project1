from .views import PostAPIView, CommentAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostAPIView, basename='user')
router.register(r'comment', CommentAPIView, basename='comment')
urlpatterns = router.urls

