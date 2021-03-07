from argparse import Namespace
from contextlib import contextmanager
import functools

from toil.common import Toil

from demo.toil_options import ToilOptions


@contextmanager
def toil_workflow(**toil_options):
    options = Namespace(**ToilOptions().load(toil_options))
    # TODO: restart? https://github.com/BD2KGenomics/toil-rnaseq/blob/master/src/toil_rnaseq/toil_rnaseq.py#L210-L214
    with Toil(options) as toil:
        yield toil


def validate_workflow_params(schema):
    def decorator(workflow):
        @functools.wraps(workflow)
        def wrapped_workflow(params):
            return workflow(schema.load(params))

        return wrapped_workflow

    return decorator
