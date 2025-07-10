import httpx
import os
from typing import List, Dict, Any

class ConnectWiseSyncClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.timeout = httpx.Timeout(60.0)  # Longer timeout for sync operations
        
    async def sync_clients_contacts(self, msp_custom_domain: str) -> Dict[str, Any]:
        """
        Sync all clients and contacts from ConnectWise.
        This operation fetches and updates the local database with ConnectWise data.
        
        Args:
            msp_custom_domain: The MSP custom domain
            
        Returns:
            Dictionary with sync results or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/syncClientsContacts",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "sync_result": response.json(),
                        "message": "Clients and contacts synced successfully"
                    }
                return {
                    "success": False,
                    "error": f"Failed with status {response.status_code}",
                    "message": response.text
                }
        except httpx.TimeoutError:
            return {
                "success": False,
                "error": "Sync operation timed out",
                "message": "The sync is taking longer than expected. It may still be running in the background."
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    async def sync_board_tickets(self, msp_custom_domain: str, board_sync_requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Sync tickets for specific boards from ConnectWise.
        
        Args:
            msp_custom_domain: The MSP custom domain
            board_sync_requests: List of board sync configurations
                Each item should have:
                - boardId: ID of the board to sync
                - boardName: Name of the board
                - syncFromDate: Optional date to sync from (ISO format)
                - syncStatus: Optional list of statuses to sync
                
        Returns:
            Dictionary with sync results or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/syncBoardTickets",
                    params={"mspCustomDomain": msp_custom_domain},
                    json=board_sync_requests
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "message": "Board tickets sync initiated successfully",
                        "boards_synced": len(board_sync_requests)
                    }
                return {
                    "success": False,
                    "error": f"Failed with status {response.status_code}",
                    "message": response.text
                }
        except httpx.TimeoutError:
            return {
                "success": False,
                "error": "Sync operation timed out",
                "message": "The sync is taking longer than expected. It may still be running in the background."
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }