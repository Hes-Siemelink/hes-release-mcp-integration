import asyncio
import os

from digitalai.release.integration import BaseTask
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


class AgentPrompt(BaseTask):

    def execute(self) -> None:
        # Get input
        prompt = self.input_properties.get('prompt')
        model = self.input_properties['model']
        os.environ["GOOGLE_API_KEY"] = model['apiKey']
        mcp_servers = {}
        for server in [self.input_properties.get('mcpServer1'), self.input_properties.get('mcpServer2'),
                       self.input_properties.get('mcpServer3')]:
            if server:
                transport = server['transport']
                if transport == 'http':
                    transport = 'streamable_http'
                mcp_servers[server['title']] = {
                    "url": server['url'],
                    "transport": transport,
                    "headers": server.get('headers', {})
                }

        # Call agent
        output = asyncio.run(send_prompt(prompt, model['model'], mcp_servers))
        print("AgentPrompt Result:\n", output)
        result = first_agent_message(output)

        # Process result
        self.set_output_property('result', result)


async def send_prompt(prompt, model, mcp_servers):
    client = MultiServerMCPClient(mcp_servers)
    tools = await client.get_tools()

    model = ChatGoogleGenerativeAI(
        model=model,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    agent = create_react_agent(model=model, tools=tools)

    response = await agent.ainvoke({"messages": prompt})

    return response


def first_agent_message(output):
    # Get content field of first object of type AIMessage
    # Example format: {'messages': [HumanMessage(content='Say hello in Spanish', additional_kwargs={}, response_metadata={}, id='b373ad51-0d96-4dde-9fe3-c8d9828e0cc5'), AIMessage(content='Hola', additional_kwargs={}, response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash-lite', 'safety_ratings': []}, id='run--2f487ae6-3286-4949-8f18-3db50fd8f124-0', usage_metadata={'input_tokens': 5, 'output_tokens': 1, 'total_tokens': 6, 'input_token_details': {'cache_read': 0}})]}
    for message in output['messages']:
        print("Message type:", type(message), "content:", getattr(message, 'content', None))
        if isinstance(message, AIMessage):
            return message.content
    return "No response from agent"
