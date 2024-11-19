# backend/api/tests.py
from http import HTTPStatus

from api import models
from django.test import Client, TestCase

class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()
