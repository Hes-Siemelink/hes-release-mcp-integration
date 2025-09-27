import unittest

from src.call_tool_task import CallTool


class TestCallTool(unittest.TestCase):

    def test_call_tool(self):
        # Given
        task = CallTool()
        task.input_properties = {
            'server': {
                'url': 'http://localhost:8080/',
                'transport': 'sse'
            },
            'tool': 'list_tickets',
            'input': {}
        }

        # When
        task.execute_task()

        result = task.get_output_properties()['result']
        print(result)

        # Then
        # Check if result contains 'TICKET'
        self.assertIn('TICKET', result)


if __name__ == '__main__':
    unittest.main()
