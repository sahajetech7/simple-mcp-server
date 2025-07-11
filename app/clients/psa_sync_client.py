import httpx
import os
from typing import Dict, Any

class PSASyncClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:8080")
        self.sync_endpoint = f"{self.base_url}/psa/sync"
        self.timeout = httpx.Timeout(60.0)  # Longer timeout for sync operations
        
    async def sync_tickets_for_domain(self, msp_custom_domain: str) -> Dict[str, Any]:
        """
        Manually trigger ticket sync for a specific MSP domain.
        This syncs tickets from the configured PSA system to the local database.
        
        Args:
            msp_custom_domain: The MSP custom domain to sync
            
        Returns:
            Dictionary with sync status or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.sync_endpoint}/tickets",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "message": response.text,
                        "domain": msp_custom_domain
                    }
                elif response.status_code == 400:
                    return {
                        "success": False,
                        "error": "Bad Request",
                        "message": response.text,
                        "domain": msp_custom_domain
                    }
                else:
                    return {
                        "success": False,
                        "error": f"Failed with status {response.status_code}",
                        "message": response.text,
                        "domain": msp_custom_domain
                    }
        except httpx.TimeoutError:
            return {
                "success": False,
                "error": "Sync operation timed out",
                "message": "The sync is taking longer than expected. It may still be running in the background.",
                "domain": msp_custom_domain
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "domain": msp_custom_domain
            }
    
    async def sync_all_domains(self) -> Dict[str, Any]:
        """
        Manually trigger ticket sync for all configured MSP domains.
        This syncs tickets from all PSA systems to the local database.
        
        Returns:
            Dictionary with sync status or error information
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(f"{self.sync_endpoint}/all")
                
                if response.status_code == 200:
                    return {
                        "success": True,
                        "message": response.text,
                        "scope": "all_domains"
                    }
                else:
                    return {
                        "success": False,
                        "error": f"Failed with status {response.status_code}",
                        "message": response.text,
                        "scope": "all_domains"
                    }
        except httpx.TimeoutError:
            return {
                "success": False,
                "error": "Sync operation timed out",
                "message": "The sync is taking longer than expected. It may still be running in the background.",
                "scope": "all_domains"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "scope": "all_domains"
            }