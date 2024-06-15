from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_Valido(self, documento):
        # if len(documento) == 11:
        #     # return True
        #     validador = CPF()
        #     return validador.validate(documento)
        # else:
        #     # return False
        #     raise ValueError("Quantidade de dígitos inválida")
        cpf = CPF()
        return cpf.validate(documento)

    # def format_cpf(self):
    #     fatia_um = self.cpf[:3]
    #     fatia_dois = self.cpf[3:6]
    #     fatia_tres = self.cpf[6:9]
    #     fatia_quatro = self.cpf[9:]
    #
    #     return ("{}.{}.{}-{}".format(
    #         fatia_um,
    #         fatia_dois,
    #         fatia_tres,
    #         fatia_quatro
    #     ))

    def __str__(self):
        # return self.format_cpf()

        # Melhoria 01:
        return CPF().mask(self.cpf) \
            if len(self.cpf) == 11 \
            else self.cpf