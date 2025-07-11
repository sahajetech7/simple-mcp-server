import httpx
import os
from typing import Dict, Any, Optional

class PSATicketingClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:8080")
        self.timeout = httpx.Timeout(30.0)
        
    async def get_ticket_diagnostic_qa(self, 
                                     msp_custom_domain: str, 
                                     user_message: str,
                                     user_id: Optional[str] = None,
                                     tech_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get diagnostic Q&A for ticket categorization.
        Either user_id or tech_id must be provided.
        """
        try:
            request_body = {
                "mspCustomDomain": msp_custom_domain,
                "userMessage": user_message
            }
            
            if user_id:
                request_body["userId"] = user_id
            if tech_id:
                request_body["techId"] = tech_id
                
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/getTicketCategorizationDiagnosticQandA",
                    json=request_body
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "diagnostic_qa": response.json()
                    }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "Bad Request",
                        "message": "Either userId or techId must be provided"
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
    
    async def create_ticket(self, 
                          msp_custom_domain: str, 
                          ticket_request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new ticket in the PSA system.
        Requires specific fields based on PSA type.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/createTicket",
                    params={"mspCustomDomain": msp_custom_domain},
                    json=ticket_request
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "ticket": response.json()
                    }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "Bad Request",
                        "message": response.text
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
    
    async def add_notes_to_ticket(self, 
                                msp_custom_domain: str, 
                                ticket_id: str,
                                notes_request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add notes to an existing ticket.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/addNotesToTicket",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id
                    },
                    json=notes_request
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "result": response.json()
                    }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "Bad Request",
                        "message": response.text
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
    
    async def get_ticket_notes(self, 
                             msp_custom_domain: str, 
                             ticket_id: str,
                             is_detailed: bool = False) -> Dict[str, Any]:
        """
        Get notes for a specific ticket.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getTicketNotes",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id,
                        "isdetailed": is_detailed
                    }
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "notes": response.json()
                    }
                elif response.status_code == 404:
                    return {
                        "success": False,
                        "error": "Not Found",
                        "message": "Ticket or notes not found"
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
    
    async def close_ticket(self, 
                         msp_custom_domain: str, 
                         ticket_id: str,
                         board_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Close a ticket in the PSA system.
        """
        try:
            params = {
                "mspCustomDomain": msp_custom_domain,
                "ticketId": ticket_id
            }
            if board_id is not None:
                params["boardId"] = board_id
                
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/closeTicket",
                    params=params
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "result": response.json()
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
    
    async def get_ticket_status(self, 
                              msp_custom_domain: str, 
                              ticket_id: str) -> Dict[str, Any]:
        """
        Get the current status of a ticket.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getTicketStatus",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id
                    }
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "status": response.json()
                    }
                elif response.status_code == 404:
                    return {
                        "success": False,
                        "error": "Not Found",
                        "message": "Ticket not found"
                    }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "Bad Request",
                        "message": "Ticket ID is required"
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