from rest_framework.test import APIClient
from django.test import TestCase
from . import models, serializers


class DiscountTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.discount1 = models.Discount.objects.create(
            title="new year",
            value=10,
            type=models.Discount.DISCOUNT_TYPES_PERCENT,
            start_date="2022-09-20 10:27:00.00Z",
            expire_date="2022-09-21 10:27:00.00Z"
        )
        self.discount2 = models.Discount.objects.create(
            title="halloween",
            value=50000,
            type=models.Discount.DISCOUNT_TYPES_NUMBER,
            start_date="2022-09-20 10:27:00.00Z",
            expire_date="2022-10-20 10:27:00.00Z"
        )

    def test_get_list_api_200(self):
        response = self.client.get("/discount/discount/")
        self.assertEqual(response.status_code, 200)

    def test_get_list_api_object(self):
        response = self.client.get("/discount/discount/")
        self.assertEqual(response.status_code, 200)
        data = serializers.DiscountSerializer(data=response.data, many=True)
        discounts = data.save() if data.is_valid() else None
        objs = [self.discount1, self.discount2]
        for response_obj, model_obj in zip(discounts, objs):
            self.assertEqual(response_obj.title, model_obj.title)
            self.assertEqual(response_obj.value, model_obj.value)
            self.assertEqual(response_obj.type, model_obj.type)

    def test_get_by_id_api_200(self):
        id = self.discount1.id
        response = self.client.get(f"/discount/discount/{id}/")
        self.assertEqual(response.status_code, 200)

    def test_get_by_id_api_object(self):
        id = self.discount1.id
        response = self.client.get(f"/discount/discount/{id}/")
        discount = serializers.DiscountSerializer(data=response.data)
        discount = discount.save() if discount.is_valid() else None
        self.assertEqual(discount.title, self.discount1.title)
        self.assertEqual(discount.value, self.discount1.value)
        self.assertEqual(discount.type, self.discount1.type)

    def test_get_by_id_not_found(self):
        id = 100
        response = self.client.get(f"/discount/discount/{id}/")
        self.assertEqual(response.status_code, 404)

    def test_post_api_200(self):
        discount = {
            "title": "test",
            "value": 15,
            "type": "p",
            "start_date": "2022-09-20 10:27:00.00Z",
            "expire_date": "2022-10-20 10:27:00.00Z"
        }
        response = self.client.post("/discount/discount/", data=discount)
        self.assertEqual(response.status_code, 201)

    def test_read_created_post_api(self):
        discount = {
            "title": "test",
            "value": 15,
            "type": "p",
            "start_date": "2022-09-20 10:27:00.00Z",
            "expire_date": "2022-10-20 10:27:00.00Z"
        }
        response = self.client.post("/discount/discount/", data=discount)
        self.assertEqual(response.status_code, 201)
        deserialized_data = serializers.DiscountSerializer(data=discount)
        deserialized_data = deserialized_data.save(
        ) if deserialized_data.is_valid() else None
        id = deserialized_data.id
        object_from_database = models.Discount.objects.get(id=id)
        self.assertEqual(object_from_database, deserialized_data)

    def test_update_created_patch_api(self):
        id = self.discount2.id
        discount = {
            "title": "behrad"
        }
        response = self.client.patch(
            f"/discount/discount/{id}/", data=discount)
        self.assertEqual(response.status_code, 200)

    def test_delete_api(self):
        id = self.discount2.id
        response = self.client.delete(f"/discount/discount/{id}/")
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f"/discount/discount/{id}/")
        self.assertEqual(response.status_code, 404)
