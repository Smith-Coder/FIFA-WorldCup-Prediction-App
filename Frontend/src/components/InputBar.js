import { useState } from "react";

function InputBar({ onSend }) {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <div className="input-container">
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about matches..."
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();   // ✅ ENTER submits
          }
        }}
      />

      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default InputBar;