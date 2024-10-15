# GitHub Issues AI Agent

This project is a Streamlit-based application that allows users to query and manage GitHub issues using a LangChain-based language model agent and AstraDB vector store for efficient retrieval.

## Features

- **Fetch Issues:** Retrieve GitHub issues from a specified repository and store them in AstraDB.
- **Query Issues:** Use natural language to query the issues via a LangChain agent.
- **Save Notes:** Save notes locally using the note tool.
- **Clear Vector Store:** Optionally clear the vector store if you need to reset the stored data.

## Setup Instructions

To run this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment:

    ```bash
    python -m venv virenv
    source virenv/bin/activate   # On Windows: virenv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

   Create a `.env` file in the project root and add the following:

    ```ini
    GITHUB_TOKEN=your_github_token
    ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
    ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
    ASTRA_DB_KEYSPACE=your_keyspace
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

   The Streamlit app will be available at [http://localhost:8501](http://localhost:8501).

## Usage Instructions

1. **Enter GitHub Repository Details:**
   - Specify the repository owner and name (e.g., `mediar-ai/screenpipe`).
   - Click "Fetch Issues" to retrieve the latest issues and store them in AstraDB.

2. **Query GitHub Issues:**
   - Enter a natural language question about the GitHub issues.
   - The LangChain agent will respond based on the stored issues.

3. **Save Notes:**
   - Add a note using the app, and it will be saved locally in `notes.txt`.

4. **Clear Vector Store:**
   - Optionally, click "Clear Vector Store" to remove the stored issues from AstraDB.

## Technologies Used

- [LangChain](https://langchain.com/) - For creating the language model agent and handling vector stores.
- [Streamlit](https://streamlit.io/) - Provides the web-based interface.
- [AstraDB](https://astra.datastax.com/) - For storing GitHub issues as vector embeddings.
- [GitHub API](https://docs.github.com/en/rest) - For fetching issues from specified repositories.
- [Python](https://www.python.org/) - The core programming language.

## Future Improvements

- Add user authentication for GitHub.
- Support querying across multiple repositories.
- Improve the note-taking functionalities.
- Enhance error handling and logging.


