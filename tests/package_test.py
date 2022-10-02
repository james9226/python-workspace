from python_workspace import demo

def test_answer():
    assert True == 1

def test_data_loads():
    assert len(demo.load_data(5)) == 5