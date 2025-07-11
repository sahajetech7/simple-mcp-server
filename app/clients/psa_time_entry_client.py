import httpx
import os
from typing import Dict, Any, Optional
from datetime import datetime

class PSATimeEntryClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:8080")
        self.api_endpoint = f"{self.base_url}/api/psa"
        self.timeout = httpx.Timeout(30.0)
        
    async def create_time_entry(self, time_entry_request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a time entry in the PSA system.
        
        Args:
            time_entry_request: Dictionary containing time entry details
                - mspCustomDomain: MSP domain
                - ticketId: Ticket ID to log time against
                - technicianId: ID of the technician
                - timeSpent: Time spent (in minutes or hours based on PSA)
                - notes: Description of work performed
                - workDate: Date of work (optional)
                - billable: Whether the time is billable (optional)
                
        Returns:
            Dictionary with time entry creation results
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.api_endpoint}/time-entries",
                    json=time_entry_request
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return {
                        "success": result.get("success", True),
                        "time_entry": result,
                        "message": "Time entry created successfully"
                    }
                elif response.status_code == 500:
                    error_data = response.json()
                    return {
                        "success": False,
                        "error": error_data.get("error", "Time entry creation failed"),
                        "details": error_data
                    }
                else:
                    return {
                        "success": False,
                        "error": f"Failed with status {response.status_code}",
                        "message": response.text
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def check_service_health(self) -> Dict[str, Any]:
        """
        Check the health status of the PSA time entry service.
        
        Returns:
            Dictionary with service health information
        """
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(10.0)) as client:
                response = await client.get(f"{self.api_endpoint}/health")
                
                if response.status_code == 200:
                    health_data = response.json()
                    return {
                        "success": True,
                        "healthy": health_data.get("status") == "UP",
                        "service": health_data.get("service"),
                        "timestamp": health_data.get("timestamp"),
                        "status": health_data.get("status")
                    }
                else:
                    return {
                        "success": False,
                        "healthy": False,
                        "error": f"Health check failed with status {response.status_code}"
                    }
        except Exception as e:
            return {
                "success": False,
                "healthy": False,
                "error": f"Health check failed: {str(e)}"
            }