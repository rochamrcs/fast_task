from http import HTTPStatus

from fastapi.testclient import TestClient

from intro_fastapi.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/olamundo')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""}  # Assert
