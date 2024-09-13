// Function to update the word count as the user types
function updateWordCount() {
    const word = document.getElementById('word').value.trim();
    const partialMatch = document.getElementById('partialMatch').checked;
    const countElement = document.getElementById('count');

    if (word.length > 0) {
        // Make an API call to get the word count
        fetch(`/word_count?word=${word}&partial=${partialMatch}`)
            .then(response => response.json())
            .then(data => {
                // If it's just a single letter, customize the message
                if (word.length === 1) {
                    countElement.textContent = `The letter "${word}" appears ${data.count} times in the KJV Bible.`;
                } else {
                    countElement.textContent = `The word/phrase "${word}" appears ${data.count} times in the KJV Bible.`;
                }
            })
            .catch(error => {
                console.error('Error fetching word count:', error);
                countElement.textContent = 'An error occurred while fetching word count.';
            });
    } else {
        countElement.textContent = 'Number of occurrences will be displayed here';
    }
}
