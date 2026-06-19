// src/services/authService.ts
import { CUsuarioDTO } from "../dominios/CUsuarioDTO";

export interface LoginResponse {
  usuario: CUsuarioDTO;
  token: string;
}

export async function login(
  email: string,
  password: string
): Promise<LoginResponse> {
  const response = await fetch("http://127.0.0.1:5000/api/usuarios/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    throw new Error("Error en la autenticación");
  }

  const data = await response.json();

  // Mapear el JSON al DTO
  const usuario = new CUsuarioDTO(
    data.usuario.cestado,
    data.usuario.nidtusuario,
    data.usuario.cemail,
    data.usuario.nidtperfil,
    data.usuario.cnombre
  );

  return {
    usuario,
    token: data.token,
  };
}
