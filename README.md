# Clarify

AI that asks better questions before answering.

## The Idea

Most AI assistants try to answer immediately, even when the user’s request is vague or underspecified. That often leads to generic responses, wrong assumptions, or unnecessary hallucinations.

Clarify explores a simple idea:

> What if AI assistants paused briefly to ask one focused clarification question before responding?

Instead of treating every prompt as fully specified, Clarify first determines whether the request has enough information to generate a useful answer. If not, it asks a single concise follow-up question and then generates a more context-aware response.

---

## Example

**User:**  
`Recommend a laptop`

**Clarify:**  
`Are you optimizing more for portability, gaming, or budget?`

**User:**  
`Portability`

**Clarify:**  
Generates a more targeted recommendation instead of making assumptions upfront.

---

## Why I Built This

I’ve noticed that many conversational AI systems fail not because the models are weak, but because they answer too confidently without properly understanding user intent.

This project was an attempt to explore whether improving clarification behavior alone could make AI interactions feel more reliable and useful.

Rather than building a large multi-agent system or a full chatbot platform, I intentionally focused on the smallest interaction loop that still felt interesting and usable.

---

## What I Intentionally Left Out

To keep the project focused and lightweight, I intentionally avoided adding:

- Long-term memory
- Multi-turn conversations
- Tool usage
- Vector databases / RAG
- Authentication
- Complex UI layers

The goal was not to build a full assistant, but to prototype a better interaction pattern.

---

## Tech Stack

- Streamlit
- Ollama
- Llama 3
- Python

---

## Running Locally

```bash
streamlit run app.py