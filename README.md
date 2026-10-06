# AI Customer Support Bot

## 1. Project Overview

AI Customer Support Bot is an AI-powered customer service application developed using Python, Streamlit, and Ollama. The application simulates customer support for a fictional electronics company called **TechCare Electronics**.

The bot allows customers to ask questions about products, orders, delivery, returns, refunds, warranty, and technical problems. It searches a local company knowledge base, retrieves relevant information, and uses a local AI model to generate a clear response.

The system also classifies customer issues, detects their priority, and can create a support ticket for technical problems.

---

## 2. Company Used in the Project

### TechCare Electronics

TechCare Electronics is a fictional electronics company created for this project.

The company provides:

* Laptops
* Smartphones
* Wireless earbuds
* Smartwatches

The AI bot acts as the company's customer support assistant.

---

## 3. Main Objective

The main objective is to develop an intelligent customer support system that can:

* Understand customer questions
* Provide product information
* Answer company-policy questions
* Provide troubleshooting assistance
* Retrieve relevant information from a knowledge base
* Classify customer problems
* Detect issue priority
* Generate support tickets
* Maintain conversation history
* Provide a simple and attractive web interface

---

## 4. Products Included

### TechCare Laptop Pro X1

* 15.6-inch Full HD display
* 16 GB RAM
* 512 GB SSD
* Wi-Fi
* Bluetooth
* Windows
* Suitable for programming, office work, engineering software and productivity

### TechCare Phone X

* 6.5-inch display
* 8 GB RAM
* 256 GB storage
* Wi-Fi
* Bluetooth
* Mobile network connectivity

### TechCare Buds Pro

* Wireless Bluetooth connectivity
* Charging case
* Touch controls
* Built-in microphone

### TechCare SmartWatch S1

* Activity tracking
* Notifications
* Bluetooth connectivity
* Fitness monitoring

---

## 5. Customer Support Features

The chatbot provides support for:

### Product Information

Customers can ask about:

* Product specifications
* RAM
* Storage
* Display
* Features
* Product usage

### Order Support

The system can answer general questions about orders and purchases.

It does not invent order numbers or customer information.

### Delivery Support

The knowledge base provides standard delivery information.

Standard delivery is normally:

**3–7 business days**

The system does not invent an order status or delivery date.

### Returns

Customers can ask about the return policy.

The project uses a:

**7-day return period**

subject to the specified conditions.

### Refund Information

The chatbot can explain the available return/refund policy information.

It does not promise a refund before the return is reviewed.

### Warranty

TechCare products have a:

**1-year standard warranty**

The warranty covers manufacturing defects but does not cover damage caused by accidents, misuse or unauthorized modification.

### Technical Support

The chatbot provides troubleshooting assistance for problems such as:

* Laptop not turning on
* Laptop running slowly
* Bluetooth connection problems
* Earbuds not charging
* Smartwatch connection problems

---

## 6. Knowledge Base

The project contains a local knowledge base instead of depending entirely on the AI model's general knowledge.

The knowledge base contains:

* Company information
* Product information
* Warranty policy
* Return policy
* Delivery information
* Troubleshooting information
* Customer support information

These are stored as `.txt` files inside:

```text
knowledge_base/
```

The main files are:

```text
company.txt
products.txt
warranty.txt
returns.txt
delivery.txt
troubleshooting.txt
support.txt
```

---

## 7. Retrieval System

The project includes a retrieval system that searches the local knowledge base according to the customer's question.

For example:

Customer asks:

"How long is the warranty?"

The system searches the knowledge base and retrieves the relevant warranty information.

The retrieved information is then provided to the AI model.

The basic flow is:

```text
Customer Question
       ↓
Knowledge Base Search
       ↓
Relevant Information
       ↓
Ollama AI Model
       ↓
Final Answer
```

This makes the chatbot more focused on TechCare-specific information.

---

## 8. AI Model

The project uses **Ollama** to run the AI model locally.

The project is configured to use:

```text
Llama 3.2
```

The advantage of using a local model is that the application can operate without sending customer questions to an external AI API.

---

## 9. Issue Classification

The project contains an issue-classification system.

It identifies categories such as:

* Technical Support
* Delivery
* Order Support
* Returns & Refunds
* Warranty
* Payment
* Product Information
* General Support

For example:

```text
"My laptop is not turning on."
```

The system identifies it as:

```text
Technical Support
```

---

## 10. Priority Detection

The project also detects the priority of an issue.

There are three levels:

### LOW

Used for general questions.

### NORMAL

Used for normal problems such as:

* Device not working
* Device not turning on
* General technical problems

### HIGH

Used when the message contains serious indicators such as:

* Overheating
* Smoke
* Burning
* Sparking
* Danger

This helps demonstrate how a customer-support system can identify urgent issues.

---

## 11. Support Ticket System

If a customer has a technical problem that requires further assistance, the application can generate a support ticket.

The ticket contains:

* Ticket ID
* Issue category
* Customer's issue description
* Priority
* Status
* Creation time

Example:

```text
Ticket ID: TC-1001
Category: Technical Support
Priority: NORMAL
Status: OPEN
```

Tickets are stored locally in:

```text
data/tickets.json
```

The system does not claim that a ticket was submitted to a real company because this project is a demonstration application.

---

## 12. Chat Memory

The application maintains the conversation during the current session.

For example:

```text
Customer:
What is the Laptop Pro X1?

Bot:
It has 16 GB RAM and 512 GB SSD.

Customer:
What about its display?

Bot:
It has a 15.6-inch Full HD display.
```

