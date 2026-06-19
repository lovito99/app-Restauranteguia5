// src/pages/LoginPage.tsx
import LoginForm from "../componentes/LoginForm";

export default function LoginPage() {
  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
      padding: "20px",
    }}>
      <div style={{
        background: "#fff",
        borderRadius: "16px",
        boxShadow: "0 20px 60px rgba(0,0,0,0.3)",
        padding: "48px 40px",
        width: "100%",
        maxWidth: "420px",
      }}>
        <div style={{ textAlign: "center", marginBottom: "32px" }}>
          <div style={{ fontSize: "48px", marginBottom: "8px" }}>🍽️</div>
          <h2 style={{
            margin: "0 0 8px",
            fontSize: "28px",
            fontWeight: 700,
            color: "#1a1a2e",
          }}>
            Sistema Restaurante
          </h2>
          <p style={{ margin: 0, color: "#6b7280", fontSize: "15px" }}>
            Ingresa tus credenciales para continuar
          </p>
        </div>
        <LoginForm />
      </div>
    </div>
  );
}
