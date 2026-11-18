import streamlit as st

from rag import (
    model,
    UPLOADS_DIR,
    DOCUMENTS_DIR,
    load_documents,
    create_chunks,
    generate_embeddings,
    create_vector_index,
    retrieve_chunks,
    generate_answer
)
from pathlib import Path

st.set_page_config(
    page_title="Inlite Knowledge Assistant",
    page_icon="💡",
    layout="centered"
)


@st.cache_resource
def prepare_rag_pipeline():

    documents = load_documents(DOCUMENTS_DIR)

    chunks = create_chunks(documents)

    embeddings = generate_embeddings(chunks)

    index = create_vector_index(embeddings)

    return chunks, index


st.title("💡 Inlite Knowledge Assistant")

st.write(
    "Ask questions about Inlite Media's services, "
    "marketing strategies and campaign reports."
)


with st.spinner("Preparing knowledge base..."):

    chunks, index = prepare_rag_pipeline()


st.success(f"Knowledge base ready! {len(chunks)} chunks loaded.")

st.subheader("📁 Manage Documents")

uploaded_files = st.file_uploader(
    "Upload your documents",
    type=["txt", "xlsx", "xls"],
    accept_multiple_files=True
)

if st.button("Add / Update Knowledge Base"):

    if uploaded_files:

        UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

        for uploaded_file in uploaded_files:

            # Prevent directory traversal through filenames
            file_name = Path(uploaded_file.name).name

            file_path = UPLOADS_DIR / file_name

            # Save or replace the uploaded file
            file_path.write_bytes(uploaded_file.getvalue())

        st.success("Documents saved successfully!")

        # Clear the previously cached knowledge base
        st.cache_resource.clear()

        # Reload the application with updated documents
        st.rerun()

    else:
        st.warning("Please upload at least one document.")

with st.form(key="question_form"):

    question = st.text_input(
        "Ask your question:",
        placeholder="What services does Inlite Media provide?"
    )

    submit = st.form_submit_button("Generate Answer")


if submit:

    if question.strip():

        with st.spinner("Searching documents and generating answer..."):

            results = retrieve_chunks(
                question,
                model,
                index,
                chunks
            )

            answer = generate_answer(question, results)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        sources = set(result["source"] for result in results)

        for result in results:

            with st.expander(
                f"📄 {result['source']} | "
                f"Similarity: {result['score']:.3f}"
            ):

                st.write(result["text"])

    else:
        st.warning("Please enter a question.")