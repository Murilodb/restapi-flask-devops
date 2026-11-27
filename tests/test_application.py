import pytest
from applications import create_app

class TestApp():

    # Fixtures para criar o cliente de teste e dados de usuário válidos e inválidos
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        
        return app.test_client()

    #Fixtures para criar dados de usuário válidos e inválidos
    @pytest.fixture
    def valid_user(self):
        return {
            'first_name': 'Maria',
            'last_name': 'Silva',
            'email': 'maria@example.com',
            'cpf': '006.741.880-55',
            'birth_date': '1990-01-01',
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            'first_name': 'Maria',
            'last_name': 'Silva',
            'email': 'maria@example.com',
            'cpf': '12345678900',  # Invalid CPF
            'birth_date': '1990-01-01',
        }

    #Fixture para validar se usuario já existe no banco de dados
    @pytest.fixture
    def existing_user(self, client, valid_user):
        client.post('/user', json=valid_user)
        return valid_user

    
    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert response.get_json() == {'message': 'User created successfully'}

    def test_post_user_invalid_cpf(self, client, invalid_user):
        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert response.get_json() == {'message': 'Invalid CPF'}

    def test_post_user_existing_cpf(self, client, existing_user):
        response = client.post('/user', json=existing_user)
        assert response.status_code == 400
        assert response.get_json() == {'message': 'User with this CPF already exists'}


    def test_get_user(self, client, existing_user):
        response = client.get(f"/user/{existing_user['cpf']}")
        assert response.status_code == 200
        assert response.get_json()[0]['cpf'] == existing_user['cpf']