from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class MediaFile:
    path: Path
    size_bytes: int
    modified_ts: float  # epoch seconds

    @property
    def ext(self) -> str:
        return self.path.suffix.lower()

