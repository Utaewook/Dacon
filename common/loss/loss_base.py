from typing import Any
from abc import ABC, abstractmethod

class LossBase(ABC):
    def __init__(self) -> None:
        self._name: str = ''

    @abstractmethod
    def compute_loss(self, pred, target) -> Any:
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        pass