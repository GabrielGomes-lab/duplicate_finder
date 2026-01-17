from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .fingerprint import Fingerprint
from .media_file import MediaFile


@dataclass(frozen=True, slots=True)
class DuplicateGroup:
    fingerprint: Fingerprint
    files: Sequence[MediaFile]
