from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from stringcase import spinalcase


class KebabCaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=spinalcase, populate_by_name=True)
