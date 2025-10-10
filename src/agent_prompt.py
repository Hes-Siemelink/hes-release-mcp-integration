import asyncio
import os

from digitalai.release.integration import BaseTask
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
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
        model_connector = create_model(model)
        output = asyncio.run(send_prompt(prompt, model_connector, mcp_servers))
        print("AgentPrompt Result:\n", output)

        report = create_markdown_report(output)
        print(report)
        self.add_comment(report)

        # Process result
        result = last_agent_message(output)
        self.set_output_property('result', result)


async def send_prompt(prompt, model, mcp_servers):
    client = MultiServerMCPClient(mcp_servers)
    tools = await client.get_tools()

    agent = create_react_agent(model=model, tools=tools)

    response = await agent.ainvoke({"messages": prompt})

    return response


def create_model(model):
    provider = model['provider']
    
    if provider == 'gemini':
        return ChatGoogleGenerativeAI(
            model=model['model_id'],
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
    if provider == 'openai':
        return ChatOpenAI(
            base_url=model['url'],
            default_headers={'Authorization': f'Token {model["apiKey"]}'},
            model=model['model_id'],
            temperature=0.0,
            api_key=model["apiKey"]
        )
    raise ValueError(f"Provider {provider} is not supported")


def last_agent_message(output):
    return output['messages'][-1].content


def create_markdown_report(output):
    markdown = ''
    for message in output['messages']:
        if isinstance(message, HumanMessage):
            markdown += f"_{message.content}_\n\n"
        if isinstance(message, AIMessage):
            if message.content:
                markdown += f"{message.content}\n\n"
        if isinstance(message, ToolMessage):
            success = message.status == 'success'
            status = "✅" if success else "❌"
            markdown += f"```\n {status} {message.name}\n```\n\n"
            if not success:
                markdown += f"```\n{message.content}\n```\n\n"

    return markdown
