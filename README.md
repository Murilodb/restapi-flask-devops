# restapi-flask-devops
API Rest feita em Flask para praticar conteúdos de devops, como CI/CD, Kubernetes e Helm

# Troubleshooting
- **Flask 3.x / Werkzeug 3.x incompatíveis com flask-mongoengine:** versões fixadas em Flask 2.1.2 e Werkzeug 2.2.2 (`requirements.txt`).
- **Connection refused ao acessar a API no container:** `app.run` com `host='0.0.0.0'`.
- **Connection refused no MongoDB:** o host em `MONGODB_SETTINGS` deve ser o nome do serviço do compose (`mongo`), e não `localhost`.
- **Container inacessível com a VPN ativa:** a rota da VPN sobrepunha a rede do Docker (`172.22.0.0/16`); sub-rede fixada em `192.168.200.0/24` no `docker-compose.yaml`.