The application stores the conversation using Streamlit session state.

---

## 13. User Interface

The application is developed using **Streamlit**.

The interface contains:

* Project title
* TechCare company information
* Product selection
* Support categories
* AI chat interface
* Chat history
* Issue analysis
* Priority information
* Support ticket option
* Clear conversation button
* System status information

---

## 14. Sidebar

The sidebar provides:

### Product Selection

Users can select:

* All Products
* TechCare Laptop Pro X1
* TechCare Phone X
* TechCare Buds Pro
* TechCare SmartWatch S1

### Support Options

* Order Support
* Delivery Support
* Returns
* Refunds
* Payments
* Technical Support
* Warranty

### System Status

The application displays:

* AI Assistant: Online
* Knowledge Base: Available
* Local LLM: Ollama

---

## 15. Main Python Files

The project contains four important Python files.

### app.py

This is the main application.

It handles:

* Streamlit interface
* Chat
* Session memory
* Product selection
* Knowledge retrieval
* Ollama communication
* Issue analysis
* Support tickets

### retriever.py

This handles the knowledge-base search.

It:

* Reads `.txt` files
* Splits the information into sections
* Searches for relevant information
* Returns useful context to the AI

### classifier.py

This handles:

* Issue classification
* Priority detection

### ticket.py

This handles:

* Ticket creation
* Ticket numbering
* Ticket storage
* Ticket status
* Creation time

---

## 16. Data Files

The project uses:

```text
data/tickets.json
```

to store generated support tickets.

The JSON format makes the information easy to read and process using Python.

---

## 17. Technologies Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Application logic         |
| Streamlit       | Web application interface |
| Ollama          | Local AI platform         |
| Llama 3.2       | AI language model         |
| JSON            | Ticket storage            |
| Local TXT files | Knowledge base            |
| Git             | Version control           |
| GitHub          | Project hosting           |

---

## 18. Complete Project Structure

```text
AI Customer Support Bot/
│
├── .venv/
│
├── app.py
├── retriever.py
├── classifier.py
├── ticket.py
├── requirements.txt
├── README.md
│
├── knowledge_base/
│   ├── company.txt
│   ├── products.txt
│   ├── warranty.txt
│   ├── returns.txt
│   ├── delivery.txt
│   ├── troubleshooting.txt
│   └── support.txt
│
└── data/
    └── tickets.json
```

---

## 19. Complete Working Flow

```text
                 CUSTOMER
                    │
                    ▼
            Streamlit Interface
                    │
                    ▼
             Customer Question
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   Issue Classifier      Knowledge Search
          │                   │
          ▼                   ▼
      Category            Local Files
          │                   │
          ▼                   ▼
      Priority          Relevant Context
          │                   │
          └─────────┬─────────┘
                    ▼
              System Prompt
                    │
                    ▼
              Ollama / Llama
                    │
                    ▼
              AI Response
                    │
                    ▼
          Technical Problem?
                    │
                    ▼
             Create Ticket
                    │
                    ▼
              tickets.json
```

---

## 20. Example User Questions

The user can ask:

```text
What is TechCare Electronics?
```

```text
What are the specifications of the Laptop Pro X1?
```

```text
How much RAM does the Phone X have?
```

```text
How long is the warranty?
```

```text
Can I return my product?
```

```text
How long does delivery take?
```

```text
My laptop is not turning on.
```

```text
My earbuds are not charging.
```

```text
My smartwatch is not connecting.
```

```text
My laptop is overheating and there is smoke.
```

The system then retrieves information, generates an AI response, classifies the issue and assigns priority where applicable.

---

## 21. Advantages of the Project

The project demonstrates several important AI and software-development concepts:

* AI chatbot development
* Local LLM integration
* Knowledge retrieval
* Prompt engineering
* Natural-language interaction
* Issue classification
* Priority detection
* Automated support-ticket generation
* Session-based conversation memory
* Web application development
* Local data storage

---

## 22. Real-World Use

A similar system could be used by:

* Electronics companies
* E-commerce companies
* Educational institutions
* Software companies
* Banks
* Telecom companies
* Online service providers

A production version could be connected to a real customer database, order-management system, CRM, email service and ticketing platform.

---

## 23. Future Improvements

The project can later be extended with:

* Real-time order tracking
* Customer login
* Database integration
* Email notifications
* Admin dashboard
* Real CRM integration
* Voice-based support
* Multilingual support
* Analytics dashboard
* Semantic/vector search
* Cloud deployment
* Authentication
* Real customer-ticket management

---

## 24. Project Limitation

TechCare Electronics is a **fictional company created for educational and demonstration purposes**.

The current application does not connect to:

* A real customer database
* Real orders
* Real payment systems
* Real delivery systems
* A real company's ticketing system

Therefore, the application should not claim to provide real-time customer account information.

---

## 25. One-Line Project Explanation

**AI Customer Support Bot is a local AI-powered customer service application that retrieves company-specific information, answers customer questions, troubleshoots technical issues, classifies problems, detects priority and generates support tickets.**

## 26. Interview Explanation

If an interviewer asks, **"Tell me about your project,"** you can say:

"I developed an AI Customer Support Bot for a fictional electronics company called TechCare Electronics. I used Python and Streamlit for the application interface and Ollama with Llama 3.2 as the local AI model. The application uses a local knowledge base to retrieve relevant company information before generating responses. It can handle product, order, delivery, return, refund, warranty and technical-support questions. I also implemented issue classification, priority detection and support-ticket generation using JSON storage. The project demonstrates how AI can be integrated with a knowledge base to build a practical customer-support system."
