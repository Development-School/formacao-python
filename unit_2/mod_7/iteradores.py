
registro = open('acessos.log', 'r')
sites_sem_https = [url for url in registro if url.startswith('http://')]

print("-----------------------------------------------")

print(sites_sem_https)
print(sites_sem_https[0])

print("-----------------------------------------------")

for site in sites_sem_https:
    print(site.replace('\n', ""))

print("-----------------------------------------------")

class IteradorHttp():
    def __init__(self):
        self.registro = open('acessos.log', 'r')
        self.linha_atual = ''
    def __iter__(self):
        return self
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration

iterador = IteradorHttp()

print(next(iterador))
print(next(iterador))
# print(next(iterador)) #Error
print(next(iterador, 'Fim da extração!'))

print("-----------------------------------------------")

iterador = IteradorHttp()

for url in iterador:
    print(url)

print("-----------------------------------------------")