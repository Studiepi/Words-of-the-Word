from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

# Load the KJV Bible JSON
with open('bible_kjv.json', 'r', encoding='utf-8-sig') as kjv_file:
    kjv_bible = json.load(kjv_file)

# Function to search the Bible
def search_bible(bible, word):
    results = []
    word_lower = word.strip().lower()  # Strip whitespace and convert to lowercase
    footnote_pattern = r'\{.*?\}'  # Regular expression to match content inside {}

    for book_data in bible:
        book_abbrev = book_data.get("abbrev", "")
        chapters = book_data.get("chapters", [])

        for chapter_number, verses in enumerate(chapters, start=1):
            for verse_number, verse_text in enumerate(verses, start=1):
                # Remove footnotes from verse text for the search
                verse_text_cleaned = re.sub(footnote_pattern, '', verse_text).strip().lower()

                # If the cleaned verse contains the word, include the full verse in the results
                if word_lower in verse_text_cleaned:
                    results.append({
                        "reference": f"{book_abbrev} {chapter_number}:{verse_number}",
                        "text": verse_text  # Include the full verse with footnotes
                    })

    return results

# Route to handle real-time word count
@app.route('/count', methods=['POST'])
def count_word():
    word = request.json.get('word', '').strip().lower()
    if word:
        results = search_bible(kjv_bible, word)
        return jsonify(count=len(results))  # Return the count of occurrences
    else:
        return jsonify(count=0)

# Home route with the search form
@app.route('/')
def home():
    return render_template('index.html')

# Search route that handles the word search and shows results
@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('word', '').strip().lower()
    if word:
        results = search_bible(kjv_bible, word)
        return render_template('results.html', word=word, results=results)
    else:
        return render_template('results.html', word=word, results=[])

if __name__ == '__main__':
    app.run(debug=True)
