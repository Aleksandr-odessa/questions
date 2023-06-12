from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "Welcome  to servis vikorina"}

def test_is_creating_victorina():
    responce = client.post("/questions", json={'questions_num': 9})
    assert responce.status_code == 200
    responce_bad_json = client.post("/questions", json={'questions_num': 'w'})
    assert responce_bad_json.status_code == 422
    assert responce_bad_json.json() == {'detail': [{'loc': ['body', 'questions_num'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}
    responce_bad_path = client.post("/questio", json={'questions_num': 2})
    assert responce_bad_path.status_code == 404