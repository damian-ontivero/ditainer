class ServiceA:
    def __init__(self, bus):
        self._bus = bus

    def run(self):
        self._bus.publish("ServiceA")


class ServiceB:
    def __init__(self, bus):
        self._bus = bus

    def run(self):
        self._bus.publish("ServiceB")


class Subscriber:
    def __init__(self, service):
        self._service = service

    def subscribed_to(self):
        return "ServiceA"

    def on(self):
        self._service.run()


class Bus:
    def __init__(self, subscribers):
        self._subscribers = subscribers

    def publish(self, message):
        for subscriber in self._subscribers:
            if subscriber.subscribed_to() == message:
                subscriber.on()
