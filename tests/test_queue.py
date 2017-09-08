import unittest
from boto.sqs.message import Message
from mock import patch, Mock, PropertyMock

from pyqueue.queue import Queue


class QueueTestCase(unittest.TestCase):

    @patch.object(Queue, '_get_queue')
    # This is the same thing
    # @patch('pyqueue.queue.Queue._get_queue')
    def test_queue_initialization(self, get_queue_mock):
        """
        Can use either path or patch.object as Queue object is
        imported.

         * To check that a method called only once:
           `assert_called_once_with`
         * To check the last call: `assert_called_with`
         * To check that a particular call is done among other:
           `assert_any_call`

        """
        queue = Queue('foo')
        get_queue_mock.assert_called_once_with('foo')
        assert queue._queue == get_queue_mock.return_value

    # Mock the imported module
    @patch('pyqueue.queue.connect_to_region')
    def test_get_queue(self, connect_to_region_mock):
        """
        When mocking object, should be done were it will be used.
        Here connect_to_region comes from boto but it is imported and
        used in pyqueue.queue

        Here connect_to_region returns a connection object from which
        we call the get_queue method. That's why we need the
        connect_to_region_mock to return the sqs_connection_mock.

        Two way to know if a method (i.e. a mock) have been called:
         * my_mock.called: returns a boolean regardless the number
           of call
         * my_mock.call_count: returns the actual number of call

        """
        sqs_connection_mock = Mock()
        sqs_connection_mock.get_queue.return_value = 'bar'

        connect_to_region_mock.return_value = sqs_connection_mock

        queue = Queue('foo')
        assert connect_to_region_mock.called
        assert queue._queue == 'bar'
        sqs_connection_mock.get_queue.assert_called_once_with('foo')

    @patch.object(Queue, '_get_queue')
    def test_is_empty_should_return_false(self, get_queue_mock):
        """
        If you understand the previous examples this test is
        straightforward.

        We create a mocked queue object that will respond to count
        with our value.
        """
        queue_mock = Mock()
        queue_mock.count.return_value = 10

        get_queue_mock.return_value = queue_mock

        queue = Queue('foo')
        assert queue.is_empty is False

    @patch('pyqueue.queue.Message', spec=Message)
    # Notice the argument order
    @patch.object(Queue, '_get_queue')
    def test_push_multiple_messages(self,
                                    get_queue_mock,
                                    message_mock):
        """
        Notice the decoration and parameter order: the first
        parameter is the closest to the function name (thing how
        decorator are called).

        Same as previously we start by mocking the queue
        initialization.

        Then we create a Message container (envelope) that match the
        specification of a real Message object with spec=Message.
        It means that if the object signature change or if we have a
        typo in the code and the test it will raise (Mock object has
        no attribute ...).

        Finally we check that every message is well written in the
        queue.
        """
        queue_mock = Mock()
        get_queue_mock.return_value = queue_mock

        envelope_mock = Mock(spec=Message)
        message_mock.return_value = envelope_mock

        queue = Queue('foo')
        queue.push('foo', 'bar')

        assert queue_mock.write.call_count == 2
        envelope_mock.set_body.assert_any_call('foo')

    @patch.object(Queue, '_get_queue')
    # by default new_callable=Mock
    @patch.object(Queue, 'is_empty', new_callable=PropertyMock)
    def test_pop_empty_queue_should_return_none(self,
                                                is_empty_mock,
                                                get_queue_mock):
        """
        The new thing here is the new_callable=PropertyMock, it tells
        mock that the mocked element is a property and should be
        called as it.
        If not set mock will tell you that it was not called
        (Expected to be called once).

        To sum up, the my_mock.return_value is returned when the
        object is called think parenthesis () but also if
        new_callable is set to PropertyMock. An attribute of a mock
        can simply be set with my_mock.foo = 'bar'.
        """
        queue_mock = Mock()
        get_queue_mock.return_value = queue_mock
        is_empty_mock.return_value = True

        queue = Queue('foo')
        assert queue.pop() is None
        assert queue_mock.read.called is False
        is_empty_mock.assert_called_once_with()
