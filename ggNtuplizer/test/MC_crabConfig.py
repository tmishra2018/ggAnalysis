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
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits      = -1

config.section_("Site")
#config.Site.storageSite = "T2_CH_CERN"
#config.Data.outLFNDirBase = '/store/group/phys_susy/Tribeni'

config.Site.storageSite = "T3_US_FNALLPC"
config.Data.outLFNDirBase = '/eos/uscms/store/user/lpcsusyphotons/Tribeni'
#config.Site.storageSite     = 'T2_IN_TIFR'



#config.Site.storageSite     = 'T2_CH_CERN'
#config.Site.blacklist          = ['T1_US_FNAL','T2_US_UCSD','T2_US_Purdue','T2_US_Caltech','T2_US_Vanderbilt']
