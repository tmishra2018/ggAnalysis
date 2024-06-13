#!/usr/bin/env python

from __future__ import print_function, division

import subprocess, argparse, os, re, sys

x509Proxy = os.getenv("X509_USER_PROXY")

inputArgumentsParser = argparse.ArgumentParser(description='Submit crab jobs.')
inputArgumentsParser.add_argument('--year', default="all", help="Year of data-taking.", type=str)
inputArgumentsParser.add_argument('--isProductionRun', action='store_true', help="By default, this script submits dry runs. Passing this switch will submit full production jobs.")
inputArguments = inputArgumentsParser.parse_args()

def execute_in_crab_env(commandToRun, printDebug=False):
    current_working_directory = os.getcwd()
    env_setup_command = "cd {cwd} && source /cvmfs/cms.cern.ch/crab3/crab.sh".format(cwd=current_working_directory)
    runInEnv = "{e_s_c} && set -x && {c} && set +x".format(e_s_c=env_setup_command, c=commandToRun)
    if (printDebug):
        print("About to execute command:")
        print("{c}".format(c=runInEnv))
    os.system(runInEnv)

datasets = {
    2016: [
      "/SMS-T5Wg_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-FSUL16_106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
      "/SMS-TChiWG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-FSUL16_106X_mcRun2_asymptotic_v17-v2/MINIAODSIM"
    ],
    2017: [
     "/SMS-T5Wg_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-FSUL17_106X_mc2017_realistic_v9-v2/MINIAODSIM",
     "/SMS-TChiWG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-FSUL17_106X_mc2017_realistic_v9-v2/MINIAODSIM"
    ],
    2018: [
     "/SMS-T5Wg_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
     "/SMS-TChiWG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM"
    ]
}

psetFiles = {
    #2016: "T5Wg_run_mc2016_preVFP_106X.py",
    2016: "T5Wg_run_mc2016_postVFP_106X.py",
    2017: "T5Wg_run_mc2017_106X.py",
    2018: "T5Wg_run_mc2018_106X.py"
}

yearsToRun = []
if (inputArguments.year == "2016"):
    yearsToRun.append(2016)
elif (inputArguments.year == "2017"):
    yearsToRun.append(2017)
elif (inputArguments.year == "2018"):
    yearsToRun.append(2018)
elif (inputArguments.year == "all"):
    yearsToRun.append(2016)
    yearsToRun.append(2017)
    yearsToRun.append(2018)
else:
    sys.exit("ERROR: invalid value for argument \"year\": {v}".format(v=inputArguments.year))

def extract_dataset_identifier(dataset):
    splitDataset = dataset.split("/")
    if not(len(splitDataset) == 4):
        sys.exit("dataset: {d} in unexpected format; splitDataset = {s}".format(d=dataset, s=splitDataset))
    #return (splitDataset[1] + "_" + splitDataset[2] + "preVFP")
    return (splitDataset[1] + "_" + splitDataset[2])

# execute_in_crab_env("which crab && type crab")
for year in yearsToRun:
    for dataset in datasets[year]:
        print("Running submission for dataset: {d}".format(d=dataset))
        datasetIdentifier = extract_dataset_identifier(dataset)
        commandToSubmit = ""
        commandToSubmit += "crab submit "
        if (inputArguments.isProductionRun): commandToSubmit += "--wait "
        else: commandToSubmit += "--dryrun "
        #lfnDirBase = "/store/group/phys_susy/Tribeni/{did}".format(did=datasetIdentifier)     
        lfnDirBase = "/store/user/trmishra/{did}".format(did=datasetIdentifier)     
	crabReqName = "ntuplizer_10620_mc_{did}".format(did=datasetIdentifier)
        commandToSubmit += "-c MC_crabConfig.py General.requestName=crabReqName General.workArea=CRAB_mc/{did} JobType.psetName={p} Data.inputDataset={d} Data.outLFNDirBase={lDB}".format(did=datasetIdentifier, d=dataset, p=psetFiles[year], lDB=lfnDirBase)
        print(commandToSubmit)
        execute_in_crab_env(commandToSubmit)
