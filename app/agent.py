from app.retriever import search_catalog


def generate_reply(messages):

    latest_user_message = messages[-1]["content"]

    retrieved = search_catalog(
        latest_user_message,
        top_k=5
    )

    return {
        "reply": "Recommended assessments generated successfully.",
        "recommendations": retrieved,
        "end_of_conversation": False
    }