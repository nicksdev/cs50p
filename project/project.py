import pdfplumber
import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
model_tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

def main():
    st.title("nickdev's PDF Summerizer Tool")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    if uploaded_file is not None:

        if st.button("Summarize"):
            rawtext = extract(uploaded_file)
            summary = model_pipeline(rawtext)
            print(summary)
            st.info("Summarization Complete")
            st.success(summary)
             
             
def model_pipeline(rawtext):
    summarization_pipeline = pipeline(
        'summarization',
        model=model,
        tokenizer=model_tokenizer,
        max_length=1000, 
        min_length=70)
    summary_result = summarization_pipeline(rawtext)
    summarized_text = summary_result[0]['summary_text']
    return summarized_text         
        

def extract(file):
    with pdfplumber.open(file) as pdf:
        extracted_text = ''
        for x in pdf.pages:
            single_page_text = x.extract_text()
            extracted_text = extracted_text + '\n' + single_page_text
        short_text = resize_file(extracted_text)
        return short_text

def resize_file(input):
    output = (input[:3000] + '..') if len(input) > 3000 else input
    return output

if __name__ == "__main__":
    main()