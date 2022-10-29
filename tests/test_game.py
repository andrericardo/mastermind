from core.constants import ColorPeg
from core.game import get_colors_pegs


class TestGame:
    def test_get_colors_pegs(self):
        expected = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        result = get_colors_pegs()
        assert result == expected
