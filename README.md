# News Article Summarizer

This project is a web application that summarizes news articles using `dotenv`, `Streamlit`, and `langchain_groq`.

## Features

- Upload a news article in `.txt` format
- View the uploaded article
- Summarize the article with a click of a button
- Display the summarized news article

## Requirements

- Python 3.x
- `dotenv`
- `Streamlit`
- `langchain_groq`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/news-article-summarizer.git
    cd news-article-summarizer
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with the necessary environment variables:
    ```dotenv
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload a `.txt` file containing your news article.

4. Click the "Summarize Article" button to get the summarized version of the article.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Thanks

Thank you for checking out this project! If you have any questions or feedback, feel free to reach out.
