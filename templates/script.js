function getEmoji(emotion) {
    const emojis = {
        "Happy": "😊",
        "Positive": "🙂",
        "Neutral": "😐",
        "Sad": "😢",
        "Negative": "😠"
    };
    return emojis[emotion] || "😶";
}

async function analyzeEmotion() {
    const text = document.getElementById("textInput").value;
    const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    });

    const result = await response.json();
    const emoji = getEmoji(result.emotion);

    document.getElementById("result").innerHTML = `
                Emotion detected: <strong>${result.emotion}</strong>
                <div class="emoji">${emoji}</div>
            `;
}
