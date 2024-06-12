import os

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.status_code == 200


def test_f1_score():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file = open(os.path.join(parent_dir, 'results/results'), "r")

    score = 0

    while True:
        line = file.readline()
        if not line:
            break
        if 'f1 on test data' in line:
            score = float(line[17:])
            break

    file.close

    assert score > 0.5
