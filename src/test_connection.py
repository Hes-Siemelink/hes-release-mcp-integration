import asyncio

from digitalai.release.integration import BaseTask
from fastmcp import Client

from src.call_tool import create_transport


class TestConnection(BaseTask):
    """
        Testing connection to the remote server
    """

    def execute(self) -> None:

        try:
            # Process input
            server = self.input_properties['server']
            if server is None:
                raise ValueError("Server field cannot be empty")

            # Make request
            transport = create_transport(server)
            client = Client(transport)
            output = asyncio.run(ping(client))

            # Process result
            result = {"success": True, "output": "Connection success"}
        except Exception as e:
            result = {"success": False, "output": str(e)}
        finally:
            self.set_output_property("commandResponse", result)


# Async method to call tool
async def ping(client):
    async with client:
        return await client.ping()
