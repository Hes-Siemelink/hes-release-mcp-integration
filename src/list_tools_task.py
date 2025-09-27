from digitalai.release.integration import BaseTask

import asyncio
from fastmcp import Client
import json
from mcp.types import Tool

from src.call_tool_task import create_transport


class ListTools(BaseTask):

    def execute(self) -> None:
        # Process input
        server = self.input_properties['server']
        if server is None:
            raise ValueError("Server field cannot be empty")
        transport = create_transport(server)

        # Make request
        client = Client(transport)
        output = asyncio.run(list_tools(client))

        # Process result
        self.set_output_property('tools', extract_tools(output))
        self.set_output_property('inputSchema', extract_input_schema(output))


# Async method to call tool
async def list_tools(client):
    async with client:
        return await client.list_tools()


def extract_tools(result: list[Tool]):
    # Create a dict with tool names as keys and descriptions as values
    return {tool.name: tool.description for tool in result}


def extract_input_schema(result: Tool):
    return {tool.name: convert_dict_to_pretty_json(tool.inputSchema) for tool in result}


def convert_dict_to_pretty_json(input_dict):
    return json.dumps(input_dict, indent=2)
