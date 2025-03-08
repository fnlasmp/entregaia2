document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function() {
        const message = userInput.value;
        if (message.trim() !== '') {
            // Display user message
            const userMessage = document.createElement('div');
            userMessage.textContent = 'User: ' + message;
            chatContainer.appendChild(userMessage);

            // Get chatbot response (replace with actual chatbot logic)
            const chatbotMessage = document.createElement('div');
            chatbotMessage.textContent = 'Chatbot: I\'m still under development, but I can tell you about our delicious donuts!';
            chatContainer.appendChild(chatbotMessage);

            // Clear user input
            userInput.value = '';
        }
    });
});