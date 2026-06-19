// src/context/AuthContext.tsx
import { createContext, useState } from "react";
import type { ReactNode } from "react";
import { CUsuarioDTO } from "../dominios/CUsuarioDTO";

interface AuthContextType {
  user: CUsuarioDTO | null;
  token: string | null;
  login: (userData: CUsuarioDTO, token: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType>({
  user: null,
  token: null,
  login: () => {},
  logout: () => {},
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<CUsuarioDTO | null>(null);
  const [token, setToken] = useState<string | null>(null);

  const login = (userData: CUsuarioDTO, token: string) => {
    setUser(userData);
    setToken(token);
    localStorage.setItem("token", token);
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
