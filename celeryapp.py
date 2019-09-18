from celery import Celery

app = Celery("celeryapp", broker="amqp://localhost//", backend="mongodb://localhost:27017/")

app.config_from_object("celeryconfig")

@app.task
def reverse(string):
    return string[::-1]
