import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------- Given examples ----------
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_small_group():
    assert group_discount(2, False) == 0


# ---------- ticket_price: error paths ----------
def test_unknown_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


def test_invalid_show_time():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


# ---------- ticket_price: pricing lines ----------
def test_morning_show_discount():
    assert ticket_price("regular", 25, 10, False) == 100


def test_evening_show_surcharge():
    assert ticket_price("premium", 25, 20, False) == 280


def test_weekend_surcharge():
    assert ticket_price("regular", 25, 15, True) == 190


def test_infant_is_free():
    assert ticket_price("recliner", 2, 15, False) == 0


def test_child_half_price():
    assert ticket_price("regular", 10, 15, False) == 75


# ---------- group_discount ----------
def test_zero_tickets_raises():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_large_group():
    assert group_discount(12, False) == 15


def test_medium_group():
    assert group_discount(6, False) == 10


def test_student_group_bonus():
    assert group_discount(6, True) == 15


# ---------- snack_combo ----------
def test_small_combo():
    assert snack_combo("small", False) == 120


def test_medium_combo():
    assert snack_combo("medium", False) == 180


def test_large_combo():
    assert snack_combo("large", False) == 250


def test_combo_with_coupon():
    assert snack_combo("small", True) == 70
