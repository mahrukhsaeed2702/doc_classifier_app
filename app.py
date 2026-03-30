import streamlit as st
from classifier import classify_document
from ocr_utils import extract_text_from_pdf, extract_text_from_image
from PIL import Image
import tempfile

st.set_page_config(page_title="Bulk Document Classifier", layout="centered")

st.title("Bulk Document Classifier")
st.write("Upload multiple PDFs or images to classify document types")

uploaded_files = st.file_uploader(
    "Upload files",
    type=["pdf", "jpg", "png", "jpeg"],
    accept_multiple_files=True
)

results = []

if uploaded_files:
    st.info(f" Processing {len(uploaded_files)} files...")

    for uploaded_file in uploaded_files:
        file_type = uploaded_file.type

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        try:
            # OCR
            if "pdf" in file_type:
                text = extract_text_from_pdf(file_path)
            else:
                image = Image.open(uploaded_file)
                text = extract_text_from_image(image)

            # Classification
            doc_type = classify_document(text)

            results.append({
                "file": uploaded_file.name,
                "type": doc_type
            })

        except Exception as e:
            results.append({
                "file": uploaded_file.name,
                "type": f"Error: {str(e)}"
            })

    st.success("Processing Completed")

    # Display Results
    st.subheader("Results")

    for res in results:
        st.write(f"**{res['file']}** → {res['type']}")
