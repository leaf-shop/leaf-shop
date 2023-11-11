from rest_framework.test import APIClient
from django.test import TestCase
from . import models, serializers


class AttributeTest(TestCase):
    def setUp(self) -> None:

        self.client = APIClient()

        self.attribute_1 = models.Attribute.objects.create(
            key="Brand",
            value="Samsung"
        )
        self.attribute_2 = models.Attribute.objects.create(
            key="Brand",
            value="Apple"
        )

        self.product_1 = models.Product.objects.create(
            title="Product1",
            description="Test text for description 1",
            price=10,
            count=20,
            slug="test-product-1"
        )
        self.product_1.attribute.set([self.attribute_1])

        self.product_2 = models.Product.objects.create(
            title="Product2",
            description="Test text for description 2",
            price=10,
            count=20,
            slug="test-product-2"
        )
        self.product_2.attribute.set([self.attribute_2])

        self.product_3 = models.Product.objects.create(
            title="Product3",
            description="Test text for description 3",
            price=10,
            count=20,
            slug="test-product-3"
        )
        self.product_3.attribute.set([self.attribute_1])

    def test_get_list_200(self):
        response = self.client.get("/product/attribute/")
        self.assertEqual(response.status_code, 200)

    def test_get_list_objects(self):
        response = self.client.get("/product/attribute/")
        serialized_data = serializers.AttributeSerializer(
            [self.attribute_1, self.attribute_2], many=True).data
        for attr in serialized_data:
            self.assertEqual(serialized_data, response.data)

    def test_post_201(self):
        attr = {
            "key": "test attr",
            "value": "test value",
            "is_default": True
        }
        response = self.client.post("/product/attribute/", data=attr)
        self.assertEqual(response.status_code, 201)

    def test_post_object(self):
        attr = {
            "key": "test attr",
            "value": "test value",
            "is_default": True
        }
        response = self.client.post("/product/attribute/", data=attr)
        self.assertEqual(response.status_code, 201)
        serialized_data = serializers.AttributeSerializer(data=response.data)
        serialized_data = serialized_data.save() if serialized_data.is_valid() else None
        id = serialized_data.id
        obj = models.Attribute.objects.get(id=id)
        self.assertNotEqual(obj, None)
        self.assertEqual(serialized_data, obj)

    def test_patch_200(self):
        attr = {
            "is_default": True
        }
        response = self.client.patch(
            f"/product/attribute/{self.attribute_1.id}/", data=attr)
        self.assertEqual(response.status_code, 200)

    def test_patch_object(self):
        attr = {
            "is_default": True
        }
        response = self.client.patch(
            f"/product/attribute/{self.attribute_1.id}/", data=attr)
        serialized_data = serializers.AttributeSerializer(data=response.data)
        serialized_data = serialized_data.save() if serialized_data.is_valid() else None
        id = serialized_data.id
        obj = models.Attribute.objects.get(id=id)
        self.assertEqual(attr['is_default'], serialized_data.is_default)
        self.assertEqual(serialized_data.is_default, obj.is_default)

    def test_delete_204(self):
        response = self.client.delete(
            f"/product/attribute/{self.attribute_1.id}/")
        self.assertEqual(response.status_code, 204)

        
class ProductGalleryTest(TestCase):
    pass


class ProductTest(TestCase):
    pass
