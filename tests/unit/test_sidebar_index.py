from generate_sidebar_index import generate_sidebar_index

def test_sidebar_index_is_updated():
    with open('SIDEBAR-INDEX.json', 'r') as f:
        saved_sidebar_index = f.read()
    assert generate_sidebar_index() == saved_sidebar_index
