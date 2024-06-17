from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        self.tipo_documento = tipo_documento

        if self.tipo_documento == 'cpf':
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def cpf_eh_Valido(self, documento):
        # if len(cpf) == 11:
        #     validador = CPF()
        #     return validador.validate(cpf)
        # else:
        #     raise ValueError("Quantidade de dígitos inválida!")
        # cpf = CPF()
        # return cpf.validate(documento)
        return CPF().validate(documento)


    def cnpj_eh_Valido(self, documento):
        # if len(documento) == 14:
        #     validate_cnpj = CNPJ()
        #     return validate_cnpj.validate(documento)
        # else:
        #     raise ValueError("Quantidade de dígitos inválida!")
        return CNPJ().validate(documento)

    # def format_cpf(self):
    #     mascara = CPF()
    #     return mascara.mask(self.cpf)

    def __str__(self):
        # return self.format_cpf()

        # Melhoria 01:
        # return CPF().mask(self.cpf) \
        #     if len(self.cpf) == 11 \
        #     else self.cpf
        if (self.tipo_documento == 'cpf'):
            return CPF().mask(self.cpf) \
                if len(self.cpf) == 11 \
                else self.cpf
        else:
            return CNPJ().mask(self.cnpj) \
                if len(self.cnpj) == 14 \
                else self.cnpj