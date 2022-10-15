from django.urls import include, path
from .views import index_view, BookCreate, BookDetail, my_view, SignUpView, CheckOurBooks
# app_name = "catalog"

urlpatterns = [
    path('', index_view, name="index"),
    path('create_book/', BookCreate.as_view(), name="create_book"),
    path('book_detail/<int:pk>', BookDetail.as_view(), name="book_detail"),
    path('my_view/', my_view, name='my_view'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', CheckOurBooks.as_view(), name='profile')
]
