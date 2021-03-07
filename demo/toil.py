from argparse import Namespace
from contextlib import contextmanager

from toil.common import Toil

from demo.toil_options import ToilOptions


@contextmanager
def toil_workflow(**toil_options):
    options = Namespace(**ToilOptions().load(toil_options))
    with Toil(options) as toil:
        yield toil
