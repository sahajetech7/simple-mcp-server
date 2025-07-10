import httpx
import os
from typing import List, Dict, Any, Optional

class ConnectWiseClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.timeout = httpx.Timeout(30.0)
        
    # Board Management
    async def create_board(self, board_request: Dict[str, Any], msp_custom_domain: str) -> Dict[str, Any]:
        """Create a new ConnectWise board"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/createConnectWiseBoard",
                    params={"mspCustomDomain": msp_custom_domain},
                    json=board_request
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "board": response.json()
                    }
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
    
    async def get_boards(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise boards"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseBoards",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "boards": response.json()
                    }
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
    
    async def get_statuses(self, board_id: int, msp_custom_domain: str) -> Dict[str, Any]:
        """Get statuses for a specific board"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseStatuses",
                    params={
                        "boardId": board_id,
                        "mspCustomDomain": msp_custom_domain
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "statuses": response.json()
                    }
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
    
    async def get_clients(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise clients"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseClients",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "clients": response.json()
                    }
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
    
    async def get_contacts(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise contacts"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseContacts",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "contacts": response.json()
                    }
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
    
    async def get_members(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise members (technicians)"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseMembers",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "members": response.json()
                    }
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
    
    async def get_departments(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise departments"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWiseDepartments",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "departments": response.json()
                    }
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
    
    async def get_priorities(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ConnectWise priorities"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getConnectWisePriorities",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "priorities": response.json()
                    }
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
    
    async def get_configuration(self, msp_custom_domain: str, board_id: int, board_name: str) -> Dict[str, Any]:
        """Get merged categorization configuration for a board"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getMergedConnectWiseCategorizationWithoutImpactSeverity",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "boardId": board_id,
                        "boardName": board_name
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "configuration": response.json()
                    }
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
    
    async def add_contact(self, msp_custom_domain: str, contact_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new contact in ConnectWise"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/addConnectWiseContact",
                    params={"mspCustomDomain": msp_custom_domain},
                    json=contact_data
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "contact": response.json()
                    }
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