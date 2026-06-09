import { useState } from "react";
import axios from "axios";
import ChatBox from "./components/ChatBox";
import InputBar from "./components/InputBar";
import "./App.css";

function App() {
  const [chat, setChat] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (message) => {
    if (!message.trim()) return;

    setChat((prev) => [...prev, { role: "user", content: message }]);
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message,
        history,
      });

      setHistory(res.data.history);

      setChat((prev) => [
        ...prev,
        { role: "assistant", content: res.data.response },
      ]);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <header>⚽ FIFA Predictor</header>

      <ChatBox chat={chat} loading={loading} />

      <InputBar onSend={sendMessage} />
    </div>
  );
}

export default App;