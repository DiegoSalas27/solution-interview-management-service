from uuid import UUID
from dataclasses import dataclass

@dataclass
class SimulationConfiguration:
    """
    The configuration used for an interview simulation which contains primary and secondary LLMs to use
    and the expected latency at which the primary model should peform.
    """
    id: UUID
    primary_model: UUID
    secondary_model: UUID
    expected_max_latency: int # expected max latency in milliseconds
