import streamlit as st
import ollama

from retriever import get_context
from classifier import classify_issue, detect_priority
from ticket import create_ticket


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Customer Support Bot",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_issue" not in st.session_state:
    st.session_state.last_issue = ""

if "last_category" not in st.session_state:
    st.session_state.last_category = ""

if "last_priority" not in st.session_state:
    st.session_state.last_priority = ""


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 25px;
    }

    .company-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #f5f7fb;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
    }

    .status-card {
        padding: 15px;
        border-radius: 12px;
        background-color: #f5f7fb;
        border: 1px solid #dddddd;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🏢 TechCare Electronics")

    st.write(
        "AI-powered customer support for TechCare products."
    )

    st.divider()

    st.subheader("🛍️ Products")

    selected_product = st.selectbox(
        "Select a product",
        [
            "All Products",
            "TechCare Laptop Pro X1",
            "TechCare Phone X",
            "TechCare Buds Pro",
            "TechCare SmartWatch S1"
        ]
    )

    st.divider()

    st.subheader("🛠️ Support Areas")

    st.write("📦 Order Support")
    st.write("🚚 Delivery Support")
    st.write("↩️ Returns")
    st.write("💰 Refunds")
    st.write("💳 Payments")
    st.write("🔧 Technical Support")
    st.write("🛡️ Warranty")

    st.divider()

    st.subheader("📊 System")

    st.write("🟢 AI Assistant: Online")
    st.write("🟢 Knowledge Base: Available")
    st.write("🟢 Local LLM: Ollama")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.last_issue = ""

        st.session_state.last_category = ""

        st.session_state.last_priority = ""

        st.rerun()


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Customer Support Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart customer support powered by local AI and a company knowledge base.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# COMPANY INFORMATION
# --------------------------------------------------

st.markdown(
    """
    <div class="company-card">

    <h3>🏢 TechCare Electronics</h3>

    <p>
    Welcome to TechCare Electronics customer support.
    Our AI assistant helps customers with product information,
    orders, delivery, returns, refunds, warranty and technical issues.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PRODUCT INFORMATION
# --------------------------------------------------

if selected_product != "All Products":

    st.info(
        f"Currently selected product: {selected_product}"
    )


# --------------------------------------------------
# WELCOME MESSAGE
# --------------------------------------------------

if not st.session_state.messages:

    st.subheader("How can I help you?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "📦 Order Support\n\n"
            "Ask about orders and purchases."
        )

    with col2:

        st.info(
            "🔧 Technical Support\n\n"
            "Get troubleshooting help."
        )

    with col3:

        st.info(
            "🛡️ Warranty & Returns\n\n"
            "Ask about policies."
        )


# --------------------------------------------------
# DISPLAY PREVIOUS CHAT
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Ask TechCare Support something..."
)


# --------------------------------------------------
# PROCESS USER QUESTION
# --------------------------------------------------

if user_input:

    # Display user message
    with st.chat_message("user"):

        st.write(user_input)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # --------------------------------------------------
    # CLASSIFY ISSUE
    # --------------------------------------------------

    category = classify_issue(
        user_input
    )

    priority = detect_priority(
        user_input
    )


    # Save issue information
    st.session_state.last_issue = user_input

    st.session_state.last_category = category

    st.session_state.last_priority = priority


    # --------------------------------------------------
    # RETRIEVE KNOWLEDGE
    # --------------------------------------------------

    context = get_context(
        user_input
    )


    # --------------------------------------------------
    # SYSTEM PROMPT
    # --------------------------------------------------

    system_prompt = f"""
You are the official AI customer support assistant
for TechCare Electronics.

TechCare Electronics is a fictional company used for
this demonstration project.

The customer selected this product:
{selected_product}

Your responsibilities:

- Help with TechCare products.
- Help with orders.
- Help with delivery.
- Help with returns.
- Help with refunds.
- Help with warranty.
- Help with technical troubleshooting.
- Answer product questions.
- Be polite and professional.
- Give clear and simple answers.

IMPORTANT RULES:

1. Use the provided TechCare knowledge base as your
   primary source of information.

2. Do not invent order numbers.

3. Do not invent customer information.

4. Do not invent refund amounts.

5. Do not invent delivery dates.

6. Do not claim that a real ticket was submitted.

7. If the knowledge base does not contain the answer,
   clearly say that the information is not available
   and recommend contacting TechCare support.

8. Keep responses concise and useful.

TECHCARE KNOWLEDGE BASE:

{context}
"""


    # --------------------------------------------------
    # CALL OLLAMA
    # --------------------------------------------------

    try:

        response = ollama.chat(

            model="llama3.2",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                }
            ]
            + st.session_state.messages
        )

        assistant_reply = (
            response["message"]["content"]
        )


    except Exception as error:

        assistant_reply = (
            "⚠️ I could not connect to the local AI model.\n\n"
            "Please make sure Ollama is running and "
            "the llama3.2 model is installed.\n\n"
            f"Technical details: {error}"
        )


    # --------------------------------------------------
    # DISPLAY AI RESPONSE
    # --------------------------------------------------

    with st.chat_message(
        "assistant"
    ):

        st.write(
            assistant_reply
        )


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )


# --------------------------------------------------
# ISSUE INFORMATION
# --------------------------------------------------

if st.session_state.last_issue:

    st.divider()

    st.subheader("📊 Issue Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Category:** "
            f"{st.session_state.last_category}"
        )

    with col2:

        st.write(
            f"**Priority:** "
            f"{st.session_state.last_priority}"
        )


# --------------------------------------------------
# SUPPORT TICKET
# --------------------------------------------------

if (
    st.session_state.last_issue
    and st.session_state.last_category
):

    if st.session_state.last_category == "Technical Support":

        st.divider()

        st.subheader(
            "🎫 Support Ticket"
        )

        st.write(
            "If the troubleshooting steps did not solve "
            "your problem, you can create a support ticket."
        )

        if st.button(
            "Create Support Ticket"
        ):

            ticket = create_ticket(

                st.session_state.last_category,

                st.session_state.last_issue,

                st.session_state.last_priority
            )

            st.success(
                "Support ticket created successfully."
            )

            st.write(
                f"**Ticket ID:** "
                f"{ticket['ticket_id']}"
            )

            st.write(
                f"**Category:** "
                f"{ticket['category']}"
            )

            st.write(
                f"**Priority:** "
                f"{ticket['priority']}"
            )

            st.write(
                f"**Status:** "
                f"{ticket['status']}"
            )