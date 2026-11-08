import logging
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_logs_operation_operands_and_result(caplog):
    caplog.set_level(logging.INFO)

    response = client.post("/add", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert "Operation: add" in caplog.text
    assert "a=10.0, b=5.0" in caplog.text
    assert "result=15.0" in caplog.text

def test_subtract_logs_operation_operands_and_result(caplog):
    caplog.set_level(logging.INFO)

    response = client.post("/subtract", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert "Operation: subtract" in caplog.text
    assert "a=10.0, b=5.0" in caplog.text
    assert "result=5.0" in caplog.text

def test_multiply_logs_operation_operands_and_result(caplog):
    caplog.set_level(logging.INFO)

    response = client.post("/multiply", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert "Operation: multiply" in caplog.text
    assert "a=10.0, b=5.0" in caplog.text
    assert "result=50.0" in caplog.text

def test_divide_logs_operation_operands_and_result(caplog):
    caplog.set_level(logging.INFO)

    response = client.post("/divide", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert "Operation: divide" in caplog.text
    assert "a=10.0, b=5.0" in caplog.text
    assert "result=2.0" in caplog.text  

def test_divide_by_zero_logs_error(caplog):
    caplog.set_level(logging.ERROR)

    response = client.post("/divide", json={"a": 10, "b": 0})

    assert response.status_code == 400
    assert "Divide Operation Error" in caplog.text
    assert "Cannot divide by zero - you just broke the internet!" in caplog.text
