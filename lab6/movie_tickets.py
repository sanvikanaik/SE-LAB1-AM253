SEAT_PRICE = {"regular": 150, "premium": 250, "recliner": 400}


def ticket_price(seat, age, show_hour, is_weekend):
    if seat not in SEAT_PRICE:
        raise ValueError("unknown seat")
    if show_hour < 0 or show_hour > 23:
        raise ValueError("invalid show time")
    price = SEAT_PRICE[seat]
    if show_hour < 12:
        price -= 50
    elif show_hour >= 18:
        price += 30
    if is_weekend:
        price += 40
    if age < 3:
        return 0
    if age <= 12 or age >= 60:
        price = price // 2
    return price


def group_discount(tickets, is_student_group):
    if tickets < 1:
        raise ValueError("no tickets")
    if tickets >= 10:
        discount = 15
    elif tickets >= 5:
        discount = 10
    else:
        discount = 0
    if is_student_group and discount > 0:
        discount += 5
    return discount


def snack_combo(size, has_coupon):
    if size == "small":
        cost = 120
    elif size == "medium":
        cost = 180
    else:
        cost = 250
    if has_coupon:
        cost -= 50
    return cost
