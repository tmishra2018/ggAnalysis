from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ""
config.General.workArea = ""
config.General.transferLogs = False

config.JobType.pluginName = "Analysis"
config.JobType.psetName = ""
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDBS        = 'global'
config.Data.publication     = False

config.Data.inputDataset = ""
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
#config.Data.unitsPerJob = 1
config.Data.totalUnits      = -1
config.Data.outLFNDirBase = ""
config.Site.storageSite = ""
config.Site.storageSite     = 'T2_IN_TIFR'
#config.Site.storageSite     = 'T2_CH_CERN'
