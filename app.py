import streamlit as st
import json
import zipfile
import io

jsonString = {"name": "Test", "prop": [{"a": 1, "b": 2}]}

# Create an in-memory buffer to store the zip file
with io.BytesIO() as buffer:
    # Write the zip file to the buffer
    with zipfile.ZipFile(buffer, "w") as zip:
        zip.writestr("Data.json", json.dumps(jsonString))

    buffer.seek(0)

    btn = st.download_button(
        label="Download ZIP",
        data=buffer,  # Download buffer
        file_name="file.zip"
    )