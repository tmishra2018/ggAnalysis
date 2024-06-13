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
### "pre-VFP" (aka "HIPM" or "APV"): eras B-F

#        "/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",

#        "/DoubleMuon/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
#         "/DoubleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",

#        "/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#	 "/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
#        "/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD",
        
#	"/DoubleEG/Run2016F-UL2016_MiniAODv2-v1/MINIAOD",
#	"/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD",
	"/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD",

#        "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#        "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#	 "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#        "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#	 "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2-v5/MINIAOD",
#        "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",

#        "/SingleElectron/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
	 "/SingleElectron/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
#        "/SingleElectron/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",


#         "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",

### "post-VFP" (aka "no-HIPM"): eras F(7 runs)-H 

#        "/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
#        "/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
#        "/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",

#         "/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/MuonEG/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/MuonEG/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/MuonEG/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
#         "/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",

#        "/MuonEG/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
#        "/MuonEG/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
#        "/MuonEG/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
    ],
    2017: [


#        "/DoubleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2017E-UL2017_MiniAODv2-v2/MINIAOD",
#        "/DoubleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",

         "/SingleElectron/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
         "/SingleElectron/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
         "/SingleElectron/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
         "/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
         "/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
#
#         "/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
#         "/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
#         "/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
#         "/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
#         "/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
#
#         "/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
#         "/DoubleEG/Run2017C-UL2017_MiniAODv2-v2/MINIAOD",
#         "/DoubleEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
#         "/DoubleEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
#         "/DoubleEG/Run2017F-UL2017_MiniAODv2-v2/MINIAOD",
#
#         "/MuonEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
    ],
    2018: [

#        "/DoubleMuon/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
#        "/DoubleMuon/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",

	 "/SingleMuon/Run2018A-UL2018_MiniAODv2-v3/MINIAOD",
#         "/SingleMuon/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
#         "/SingleMuon/Run2018C-UL2018_MiniAODv2-v2/MINIAOD",
#         "/SingleMuon/Run2018D-UL2018_MiniAODv2-v3/MINIAOD",

#         "/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
#         "/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
#         "/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
#         "/EGamma/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
# redoing 
#	  "/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD"

#         "/MuonEG/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
#         "/MuonEG/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
    ]
}

psetFiles = {
#    2016: "run_data2016preVFP_106X.py",
    2016: "run_data2016postVFP_106X.py",
    2017: "run_data2017_106X.py",
    2018: "run_data2018_106X.py"
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
        commandToSubmit += "-c data_crabConfig.py General.requestName=ntuplizer_10620_data_{did} General.workArea=crab_10620_data_{did} JobType.psetName={p} Data.inputDataset={d} Data.outLFNDirBase={lDB}".format(did=datasetIdentifier, d=dataset, p=psetFiles[year], lDB=lfnDirBase)
        print(commandToSubmit)
        execute_in_crab_env(commandToSubmit)
