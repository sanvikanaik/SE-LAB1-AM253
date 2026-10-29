import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ================= ticket_price =================
# --- validation branches (True and False side of each condition) ---
def test_unknown_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


def test_negative_show_hour():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_show_hour_above_23():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_boundary_hours_are_valid():
    assert ticket_price("regular", 25, 0, False) == 100    # earliest valid
    assert ticket_price("regular", 25, 23, False) == 180   # latest valid


# --- show time branches: morning / afternoon / evening ---
def test_morning_show():
    assert ticket_price("regular", 25, 11, False) == 100


def test_noon_is_afternoon():            # 12 is NOT < 12
    assert ticket_price("regular", 25, 12, False) == 150


def test_afternoon_show():
    assert ticket_price("regular", 25, 17, False) == 150


def test_six_pm_is_evening():            # 18 is >= 18
    assert ticket_price("regular", 25, 18, False) == 180


# --- weekend branch ---
def test_weekend_true():
    assert ticket_price("premium", 25, 15, True) == 290


def test_weekend_false():
    assert ticket_price("premium", 25, 15, False) == 250


# --- age branches ---
def test_age_below_3_free():
    assert ticket_price("recliner", 2, 15, False) == 0


def test_age_exactly_3_child_price():
    assert ticket_price("regular", 3, 15, False) == 75


def test_age_exactly_12_child_price():
    assert ticket_price("regular", 12, 15, False) == 75


def test_age_13_full_price():
    assert ticket_price("regular", 13, 15, False) == 150


def test_age_59_full_price():
    assert ticket_price("regular", 59, 15, False) == 150


def test_age_exactly_60_senior_price():
    assert ticket_price("regular", 60, 15, False) == 75


def test_all_seat_types():
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 25, 15, False) == 400


def test_combined_modifiers_child_evening_weekend():
    # recliner 400 + 30 (evening) + 40 (weekend) = 470 -> half = 235
    assert ticket_price("recliner", 8, 19, True) == 235


# ================= group_discount =================
def test_zero_tickets_raises():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_negative_tickets_raises():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(-3, True)


def test_one_ticket_no_discount():
    assert group_discount(1, False) == 0


def test_four_tickets_no_discount():
    assert group_discount(4, False) == 0


def test_five_tickets_medium_discount():
    assert group_discount(5, False) == 10


def test_nine_tickets_medium_discount():
    assert group_discount(9, False) == 10


def test_ten_tickets_large_discount():
    assert group_discount(10, False) == 15


def test_student_group_with_discount():
    assert group_discount(5, True) == 15
    assert group_discount(10, True) == 20


def test_student_group_without_discount():
    # is_student_group True but discount == 0 -> no bonus
    assert group_discount(3, True) == 0


# ================= snack_combo =================
def test_small_combo():
    assert snack_combo("small", False) == 120


def test_medium_combo():
    assert snack_combo("medium", False) == 180


def test_large_combo():
    assert snack_combo("large", False) == 250


def test_unknown_size_falls_to_large_price():
    assert snack_combo("jumbo", False) == 250


def test_coupon_applied():
    assert snack_combo("medium", True) == 130


def test_coupon_not_applied():
    assert snack_combo("medium", False) == 180
