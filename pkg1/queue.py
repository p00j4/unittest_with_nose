from boto.sqs import connect_to_region
from boto.sqs.message import Message


class Queue(object):

    def __init__(self, name):
        self._queue = self._get_queue(name)

    def _get_queue(self, name):
        sqs_connection = connect_to_region('us-east-1')
        return sqs_connection.get_queue(name)

    @property
    def is_empty(self):
        return self._queue.count() == 0

    def push(self, *messages):
        for message in messages:
            envelope = Message()
            envelope.set_body(message)
            self._queue.write(envelope)

    def pop(self):
        if self.is_empty:
            return None
        message = self._queue.read()
        return message.get_body()
