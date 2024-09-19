// Function to update the word count as the user types
function updateWordCount() {
    const word = document.getElementById("word").value.trim();
    const partialMatch = document.getElementById("partialMatch").checked;

    if (word.length > 0) {
        fetch(`/count?word=${encodeURIComponent(word)}&partialMatch=${partialMatch}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById("count").innerHTML = `"${word}" appears ${data.count} times in the KJV Bible.`;
                } else {
                    document.getElementById("count").innerHTML = "An error occurred while fetching word count.";
                }
            })
            .catch(() => {
                document.getElementById("count").innerHTML = "An error occurred while fetching word count.";
            });
    } else {
        document.getElementById("count").innerHTML = "";
    }
}
