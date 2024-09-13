from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the KJV Bible JSON file
with open('static/bible_kjv.json', 'r', encoding='utf-8-sig') as kjv_file:
    kjv_bible = json.load(kjv_file)

# Function to search the Bible for the word/phrase (with optional partial matching)
def search_bible(bible, word, partial):
    results = []
    word_lower = word.lower()

    for book in bible:
        for chapter_index, chapter in enumerate(book['chapters']):
            for verse_index, verse in enumerate(chapter):
                # Apply filtering based on the checkbox value (exact or partial match)
                if partial:
                    if word_lower in verse.lower():
                        results.append({
                            'book': book['abbrev'],
                            'chapter': chapter_index + 1,
                            'verse': verse_index + 1,
                            'text': verse
                        })
                else:
                    words_in_verse = verse.lower().split()
                    if word_lower in words_in_verse:
                        results.append({
                            'book': book['abbrev'],
                            'chapter': chapter_index + 1,
                            'verse': verse_index + 1,
                            'text': verse
                        })
    return results

# Function to count occurrences of the word/phrase (with optional partial matching)
def search_bible_count(bible, word, partial):
    count = 0
    word_lower = word.lower()

    for book in bible:
        for chapter in book['chapters']:
            for verse in chapter:
                # Apply filtering based on the checkbox value (exact or partial match)
                if partial:
                    if word_lower in verse.lower():
                        count += 1
                else:
                    words_in_verse = verse.lower().split()
                    if word_lower in words_in_verse:
                        count += 1

    return count

# Route to handle the word count query for real-time updating
@app.route('/word_count')
def word_count():
    word = request.args.get('word', '')
    partial = request.args.get('partial', 'false').lower() == 'true'
    count = search_bible_count(kjv_bible, word, partial)
    
    return jsonify({"count": count})

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the search query
@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('word', '')
    partial = request.form.get('partialMatch') == 'on'
    
    results = search_bible(kjv_bible, word, partial)
    
    return render_template('results.html', word=word, results=results)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
