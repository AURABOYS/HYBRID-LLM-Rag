from hybrid_llm.web.google_search import google_search

def build_web_prompt(question, results):
    context = ""
    for i, r in enumerate(results, 1):
        title = r.get("title", "")
        snippet = r.get("snippet", "")
        link = r.get("link", "")
        context += f"[{i}] {title}\n{snippet}\n{link}\n\n"

    prompt = f"""
Use ONLY the web results below to answer the question.

WEB RESULTS:
{context}

QUESTION:
{question}

Provide a clear answer based strictly on the results.
"""
    return prompt


def answer_with_google_local(question, router, num_results=5):
    # Run Google Search
    results = google_search(question, num_results)

    # Build prompt for mistral
    prompt = build_web_prompt(question, results)

    # Local LLM answer
    out = router.answer(prompt)

    return {
        "answer": out.get("response", ""),
        "sources": results
    }
