import httpx
import os
from typing import Dict, Any, List, Optional

class ConnectWiseTicketingClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.timeout = httpx.Timeout(30.0)
        
    async def get_ticket_categorization(self, msp_custom_domain: str, user_id: str, user_message: str) -> Dict[str, Any]:
        """
        Get AI-powered ticket categorization based on user message.
        Analyzes the message and suggests appropriate categories, priority, etc.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/getTicketCategorization",
                    json={
                        "mspCustomDomain": msp_custom_domain,
                        "userId": user_id,
                        "userMessage": user_message
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "categorization": response.json()
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
    
    async def get_ticket_board_categorization(self, msp_custom_domain: str, user_id: str, user_message: str) -> Dict[str, Any]:
        """
        Get ticket categorization with board-specific details.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/getTicketBoardCategorization",
                    json={
                        "mspCustomDomain": msp_custom_domain,
                        "userId": user_id,
                        "userMessage": user_message
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "board_categorization": response.json()
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
    
    async def get_ticket_diagnostic_qa(self, msp_custom_domain: str, user_id: str, user_message: str) -> Dict[str, Any]:
        """
        Get diagnostic Q&A for ticket categorization.
        Returns follow-up questions to better understand the issue.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/getTicketBoardCategorizationDiagnosticQandA",
                    json={
                        "mspCustomDomain": msp_custom_domain,
                        "userId": user_id,
                        "userMessage": user_message
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "diagnostic_qa": response.json()
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
    
    async def create_board_ticket(self, msp_custom_domain: str, ticket_details: Dict[str, Any], user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new ticket on a specific board.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                params = {"mspCustomDomain": msp_custom_domain}
                if user_id:
                    params["userId"] = user_id
                    
                response = await client.post(
                    f"{self.base_url}/createBoardTicket",
                    params=params,
                    json=ticket_details
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "ticket": response.json()
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
    
    async def update_ticket(self, msp_custom_domain: str, ticket_id: str, ticket_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing ticket.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.put(
                    f"{self.base_url}/updateTicket/{ticket_id}",
                    params={"mspCustomDomain": msp_custom_domain},
                    json=ticket_details
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "updated_ticket": response.json()
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
    
    async def get_ticket_by_id(self, msp_custom_domain: str, ticket_id: str) -> Dict[str, Any]:
        """
        Get ticket details by ID.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/getTicketsById",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "ticket": response.json()
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
    
    async def get_ticket_notes(self, msp_custom_domain: str, ticket_id: str, detailed: bool = True) -> Dict[str, Any]:
        """
        Get notes for a ticket.
        """
        try:
            endpoint = "/getConnectWiseTicketNotesById" if detailed else "/getTicketNotesById"
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}{endpoint}",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "notes": response.json()
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
    
    async def add_note_to_ticket(self, 
                                msp_custom_domain: str, 
                                ticket_id: int, 
                                note_info: str,
                                note_text: str,
                                detail_description: bool = False,
                                internal_analysis: bool = False,
                                resolution: bool = False) -> Dict[str, Any]:
        """
        Add a note to an existing ticket.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/addNoteToTicketObject",
                    params={
                        "mspCustomDomain": msp_custom_domain,
                        "ticketId": ticket_id,
                        "detailDescriptionFlag": detail_description,
                        "internalAnalysisFlag": internal_analysis,
                        "resolutionFlag": resolution
                    },
                    json={
                        "info": note_info,
                        "text": note_text
                    }
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "note": response.json()
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
    
    async def complete_ticket(self, 
                            msp_custom_domain: str, 
                            ticket_id: str, 
                            board_id: int,
                            tech_id: str,
                            notes: Optional[str] = None,
                            status: Optional[str] = None) -> Dict[str, Any]:
        """
        Complete a ticket and update queue status.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                params = {
                    "mspCustomDomain": msp_custom_domain,
                    "ticketId": ticket_id,
                    "boardId": board_id,
                    "techId": tech_id
                }
                if notes:
                    params["notes"] = notes
                if status:
                    params["status"] = status
                    
                response = await client.post(
                    f"{self.base_url}/completeTicketForQueueAndConnectwise",
                    params=params
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "message": "Ticket completed successfully"
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