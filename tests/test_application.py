import pytest
from applications import create_app

class TestApp():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            'first_name': 'Maria',
            'last_name': 'Silva',
            'email': 'maria@example.com',
            'cpf': '52998224725',
            'birth_date': '1990-01-01',
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            'first_name': 'Maria',
            'last_name': 'Silva',
            'email': 'maria@example.com',
            'cpf': '52998224727',
            'birth_date': '1990-01-01',
        }

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