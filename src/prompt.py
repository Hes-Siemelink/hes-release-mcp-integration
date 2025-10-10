from digitalai.release.integration import BaseTask
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


class AiPrompt(BaseTask):

    def execute(self) -> None:
        # Get input
        prompt = self.input_properties.get('prompt')
        model = self.input_properties['model']

        # Call agent
        model_connector = create_model(model)
        # output = asyncio.run(send_prompt(prompt, model_connector))
        output = model_connector.invoke(prompt)
        print("AgentPrompt Result:\n", output)

        response = output.content
        print(response)
        self.add_comment(response)

        # Process result
        self.set_output_property('response', response)


async def send_prompt(prompt, model):
    return await model.invoke(prompt)


def create_model(model):
    provider = model['provider']

    if provider == 'gemini':
        return ChatGoogleGenerativeAI(
            google_api_key=model['apiKey'],
            model=model['model_id'],
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
    if provider == 'openai':
        return ChatOpenAI(
            base_url=model['url'],
            api_key=model["apiKey"],
            model=model['model_id'],
            default_headers={'Authorization': f'Token {model["apiKey"]}'},
            temperature=0.0
        )
    raise ValueError(f"Provider {provider} is not supported")
