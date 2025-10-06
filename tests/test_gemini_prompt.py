import unittest

from src.gemini_prompt import GeminiPrompt
import os
from dotenv import load_dotenv


class TestGeminiPrompt(unittest.TestCase):

    def test_prompt(self):
        # Given
        # Get GEMINI_API_KEY from environment variable or .env file
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')

        task = GeminiPrompt()
        task.input_properties = {
            'prompt': 'Say hello in Spanish',
            'model': {
                'apiKey': api_key,
                'model': 'gemini-2.5-flash-lite'
            },
        }

        # When
        task.execute_task()

        result = task.get_output_properties()['response']
        print(result)

        # Then
        self.assertIn('Hola', result)


if __name__ == '__main__':
    unittest.main()
