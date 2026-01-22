from abc import ABC, abstractmethod
from pathlib import Path

class BaseTask(ABC):

    BASE_DIR = Path(__file__).resolve().parent.parent
    file_data = BASE_DIR / "data.json"

    @abstractmethod
    def run(self) -> None:
        pass
