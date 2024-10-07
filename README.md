
# Words of the Word - Bible Search Application

This is a Flask-based web application that allows users to search the King James Version (KJV) of the Bible for specific words or phrases. It provides the option to match exact words or allow partial matches. The results display Bible verses where the word/phrase appears, and the matched words are highlighted in bold.

## Features

- **Search the KJV Bible**: Enter a word or phrase, and the app will search the Bible and return matching verses.
- **Word Count Display**: As the user types, the number of times the word or phrase appears in the Bible is shown dynamically.
- **Exact or Partial Match**: Users can toggle between exact word matches or partial matches using a checkbox.
- **Highlighted Search Terms**: The search term is highlighted in the search results to help users easily spot it in the verses.
- **Dark Themed UI**: The application features a clean, dark-themed user interface with shades of grey for a pleasant reading experience.

## Installation

### Prerequisites

- Python 3.x installed on your machine
- `Flask` installed in your Python environment
  ```bash
  pip install flask
  ```

### Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/words-of-the-word.git
    cd words-of-the-word
    ```

2. **Install dependencies**:
    If you don’t have Flask installed, run:
    ```bash
    pip install flask
    ```

3. **Download the KJV JSON file**:
    Place the `kjv.json` file inside the `static/` folder. This file contains the entire King James Bible in JSON format.

4. **Run the app**:
    ```bash
    python app.py
    ```

5. **Visit the app**:
    Open your browser and go to `http://127.0.0.1:5000` to start using the application.

## File Structure

```
words-of-the-word/
│
├── static/
│   ├── kjv.json          # The King James Bible in JSON format
│   ├── styles.css        # Custom styles for the UI
│   └── scripts.js        # JavaScript for dynamic word count
│
├── templates/
│   ├── index.html        # Main search page
│   └── results.html      # Search results page
│
├── app.py                # The Flask application
├── README.md             # This README file
└── requirements.txt      # Python dependencies (optional)
```

## How to Use

1. **Search**: On the main page, enter a word or phrase in the search bar. As you type, the number of occurrences in the Bible will be displayed dynamically.
2. **Exact or Partial Match**: Use the checkbox to choose between exact matches (default) or partial matches. 
3. **Results**: Click "See all verses containing word/phrase" to view verses where the word/phrase appears. The results will be highlighted in bold within the verse.
4. **Back to Search**: You can return to the search page by clicking the "Back to Search" link.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.