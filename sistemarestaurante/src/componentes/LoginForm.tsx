// src/components/LoginForm.tsx
import { useState, useContext } from "react";
import  { useLogin } from "../hooks/userlogin";
import { AuthContext } from "../context/AuthProvider";

const inputStyle: React.CSSProperties = {
  width: "100%",
  padding: "14px 16px",
  fontSize: "15px",
  border: "2px solid #e5e7eb",
  borderRadius: "10px",
  outline: "none",
  transition: "border-color 0.2s, box-shadow 0.2s",
  boxSizing: "border-box",
  background: "#f9fafb",
  color: "#1a1a2e",
};

const inputFocusHandler = (e: React.FocusEvent<HTMLInputElement>) => {
  e.target.style.borderColor = "#764ba2";
  e.target.style.boxShadow = "0 0 0 3px rgba(118,75,162,0.15)";
  e.target.style.background = "#fff";
};

const inputBlurHandler = (e: React.FocusEvent<HTMLInputElement>) => {
  e.target.style.borderColor = "#e5e7eb";
  e.target.style.boxShadow = "none";
  e.target.style.background = "#f9fafb";
};

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { handleLogin, error } = useLogin();
  const { login } = useContext(AuthContext);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    const result = await handleLogin(email, password);
    if (result) login(result.usuario, result.token);
    setLoading(false);
  }

  return (
    <form onSubmit={onSubmit} style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
      <div>
        <label style={{ display: "block", marginBottom: "6px", fontSize: "14px", fontWeight: 600, color: "#374151" }}>
          Correo electrónico
        </label>
        <input
          type="email"
          placeholder="usuario@correo.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          onFocus={inputFocusHandler}
          onBlur={inputBlurHandler}
          style={inputStyle}
          required
        />
      </div>

      <div>
        <label style={{ display: "block", marginBottom: "6px", fontSize: "14px", fontWeight: 600, color: "#374151" }}>
          Contraseña
        </label>
        <input
          type="password"
          placeholder="••••••••"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          onFocus={inputFocusHandler}
          onBlur={inputBlurHandler}
          style={inputStyle}
          required
        />
      </div>

      <button
        type="submit"
        disabled={loading}
        style={{
          marginTop: "8px",
          padding: "14px",
          fontSize: "16px",
          fontWeight: 600,
          color: "#fff",
          background: loading
            ? "#a78bfa"
            : "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
          border: "none",
          borderRadius: "10px",
          cursor: loading ? "not-allowed" : "pointer",
          transition: "opacity 0.2s, transform 0.1s",
          opacity: loading ? 0.7 : 1,
        }}
        onMouseDown={(e) => !loading && ((e.target as HTMLElement).style.transform = "scale(0.98)")}
        onMouseUp={(e) => ((e.target as HTMLElement).style.transform = "scale(1)")}
        onMouseLeave={(e) => ((e.target as HTMLElement).style.transform = "scale(1)")}
      >
        {loading ? "Ingresando..." : "Ingresar"}
      </button>

      {error && (
        <div style={{
          padding: "12px 16px",
          background: "#fef2f2",
          border: "1px solid #fecaca",
          borderRadius: "10px",
          color: "#dc2626",
          fontSize: "14px",
          textAlign: "center",
        }}>
          {error}
        </div>
      )}
    </form>
  );
}
