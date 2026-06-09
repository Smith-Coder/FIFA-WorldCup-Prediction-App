import Message from "./Message";

function ChatBox({ chat, loading }) {
  return (
    <div className="chat-container">
      {chat.map((msg, i) => (
        <Message key={i} msg={msg} />
      ))}

      {loading && <Message msg={{ role: "assistant", content: "🤖 Thinking..." }} />}
    </div>
  );
}

export default ChatBox;