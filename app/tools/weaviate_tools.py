from typing import Dict, Any
from server import mcp
from app.clients.weaviate_client import WeaviateClient

@mcp.tool
async def test_weaviate_connection() -> Dict[str, Any]:
    """
    Test the connection to Weaviate database.
    
    Returns:
        Dictionary with connection status
    """
    client = WeaviateClient()
    connected = await client.test_connection()
    return {
        "connected": connected,
        "message": "Weaviate connection successful" if connected else "Failed to connect to Weaviate"
    }

@mcp.tool
async def check_weaviate_schema() -> Dict[str, bool]:
    """
    Check if the Weaviate schema exists.
    
    Returns:
        Dictionary indicating if schema exists
    """
    client = WeaviateClient()
    exists = await client.check_schema_exists()
    return {"schema_exists": exists}

@mcp.tool
async def create_weaviate_schema() -> Dict[str, str]:
    """
    Create the Weaviate schema if it doesn't exist.
    
    Returns:
        Dictionary with operation status
    """
    client = WeaviateClient()
    
    # Check if schema already exists
    if await client.check_schema_exists():
        return {"status": "exists", "message": "Schema already exists"}
    
    # Create schema
    success = await client.create_schema()
    return {
        "status": "created" if success else "failed",
        "message": "Schema created successfully" if success else "Failed to create schema"
    }

@mcp.tool
async def delete_weaviate_schema() -> Dict[str, str]:
    """
    Delete the Weaviate schema (use with caution).
    
    Returns:
        Dictionary with operation status
    """
    client = WeaviateClient()
    success = await client.delete_schema()
    return {
        "status": "deleted" if success else "failed",
        "message": "Schema deleted successfully" if success else "Failed to delete schema"
    }