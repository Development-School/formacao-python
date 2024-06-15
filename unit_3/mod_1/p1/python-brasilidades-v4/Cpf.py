from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_Valido(self, documento):
        if len(documento) == 11:
            # return True
            validador = CPF()
            return validador.validate(documento)
        else:
            # return False
            raise ValueError("Quantidade de dígitos inválida")
        # cpf = CPF()
        # return cpf.validate(documento)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()

        # Melhoria 01:
        # return CPF().mask(self.cpf) \
        #     if len(self.cpf) == 11 \
        #     else self.cpf