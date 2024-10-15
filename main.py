# from dotenv import load_dotenv
# import os
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_astradb import AstraDBVectorStore
# from langchain.agents import create_tool_calling_agent
# from langchain.agents import AgentExecutor
# from langchain.tools.retriever import create_retriever_tool
# from langchain import hub
# from github import fetch_github_issues
# from note import note_tool

# load_dotenv()

# def connect_to_vstore():
    
#     embeddings = OpenAIEmbeddings()
#     ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
#     ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
#     desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")

#     if desired_namespace:
#         ASTRA_DB_KEYSPACE = desired_namespace
#     else:
#         ASTRA_DB_KEYSPACE = None

#     # Create the AstraDB vector store
#     vstore = AstraDBVectorStore(
#         embedding=embeddings,
#         collection_name="github_st",
#         api_endpoint=ASTRA_DB_API_ENDPOINT,
#         token=ASTRA_DB_APPLICATION_TOKEN,
#         namespace=ASTRA_DB_KEYSPACE
#     )
#     return vstore

# vstore=connect_to_vstore()
# add_to_vectorstore=input("Do you want to update the issues> (y/N): ").lower() in ["yes", "y"]

# if add_to_vectorstore:
#     owner="mediar-ai"
#     repo="screenpipe"
#     issues=fetch_github_issues(owner,repo)

#     try:
#         vstore.delete_collection()
#     except:
#         pass

#     vstore = connect_to_vstore()
#     vstore.add_documents(issues)

#     # results = vstore.similarity_search("flash messages", k=3)
#     # for res in results:
#     #     print(f"* {res.page_content} {res.metadata}")

# retriever = vstore.as_retriever(search_kwargs={"k":3})
# retriever_tool = create_retriever_tool(
#     retriever,
#     "github_search",
#     "Search for information about github issues. For any questions about github issue you must use htis tool!"
# )

# prompt = hub.pull("hwchase17/openai-functions-agent")
# llm = ChatOpenAI()

# tools = [retriever_tool,note_tool]
# agent = create_tool_calling_agent(llm,tools,prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# while(question := input("Ask a question about the github issues (Enter q to quit): ")) !='q':
#     result=agent_executor.invoke({"input": question})
#     print(result["output"])







# import streamlit as st
# from dotenv import load_dotenv
# import os
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_astradb import AstraDBVectorStore
# from langchain.agents import create_tool_calling_agent
# from langchain.agents import AgentExecutor
# from langchain.tools.retriever import create_retriever_tool
# from langchain import hub
# from github import fetch_github_issues
# from note import note_tool

# # Load environment variables
# load_dotenv()

# # Streamlit title and description
# st.title("GitHub Issues Assistant")
# st.write("Ask questions about the GitHub issues and store notes!")

# # Connect to vector store
# def connect_to_vstore():
#     embeddings = OpenAIEmbeddings()
#     ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
#     ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
#     desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")

#     if desired_namespace:
#         ASTRA_DB_KEYSPACE = desired_namespace
#     else:
#         ASTRA_DB_KEYSPACE = None
    

#     # Create the AstraDB vector store
#     vstore = AstraDBVectorStore(
#         embedding=embeddings,
#         collection_name="github_st",
#         api_endpoint=ASTRA_DB_API_ENDPOINT,
#         token=ASTRA_DB_APPLICATION_TOKEN,
#         namespace=ASTRA_DB_KEYSPACE
#     )
#     return vstore

# vstore = connect_to_vstore()

# # Option to update GitHub issues in the vector store
# if st.checkbox("Update GitHub Issues in Vector Store"):
#     owner = st.text_input("GitHub Repo Owner:")
#     repo = st.text_input("GitHub Repo Name:")

#     if st.button("Fetch and Update Issues"):
#         issues = fetch_github_issues(owner, repo)
#         try:
#             vstore.delete_collection()
#         except:
#             pass

#         vstore.add_documents(issues)
#         st.success("GitHub Issues updated in the vector store.")

# # Create retriever tool
# retriever = vstore.as_retriever(search_kwargs={"k": 3})
# retriever_tool = create_retriever_tool(
#     retriever,
#     "github_search",
#     "Search for information about GitHub issues. For any questions about GitHub issues, you must use this tool!"
# )

# # Pull the prompt and LLM setup
# prompt = hub.pull("hwchase17/openai-functions-agent")
# llm = ChatOpenAI()

# # Tools and agent setup
# tools = [retriever_tool, note_tool]
# agent = create_tool_calling_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# # Input field for questions
# question = st.text_input("Ask a question about the GitHub issues:", placeholder="Type your question here...")

# if question:
#     result = agent_executor.invoke({"input": question})
#     st.write("Answer:")
#     st.write(result["output"])

# # Text area for saving notes
# note = st.text_area("Save a note:", placeholder="Type your note here...")

# if st.button("Save Note"):
#     note_tool(note)
#     st.success("Note saved successfully.")







import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from github import fetch_github_issues
from note import note_tool

# Load environment variables
load_dotenv()

def connect_to_vstore():
    embeddings = OpenAIEmbeddings()
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    desired_namespace = os.getenv("ASTRA_DB_KEYSPACE")

    if desired_namespace:
        ASTRA_DB_KEYSPACE = desired_namespace
    else:
        ASTRA_DB_KEYSPACE = None

    # Create the AstraDB vector store
    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name="github_st",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )
    return vstore

# Streamlit app
st.title("GitHub Issues Query Tool")

vstore=connect_to_vstore()

# Input for GitHub repository
owner = st.text_input("GitHub Repository Owner:", "mediar-ai")
repo = st.text_input("GitHub Repository Name:", "screenpipe")

# Button to fetch issues
if st.button("Fetch Issues"):
    issues = fetch_github_issues(owner, repo)

    # Clear existing collection
    try:
        vstore.delete_collection()
    except:
        pass
    # Update vector store with issues
    vstore=connect_to_vstore()
    vstore.add_documents(issues)
    st.success("Issues fetched and added to vector store.")

# Set up retriever
retriever = vstore.as_retriever(search_kwargs={"k": 3})
retriever_tool = create_retriever_tool(
    retriever,
    "github_search",
    "Search for information about GitHub issues. For any questions about GitHub issues you must use this tool!"
)

# Load LLM and create agent
prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI()
tools = [retriever_tool, note_tool]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Input for user question
question = st.text_input("Ask a question about the GitHub issues:")

if st.button("Submit Question"):
    if question:
        result = agent_executor.invoke({"input": question})
        st.write("Response:", result["output"])
    else:
        st.warning("Please enter a question.")

# Option to clear vector store (optional)
if st.button("Clear Vector Store"):
    try:
        vstore.delete_collection()
        st.success("Vector store cleared.")
    except:
        st.error("Failed to clear vector store.")
