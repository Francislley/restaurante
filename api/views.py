from django.db.models import Q
from rest_framework.filters import * 
from rest_framework.pagination import * 
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

class create_comment(CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = commentserializer

	#def perform_create(self, serializer):
	#nb	serializer.save(user = self.request.user)	  

class get_comment(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = listserializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['name','comment']
	list_filter = ['date']
	pagination_class = LimitOffsetPagination
	def get_queryset(self,*args,**kwargs):
		query  = self.request.GET.get("q")
		queryset_list = Comment.objects.all()
		if query:
			queryset_list = queryset_list.filter(
					Q(name__icontains=query)|
                    Q(comment__icontains=query)).distinct()
		return queryset_list

class detail_comment(RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = commentserializer
	#lookup_field = 'slug'
	#lookup_url_kwarg = 'field'

class update_comment(RetrieveUpdateAPIView):
	queryset = Comment.objects.all()
	serializer_class = commentserializer

class delete_comment(DestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = commentserializer


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))