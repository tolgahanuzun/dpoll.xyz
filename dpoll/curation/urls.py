from django.urls import path, register_converter

from . import views

# https://stackoverflow.com/questions/48867977/django-2-url-path-matching-negative-value
# Added to detect negative numbers.
class NegativeIntConverter:
    regex = '-?\d+'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return '%d' % value


register_converter(NegativeIntConverter, 'negint')

urlpatterns = [
    path('blacklist/', views.index, name='blacklist'),
    path('blacklist/@<str:user>/<negint:expire_day>/', views.add, name='blacklist_add'),
]