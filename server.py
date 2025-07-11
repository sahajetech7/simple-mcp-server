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

# Add this import after your other client imports
from app.clients.psa_initialization_client import PSAInitializationClient

# ========== PSA Generic Tools ==========
# These tools work across different PSA systems (ConnectWise, Autotask, etc.)

@mcp.tool
async def get_psa_clients(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all clients from the PSA system for an MSP domain.
    This is a generic tool that works with any configured PSA (ConnectWise, Autotask, etc.).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of PSA clients or error information
    """
    client = PSAInitializationClient()
    return await client.get_clients(msp_custom_domain)

@mcp.tool
async def get_psa_contacts(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all contacts from the PSA system for an MSP domain.
    This is a generic tool that works with any configured PSA (ConnectWise, Autotask, etc.).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of PSA contacts or error information
    """
    client = PSAInitializationClient()
    return await client.get_contacts(msp_custom_domain)

@mcp.tool
async def get_psa_members(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get all members (technicians/employees) from the PSA system for an MSP domain.
    This is a generic tool that works with any configured PSA (ConnectWise, Autotask, etc.).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing list of PSA members or error information
    """
    client = PSAInitializationClient()
    return await client.get_members(msp_custom_domain)

@mcp.tool
async def add_psa_contact(
    msp_custom_domain: str,
    first_name: str,
    last_name: str,
    email: str,
    company_id: int,
    phone: str ,
    email_type_id: int,
    phone_type_id: int
) -> Dict[str, Any]:
    """
    Add a new contact to the PSA system.
    This is a generic tool that works with any configured PSA (ConnectWise, Autotask, etc.).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        first_name: Contact's first name
        last_name: Contact's last name
        email: Contact's email address
        company_id: ID of the company this contact belongs to in the PSA system
        phone: Contact's phone number (optional)
        email_type_id: Type ID for email (optional, used by some PSAs like ConnectWise)
        phone_type_id: Type ID for phone (optional, used by some PSAs like ConnectWise)
        
    Returns:
        Dictionary containing created contact information or error
    """
    client = PSAInitializationClient()
    
    contact_data = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "psaCompanyId": company_id
    }
    
    if phone:
        contact_data["phone"] = phone
    if email_type_id:
        contact_data["emailTypeId"] = email_type_id
    if phone_type_id:
        contact_data["phoneTypeId"] = phone_type_id
    
    return await client.add_contact(msp_custom_domain, contact_data)

@mcp.tool
async def search_psa_entities(
    msp_custom_domain: str,
    entity_type: str,
    search_term: str
) -> Dict[str, Any]:
    """
    Search for entities (clients, contacts, or members) in the PSA system.
    This tool provides a unified way to search across different entity types.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        entity_type: Type of entity to search - 'clients', 'contacts', or 'members'
        search_term: Optional search term to filter results (searches in names/emails)
        
    Returns:
        Dictionary containing filtered results or all entities if no search term
    """
    client = PSAInitializationClient()
    
    # Get the appropriate entities
    if entity_type.lower() == "clients":
        result = await client.get_clients(msp_custom_domain)
        entity_key = "clients"
    elif entity_type.lower() == "contacts":
        result = await client.get_contacts(msp_custom_domain)
        entity_key = "contacts"
    elif entity_type.lower() == "members":
        result = await client.get_members(msp_custom_domain)
        entity_key = "members"
    else:
        return {
            "success": False,
            "error": f"Invalid entity type: {entity_type}",
            "message": "Entity type must be 'clients', 'contacts', or 'members'"
        }
    
    if not result.get("success"):
        return result
    
    # Filter results if search term provided
    if search_term and result.get(entity_key):
        search_lower = search_term.lower()
        filtered = []
        
        for entity in result[entity_key]:
            # Search in common fields
            if (
                search_lower in str(entity.get("name", "")).lower() or
                search_lower in str(entity.get("firstName", "")).lower() or
                search_lower in str(entity.get("lastName", "")).lower() or
                search_lower in str(entity.get("email", "")).lower() or
                search_lower in str(entity.get("companyName", "")).lower()
            ):
                filtered.append(entity)
        
        result[entity_key] = filtered
        result["filtered"] = True
        result["search_term"] = search_term
        result["total_found"] = len(filtered)
    
    return result

@mcp.tool
async def get_psa_overview(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Get a comprehensive overview of all PSA entities for an MSP domain.
    Returns counts and basic information about clients, contacts, and members.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        
    Returns:
        Dictionary containing overview of all PSA entities
    """
    psa_client = PSAInitializationClient()
    
    overview = {
        "msp_domain": msp_custom_domain,
        "clients": {"count": 0, "status": "pending"},
        "contacts": {"count": 0, "status": "pending"},
        "members": {"count": 0, "status": "pending"},
        "overall_success": True
    }
    
    # Get clients
    clients_result = await psa_client.get_clients(msp_custom_domain)
    if clients_result.get("success"):
        overview["clients"]["count"] = len(clients_result.get("clients", []))
        overview["clients"]["status"] = "success"
        
        # Get sample client names (first 5)
        if clients_result.get("clients"):
            overview["clients"]["sample"] = [
                c.get("name", "Unknown") 
                for c in clients_result["clients"][:5]
            ]
    else:
        overview["clients"]["status"] = "failed"
        overview["clients"]["error"] = clients_result.get("error")
        overview["overall_success"] = False
    
    # Get contacts
    contacts_result = await psa_client.get_contacts(msp_custom_domain)
    if contacts_result.get("success"):
        overview["contacts"]["count"] = len(contacts_result.get("contacts", []))
        overview["contacts"]["status"] = "success"
        
        # Get sample contact names (first 5)
        if contacts_result.get("contacts"):
            overview["contacts"]["sample"] = [
                f"{c.get('firstName', '')} {c.get('lastName', '')}"
                for c in contacts_result["contacts"][:5]
            ]
    else:
        overview["contacts"]["status"] = "failed"
        overview["contacts"]["error"] = contacts_result.get("error")
        overview["overall_success"] = False
    
    # Get members
    members_result = await psa_client.get_members(msp_custom_domain)
    if members_result.get("success"):
        overview["members"]["count"] = len(members_result.get("members", []))
        overview["members"]["status"] = "success"
        
        # Get sample member names (first 5)
        if members_result.get("members"):
            overview["members"]["sample"] = [
                m.get("name", "Unknown")
                for m in members_result["members"][:5]
            ]
    else:
        overview["members"]["status"] = "failed"
        overview["members"]["error"] = members_result.get("error")
        overview["overall_success"] = False
    
    return overview

# Add this import after your other client imports
from app.clients.psa_sync_client import PSASyncClient

# ========== PSA Sync Tools ==========
# These tools handle synchronization of PSA data to the local system

@mcp.tool
async def sync_psa_tickets(msp_custom_domain: str) -> Dict[str, Any]:
    """
    Manually trigger ticket synchronization for a specific MSP domain.
    This syncs tickets from the configured PSA system (ConnectWise, Autotask, etc.) to the local database.
    
    Args:
        msp_custom_domain: The MSP custom domain to sync (e.g., 'etech7')
        
    Returns:
        Dictionary containing sync status and results
        
    Note: This operation may take some time depending on the number of tickets.
    """
    client = PSASyncClient()
    return await client.sync_tickets_for_domain(msp_custom_domain)

@mcp.tool
async def sync_all_psa_tickets() -> Dict[str, Any]:
    """
    Manually trigger ticket synchronization for ALL configured MSP domains.
    This syncs tickets from all PSA systems to the local database.
    
    Returns:
        Dictionary containing sync status and results
        
    Warning: This operation may take considerable time if multiple domains are configured.
    Use with caution during business hours.
    """
    client = PSASyncClient()
    return await client.sync_all_domains()

@mcp.tool
async def sync_psa_with_status_check(
    msp_custom_domain: str,
    check_integration_first: bool = True
) -> Dict[str, Any]:
    """
    Sync PSA tickets with optional integration status check.
    This provides more control over the sync process.
    
    Args:
        msp_custom_domain: The MSP custom domain to sync (e.g., 'etech7')
        check_integration_first: If True, verifies integration exists before syncing
        
    Returns:
        Dictionary containing sync status and detailed results
    """
    result = {
        "domain": msp_custom_domain,
        "integration_check": None,
        "sync_result": None
    }
    
    # Optionally check if integration exists first
    if check_integration_first:
        psa_client = PSAInitializationClient()
        overview = await psa_client.get_clients(msp_custom_domain)
        
        if not overview.get("success"):
            result["integration_check"] = "failed"
            result["error"] = "No PSA integration found or accessible"
            result["success"] = False
            return result
        
        result["integration_check"] = "passed"
    
    # Proceed with sync
    sync_client = PSASyncClient()
    sync_result = await sync_client.sync_tickets_for_domain(msp_custom_domain)
    result["sync_result"] = sync_result
    result["success"] = sync_result.get("success", False)
    
    return result

@mcp.tool
async def batch_sync_domains(domain_list: List[str]) -> Dict[str, Any]:
    """
    Sync multiple specific PSA domains in sequence.
    Useful when you want to sync several domains but not all.
    
    Args:
        domain_list: List of MSP custom domains to sync
        
    Returns:
        Dictionary containing results for each domain
        
    Example:
        domain_list = ["etech7", "msp2", "techcorp"]
    """
    sync_client = PSASyncClient()
    results = {
        "total_domains": len(domain_list),
        "successful": 0,
        "failed": 0,
        "domain_results": {}
    }
    
    for domain in domain_list:
        try:
            sync_result = await sync_client.sync_tickets_for_domain(domain)
            results["domain_results"][domain] = sync_result
            
            if sync_result.get("success"):
                results["successful"] += 1
            else:
                results["failed"] += 1
                
        except Exception as e:
            results["domain_results"][domain] = {
                "success": False,
                "error": str(e)
            }
            results["failed"] += 1
    
    results["overall_success"] = results["failed"] == 0
    return results


# Add this import after your other client imports
from app.clients.psa_ticketing_client import PSATicketingClient

# ========== Generic PSA Ticketing Tools ==========
# These tools work across different PSA systems (ConnectWise, Autotask, etc.)

@mcp.tool
async def get_psa_ticket_diagnostic(
    msp_custom_domain: str,
    user_message: str,
    user_id: str,
    tech_id: str
) -> Dict[str, Any]:
    """
    Get diagnostic questions for a ticket request using AI analysis.
    Works with any configured PSA system. Either user_id or tech_id must be provided.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        user_message: The user's description of their issue
        user_id: ID of the user (required if tech_id not provided)
        tech_id: ID of the technician (required if user_id not provided)
        
    Returns:
        Dictionary containing diagnostic Q&A to clarify the issue
    """
    if not user_id and not tech_id:
        return {
            "success": False,
            "error": "Validation Error",
            "message": "Either user_id or tech_id must be provided"
        }
    
    client = PSATicketingClient()
    return await client.get_ticket_diagnostic_qa(
        msp_custom_domain, 
        user_message,
        user_id,
        tech_id
    )

@mcp.tool
async def create_psa_ticket(
    msp_custom_domain: str,
    psa_type: str,
    summary: str,
    description: str,
    board_id: int,
    user_id: str,
    tech_id: str,
    psa_company_id: int,
    priority_id: int,
    category_id: int,
    subcategory_id: int
) -> Dict[str, Any]:
    """
    Create a ticket in the configured PSA system (ConnectWise, Autotask, etc.).
    Validation: If user_id is not provided, both tech_id and psa_company_id are required.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        psa_type: Type of PSA system ('ConnectWise' or 'Autotask')
        summary: Brief summary of the issue
        description: Detailed description of the issue
        board_id: ID of the board/queue
        user_id: User creating the ticket (optional)
        tech_id: Technician ID (required if user_id not provided)
        psa_company_id: Company ID in PSA (required if user_id not provided)
        priority_id: Priority level ID (optional)
        category_id: Category ID (optional)
        subcategory_id: Subcategory ID (optional)
        
    Returns:
        Dictionary containing created ticket information
    """
    # Validation
    if not user_id and (not tech_id or not psa_company_id):
        return {
            "success": False,
            "error": "Validation Error",
            "message": "If userId is null, techId and psaCompanyId are mandatory"
        }
    
    client = PSATicketingClient()
    
    ticket_request = {
        "psaType": psa_type,
        "summary": summary,
        "description": description,
        "boardId": board_id
    }
    
    if user_id:
        ticket_request["userId"] = user_id
    if tech_id:
        ticket_request["techId"] = tech_id
    if psa_company_id:
        ticket_request["psaCompanyId"] = psa_company_id
    if priority_id:
        ticket_request["priorityId"] = priority_id
    if category_id:
        ticket_request["categoryId"] = category_id
    if subcategory_id:
        ticket_request["subcategoryId"] = subcategory_id
    
    return await client.create_ticket(msp_custom_domain, ticket_request)

@mcp.tool
async def add_psa_ticket_note(
    msp_custom_domain: str,
    ticket_id: str,
    note_text: str,
    is_internal: bool = False,
    is_resolution: bool = False
) -> Dict[str, Any]:
    """
    Add a note to an existing ticket in any PSA system.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        note_text: The note content to add
        is_internal: Whether this is an internal note (optional)
        is_resolution: Whether this note represents the resolution (optional)
        
    Returns:
        Dictionary containing the result of the operation
    """
    client = PSATicketingClient()
    
    notes_request = {
        "note": note_text,
        "isInternal": is_internal,
        "isResolution": is_resolution
    }
    
    return await client.add_notes_to_ticket(msp_custom_domain, ticket_id, notes_request)

@mcp.tool
async def get_psa_ticket_notes(
    msp_custom_domain: str,
    ticket_id: str,
    detailed: bool = False
) -> Dict[str, Any]:
    """
    Get all notes for a ticket from any PSA system.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        detailed: If True, returns detailed note information (optional)
        
    Returns:
        Dictionary containing ticket notes
    """
    client = PSATicketingClient()
    return await client.get_ticket_notes(msp_custom_domain, ticket_id, detailed)

@mcp.tool
async def close_psa_ticket(
    msp_custom_domain: str,
    ticket_id: str,
    board_id: int
) -> Dict[str, Any]:
    """
    Close a ticket in any PSA system.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket to close
        board_id: ID of the board (optional, may be required for some PSAs)
        
    Returns:
        Dictionary containing the result of the operation
    """
    client = PSATicketingClient()
    return await client.close_ticket(msp_custom_domain, ticket_id, board_id)

@mcp.tool
async def get_psa_ticket_status(
    msp_custom_domain: str,
    ticket_id: str
) -> Dict[str, Any]:
    """
    Get the current status of a ticket from any PSA system.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        
    Returns:
        Dictionary containing ticket status information
    """
    client = PSATicketingClient()
    return await client.get_ticket_status(msp_custom_domain, ticket_id)

@mcp.tool
async def create_psa_ticket_with_ai(
    msp_custom_domain: str,
    psa_type: str,
    issue_description: str,
    user_id: str,
    tech_id: str,
    psa_company_id: int
) -> Dict[str, Any]:
    """
    Create a ticket with AI-powered categorization in any PSA system.
    First analyzes the issue, then creates a properly categorized ticket.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        psa_type: Type of PSA system ('ConnectWise' or 'Autotask')
        issue_description: Natural language description of the issue
        user_id: User creating the ticket (optional)
        tech_id: Technician ID (required if user_id not provided)
        psa_company_id: Company ID (required if user_id not provided)
        
    Returns:
        Dictionary containing the created ticket with AI categorization
    """
    # Validation
    if not user_id and (not tech_id or not psa_company_id):
        return {
            "success": False,
            "error": "Validation Error",
            "message": "If userId is null, techId and psaCompanyId are mandatory"
        }
    
    client = PSATicketingClient()
    
    # First, get AI diagnostic/categorization
    diagnostic_result = await client.get_ticket_diagnostic_qa(
        msp_custom_domain,
        issue_description,
        user_id,
        tech_id
    )
    
    if not diagnostic_result.get("success"):
        return diagnostic_result
    
    qa_data = diagnostic_result.get("diagnostic_qa", {})
    
    # Build ticket request from AI suggestions
    ticket_request = {
        "psaType": psa_type,
        "summary": qa_data.get("summary", issue_description[:100]),
        "description": issue_description,
        "boardId": qa_data.get("boardId", 1),  # Default to board 1 if not suggested
        "userId": user_id,
        "techId": tech_id,
        "psaCompanyId": psa_company_id
    }
    
    # Add AI-suggested categorization if available
    if qa_data.get("priorityId"):
        ticket_request["priorityId"] = qa_data["priorityId"]
    if qa_data.get("categoryId"):
        ticket_request["categoryId"] = qa_data["categoryId"]
    if qa_data.get("subcategoryId"):
        ticket_request["subcategoryId"] = qa_data["subcategoryId"]
    
    # Create the ticket
    create_result = await client.create_ticket(msp_custom_domain, ticket_request)
    
    # Include diagnostic info in response
    if create_result.get("success"):
        create_result["ai_categorization"] = qa_data
    
    return create_result


# Add this import after your other client imports
from app.clients.psa_time_entry_client import PSATimeEntryClient
from datetime import datetime

# ========== PSA Time Entry Tools ==========
# These tools handle time tracking across different PSA systems

@mcp.tool
async def create_psa_time_entry(
    msp_custom_domain: str,
    ticket_id: str,
    technician_id: str,
    time_spent: float,
    notes: str,
    work_date: str,
    billable: bool = True,
    time_unit: str = "minutes"
) -> Dict[str, Any]:
    """
    Create a time entry for a ticket in the PSA system.
    Works with any configured PSA (ConnectWise, Autotask, etc.).
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket to log time against
        technician_id: ID of the technician who performed the work
        time_spent: Amount of time spent (default unit is minutes)
        notes: Description of the work performed
        work_date: Date when work was performed (ISO format: YYYY-MM-DD) (optional, defaults to today)
        billable: Whether this time entry is billable (default: True)
        time_unit: Unit of time - 'minutes' or 'hours' (default: 'minutes')
        
    Returns:
        Dictionary containing created time entry information
        
    Example:
        Log 2.5 hours of work: time_spent=2.5, time_unit="hours"
        Log 90 minutes of work: time_spent=90, time_unit="minutes"
    """
    client = PSATimeEntryClient()
    
    # Convert time to minutes if specified in hours
    time_in_minutes = time_spent
    if time_unit.lower() == "hours":
        time_in_minutes = time_spent * 60
    
    time_entry_request = {
        "mspCustomDomain": msp_custom_domain,
        "ticketId": ticket_id,
        "technicianId": technician_id,
        "timeSpent": time_in_minutes,
        "notes": notes,
        "billable": billable
    }
    
    # Add work date if provided, otherwise PSA will use current date
    if work_date:
        time_entry_request["workDate"] = work_date
    else:
        time_entry_request["workDate"] = datetime.now().strftime("%Y-%m-%d")
    
    return await client.create_time_entry(time_entry_request)

@mcp.tool
async def log_quick_time_entry(
    msp_custom_domain: str,
    ticket_id: str,
    technician_id: str,
    time_minutes: int,
    work_description: str
) -> Dict[str, Any]:
    """
    Quick method to log time entry with minimal parameters.
    Defaults to billable time for today's date.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        technician_id: ID of the technician
        time_minutes: Time spent in minutes
        work_description: Brief description of work performed
        
    Returns:
        Dictionary containing created time entry information
    """
    client = PSATimeEntryClient()
    
    time_entry_request = {
        "mspCustomDomain": msp_custom_domain,
        "ticketId": ticket_id,
        "technicianId": technician_id,
        "timeSpent": time_minutes,
        "notes": work_description,
        "billable": True,
        "workDate": datetime.now().strftime("%Y-%m-%d")
    }
    
    return await client.create_time_entry(time_entry_request)

@mcp.tool
async def log_bulk_time_entries(
    msp_custom_domain: str,
    technician_id: str,
    time_entries: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Create multiple time entries for a technician across different tickets.
    Useful for end-of-day time logging.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        technician_id: ID of the technician logging time
        time_entries: List of time entry details, each containing:
            - ticket_id: Ticket ID
            - time_minutes: Time spent in minutes
            - notes: Work description
            - work_date: Optional work date (defaults to today)
            - billable: Optional billable flag (defaults to True)
            
    Returns:
        Dictionary containing results for each time entry
        
    Example:
        time_entries = [
            {"ticket_id": "123", "time_minutes": 30, "notes": "Initial diagnosis"},
            {"ticket_id": "124", "time_minutes": 60, "notes": "Software installation"}
        ]
    """
    client = PSATimeEntryClient()
    results = {
        "total_entries": len(time_entries),
        "successful": 0,
        "failed": 0,
        "total_minutes_logged": 0,
        "entries": []
    }
    
    for entry in time_entries:
        time_entry_request = {
            "mspCustomDomain": msp_custom_domain,
            "ticketId": entry.get("ticket_id"),
            "technicianId": technician_id,
            "timeSpent": entry.get("time_minutes", 0),
            "notes": entry.get("notes", ""),
            "billable": entry.get("billable", True),
            "workDate": entry.get("work_date", datetime.now().strftime("%Y-%m-%d"))
        }
        
        result = await client.create_time_entry(time_entry_request)
        
        entry_result = {
            "ticket_id": entry.get("ticket_id"),
            "success": result.get("success", False),
            "minutes": entry.get("time_minutes", 0)
        }
        
        if result.get("success"):
            results["successful"] += 1
            results["total_minutes_logged"] += entry.get("time_minutes", 0)
            entry_result["time_entry_id"] = result.get("time_entry", {}).get("id")
        else:
            results["failed"] += 1
            entry_result["error"] = result.get("error", "Unknown error")
            
        results["entries"].append(entry_result)
    
    results["overall_success"] = results["failed"] == 0
    results["total_hours_logged"] = round(results["total_minutes_logged"] / 60, 2)
    
    return results

@mcp.tool
async def check_psa_time_entry_health() -> Dict[str, Any]:
    """
    Check the health status of the PSA time entry service.
    Useful for verifying service availability before bulk operations.
    
    Returns:
        Dictionary containing service health information
    """
    client = PSATimeEntryClient()
    return await client.check_service_health()

@mcp.tool
async def log_time_with_completion(
    msp_custom_domain: str,
    ticket_id: str,
    technician_id: str,
    time_minutes: int,
    resolution_notes: str,
    board_id: int,
    close_ticket: bool = False
) -> Dict[str, Any]:
    """
    Log time entry and optionally close the ticket in one operation.
    Combines time tracking with ticket closure for efficiency.
    
    Args:
        msp_custom_domain: The MSP custom domain (e.g., 'etech7')
        ticket_id: ID of the ticket
        technician_id: ID of the technician
        time_minutes: Time spent in minutes
        resolution_notes: Description of work performed and resolution
        close_ticket: Whether to close the ticket after logging time (default: False)
        board_id: Board ID (required for closing some PSA tickets)
        
    Returns:
        Dictionary containing time entry and ticket closure results
    """
    results = {
        "time_entry": None,
        "ticket_closure": None,
        "overall_success": True
    }
    
    # First, create time entry
    time_client = PSATimeEntryClient()
    time_entry_request = {
        "mspCustomDomain": msp_custom_domain,
        "ticketId": ticket_id,
        "technicianId": technician_id,
        "timeSpent": time_minutes,
        "notes": resolution_notes,
        "billable": True,
        "workDate": datetime.now().strftime("%Y-%m-%d")
    }
    
    time_result = await time_client.create_time_entry(time_entry_request)
    results["time_entry"] = time_result
    
    if not time_result.get("success"):
        results["overall_success"] = False
        return results
    
    # Optionally close the ticket
    if close_ticket:
        psa_client = PSATicketingClient()
        close_result = await psa_client.close_ticket(
            msp_custom_domain, 
            ticket_id, 
            board_id
        )
        results["ticket_closure"] = close_result
        
        if not close_result.get("success"):
            results["overall_success"] = False
    
    return results


# Run the server
if __name__ == "__main__":
    mcp.run()