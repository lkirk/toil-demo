# Demo repo for messing around with toil workflows

### Installation
* Build
```
./scripts/build-sandbox library://lkirk/default/toil-demo:latest toil-sandbox
```
* Install
```
./scripts/run-sandbox toil-sandbox pip install -e .
```
* Play
```
./scripts/run-sandbox toil-sandbox ipython
```
* Test
```
./scripts/run-sandbox toil-sandbox pytest demo
```

### Useful links
* [multiple jobs, child, follow on](https://toil.readthedocs.io/en/latest/developingWorkflows/developing.html#workflows-with-multiple-jobs)
