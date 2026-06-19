// src/domain/CUsuarioDTO.ts
export class CUsuarioDTO {
  cestado: string;
  nidtusaurio: number;
  cemail: string;
  nidtperfil: number;
  cnombre: string;

  constructor(
    cestado: string,
    nidtusaurio: number,
    cemail: string,
    nidtperfil: number,
    cnombre: string
  ) {
    this.cestado = cestado;
    this.nidtusaurio = nidtusaurio;
    this.cemail = cemail;
    this.nidtperfil = nidtperfil;
    this.cnombre = cnombre;
  }
}
