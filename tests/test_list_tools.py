import unittest

from src.list_tools_task import ListTools


class TestListTools(unittest.TestCase):

    def test_list_tools(self):
        # Given
        task = ListTools()
        task.input_properties = {
            'server': {
                'url': 'http://localhost:8080/',
                'transport': 'sse'
            },
        }

        # When
        task.execute_task()

        # Then

        # Check if result contains key 'list_tickets'
        tools = task.get_output_properties()['tools']
        self.assertIn('list_tickets', tools)

        inputSchema = task.get_output_properties()['inputSchema']
        print(inputSchema)
        self.assertIn('list_tickets', inputSchema)


if __name__ == '__main__':
    unittest.main()
