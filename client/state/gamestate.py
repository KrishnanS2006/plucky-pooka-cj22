from abc import ABCMeta, abstractmethod

import pygame


class GameState:
    """Superclass for all game states.

    Attributes:
        window: The window to draw on.
        name: The name of the game state.

    """

    __metaclass__ = ABCMeta

    def __init__(self, window: pygame.Surface):
        """Initializes the game state.

        Args:
            window: The window to draw on.

        """
        self.window: pygame.Surface = window
        self.name: str = ""

    @abstractmethod
    def update(self, events: list[pygame.event.Event]) -> str | None:
        """Updates the game state

        Args:
            events: A list of events from `pygame.event.get()`, used to handle input.

        Returns:
            str if the game state should be changed, None otherwise.

        """
        pass

    @abstractmethod
    def redraw(self):
        """Redraws the elements of the current game state."""
        pass
