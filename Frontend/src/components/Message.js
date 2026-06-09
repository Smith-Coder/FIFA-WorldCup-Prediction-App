import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function Message({ msg }) {
  return (
    <div className={`message ${msg.role}`}>
      {msg.role === "assistant" ? (
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {msg.content}
        </ReactMarkdown>
      ) : (
        msg.content
      )}
    </div>
  );
}

export default Message;