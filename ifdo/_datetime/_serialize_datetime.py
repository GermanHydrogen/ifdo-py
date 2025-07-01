from typing import TYPE_CHECKING

from ifdo._datetime._format import DEFAULT_DATETIME_FORMAT

if TYPE_CHECKING:
    from ifdo import iFDO, ImageData


def add_datetime_format_info(ifdo: "iFDO") -> None:
    header_format = (
        ifdo.image_set_header.image_datetime_format or DEFAULT_DATETIME_FORMAT
    )

    setattr(ifdo.image_set_header, "_image_datetime_format", header_format)

    for image_item in ifdo.image_set_items.values():
        if isinstance(image_item, list):
            _serialize_video_datetimes(image_item, header_format)
        else:
            _serialize_image_datetimes(image_item, header_format)


def _serialize_video_datetimes(images: list["ImageData"], header_format: str) -> None:
    if len(images) == 0:
        return

    datetime_format = _serialize_image_datetimes(images[0], header_format)

    for image in images[1:]:
        _serialize_image_datetimes(image, datetime_format)


def _serialize_image_datetimes(image: "ImageData", header_format: str) -> str:
    datetime_format = image.image_datetime_format or header_format

    setattr(image, "_image_datetime_format", datetime_format)
    return datetime_format
