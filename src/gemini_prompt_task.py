from digitalai.release.integration import BaseTask

from google import genai


class GeminiPrompt(BaseTask):

    def execute(self) -> None:
        # Process input
        api_key = self.input_properties['apiKey']
        prompt = self.input_properties['prompt']
        if not prompt:
            raise ValueError("Prompt is required")

        # Make request
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents='Why is the sky blue?'
        )
        self.add_comment(response.text)

        # Process result
        self.set_output_property('response', response.text)
