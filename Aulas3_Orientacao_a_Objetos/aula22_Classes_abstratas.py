from abc import ABC, abstractmethod, ABCMeta

# class Log(metaclass = ABCMeta):  #Mesma coisa


class Log(ABC):  
  @abstractmethod
  def _log(self, msg):
    ...
  
  def log_error(self, msg):
    self._log(f"Error: {msg}")

  def log_success(self, msg):
    self._log(f"Success: {msg}")


class LogPrintMixin(Log):
  def _log(self, msg):
    print(f"{msg} ({self.__class__.__name__})")



l = LogPrintMixin()

l.log_error("Teste")