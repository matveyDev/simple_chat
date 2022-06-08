<template>
  <div class="container">
    <div class="chat">
      <h1 class="title">Simple Chat</h1>
      <hr />
      <form @submit.prevent="sendMessage" class="message-form">
        <h1 class="title__message-form">Write your message:</h1>
        <div class="inline-form">
          <input
            v-model="message"
            placeholder="Type your message"
            class="input__message-form"
            type="text"
          />
          <button class="btn__message-form">Send</button>
        </div>
      </form>
      <hr />
      <div class="chat__messages">
        <div>
          <h1 class="title__messages">Messages:</h1>
          <div class="chat__messages-blcok" id="messages">
            <li class="chat__message" v-for="m in messages" :key="m.id">
              {{ m.id }}.
              {{ m.message }}
            </li>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SimpleChat",
  data() {
    return {
      message: "",
      connection: null,
      messages: [],
    };
  },
  created() {
    this.connection = new WebSocket("ws://localhost:8000/");
    this.connection.onmessage = (event) => {
      const message = JSON.parse(event.data);
      this.messages.push(message);
    };
  },
  methods: {
    sendMessage() {
      const message_json = JSON.stringify({ message: this.message });
      this.connection.send(message_json);
      this.message = "";
    },
  },
};
</script>

<style>
li {
  display: block;
}
hr {
  padding: 0;
  margin: 10px 0;
  width: 400px;
  height: 0.1px;
  background-color: gray;
}
h1 {
  font-family: arial;
  padding: 0;
  margin: 0;
}
.title {
  color: rgb(36, 212, 154);
}
.title__messages {
  font-size: 20px;
  margin-bottom: 5px;
}
.title__message-form {
  font-size: 20px;
  padding-bottom: 10px;
}
.chat__messages-blcok {
  display: flex;
  flex-direction: column;
  padding: 0;
  margin: 0;
}
.container {
  display: flex;
  justify-content: center;
}
.chat {
  margin-top: 50px;
  padding: 40px 250px 50px 250px;
  overflow: hidden;
  max-width: 750px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 3px solid;
  border-radius: 10px;
  border-color: rgb(30, 173, 126);
}
.chat__messages {
  align-self: flex-start;
  margin-top: 50px;
}
.chat__message {
  font-family: arial;
  font-size: 19px;
  padding: 3px;
  margin: 5px 0;
  background-color: rgb(30, 173, 126);
  border-radius: 5px;
}
.message-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.inline-form {
  display: flex;
  align-items: center;
  padding-bottom: 5px;
}
.input__message-form {
  height: 15px;
  width: 200px;
}
.btn__message-form {
  margin: 0 0 0 7px;
  background-color: rgb(30, 173, 126);
  border-color: rgb(30, 173, 126);
  border-radius: 5px;
  padding: 3px 7px;
}
</style>
