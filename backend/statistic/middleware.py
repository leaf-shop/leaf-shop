from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import date
from django.db import IntegrityError
from .models import DailyRequestCount
import logging


logger = logging.getLogger(__name__)


class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if not hasattr(request, "request_counted"):
                today = date.today()
                daily_request_count, created = DailyRequestCount.objects.get_or_create(date=today)
                daily_request_count.count += 1
                daily_request_count.save()
                request.request_counted = True
            else:
                delattr(request, "request_counted")     

        except IntegrityError:
            logger.warning("IntegrityError in RequestCounterMiddleware")

        response = self.get_response(request)
        return response
