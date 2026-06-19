// src/hooks/useLogin.ts
import { useState } from "react";
import { login} from "../servicios/authservicios";
import type { LoginResponse } from "../servicios/authservicios";

export function useLogin() {
  const [error, setError] = useState<string | null>(null);

  async function handleLogin(email: string, password: string): Promise<LoginResponse | null> {
    try {
      setError(null);
      return await login(email, password);
    } catch (err: any) {
      setError(err.message);
      return null;
    }
  }

  return { handleLogin, error };
}
