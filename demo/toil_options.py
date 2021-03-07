from marshmallow import Schema, fields


CLEAN_CHOICES = {'always', 'onError', 'never', 'onSuccess'}
PROVISIONER_CHOICES = {'aws', 'gce', None}
LOG_LEVELS = {'Critical', 'Error', 'Warning', 'Debug', 'Info'}


class ToilOptions(Schema):
    # Core options
    jobStore = fields.Str(required=True)
    workDir = fields.Str(missing=None)
    noStdOutErr = fields.Bool(missing=None)
    stats = fields.Bool(missing=None)
    clean = fields.Str(validate=lambda x: x in CLEAN_CHOICES, missing=None, required=False)
    cleanWorkDir = fields.Str(validate=lambda x: x in CLEAN_CHOICES, missing='always', required=False)
    # clusterStats = nargs='?', action='store', default=None, const=os.getcwd(),
    clusterStats = fields.Str(missing=None)

    # Logging options
    logLevel = fields.Str(validate=lambda x: x in LOG_LEVELS, missing='Info')
    logFile = fields.Str(missing=None)
    logRotating = fields.Bool(missing=False)

    # Restart options
    restart = fields.Bool(missing=None)

    # Batch system options (TODO)
    # add_all_batchsystem_options(batchsystem_options)

    # statePollingWait = default=1, type=int,
    statePollingWait = fields.Int(missing=1)

    # Autoscaling options
    provisioner = fields.Str(validate=lambda x: x in PROVISIONER_CHOICES, missing=None)
    nodeTypes = fields.Str(missing=None)
    minNodes = fields.Str(missing=None)
    maxNodes = fields.Str(missing=None)
    targetTime = fields.Str(missing=None)
    betaInertia = fields.Str(missing=None)
    scaleInterval = fields.Str(missing=None)
    preemptableCompensation = fields.Str(missing=None)
    nodeStorage = fields.Int(missing=50)
    nodeStorageOverrides = fields.Int(missing=None),
    metrics = fields.Bool(missing=False)

    # Service options
    maxServiceJobs = fields.Int(missing=None)
    maxPreemptableServiceJobs = fields.Int(missing=None)
    deadlockWait = fields.Int(missing=None)
    deadlockCheckInterval = fields.Int(missing=None)

    # Resource options
    defaultMemory = fields.Int(missing=None)
    defaultCores = fields.Float(missing=None)
    defaultDisk = fields.Int(missing=None)
    # defaultPreemptable = metavar='BOOL', type='bool', nargs='?', const=True, default=False,
    defaultPreemptable = fields.Bool(missing=False)
    maxCores = fields.Int(missing=None)
    maxMemory = fields.Int(missing=None)
    maxDisk = fields.Int(missing=None)

    # Job options
    retryCount = fields.Int(missing=None)
    enableUnlimitedPreemptableRetries = fields.Bool(missing=False)
    doubleMem = fields.Bool(missing=False)
    maxJobDuration = fields.Int(missing=None)
    rescueJobsFrequency = fields.Int(missing=None)

    # Debug options
    debugWorker = fields.Bool(missing=False)
    disableWorkerOutputCapture = fields.Bool(missing=False)
    badWorker = fields.Float(missing=None)
    badWorkerFailInterval = fields.Float(missing=None)

    # Misc options
    disableCaching = fields.Bool(missing=False)
    disableChaining = fields.Bool(missing=False)
    disableJobStoreChecksumVerification = fields.Bool(missing=False)
    maxLogFileSize = fields.Int(missing=None)
    writeLogs = fields.Str(missing=None)
    writeLogsGzip = fields.Str(missing=None)
    writeLogsFromAllJobs = fields.Bool(missing=False)
    realTimeLogging = fields.Bool(missing=False)
    sseKey = fields.Str(missing=None)
    environment = fields.List(fields.Str(), missing=[])
    servicePollingInterval = fields.Float(missing=None)
    forceDockerAppliance = fields.Bool(missing=False)
    disableProgress = fields.Bool(missing=False)
