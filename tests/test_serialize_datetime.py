from datetime import datetime
from ifdo._datetime import add_datetime_format_info
from ifdo.models.ifdo import ImageSetHeader, iFDO


def test_serialize_datetimes() -> None:
    header = ImageSetHeader(
        image_set_name="",
        image_set_uuid="",
        image_set_handle="",
        image_latitude=0,
        image_longitude=0,
    )
    header.image_datetime = datetime(2025, 1, 1, 1, 1, 1, int(2 * 1e5))

    ifdo = iFDO(image_set_header=header, image_set_items={})

    add_datetime_format_info(ifdo)

    result = ifdo.model_dump(mode="json", by_alias=True, exclude_none=True)
    print(ifdo.image_set_header.__annotations__)
    assert result["image-set-header"]["image-datetime"] == "2025-01-01 01:01:01.200000"
