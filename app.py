import streamlit as st
from llm import generate_response
from prompt import ambiguity_prompt, final_answer_prompt

st.title("Clarify")
st.caption("AI that asks better questions before answering.")

if st.button("Start Over"):
    st.rerun()

st.markdown("""
Try:
- Recommend a laptop
- Plan a trip
- Help me learn ML
""")

def parse_response(response):
    if "NEEDS_CLARIFICATION: YES" in response:
        question = response.split("QUESTION:")[-1].strip()
        return True, question
    
    return False, None

query = st.text_input("Enter your query")

if query:
    full_prompt = ambiguity_prompt + f"\nUser Query: {query}"

    with st.spinner("Thinking..."):
        response = generate_response(full_prompt)

    needs_clarification, question = parse_response(response)

    if needs_clarification:
        st.markdown("### Before I answer:")
        st.write(question)

        clarification = st.text_input("Your clarification")

        if clarification:

            final_prompt = final_answer_prompt.format(
                query=query,
                clarification=clarification
            )

            with st.spinner("Generating final response..."):
                final_response = generate_response(final_prompt)

            st.markdown("### Final Response")
            st.write(final_response)

    else:
        final_prompt = final_answer_prompt.format(
            query=query,
            clarification="No clarification needed"
        )

        with st.spinner("Generating response..."):
            final_response = generate_response(final_prompt)

        st.markdown("### Final Response")
        st.write(final_response)

