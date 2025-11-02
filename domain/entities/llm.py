from dataclasses import dataclass

@dataclass(frozen=True)
class LLM:
    """
    Represents the master table for LLMS which specifies names and versions.
    """
    id: int
    name: str
    version: str
