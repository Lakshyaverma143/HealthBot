from dotenv import load_dotenv
import os
import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Load environment variables
load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
ai_project_name = os.getenv('QA_PROJECT_NAME')
ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

# Create Azure client
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

# Streamlit app layout
st.title("HealthBot Question Answering Application")
st.write("Providing Health solution to Patient")

# User input for question
user_question = st.text_input("Question:")

if st.button("Get Answer"):
    if user_question:
        try:
            # Submit the question to the AI service
            response = ai_client.get_answers(
                question=user_question,
                project_name=ai_project_name,
                deployment_name=ai_deployment_name
            )

            # Display answers
            st.write("### Answers: ")
            for candidate in response.answers:
                st.write(candidate.answer)
                # st.write(f"  - **Confidence:** {candidate.confidence:.2f}")
                # st.write(f"  - **Source:** {candidate.source}")
        except Exception as ex:
            st.error(f"Error: {ex}")
    else:
        st.warning("Please enter a question.")

