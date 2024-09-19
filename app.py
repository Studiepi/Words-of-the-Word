from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

# Load the KJV Bible JSON data
try:
    with open('static/bible_kjv.json', 'r', encoding='utf-8-sig') as kjv_file:
        kjv_bible = json.load(kjv_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading JSON file: {e}")
    kjv_bible = []  # Empty list to avoid further errors

# Function to highlight the search word in each verse
def highlight_word_in_verse(verse, word):
    escaped_word = re.escape(word)
    highlighted_verse = re.sub(f'({escaped_word})', r'<strong>\1</strong>', verse, flags=re.IGNORECASE)
    return highlighted_verse

# Function to search for the word in the Bible and return matching verses
def search_bible(bible, word, partial_match=False):
    word_lower = word.lower()
    results = []
    for book in bible:
        for chapter_number, chapter in enumerate(book['chapters'], 1):
            for verse_number, verse in enumerate(chapter, 1):
                verse_lower = verse.lower()
                if partial_match:
                    if word_lower in verse_lower:
                        results.append({
                            'book': book['abbrev'],
                            'chapter': chapter_number,
                            'verse': verse_number,
                            'text': highlight_word_in_verse(verse, word)
                        })
                else:
                    if re.search(rf'\b{re.escape(word_lower)}\b', verse_lower):
                        results.append({
                            'book': book['abbrev'],
                            'chapter': chapter_number,
                            'verse': verse_number,
                            'text': highlight_word_in_verse(verse, word)
                        })
    return results

def search_bible_count(bible, word, partial):
    count = 0
    word_lower = word.lower()
    for book in bible:
        for chapter in book['chapters']:
            for verse in chapter:
                if partial:
                    if word_lower in verse.lower():
                        count += 1
                else:
                    words_in_verse = verse.lower().split()
                    if word_lower in words_in_verse:
                        count += 1
    return count

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count')
def get_word_count():
    word = request.args.get('word', '').strip()
    partial_match = request.args.get('partialMatch', 'false').lower() == 'true'

    if word:
        count = search_bible_count(kjv_bible, word, partial_match)
        return jsonify({'success': True, 'count': count})
    return jsonify({'success': False})

@app.route('/search', methods=['POST'])
def search():
    word = request.form['word'].strip()
    partial_match = 'partialMatch' in request.form

    if word:
        results = search_bible(kjv_bible, word, partial_match)
        return render_template('results.html', word=word, results=results, count=len(results))
    else:
        return render_template('index.html', error="Please enter a valid word.")

if __name__ == "__main__":
    app.run(debug=True)
