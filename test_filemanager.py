from filemanage import list_folders

def test_list_files():
    assert list_folders()==['.pytest_cache', '__pycache__', 'venv', '.git', '.idea']
