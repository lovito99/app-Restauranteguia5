// src/components/LoginForm.tsx
import { useState, useContext } from "react";
import  { useLogin } from "../hooks/userlogin";
import { AuthContext } from "../context/AuthProvider";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { handleLogin, error } = useLogin();
  const { login } = useContext(AuthContext);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    const result = await handleLogin(email, password);
    if (result) login(result.usuario, result.token);
  }

  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        placeholder="Correo"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Ingresar</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}
