from abc import ABC, abstractmethod

class APIProvider(ABC):
    def __init__(self, model):
        self.model = model
        if (self.model is None):
            self.model = self.get_default_model()

    @abstractmethod
    def get_default_model(self):
        pass

    @abstractmethod
    def get_response(self, prompt):
        pass
