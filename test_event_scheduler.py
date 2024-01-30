
import unittest
from unittest.mock import patch
from main import add_event, list_events, delete_event, search_events, events, edit_event

class TestEventScheduler(unittest.TestCase):

    def setUp(self):

        global events
        pass

    def test_add_event(self):
        with patch('builtins.input', side_effect=['Event Title', 'Event Description', '2023-12-31', '12:30']):
            add_event()
        self.assertIn('Event Title', events)
        self.assertEqual(events['Event Title']['title'], 'Event Title')
        self.assertEqual(events['Event Title']['description'], 'Event Description')
        self.assertEqual(events['Event Title']['date'], '2023-12-31')
        self.assertEqual(events['Event Title']['time'], '12:30')

    def test_list_events(self):
        # sample events for testing
        events['Event 1'] = {'title': 'Event 1', 'description': 'Description 1', 'date': '2023-01-01', 'time': '08:00'}
        events['Event 2'] = {'title': 'Event 2', 'description': 'Description 2', 'date': '2023-01-02', 'time': '10:00'}

        with patch('builtins.print') as mock_print:
            list_events()

        # Check if the events are printed in sorted order
        expected_output = [
            'Title: Event 1', 'Description: Description 1', 'Date: 2023-01-01', 'Time: 08:00',
            'Title: Event 2', 'Description: Description 2', 'Date: 2023-01-02', 'Time: 10:00'
        ]
        actual_output = [line.strip() for call_args in mock_print.call_args_list for line in call_args[0][0].split('\n')]
        self.assertListEqual(actual_output, expected_output)

    def test_delete_event(self):
        # sample event for testing
        events['EventToDelete'] = {'title': 'EventToDelete', 'description': 'DescriptionToDelete', 'date': '2023-12-31', 'time': '12:30'}

        with patch('builtins.input', return_value='EventToDelete'):
            delete_event()

        self.assertNotIn('EventToDelete', events)

    def test_delete_event_nonexistent(self):
        with patch('builtins.input', return_value='NonExistentEvent'):
            with patch('builtins.print') as mock_print:
                delete_event()

        mock_print.assert_called_with("Event not found.\n")

    def test_search_events(self):
        # sample events for testing
        events['Event 1'] = {'title': 'Event 1', 'description': 'Description 1', 'date': '2023-01-01', 'time': '08:00'}
        events['Event 2'] = {'title': 'Event 2', 'description': 'Description 2', 'date': '2023-01-02', 'time': '10:00'}

        with patch('builtins.input', return_value='Event 1'), patch('builtins.print') as mock_print:
            search_events()

        expected_output = [
            'Title: Event 1', 'Description: Description 1', 'Date: 2023-01-01', 'Time: 08:00'
        ]
        actual_output = [line.strip() for call_args in mock_print.call_args_list for line in call_args[0][0].split('\n')]
        self.assertListEqual(actual_output, expected_output)

    def test_edit_event(self):
        events['EventToEdit'] = {'title': 'EventToEdit', 'description': 'DescriptionToEdit', 'date': '2023-12-31', 'time': '12:30'}

        with patch('builtins.input', side_effect=['EventToEdit', 'UpdatedTitle', 'UpdatedDescription', '2023-12-31', '15:30']), patch('builtins.print') as mock_print:
            edit_event()

        self.assertIn('UpdatedTitle', events)
        self.assertEqual(events['UpdatedTitle']['title'], 'UpdatedTitle')
        self.assertEqual(events['UpdatedTitle']['description'], 'UpdatedDescription')
        self.assertEqual(events['UpdatedTitle']['date'], '2023-12-31')
        self.assertEqual(events['UpdatedTitle']['time'], '15:30')

    def test_edit_event_nonexistent(self):
        with patch('builtins.input', return_value='NonExistentEvent'), patch('builtins.print') as mock_print:
            edit_event()

        mock_print.assert_called_with("Event not found.")


    def test_search_events_no_match(self):
        # Test searching for an event that does not exist
        with patch('builtins.input', return_value='NonExistentEvent'), patch('builtins.print') as mock_print:
            search_events()

        mock_print.assert_called_with("No matching events found.\n")

if __name__ == '__main__':
    unittest.main()
