import httpx
import os
from typing import List, Dict

class PSAClient:
    def __init__(self):
        self.use_mock = os.getenv("USE_MOCK_DATA", "false").lower() == "true"
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:8080")
        self.timeout = httpx.Timeout(30.0)
        
    async def get_tickets_by_domain(self, domain: str) -> List[Dict]:
        """Get tickets for a domain."""
        
        if self.use_mock:
            # Return mock data for testing
            return [
                {
                    "id": "1",
                    "title": "Printer not working",
                    "status": "Open",
                    "priority": "High",
                    "created_at": "2024-01-15T10:00:00Z",
                    "updated_at": "2024-01-15T14:30:00Z"
                },
                {
                    "id": "2",
                    "title": "Email issues",
                    "status": "In Progress",
                    "priority": "Medium",
                    "created_at": "2024-01-14T09:00:00Z",
                    "updated_at": "2024-01-15T11:00:00Z"
                }
            ]
        
        # Real API call
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # Adjust the endpoint based on your actual PSA API
                response = await client.get(
                    f"{self.base_url}/api/tickets",
                    params={"domain": domain}
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            return [{
                "error": f"HTTP error: {e.response.status_code}",
                "message": str(e)
            }]
        except Exception as e:
            return [{
                "error": "Connection error",
                "message": str(e)
            }]