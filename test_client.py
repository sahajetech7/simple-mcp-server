import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Create server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        cwd=r"C:\Users\sahaj\simple-mcp-server"
    )
    
    # Create and connect client
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            
            # Call the get_tickets_by_domain tool
            result = await session.call_tool(
                "get_tickets_by_domain",
                arguments={"domain": "etech7"}
            )
            
            print("\nTickets found:")
            for ticket in result.content:
                # result.content is already a list of dicts after the fix
                print(ticket)

        # After listing tools, test the new Weaviate tools
        print("\n--- Testing Weaviate Tools ---")

        # Test connection
        connection_result = await session.call_tool(
            "test_weaviate_connection",
            arguments={}
        )
        print(f"Connection test: {connection_result.content}")

        # Check schema
        schema_result = await session.call_tool(
            "check_weaviate_schema",
            arguments={}
        )
        print(f"Schema check: {schema_result.content}")

if __name__ == "__main__":
    asyncio.run(main())