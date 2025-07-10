import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

# Create the MCP server
mcp = FastMCP("Simple PSA Server")

# Import dependencies
from app.schemas.ticket import Ticket
from app.clients.psa_client import PSAClient
from app.clients.weaviate_client import WeaviateClient

# ========== Ticket Tools ==========

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

# ========== Weaviate Tools ==========

@mcp.tool
async def test_weaviate_connection() -> Dict[str, Any]:
    """
    Test the connection to Weaviate database through PSA service.
    
    Returns:
        Dictionary with connection status and details
    """
    client = WeaviateClient()
    return await client.test_connection()

@mcp.tool
async def check_weaviate_schema() -> Dict[str, Any]:
    """
    Check if the Weaviate schema exists in the PSA service.
    
    Returns:
        Dictionary with schema existence status
    """
    client = WeaviateClient()
    return await client.check_schema_exists()

@mcp.tool
async def create_weaviate_schema() -> Dict[str, Any]:
    """
    Create the Weaviate schema through PSA service if it doesn't exist.
    
    Returns:
        Dictionary with operation status and message
    """
    client = WeaviateClient()
    
    # First check if schema exists
    check_result = await client.check_schema_exists()
    if check_result.get("success") and check_result.get("schema_exists"):
        return {
            "success": True,
            "status": "already_exists",
            "message": "Schema already exists"
        }
    
    # Create schema
    return await client.create_schema()

@mcp.tool
async def delete_weaviate_schema() -> Dict[str, Any]:
    """
    Delete the Weaviate schema from PSA service (use with caution).
    
    Returns:
        Dictionary with operation status and message
    """
    client = WeaviateClient()
    return await client.delete_schema()
# ========== Autotask Tools ==========

from app.clients.autotask_client import AutotaskClient

