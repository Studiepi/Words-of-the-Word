import json

def search_bible(bible, word):
    results = []
    word_lower = word.strip().lower()  # Strip whitespace and convert to lowercase

    for book_data in bible:
        book_abbrev = book_data.get("abbrev", "")
        chapters = book_data.get("chapters", [])

        for chapter_number, verses in enumerate(chapters, start=1):
            for verse_number, verse_text in enumerate(verses, start=1):
                verse_text_cleaned = verse_text.strip().lower()  # Strip whitespace and convert to lowercase

                # Debug print statements
                print(f"Checking verse {verse_number} in {book_abbrev} Chapter {chapter_number}: {verse_text_cleaned}")

                if word_lower in verse_text_cleaned:
                    results.append({
                        "reference": f"{book_abbrev} {chapter_number}:{verse_number}",
                        "text": verse_text
                    })

    return results

if __name__ == "__main__":
    try:
        with open('bible_kjv.json', 'r', encoding='utf-8-sig') as kjv_file:
            kjv_bible = json.load(kjv_file)
            # Print structure of first few books
            for i, book_data in enumerate(kjv_bible[:2]):  # Inspect first 2 books for brevity
                print(f"Book {i}: {book_data}")

            test_word = 'God'  # Change to a common word for testing
            results = search_bible(kjv_bible, test_word)
            if results:
                print(f"Results for '{test_word}':")
                for result in results:
                    print(f"{result['reference']}: {result['text'][:200]}...")  # Print only the first 200 characters of each verse
            else:
                print(f"No results found for '{test_word}'")
    except Exception as e:
        print(f"Error: {e}")

