<script>
  let messages = [
    // Existing messages...
  ];

  let newMessage = '';

  async function sendMessage() {
    if (newMessage.trim() !== '') {
      // Add the new message to the messages array
      messages = [
        ...messages,
        {
          id: messages.length + 1,
          sender: 'You',
          text: newMessage,
          time: new Date().toLocaleTimeString(),
        },
      ];

      // Prepare the conversation history (last 10 messages)
      const history = messages.slice(-10);

      // Send the new message and history to the backend
      try {
        const response = await fetch('http://localhost:8000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: newMessage, history: history }),
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();

        // Add the response message to the messages array
        messages = [
          ...messages,
          {
            id: messages.length + 1,
            sender: 'Assistant',
            text: data.reply,
            time: new Date().toLocaleTimeString(),
          },
        ];
      } catch (error) {
        console.error('Error:', error);
      }

      // Clear the input field
      newMessage = '';
    }
  }
</script>


<main>
    <!-- Header -->
    <div class="chat-header">
      <h2>Chat With Your Documents</h2>
    </div>

    <!-- Messages -->
    <div class="chat-messages">
      {#each messages as message}
        <div class="message {message.sender === 'You' ? 'user' : 'system'}">
          <div class="message-content">
            <p>{message.text}</p>
          </div>
        </div>
      {/each}
    </div>

    <!-- Input -->
    <div class="chat-input">
      <input class="input-field"
        type="text"
        placeholder="Ask something about your documents..."
        bind:value={newMessage}
      />
      <button on:click={sendMessage}>Send</button>
    </div>
</main>

<style>
    main {
        width: 80ex;
        margin: 0 10%;
    }

    .message {
        margin: 10px;
        padding: 10px;
        border-radius: 20px;
    }

    .message.user {
        background-color: lightgray;
        margin-left: 5ex;
    }
    
    .message.system {
        background-color: rgb(255, 211, 192);
        margin-right: 5ex;
    }

    p {
        margin: 1ex;
    }

</style>