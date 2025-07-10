import httpx
import os
from typing import List, Dict, Any, Optional

class AutotaskClient:
    def __init__(self):
        self.base_url = os.getenv("PSA_SERVICE_URL", "http://localhost:9030")
        self.autotask_endpoint = f"{self.base_url}/autotask"
        self.timeout = httpx.Timeout(30.0)
    
    async def get_statuses(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all statuses for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getStatuses",
                    params={"mspCustomDomain": msp_custom_domain}
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
    
    async def get_priorities(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all priorities for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getPriorities",
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
    
    async def get_issue_types(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all issue types for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getIssueTypes",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "issue_types": response.json()
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
    
    async def get_ticket_categories(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ticket categories for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getTicketCategories",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "categories": response.json()
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
    
    async def get_ticket_types(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all ticket types for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getTicketTypes",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "ticket_types": response.json()
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
    
    async def get_queues(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all queues for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getQueues",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "queues": response.json()
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
    
    async def get_queue_details(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get detailed queue information for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getQueueDetails",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "queue_details": response.json()
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
    
    async def get_sources(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all sources for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getSources",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "sources": response.json()
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
    
    async def get_all_companies(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all companies for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getAllCompanies",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "companies": response.json()
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
    
    async def get_all_contacts(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all contacts for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getAllContacts",
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
    
    async def get_all_resources(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get all resources for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/getAllResources",
                    params={"mspCustomDomain": msp_custom_domain}
                )
                if response.status_code == 200:
                    return {
                        "success": True,
                        "resources": response.json()
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
    
    async def merge_queues_and_issue_types(self, msp_custom_domain: str) -> Dict[str, Any]:
        """Get merged configuration of queues and issue types for an MSP domain."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.autotask_endpoint}/mergeQueuesAndIssueTypes",
                    params={"mspCustomDomain": msp_custom_domain}
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