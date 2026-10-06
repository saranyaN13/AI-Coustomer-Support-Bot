import json
import os
from datetime import datetime


TICKET_FILE = "data/tickets.json"


def create_ticket(
    category,
    issue,
    priority
):

    os.makedirs(
        "data",
        exist_ok=True
    )

    tickets = []

    if os.path.exists(TICKET_FILE):

        with open(
            TICKET_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            try:
                tickets = json.load(file)

            except json.JSONDecodeError:
                tickets = []

    ticket_number = len(tickets) + 1001

    ticket = {

        "ticket_id":
            f"TC-{ticket_number}",

        "category":
            category,

        "issue":
            issue,

        "priority":
            priority,

        "status":
            "OPEN",

        "created_at":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
    }

    tickets.append(ticket)

    with open(
        TICKET_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            tickets,
            file,
            indent=4
        )

    return ticket