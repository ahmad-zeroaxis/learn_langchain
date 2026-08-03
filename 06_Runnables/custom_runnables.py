from abc import ABC, abstractmethod
from dataclasses import dataclass
from pydantic import BaseModel


# every class that will inherit feom this Base class should overide the all abstract methods
class Runnable(ABC):

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def batch(self):
        pass

    @abstractmethod
    def stream(self):
        pass

    def optionla_functional(self):
        print("optional method in base that will inherided as it is, if not overide in child class")



@dataclass
class PromptTemplate(Runnable):
    template: str

    def invoke(self):
        print(self.template)
        return "invoke method of prompt template"

    def batch(self):
        return "batch method of prompt template"

    def stream(self):
        return "stream method of prompt template"




template = PromptTemplate("this is template")

print( template.invoke() )
print( template.batch() )
print( template.stream() )

template.optionla_functional()