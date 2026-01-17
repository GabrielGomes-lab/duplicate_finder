from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Fingerprint:
    algorithm: str   # e.g. "sha256", "phash"
    value: str       # hex or string representation
