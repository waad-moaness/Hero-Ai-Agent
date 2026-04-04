import streamlit as st
import asyncio
import time 
import ingest
import search_agent
import logs


# --- Initialization ---
@st.cache_resource
def init_agent():
    repo_owner = "huggingface"
    repo_name = "hub-docs"


    st.write("🔄 Indexing repo...")
    index = ingest.index_data(repo_owner, repo_name)
    agent = search_agent.init_agent(index, repo_owner, repo_name)
    return agent


agent = init_agent()

# --- Streamlit UI ---
st.set_page_config(page_title="Hugging Face AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 Hugging Face AI Assistant")
st.caption("Ask me anything about the Hugging Face documentation repository!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# --- ✅ FIXED Streaming helper ---
def stream_response(prompt: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # 🔥 SAFE: run WITHOUT streaming (tools won't break)
        result = loop.run_until_complete(
            agent.run(user_prompt=prompt)
        )

        full_text = result.output

        # log interaction
        logs.log_interaction_to_file(agent, result.new_messages())

        # store full response
        st.session_state._last_response = full_text

        # ✅ Fake streaming (UI only)
        for chunk in full_text.split(" "):
            yield chunk + " "
            time.sleep(0.02) 

    except Exception as e:
        yield "⚠️ Error: " + str(e)


# --- Chat input ---
if prompt := st.chat_input("Ask your question..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant message (streamed)
    with st.chat_message("assistant"):
        response_text = st.write_stream(stream_response(prompt))

    # Save full response to history
    final_text = getattr(st.session_state, "_last_response", response_text)
    st.session_state.messages.append({"role": "assistant", "content": final_text})