import pytest
from ifdo._datetime import check_datatime_format


def test_check_datatime_default() -> None:
    valid_test_data = {
        "image-set-header": {
            "image-datetime": "2015-01-01 02:04:03.1000",
        }
    }

    check_datatime_format(valid_test_data)

    invalid_test_data = {
        "image-set-header": {
            "image-datetime": "2015-01-01 02:04:03",
        }
    }
    with pytest.raises(Exception):
        check_datatime_format(invalid_test_data)


def test_check_datetime_images() -> None:
    valid_test_data = {
        "image-set-header": {
            "image-datetime": "2015-01-01T20:21:32",
            "image-datetime-format": "%Y-%m-%dT%H:%M:%S",
        },
        "image-set-items": {"image": {"image-datetime": "2015-01-01T20:21:32"}},
    }
    check_datatime_format(valid_test_data)
    invalid_test_data = {
        "image-set-header": {
            "image-datetime": "2015-01-01T20:21:32",
            "image-datetime-format": "%Y-%m-%dT%H:%M:%S",
        },
        "image-set-items": {"image": {"image-datetime": "2015-01-01 20:21:32"}},
    }
    with pytest.raises(Exception):
        check_datatime_format(invalid_test_data)


def test_check_datetime_videos() -> None:
    valid_test_data = {
        "image-set-header": {},
        "image-set-items": {
            "image": [
                {
                    "image-datetime-format": "%Y-%m-%dT%H:%M:%S",
                    "image-datetime": "2015-01-01T20:21:32",
                },
                {"image-datetime": "2015-01-01T20:21:32"},
            ]
        },
    }
    check_datatime_format(valid_test_data)
    invalid_test_data = {
        "image-set-header": {},
        "image-set-items": {
            "image": [
                {
                    "image-datetime-format": "%Y-%m-%dT%H:%M:%S",
                    "image-datetime": "2015-01-01T20:21:32",
                },
                {"image-datetime": "2015-01-01 20:21:32"},
            ]
        },
    }

    with pytest.raises(Exception):
        check_datatime_format(invalid_test_data)
