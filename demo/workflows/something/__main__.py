from . import workflow
from demo.toil import toil_workflow

def main():
    with toil_workflow(jobStore="workflow_out", retryCount=1) as wf:
        wf.start(workflow({"shape": (100, 20, 30)}))

if __name__ == '__main__':
    main()
