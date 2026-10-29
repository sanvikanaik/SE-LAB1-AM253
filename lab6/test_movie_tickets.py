import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

#Example test cases:
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150

def test_small_group():
    assert group_discount(2, False) == 0

#Write the rest of the test cases so that the code is 90- 100% covered.
