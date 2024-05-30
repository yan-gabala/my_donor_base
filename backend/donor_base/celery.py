import os
import logging
from celery import Celery

logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler("celery.log")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "donor_base.settings")
app = Celery("donor_base")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """
    Представляет собой задачу,
    которая выгружает собственную информацию о запросе.
    """
    logging.info(f"Request: {self.request}")
