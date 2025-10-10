from digitalai.release.integration import BaseTask

from google import genai


class GeminiPrompt(BaseTask):

    def execute(self) -> None:
        # Process input
        model = self.input_properties['model']
        api_key = model['apiKey']
        prompt = self.input_properties['prompt']

        if not prompt:
            raise ValueError("Prompt is required")

        # Make request
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=model['model_id'], contents=prompt
        )
        self.add_comment(response.text)

        # Process result
        self.set_output_property('response', response.text)
