def classify_issue(message):

    message = message.lower()

    technical_words = [
        "not working",
        "not turning on",
        "slow",
        "problem",
        "issue",
        "broken",
        "charging",
        "bluetooth",
        "connect",
        "overheating",
        "screen",
        "battery"
    ]

    order_words = [
        "order",
        "ordered",
        "order number",
        "purchase"
    ]

    delivery_words = [
        "delivery",
        "delivered",
        "shipping",
        "arrive",
        "package"
    ]

    return_words = [
        "return",
        "refund",
        "money back"
    ]

    warranty_words = [
        "warranty",
        "guarantee",
        "manufacturing defect"
    ]

    payment_words = [
        "payment",
        "paid",
        "card",
        "transaction"
    ]

    product_words = [
        "specification",
        "specifications",
        "features",
        "ram",
        "storage",
        "display",
        "price",
        "product"
    ]

    if any(
        word in message
        for word in technical_words
    ):
        return "Technical Support"

    if any(
        word in message
        for word in delivery_words
    ):
        return "Delivery"

    if any(
        word in message
        for word in order_words
    ):
        return "Order Support"

    if any(
        word in message
        for word in return_words
    ):
        return "Returns & Refunds"

    if any(
        word in message
        for word in warranty_words
    ):
        return "Warranty"

    if any(
        word in message
        for word in payment_words
    ):
        return "Payment"

    if any(
        word in message
        for word in product_words
    ):
        return "Product Information"

    return "General Support"


def detect_priority(message):

    message = message.lower()

    high_priority_words = [
        "overheating",
        "smoke",
        "burning",
        "danger",
        "sparking"
    ]

    normal_priority_words = [
        "not working",
        "problem",
        "issue",
        "broken",
        "not turning on"
    ]

    if any(
        word in message
        for word in high_priority_words
    ):
        return "HIGH"

    if any(
        word in message
        for word in normal_priority_words
    ):
        return "NORMAL"

    return "LOW"