// src/pages/Dashboard.tsx
import { useContext } from "react";
import { AuthContext } from "../context/AuthProvider";

export default function Dashboard() {
  const { user } = useContext(AuthContext);

  return (
    <div>
      <h2>Bienvenido al Dashboard</h2>
      {user && <p>Hola, {user.cnombre} 👋</p>}
    </div>
  );
}
