from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    #Função que mostra o nome do objeto de uma melhor forma
    def __str__(self):
        """
        Devolve uma representação em string do modelo.
        """
        return self.text
    
class Entry(models.Model):
    """Anotações de um assunto.
    https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Definindo como fica a classe no plural"""  
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'
