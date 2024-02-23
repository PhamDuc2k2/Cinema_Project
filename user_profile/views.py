from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework import permissions
from .serializers import AccountSerializer
from .models import Account
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class AccountViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = AccountSerializer

    def get(self, request):
        query = Account.objects.all()
        serializer = AccountSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AccountViewDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = AccountSerializer

    def get_object(self, account_id):
        try:
            return Account.objects.get(user_id=account_id)
        except Account.DoesNotExist:
            return None
    
    def get(self, request, account_id):
        account_instance = self.get_object(account_id)
        if not account_instance:
            return Response(
                {"res": "Account with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AccountSerializer(account_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, account_id):
        account_instance = self.get_object(account_id)
        if not account_instance:
            return Response(
                {"res": "Account with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Nhận danh sách các hạng mục từ PUT request
        categories = request.data.getlist('interested_categories')

        # Chuyển đổi các giá trị từ chuỗi sang kiểu dữ liệu phù hợp (nếu cần thiết)
        categories = [int(category_id) for category_id in categories]

        # Gán danh sách vào trường ArrayField trong mô hình Django
        account_instance.interested_categories = categories
        account_instance.save()

        serializer = AccountSerializer(account_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)