@mcp.tool
async def get_autotask_statuses(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket statuses from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of statuses or error information
    """
    client = AutotaskClient()
    return await client.get_statuses(msp_custom_domain)

@mcp.tool
async def get_autotask_priorities(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket priorities from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of priorities or error information
    """
    client = AutotaskClient()
    return await client.get_priorities(msp_custom_domain)

@mcp.tool
async def get_autotask_issue_types(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all issue types from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of issue types or error information
    """
    client = AutotaskClient()
    return await client.get_issue_types(msp_custom_domain)

@mcp.tool
async def get_autotask_ticket_categories(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket categories from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of ticket categories or error information
    """
    client = AutotaskClient()
    return await client.get_ticket_categories(msp_custom_domain)

@mcp.tool
async def get_autotask_ticket_types(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket types from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of ticket types or error information
    """
    client = AutotaskClient()
    return await client.get_ticket_types(msp_custom_domain)

@mcp.tool
async def get_autotask_queues(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all queues from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of queues or error information
    """
    client = AutotaskClient()
    return await client.get_queues(msp_custom_domain)

@mcp.tool
async def get_autotask_queue_details(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get detailed queue information from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing detailed queue information or error information
    """
    client = AutotaskClient()
    return await client.get_queue_details(msp_custom_domain)

@mcp.tool
async def get_autotask_sources(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket sources from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of sources or error information
    """
    client = AutotaskClient()
    return await client.get_sources(msp_custom_domain)

@mcp.tool
async def get_autotask_companies(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all companies from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of companies or error information
    """
    client = AutotaskClient()
    return await client.get_all_companies(msp_custom_domain)

@mcp.tool
async def get_autotask_contacts(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all contacts from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of contacts or error information
    """
    client = AutotaskClient()
    return await client.get_all_contacts(msp_custom_domain)

@mcp.tool
async def get_autotask_resources(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all resources (technicians/employees) from Autotask for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of resources or error information
    """
    client = AutotaskClient()
    return await client.get_all_resources(msp_custom_domain)

@mcp.tool
async def get_autotask_configuration(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get merged configuration of queues and issue types from Autotask for an MSP domain.
    This provides a complete ticketing configuration including PSA type.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing PSA ticketing configuration or error information
    """
    client = AutotaskClient()
    return await client.merge_queues_and_issue_types(msp_custom_domain)

# Add this import after your other client imports
from app.clients.connectwise_client import ConnectWiseClient

# ========== ConnectWise Tools ==========

@mcp.tool
async def get_connectwise_boards(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all boards from ConnectWise for an MSP domain.
    Boards are used to organize tickets by type (e.g., Service Board, Project Board).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of boards or error information
    """
    client = ConnectWiseClient()
    return await client.get_boards(msp_custom_domain)

@mcp.tool
async def get_connectwise_board_statuses(msp_custom_domain: str, board_id: int) -> Dict[str, Any]:
    """
    Get all statuses for a specific ConnectWise board.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_id: The ID of the board
        
    Returns:
        Dictionary containing list of statuses or error information
    """
    client = ConnectWiseClient()
    return await client.get_statuses(board_id, msp_custom_domain)

@mcp.tool
async def get_connectwise_clients(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all clients/companies from ConnectWise for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of clients or error information
    """
    client = ConnectWiseClient()
    return await client.get_clients(msp_custom_domain)

@mcp.tool
async def get_connectwise_contacts(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all contacts from ConnectWise for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of contacts or error information
    """
    client = ConnectWiseClient()
    return await client.get_contacts(msp_custom_domain)

@mcp.tool
async def get_connectwise_members(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all members (technicians/employees) from ConnectWise for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of members or error information
    """
    client = ConnectWiseClient()
    return await client.get_members(msp_custom_domain)

@mcp.tool
async def get_connectwise_departments(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all departments from ConnectWise for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of departments or error information
    """
    client = ConnectWiseClient()
    return await client.get_departments(msp_custom_domain)

@mcp.tool
async def get_connectwise_priorities(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all ticket priorities from ConnectWise for an MSP domain.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of priorities or error information
    """
    client = ConnectWiseClient()
    return await client.get_priorities(msp_custom_domain)

@mcp.tool
async def get_connectwise_board_configuration(msp_custom_domain: str, board_id: int, board_name: str) -> Dict[str, Any]:
    """
    Get the complete configuration for a ConnectWise board including categories and subcategories.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_id: The ID of the board
        board_name: The name of the board
        
    Returns:
        Dictionary containing board configuration or error information
    """
    client = ConnectWiseClient()
    return await client.get_configuration(msp_custom_domain, board_id, board_name)

@mcp.tool
async def create_connectwise_board(msp_custom_domain: str, board_name: str, board_type: str = "Service") -> Dict[str, Any]:
    """
    Create a new board in ConnectWise.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_name: Name for the new board
        board_type: Type of board (default: "Service")
        
    Returns:
        Dictionary containing created board information or error
    """
    client = ConnectWiseClient()
    board_request = {
        "name": board_name,
        "type": board_type
    }
    return await client.create_board(board_request, msp_custom_domain)

@mcp.tool
async def add_connectwise_contact(
    msp_custom_domain: str,
    first_name: str,
    last_name: str,
    email: str,
    company_id: int,
    phone_number: str = None,
    title: str = None
) -> Dict[str, Any]:
    """
    Add a new contact to ConnectWise.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        first_name: Contact's first name
        last_name: Contact's last name
        email: Contact's email address
        company_id: ID of the company this contact belongs to
        phone_number: Contact's phone number (optional)
        title: Contact's job title (optional)
        
    Returns:
        Dictionary containing created contact information or error
    """
    client = ConnectWiseClient()
    contact_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "companyId": company_id
    }
    
    if phone_number:
        contact_data["phoneNumber"] = phone_number
    if title:
        contact_data["title"] = title
        
    return await client.add_contact(msp_custom_domain, contact_data)

# Run the server
if __name__ == "__main__":
    mcp.run()