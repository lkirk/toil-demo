from toil.job import Job



def test_toil_options_compat():
    options = Job.Runner.getDefaultOptions('testjobstore')
    vars(options)
