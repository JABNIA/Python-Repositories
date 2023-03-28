from emojize import emojize

def test_emojization():
    assert emojize(":1st_place_medal:") == "🥇"
    assert emojize(":money_bag:") == "💰"
    assert emojize(":grinning_cat:") == "😺"