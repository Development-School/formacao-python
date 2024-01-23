
class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views


video = Video("Stream de vídeo", "01:00", 1000)
print(video.titulo)