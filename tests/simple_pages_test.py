"""This test the homepage"""



def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Website" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"My Understanding on Docker" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"My Understanding on GIT" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"My Understanding on Python/Flask" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"My Understanding on CI/CD" in response.data
def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"Object Oriented Programming Concepts" in response.data
def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data
def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"Principles of Object Oriented Programming concepts in calculator app" in response.data
def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID principles" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404