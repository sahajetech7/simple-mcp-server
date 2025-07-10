import httpx
import os
from typing import List, Dict, Any, Optional

class PSAInitializationClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.psa_endpoint = f"{self.base_url}/psa"
        self.timeout = httpx.Timeout(30.0)
        
    async def get_clients(self, msp_custom_domain: str) -> Dict[str, Any]:
        """
        Get all PSA clients for an MSP domain.
        This is a generic endpoint that works across different PSA systems.
        
        Args:
            msp_custom_domain: The MSP custom domain
            
        Returns:
            Dictionary containing list of clients or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.psa_endpoint}/getClients",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                
                if response.status_code == 204:
                    return {
                        "success": True,
                        "clients": [],
                        "message": "No clients found"
                    }
                elif response.status_code == 200:
                    return {
                        "success": True,
                        "clients": response.json()
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
    
    async def get_contacts(self, msp_custom_domain: str) -> Dict[str, Any]:
        """
        Get all PSA contacts for an MSP domain.
        This is a generic endpoint that works across different PSA systems.
        
        Args:
            msp_custom_domain: The MSP custom domain
            
        Returns:
            Dictionary containing list of contacts or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.psa_endpoint}/getContacts",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                
                if response.status_code == 204:
                    return {
                        "success": True,
                        "contacts": [],
                        "message": "No contacts found"
                    }
                elif response.status_code == 200:
                    return {
                        "success": True,
                        "contacts": response.json()
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
    
    async def get_members(self, msp_custom_domain: str) -> Dict[str, Any]:
        """
        Get all PSA members (technicians/employees) for an MSP domain.
        This is a generic endpoint that works across different PSA systems.
        
        Args:
            msp_custom_domain: The MSP custom domain
            
        Returns:
            Dictionary containing list of members or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.psa_endpoint}/getMembers",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                
                if response.status_code == 204:
                    return {
                        "success": True,
                        "members": [],
                        "message": "No members found"
                    }
                elif response.status_code == 200:
                    return {
                        "success": True,
                        "members": response.json()
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
    
    async def add_contact(self, 
                         msp_custom_domain: str,
                         contact_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a new contact to the PSA system.
        This is a generic endpoint that works across different PSA systems.
        
        Args:
            msp_custom_domain: The MSP custom domain
            contact_data: Contact information including:
                - firstName: Contact's first name
                - lastName: Contact's last name
                - email: Contact's email
                - phone: Contact's phone (optional)
                - psaCompanyId: ID of the company in PSA system
                - emailTypeId: Email type ID (optional, for ConnectWise)
                - phoneTypeId: Phone type ID (optional, for ConnectWise)
            
        Returns:
            Dictionary containing created contact or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.psa_endpoint}/{msp_custom_domain}/addPSAContact",
                    json=contact_data
                )
                
                if response.status_code == 404:
                    return {
                        "success": False,
                        "error": "PSA integration not found or contact creation failed",
                        "message": "No PSA integration configured for this domain"
                    }
                elif response.status_code == 200:
                    return {
                        "success": True,
                        "contact": response.json()
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