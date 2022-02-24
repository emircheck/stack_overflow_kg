from django.urls import path

from applications.question.views import CategoryListView #CategoryView #category_list

urlpatterns = [
    # 1
    # path('categories-list/', category_list),
    # 2
    # path('categories-list/', CategoryView.as_view())
    # 3
    path('categories-list/', CategoryListView.as_view())
]