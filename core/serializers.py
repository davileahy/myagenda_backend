from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove o campo "username" imediatamente após a inicialização
        if 'username' in self.fields:
            self.fields.pop('username')

    def validate(self, data):
        # Define o username automaticamente como o email para evitar problemas internos
        data['username'] = data.get('email')
        return data

    def custom_signup(self, request, user):
        # Se precisar adicionar lógica customizada durante o signup, faça aqui.
        pass
