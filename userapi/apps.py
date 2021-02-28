from django.apps import AppConfig

# this i s essential to making the signals work 
class UserapiConfig(AppConfig):
    name = 'userapi'

    def ready(self):
        import userapi.signals