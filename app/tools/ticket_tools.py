from typing import List
from app.schemas.ticket import Ticket
from app.clients.psa_client import PSAClient
from server import mcp

@mcp.tool
async def get_tickets_by_domain(domain: str) -> List[dict]:
    """
    Get support tickets for a given domain.
    
    Args:
        domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        List of tickets for the domain
    """
    client = PSAClient()
    raw_tickets = await client.get_tickets_by_domain(domain)
    
    # Convert to Ticket objects for validation, then back to dict
    tickets = [Ticket(**ticket).model_dump() for ticket in raw_tickets]
    
    return tickets