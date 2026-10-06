import os
import re

KNOWLEDGE_FOLDER = "knowledge_base"


def load_documents():
    documents = []

    if not os.path.exists(KNOWLEDGE_FOLDER):
        return documents

    for filename in os.listdir(KNOWLEDGE_FOLDER):

        if filename.endswith(".txt"):

            filepath = os.path.join(
                KNOWLEDGE_FOLDER,
                filename
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            chunks = text.split("\n\n")

            for chunk in chunks:

                chunk = chunk.strip()

                if chunk:
                    documents.append({
                        "source": filename,
                        "content": chunk
                    })

    return documents


def tokenize(text):
    return set(
        re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower()
        )
    )


def calculate_score(query, document):
    query_words = tokenize(query)
    document_words = tokenize(
        document["content"]
    )

    if not query_words:
        return 0

    common_words = query_words.intersection(
        document_words
    )

    return len(common_words)


def search_knowledge(query, number_of_results=5):

    documents = load_documents()

    scored_documents = []

    for document in documents:

        score = calculate_score(
            query,
            document
        )

        if score > 0:

            scored_documents.append(
                (
                    score,
                    document
                )
            )

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    results = []

    for score, document in scored_documents[
        :number_of_results
    ]:

        results.append(document)

    return results


def get_context(query):

    results = search_knowledge(query)

    if not results:

        return "No relevant information was found in the TechCare knowledge base."

    context_parts = []

    for result in results:

        context_parts.append(
            f"Source: {result['source']}\n"
            f"{result['content']}"
        )

    return "\n\n".join(context_parts)