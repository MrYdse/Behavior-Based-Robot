from abc import ABC, abstractmethod


class Sensob(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def interpret(self):
        pass