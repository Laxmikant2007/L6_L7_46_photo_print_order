import pytest
from photo_print_order import extra_print_charge, order_valid, dispatch_status


def test_unknown_size():
    with pytest.raises(ValueError, match="unknown print size"):
        extra_print_charge("invalid", 10, "matte", False)


def test_negative_copies():
    with pytest.raises(ValueError, match="invalid copies"):
        extra_print_charge("4x6", -1, "matte", False)


def test_member_bonus_and_matte():
    assert extra_print_charge("4x6", 30, "matte", True) == 5 * 4


def test_extra_zero():
    assert extra_print_charge("4x6", 20, "matte", False) == 0


def test_non_matte():
    assert extra_print_charge("4x6", 30, "glossy", False) == 10 * 7


def test_extra_over_50_canvas():
    assert extra_print_charge("8x10", 100, "canvas", False) == 90 * 14


def test_rush():
    assert order_valid(10, 30, True) is True


def test_file_too_large():
    assert order_valid(30, 100, False) is False


def test_normal():
    assert order_valid(10, 100, False) is True


def test_framed_international_on_time():
    assert dispatch_status(48, True, True) == "on_time"


def test_unframed_domestic_tight():
    assert dispatch_status(8, False, False) == "tight"


def test_unframed_domestic_missed():
    assert dispatch_status(4, False, False) == "missed"

def test_extra_over_50_non_canvas():
    # extra = 100 - 20 = 80 > 50, finish "glossy" -> rate = 7+2 = 9 (no +5)
    assert extra_print_charge("4x6", 100, "glossy", False) == 80 * 9