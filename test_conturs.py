import chemistry

def test_get_count_contours():
    cnts = chemistry.get_cnts()
    assert 67 == chemistry.get_count_contours(cnts)
