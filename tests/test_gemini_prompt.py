import unittest

from src.gemini_prompt_task import GeminiPrompt
import os
from dotenv import load_dotenv


class TestGeminiPrompt(unittest.TestCase):

    def test_call_tool(self):
        # Given
        # Get GEMINI_API_KEY from environment variable or .env file
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')

        task = GeminiPrompt()
        task.input_properties = {
            'apiKey': api_key,
            'prompt': 'What is the weather like today?'
        }

        # When
        task.execute_task()

        result = task.get_output_properties()['response']
        print(result)

        # Then
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
