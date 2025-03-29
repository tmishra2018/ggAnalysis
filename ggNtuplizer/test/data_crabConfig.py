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
config.Data.totalUnits      = -1
config.Data.outLFNDirBase = ""
config.Site.storageSite = ""
config.Site.storageSite     = 'T3_US_FNALLPC'
config.Data.outLFNDirBase = '/eos/uscms/store/user/lpcsusyphotons/SoftPhoton/Tribeni'
#config.Site.storageSite = "T2_CH_CERN"
#config.Data.outLFNDirBase = '/store/group/phys_susy/Tribeni'

