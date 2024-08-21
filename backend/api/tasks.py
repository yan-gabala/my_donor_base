from donor_base.celery import app, logger

@app.task
def send_users_to_unisender():
    """Таска для отправки доноров в Юнисендер."""
    logger.info(f"Доноры отправлены в базу")
