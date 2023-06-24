from dataclasses import dataclass
from typing import List

@dataclass
class Atom:
    symbol: str
    position: List[float]

@dataclass
class Bond:
    atom1_position: List[float]
    atom2_position: List[float]

@dataclass
class Atoms:
    atoms: List[Atom]