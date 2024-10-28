<script>
    // Mock data for messages
    let messages = [
      { id: 1, sender: 'Alice', text: 'Hello!', time: '10:00 AM' },
      { id: 2, sender: 'You', text: 'Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice! Hi Alice!', time: '10:01 AM' },
      { id: 3, sender: 'Alice', text: 'How are you?', time: '10:02 AM' },
      { id: 4, sender: 'You', text: 'I am good, thanks!', time: '10:03 AM' },
    ];
  
    let newMessage = '';
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
      <button>Send</button>
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