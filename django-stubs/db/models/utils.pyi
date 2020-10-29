from typing import Any, Generator, MutableMapping, Tuple, Type, Union

from django.db.models.base import Model

def make_model_tuple(model: Union[Type[Model], str]) -> Tuple[str, str]: ...
  
def resolve_callables(mapping: MutableMapping[str, Any]) -> Generator[Tuple[str, Any]]: ...
