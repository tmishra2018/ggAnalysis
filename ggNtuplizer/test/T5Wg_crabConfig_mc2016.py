if __name__ == '__main__':

# Usage : python crabConfig.py (to create jobs)
#         ./multicrab -c status -d <work area> (to check job status)

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    from CRABClient.UserUtilities import config
    config = config()
    
    from multiprocessing import Process

    # Common configuration

    config.General.workArea     = 'T5Wg_mG-1500_mLSP-1_2016'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    config.JobType.psetName     = 'DYJetsToLL_run_mc2016_106X.py'
    config.JobType.sendExternalFolder = True
    config.Data.inputDBS        = 'global'    
    config.Data.splitting       = 'FileBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.totalUnits      = -1
    config.Data.publication     = False
    config.Site.storageSite     = 'T2_IN_TIFR'
    config.Data.allowNonValidInputDataset = True
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    # dataset dependent configuration
    config.JobType.allowUndistributedCMSSW = True
    config.General.requestName = ''
    config.Data.unitsPerJob    = 1
    config.Data.inputDataset   = '/SMS-T5Wg_mG-1500_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/user/trmishra/T5Wg_mG-1500_mLSP-1_2016/'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
