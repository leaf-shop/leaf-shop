from rest_framework.test import APIClient
# from rest_framework.test import MockRequest
from .views import CustomUserViewSet
from django.test import TestCase
from . import serializers



class MockRequest:
    def __init__(self, method="GET", data=None, user=None):
        self.method = method
        self.data = data or {}
        self.user = user


class CustomUserViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_serializer_class(self, method, expected_serializer):
        view = CustomUserViewSet()
        view.request = MockRequest(method=method)
        serializer_class = view.get_serializer_class()
        self.assertEqual(serializer_class, expected_serializer)

    def test_get_serializer_class_returns_correct_serializer_for_get_request(self):
        self.test_get_serializer_class("GET", serializers.CustomUserOutputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_post_request(self):
        self.test_get_serializer_class("POST", serializers.CustomUserInputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_put_request(self):
        self.test_get_serializer_class("PUT", serializers.CustomUserInputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_patch_request(self):
        self.test_get_serializer_class("PATCH", serializers.CustomUserInputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_delete_request(self):
        self.test_get_serializer_class("DELETE", serializers.CustomUserOutputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_options_request(self):
        self.test_get_serializer_class("OPTIONS", serializers.CustomUserOutputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_head_request(self):
        self.test_get_serializer_class("HEAD", serializers.CustomUserOutputSerializer)

    def test_get_serializer_class_returns_correct_serializer_for_non_standard_request(self):
        self.test_get_serializer_class("TRACE", serializers.CustomUserOutputSerializer)