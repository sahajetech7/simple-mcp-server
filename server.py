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

# Add this import after your other client imports
from app.clients.connectwise_sync_client import ConnectWiseSyncClient

# ========== ConnectWise Sync Tools ==========

@mcp.tool
async def sync_connectwise_clients_contacts(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Synchronize all clients and contacts from ConnectWise to local database.
    This is a full sync operation that updates local data with ConnectWise data.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing sync results or error information
    """
    client = ConnectWiseSyncClient()
    return await client.sync_clients_contacts(msp_custom_domain)

@mcp.tool
async def sync_connectwise_board_tickets(
    msp_custom_domain: str,
    board_id: int,
    board_name: str,
    sync_from_date: str = None,
    sync_statuses: List[str] = None
) -> Dict[str, Any]:
    """
    Synchronize tickets for a specific ConnectWise board.
    This syncs ticket data from ConnectWise to the local system.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_id: ID of the board to sync
        board_name: Name of the board to sync
        sync_from_date: Optional date to sync from (ISO format: YYYY-MM-DD)
        sync_statuses: Optional list of ticket statuses to sync (e.g., ['Open', 'In Progress'])
        
    Returns:
        Dictionary containing sync results or error information
    """
    client = ConnectWiseSyncClient()
    
    # Build board sync request
    board_sync_request = {
        "boardId": board_id,
        "boardName": board_name
    }
    
    if sync_from_date:
        board_sync_request["syncFromDate"] = sync_from_date
    
    if sync_statuses:
        board_sync_request["syncStatus"] = sync_statuses
    
    return await client.sync_board_tickets(msp_custom_domain, [board_sync_request])

@mcp.tool
async def sync_multiple_connectwise_boards(
    msp_custom_domain: str,
    board_configs: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Synchronize tickets for multiple ConnectWise boards at once.
    Useful for bulk sync operations across different boards.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_configs: List of board configurations, each containing:
            - board_id: ID of the board
            - board_name: Name of the board
            - sync_from_date: Optional date to sync from (ISO format)
            - sync_statuses: Optional list of statuses to sync
        
    Returns:
        Dictionary containing sync results or error information
        
    Example:
        board_configs = [
            {
                "board_id": 1,
                "board_name": "Service Board",
                "sync_from_date": "2024-01-01",
                "sync_statuses": ["Open", "In Progress"]
            },
            {
                "board_id": 2,
                "board_name": "Project Board"
            }
        ]
    """
    client = ConnectWiseSyncClient()
    
    # Transform the input format to match API expectations
    board_sync_requests = []
    for config in board_configs:
        request = {
            "boardId": config.get("board_id"),
            "boardName": config.get("board_name")
        }
        
        if "sync_from_date" in config:
            request["syncFromDate"] = config["sync_from_date"]
            
        if "sync_statuses" in config:
            request["syncStatus"] = config["sync_statuses"]
            
        board_sync_requests.append(request)
    
    return await client.sync_board_tickets(msp_custom_domain, board_sync_requests)

@mcp.tool
async def sync_all_connectwise_data(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Perform a complete synchronization of all ConnectWise data.
    This includes clients, contacts, and all available boards with tickets.
    Note: This is a long-running operation.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing comprehensive sync results
    """
    sync_results = {
        "clients_contacts_sync": None,
        "boards_sync": None,
        "overall_success": True,
        "errors": []
    }
    
    # First, sync clients and contacts
    sync_client = ConnectWiseSyncClient()
    cw_client = ConnectWiseClient()  # Reuse existing client
    
    # Sync clients and contacts
    clients_result = await sync_client.sync_clients_contacts(msp_custom_domain)
    sync_results["clients_contacts_sync"] = clients_result
    
    if not clients_result.get("success"):
        sync_results["overall_success"] = False
        sync_results["errors"].append("Failed to sync clients and contacts")
    
    # Get all boards to sync
    boards_result = await cw_client.get_boards(msp_custom_domain)
    
    if boards_result.get("success") and boards_result.get("boards"):
        # Prepare board sync requests
        board_configs = []
        for board in boards_result["boards"]:
            board_configs.append({
                "board_id": board.get("id"),
                "board_name": board.get("name")
            })
        
        # Sync all boards
        if board_configs:
            boards_sync_result = await sync_multiple_connectwise_boards(
                msp_custom_domain, 
                board_configs
            )
            sync_results["boards_sync"] = boards_sync_result
            
            if not boards_sync_result.get("success"):
                sync_results["overall_success"] = False
                sync_results["errors"].append("Failed to sync some boards")
    else:
        sync_results["errors"].append("Could not retrieve boards for sync")
        sync_results["overall_success"] = False
    
    return sync_results


# Add this import after your other client imports
from app.clients.connectwise_ticketing_client import ConnectWiseTicketingClient

# ========== ConnectWise Ticketing Tools ==========

@mcp.tool
async def analyze_ticket_request(
    msp_custom_domain: str,
    user_id: str,
    user_message: str
) -> Dict[str, Any]:
    """
    Analyze a user's ticket request and suggest categorization using AI.
    This tool helps determine the appropriate category, subcategory, priority, and other details.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        user_id: ID of the user submitting the request
        user_message: The user's description of their issue
        
    Returns:
        Dictionary containing AI-suggested categorization
    """
    client = ConnectWiseTicketingClient()
    return await client.get_ticket_categorization(msp_custom_domain, user_id, user_message)

@mcp.tool
async def get_ticket_diagnostic_questions(
    msp_custom_domain: str,
    user_id: str,
    user_message: str
) -> Dict[str, Any]:
    """
    Get diagnostic questions to better understand a ticket request.
    Returns follow-up questions that help clarify the issue.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        user_id: ID of the user submitting the request
        user_message: The user's description of their issue
        
    Returns:
        Dictionary containing diagnostic Q&A to clarify the issue
    """
    client = ConnectWiseTicketingClient()
    return await client.get_ticket_diagnostic_qa(msp_custom_domain, user_id, user_message)

@mcp.tool
async def create_connectwise_ticket(
    msp_custom_domain: str,
    board_id: int,
    summary: str,
    description: str,
    company_id: int,
    contact_id: int = None,
    priority_id: int = None,
    status_id: int = None,
    category_id: int = None,
    subcategory_id: int = None,
    user_id: str = None
) -> Dict[str, Any]:
    """
    Create a new ticket in ConnectWise on a specific board.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        board_id: ID of the board to create ticket on
        summary: Brief summary of the issue
        description: Detailed description of the issue
        company_id: ID of the company this ticket is for
        contact_id: ID of the contact reporting the issue (optional)
        priority_id: Priority ID for the ticket (optional)
        status_id: Initial status ID (optional)
        category_id: Category ID (optional)
        subcategory_id: Subcategory ID (optional)
        user_id: User ID creating the ticket (optional)
        
    Returns:
        Dictionary containing created ticket information
    """
    client = ConnectWiseTicketingClient()
    
    ticket_details = {
        "boardId": board_id,
        "summary": summary,
        "description": description,
        "companyId": company_id
    }
    
    if contact_id:
        ticket_details["contactId"] = contact_id
    if priority_id:
        ticket_details["priorityId"] = priority_id
    if status_id:
        ticket_details["statusId"] = status_id
    if category_id:
        ticket_details["categoryId"] = category_id
    if subcategory_id:
        ticket_details["subcategoryId"] = subcategory_id
    
    return await client.create_board_ticket(msp_custom_domain, ticket_details, user_id)

@mcp.tool
async def update_connectwise_ticket(
    msp_custom_domain: str,
    ticket_id: str,
    summary: str,
    description: str,
    priority_id: int,
    status_id: int,
    category_id: int,
    subcategory_id: int
) -> Dict[str, Any]:
    """
    Update an existing ConnectWise ticket.
    Only provide the fields you want to update.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket to update
        summary: New summary (optional)
        description: New description (optional)
        priority_id: New priority ID (optional)
        status_id: New status ID (optional)
        category_id: New category ID (optional)
        subcategory_id: New subcategory ID (optional)
        
    Returns:
        Dictionary containing updated ticket information
    """
    client = ConnectWiseTicketingClient()
    
    ticket_details = {}
    if summary:
        ticket_details["summary"] = summary
    if description:
        ticket_details["description"] = description
    if priority_id:
        ticket_details["priorityId"] = priority_id
    if status_id:
        ticket_details["statusId"] = status_id
    if category_id:
        ticket_details["categoryId"] = category_id
    if subcategory_id:
        ticket_details["subcategoryId"] = subcategory_id
    
    return await client.update_ticket(msp_custom_domain, ticket_id, ticket_details)


@mcp.tool
async def get_connectwise_ticket(
    msp_custom_domain: str,
    ticket_id: str
) -> Dict[str, Any]:
    """
    Get detailed information about a specific ConnectWise ticket.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket to retrieve
        
    Returns:
        Dictionary containing ticket details
    """
    client = ConnectWiseTicketingClient()
    return await client.get_ticket_by_id(msp_custom_domain, ticket_id)

@mcp.tool
async def get_connectwise_ticket_notes(
    msp_custom_domain: str,
    ticket_id: str,
    detailed: bool = True
) -> Dict[str, Any]:
    """
    Get all notes for a ConnectWise ticket.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        detailed: If True, returns detailed note objects; if False, returns simple text
        
    Returns:
        Dictionary containing ticket notes
    """
    client = ConnectWiseTicketingClient()
    return await client.get_ticket_notes(msp_custom_domain, ticket_id, detailed)

@mcp.tool
async def add_note_to_connectwise_ticket(
    msp_custom_domain: str,
    ticket_id: int,
    note_text: str,
    note_type: str = "general",
    is_internal: bool = False,
    is_resolution: bool = False
) -> Dict[str, Any]:
    """
    Add a note to an existing ConnectWise ticket.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        note_text: The note content to add
        note_type: Type of note - 'general', 'detail', or 'analysis'
        is_internal: Whether this is an internal note
        is_resolution: Whether this note represents the resolution
        
    Returns:
        Dictionary containing the created note
    """
    client = ConnectWiseTicketingClient()
    
    # Map note type to flags
    detail_description = note_type == "detail"
    internal_analysis = note_type == "analysis" or is_internal
    
    return await client.add_note_to_ticket(
        msp_custom_domain,
        ticket_id,
        f"Note added via MCP - Type: {note_type}",
        note_text,
        detail_description,
        internal_analysis,
        is_resolution
    )

@mcp.tool
async def complete_connectwise_ticket(
    msp_custom_domain: str,
    ticket_id: str,
    board_id: int,
    technician_id: str,
    completion_notes: str,
    final_status: str 
) -> Dict[str, Any]:
    """
    Mark a ConnectWise ticket as complete and update queue status.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket to complete
        board_id: ID of the board the ticket is on
        technician_id: ID of the technician completing the ticket
        completion_notes: Optional notes about the completion
        final_status: Final status to set (default: "Completed")
        
    Returns:
        Dictionary indicating success or failure
    """
    client = ConnectWiseTicketingClient()
    return await client.complete_ticket(
        msp_custom_domain,
        ticket_id,
        board_id,
        technician_id,
        completion_notes,
        final_status
    )

@mcp.tool
async def create_smart_ticket(
    msp_custom_domain: str,
    user_id: str,
    issue_description: str,
    company_id: int,
    contact_id: int 
) -> Dict[str, Any]:
    """
    Create a ticket with AI-powered categorization.
    This tool analyzes the issue description and automatically suggests appropriate categorization.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        user_id: ID of the user creating the ticket
        issue_description: Natural language description of the issue
        company_id: ID of the company this ticket is for
        contact_id: ID of the contact (optional)
        
    Returns:
        Dictionary containing the created ticket with AI categorization
    """
    client = ConnectWiseTicketingClient()
    
    # First, get AI categorization
    categorization_result = await client.get_ticket_board_categorization(
        msp_custom_domain, user_id, issue_description
    )
    
    if not categorization_result.get("success"):
        return categorization_result
    
    board_cat = categorization_result["board_categorization"]
    
    # Build ticket details from AI suggestions
    ticket_details = {
        "boardId": board_cat.get("boardId"),
        "summary": board_cat.get("summary", issue_description[:100]),
        "description": issue_description,
        "companyId": company_id
    }
    
    if contact_id:
        ticket_details["contactId"] = contact_id
    
    # Add AI-suggested categorization if available
    if board_cat.get("categoryId"):
        ticket_details["categoryId"] = board_cat["categoryId"]
    if board_cat.get("subcategoryId"):
        ticket_details["subcategoryId"] = board_cat["subcategoryId"]
    if board_cat.get("priorityId"):
        ticket_details["priorityId"] = board_cat["priorityId"]
    if board_cat.get("statusId"):
        ticket_details["statusId"] = board_cat["statusId"]
    
    # Create the ticket
    return await client.create_board_ticket(msp_custom_domain, ticket_details, user_id)

# Run the server
if __name__ == "__main__":
    mcp.run()