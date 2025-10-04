import os
import unittest

from dotenv import load_dotenv

from src.AgentPrompt import AgentPrompt


class TestAgentPrompt(unittest.TestCase):

    def test_agent_prompt_echo(self):
        # Given
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')

        task = AgentPrompt()
        task.input_properties = {
            'prompt': 'Say hello in Spanish',
            'model': 'gemini-2.5-flash-lite',
            'apiKey': api_key,
        }

        # When
        task.execute_task()
        result = task.get_output_properties()['result']
        print(result)

        # Then
        self.assertIn(result, 'Hola')


if __name__ == "__main__":
    unittest.main()
