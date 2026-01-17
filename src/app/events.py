from collections.abc import Callable


_handlers: dict[str, list[Callable[[dict], None]]] = {}


def register(event_name: str, handler: Callable[[dict], None]) -> None:
    _handlers.setdefault(event_name, []).append(handler)


def emit(event_name: str, payload: dict) -> None:
    for handler in _handlers.get(event_name, []):
        handler(payload)
