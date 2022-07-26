import pygame

from client import config as c


class Rectangle(pygame.Rect):
    """A subclassed pygame.Rect with built-in display and highlight functionality.

    Attributes:
        window: The pygame window to draw on.
        color: The current color of the rectangle.
        default_color: The default color of the rectangle.

    """

    def __init__(
        self,
        window: pygame.Surface,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        color: tuple[int, int, int] = (0, 0, 0),
    ):
        """Initializes the rectangle.

        Args:
            window: The pygame window to draw on.
            x1: The x coordinate of the top left corner.
            y1: The y coordinate of the top left corner.
            x2: The x coordinate of the bottom right corner.
            y2: The y coordinate of the bottom right corner.
            color: The color of the rectangle.

        """
        super().__init__(x1, y1, x2 - x1, y2 - y1)
        self.window: pygame.Surface = window
        self.color: tuple[int, int, int] = color
        self.default_color: tuple[int, int, int] = color

    @staticmethod
    def from_rect(
        window: pygame.Surface,
        rect: pygame.Rect,
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> "Rectangle":
        """Creates a rectangle from a pygame.Rect.

        Args:
            window: The pygame window to draw on.
            rect: The pygame.Rect to create the rectangle from.
            color: The color of the rectangle.

        """
        return Rectangle(window, rect.x, rect.y, rect.x + rect.width, rect.y + rect.height, color)

    @staticmethod
    def draw_rect_alpha(
        surface: pygame.Surface,
        color: tuple[int, int, int] | tuple[int, int, int, int],
        rect: pygame.Rect | tuple[int, int, int, int],
    ):
        """Draws a rectangle with transparency on a surface.

        Args:
            surface: The surface to draw the rectangle on.
            color: The color of the rectangle, optionally including an alpha value.
            rect: The rectangle to draw.

        """
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def highlight(self, color: tuple[int, int, int] = (0, 0, 255)):
        """Highlights the rectangle by setting its color to a different color.

        Args:
            color: The color to set the rectangle to.

        """
        self.color = color

    def unhighlight(self):
        """Unhighlights the rectangle by setting its color to the default color."""
        self.color = self.default_color

    def move(self, direction: str, distance: int):
        """Moves the rectangle in a direction by a certain distance.

        Args:
            direction: The direction to move the rectangle in.
            distance: The distance to move the rectangle.

        """
        if direction == "up":
            self.y -= distance
        elif direction == "down":
            self.y += distance
        elif direction == "left":
            self.x -= distance
        elif direction == "right":
            self.x += distance

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.width > c.W:
            self.x = c.W - self.width
        if self.y + self.height > c.H:
            self.y = c.H - self.height

    def redraw(self):
        """Redraws the rectangle on the window."""
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
