import httpx
import os
from typing import Dict, Any, Optional
import json

class WeaviateClient:
    def __init__(self):
        # Get base URL from environment or use default
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.weaviate_endpoint = f"{self.base_url}/weaviate/test"
        self.timeout = httpx.Timeout(30.0)
        
    async def test_connection(self) -> Dict[str, Any]:
        """Test Weaviate connection through PSA service."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.weaviate_endpoint}/connection")
                return {
                    "connected": response.status_code == 200,
                    "message": response.text if response.status_code == 200 else f"Failed with status {response.status_code}",
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "connected": False,
                "message": f"Connection failed: {str(e)}",
                "error": str(e)
            }
    
    async def check_schema_exists(self) -> Dict[str, Any]:
        """Check if Weaviate schema exists."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.weaviate_endpoint}/schema/exists")
                if response.status_code == 200:
                    # Parse the response to get boolean value
                    text = response.text
                    schema_exists = "true" in text.lower()
                    return {
                        "success": True,
                        "schema_exists": schema_exists,
                        "raw_response": text
                    }
                return {
                    "success": False,
                    "error": f"Failed with status {response.status_code}",
                    "response": response.text
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def create_schema(self) -> Dict[str, Any]:
        """Create Weaviate schema."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(f"{self.weaviate_endpoint}/schema/create")
                return {
                    "success": response.status_code == 200,
                    "message": response.text,
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def delete_schema(self) -> Dict[str, Any]:
        """Delete Weaviate schema."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.delete(f"{self.weaviate_endpoint}/schema/delete")
                return {
                    "success": response.status_code == 200,
                    "message": response.text,
                    "status_code": response.status_code
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }