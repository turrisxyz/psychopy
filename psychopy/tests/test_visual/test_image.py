from pathlib import Path

from psychopy import visual
from .test_basevisual import _TestUnitsMixin
from psychopy.tests.test_experiment.test_component_compile_python import _TestBoilerplateMixin

from ..utils import TESTS_DATA_PATH


class TestImage(_TestUnitsMixin, _TestBoilerplateMixin):
    """
    Test that images render as expected. Note: In BaseVisual tests, image colors will look different than
    seems intuitive as foreColor will be set to `"blue"`.
    """
    def setup(self):
        self.win = visual.Window()
        self.obj = visual.ImageStim(
            self.win,
            str(Path(TESTS_DATA_PATH) / 'testimage.jpg'),
            colorSpace='rgb1',
        )
