from __future__ import absolute_import, division, print_function

from os.path import join
import mock
import pytest
from i19.command_line.screen import I19Screen


def test_i19screen_command_line_help_does_not_crash():
    I19Screen().run([])


def test_i19screen(regression_data, run_in_tmpdir):
    data_dir = regression_data("X4_wide").strpath
    I19Screen().run([data_dir])

    logfile = run_in_tmpdir.join("i19.screen.log").read()

    assert "i19.screen successfully completed" in logfile
    assert "photon incidence rate is outside the linear response region" in logfile


@pytest.mark.xfail(raises=ValueError, reason="LAPACK bug?")
def test_i19screen_single_frame(regression_data, run_in_tmpdir):
    # TODO Use a single frame with fewer than 80 reflections
    data_dir = regression_data("X4_wide").strpath
    image = join(data_dir, "X4_wide_M1S4_2_0001.cbf")

    I19Screen().run([image])

    logfile = run_in_tmpdir.join("i19.screen.log").read()

    assert "i19.screen successfully completed" in logfile
