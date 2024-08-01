    # PDF Summerizer Tool
    #### Video Demo:  <URL HERE>
    #### Description:
    This tool enables the user to upload a PDF and then click a button to summerize the content of the PDF.
    It works by first extracting the text of the PDF and then running it through a Large Language Model, in this case "sshleifer/distilbart-cnn-12-6", to generate a summary using Artificial Intelligence. This model was chosen for its relativly small size and its relativly large 1024 Token limit.
    The tool uses lightweight Streamlit library to provide a user interface.
    
    TODO:
    Due to the model token limit it will only summarize the first part of the PDF. A better solution would be to use an online LLM service such as ChatGPT which has singificantly larger Token limits or to run a large dedicated open-source model such as Llama 3.
    Another approach would be to 'chunk' the PDF text into small pieces, generate a summary for each piece. It would then be possible to summerise the summeries.
    Using a more sophisticated library such as Flask would enabl;e the creation of a better interface.