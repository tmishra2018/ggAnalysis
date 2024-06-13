name = 'ULsampleMC'

dataset = {
   'DYToLL_M50_Run3': '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Run3Winter21DRMiniAOD-FlatPU30to80FEVT_112X_mcRun3_2021_realistic_v16-v2/MINIAODSIM',
   }

listOfSamples = [
    # 'DYJetsToLL_2018'
   ]




if __name__ == '__main__':
   
   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)
   
   config.General.workArea = 'crab_'+name
   config.General.transferLogs = False
   config.General.transferOutputs = True
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.outLFNDirBase = '/store/group/phys_egamma/Run3TriggerStudies/rasharma/Ntuples/' + name
   config.Data.allowNonValidInputDataset = True

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = 1
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()

    # Common configuration

    config.General.workArea     = 'ntuples_DYJetsToLL_2016preVFP'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    config.JobType.psetName     = 'DYJetsToLL_run_mc2016_preVFP_106X.py'
    config.JobType.sendExternalFolder = True
    config.Data.inputDBS        = 'global'    
    config.Data.splitting       = 'FileBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.totalUnits      = -1
    config.Data.publication     = False

    # dataset dependent configuration
    config.JobType.allowUndistributedCMSSW = True
    config.General.requestName = ''
    config.Data.unitsPerJob    = 1
    config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v1/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/group/phys_susy/Tribeni/DYJetsToLL_2016preVFP/'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
