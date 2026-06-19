// src/pages/Dashboard.tsx
import { useContext } from "react";
import { AuthContext } from "../context/AuthProvider";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  function handleLogout() {
    logout();
    navigate("/login");
  }

  return (
    <div style={{
      minHeight: "100vh",
      background: "#f3f4f6",
    }}>
      {/* Navbar */}
      <nav style={{
        background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        padding: "16px 32px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        boxShadow: "0 4px 20px rgba(0,0,0,0.15)",
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <span style={{ fontSize: "28px" }}>🍽️</span>
          <span style={{ color: "#fff", fontSize: "20px", fontWeight: 700 }}>
            Sistema Restaurante
          </span>
        </div>
        <button
          onClick={handleLogout}
          style={{
            padding: "10px 20px",
            fontSize: "14px",
            fontWeight: 600,
            color: "#764ba2",
            background: "#fff",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            transition: "opacity 0.2s",
          }}
          onMouseEnter={(e) => ((e.target as HTMLElement).style.opacity = "0.85")}
          onMouseLeave={(e) => ((e.target as HTMLElement).style.opacity = "1")}
        >
          Cerrar sesión
        </button>
      </nav>

      {/* Contenido */}
      <div style={{ padding: "40px 32px", maxWidth: "900px", margin: "0 auto" }}>
        <div style={{
          background: "#fff",
          borderRadius: "16px",
          padding: "40px",
          boxShadow: "0 4px 20px rgba(0,0,0,0.08)",
        }}>
          <h2 style={{
            margin: "0 0 8px",
            fontSize: "28px",
            fontWeight: 700,
            color: "#1a1a2e",
          }}>
            Dashboard
          </h2>
          {user && (
            <div style={{
              marginTop: "20px",
              padding: "20px",
              background: "linear-gradient(135deg, rgba(102,126,234,0.08) 0%, rgba(118,75,162,0.08) 100%)",
              borderRadius: "12px",
              border: "1px solid rgba(118,75,162,0.15)",
            }}>
              <p style={{ margin: "0 0 8px", fontSize: "22px", color: "#1a1a2e" }}>
                👋 Hola, <strong>{user.cnombre}</strong>
              </p>
              <p style={{ margin: 0, fontSize: "14px", color: "#6b7280" }}>
                {user.cemail} &middot; Perfil #{user.nidtperfil}
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
