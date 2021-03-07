from marshmallow import Schema, fields

from toil.job import Job

from demo.toil import validate_workflow_params, toil_workflow
from .analysis import generate_matrix, mult_by_n


class SomethingParams(Schema):
    shape = fields.List(fields.Int(), validate=fields.Length(equal=3))


@validate_workflow_params(SomethingParams())
def workflow(params):
    outer = Job()
    matrix = outer.addChildFn(generate_matrix, params['shape'])
    final = matrix.addChildFn(mult_by_n, matrix.rv(0), 3)
    return outer


# with toil_workflow(jobStore='workflow_out', retryCount=1) as wf:
#     wf.start(workflow({'shape': (100, 20, 30)}))
