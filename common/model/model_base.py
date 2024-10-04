import numpy as np

from abc import ABC, abstractmethod
from typing import Tuple, List, Any, Union

from common.loss.loss_base import LossBase

class ModelBase(ABC):
    def __init__(self) -> None:
        self._alg_name: str = ''
        
        self._loss: LossBase = None
        self._model = None

    def setparam(self, params: dict) -> None:
        if isinstance(params, dict):
            self._alg_name = params.get('alg_name')
            
    def loadmodel(self, path: str) -> None:
        self._loadmodel(path)

    def loadloss(self, path: str) -> None:
        self._loadloss(path)

    def savemodel(self, path: str) -> None:
        self._savemodel(path)

    def saveloss(self, path: str) -> None:
        self._saveloss(path)

    @abstractmethod
    def _savemodel(self, path: str) -> None:
        pass

    @abstractmethod
    def _loadmodel(self, path: str) -> None:
        pass

    @abstractmethod
    def _buildmodel(self) -> None:
        pass

    def _saveloss(self, path: str) -> None:
        self._loss.save(path)

    def _loadloss(self, path: str) -> None:
        self._loss.load(path)
    

class TrainModel(ModelBase):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def fit(self, input_data:np.ndarray) -> Tuple[float, np.ndarray]:
        pass


class InferenceModel(ModelBase):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def predict(self, input_data: np.ndarray) -> Any:
        pass

