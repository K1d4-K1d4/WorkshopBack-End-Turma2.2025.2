from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
    #Caso eu queira colocar aplicativos em única pasta eu preciso colocar o nomeDaPasta.nomeDoApp na linha name
