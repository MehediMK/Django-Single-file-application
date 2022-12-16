import os
import sys
import html

from django.urls import path
from django.db import models
from django.conf import settings
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))
APP_LABEL = os.path.basename(BASE_DIR)

settings.configure(
    DEBUG=(os.environ.get("DEBUG", "") == "1"),
    ALLOWED_HOSTS=["*"],
    SECRET_KEY="put_your_secreat_key",
    ROOT_URLCONF=__name__,
    MIDDLEWARE=["django.middleware.common.CommonMiddleware"],
    DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    INSTALLED_APPS=[APP_LABEL],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },
)


def index(request):
    return HttpResponse(f"Welcome Mr./Mrs ***!")


urlpatterns = [
    path("", index),
]

app = get_wsgi_application()

class Student(models.Model):
    name = models.CharField(
        max_length=128, blank=False, null=False, unique=True
    )
    Roll = models.IntegerField(default=-1, blank=False, null=False)

    class Meta:
        app_label = APP_LABEL


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
