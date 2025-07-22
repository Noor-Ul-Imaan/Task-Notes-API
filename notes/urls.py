from django.urls import path
from .views import SignupView, CustomAuthToken, NoteCreateView, NoteListView, NoteDeleteView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('create_note/', NoteCreateView.as_view()),
    path('list_notes/', NoteListView.as_view()),
    path('delete_note/<int:pk>/', NoteDeleteView.as_view()),
]
