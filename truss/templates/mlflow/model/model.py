from typing import Dict, List

import mlflow
import numpy as np


class Model:
    def __init__(self, **kwargs) -> None:
        self._data_dir = kwargs["data_dir"]
        config = kwargs["config"]
        model_metadata = config["model_metadata"]
        self._model_binary_dir = model_metadata["model_binary_dir"]
        self._model = None

    def load(self):
        model_binary_dir_path = self._data_dir / self._model_binary_dir
        self._model = mlflow.pyfunc.load_model(model_binary_dir_path / "model")

    def preprocess(self, request: Dict) -> Dict:
        """
        Incorporate pre-processing required by the model if desired here.

        These might be feature transformations that are tightly coupled to the model.
        """
        return request

    def postprocess(self, request: Dict) -> Dict:
        """
        Incorporate post-processing required by the model if desired here.
        """
        return request

    def predict(self, request: Dict) -> Dict[str, List]:
        response = {}
        inputs = request["inputs"]
        inputs = np.array(inputs)
        result = self._model.predict(inputs).tolist()
        response["predictions"] = result
        return response
