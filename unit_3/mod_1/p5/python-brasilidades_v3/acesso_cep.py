""" ALURA ▼
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
"""

import  requests

class BuscaEndereco:

    def __init__(self, cep):
        if (self.cep_e_valido(str(cep))):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!!")

    def cep_e_valido(self, cep):
        return True if (len(cep) == 8) else False

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        cep = self.cep
        return f'{str(cep)[:5]}-{str(cep)[5:]}'

    def acessa_api_via_cep(self):
        url = f"https://viacep.com.br/ws/" \
              f"{str(self.cep)}" \
              f"/json/"

        # print(url)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
