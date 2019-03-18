#!/usr/bin/env python                                                                                                                                                               
def get2016files():
    #from  commit: ed54500
    idir     = 'root://cmseos.fnal.gov/eos/uscms/store/user/lpchbb/zprimebits-v12.04/cvernier'
    idirData = 'root://cmseos.fnal.gov/eos/uscms/store/user/lpchbb/zprimebits-v12.05/'
    idirSig  = 'root://cmseos.fnal.gov/eos/uscms/store/user/cmantill/sklimZqq2016/'

    tfiles = {
        'zqq50':[idirSig+'VectorDiJet1Jet_M50_1000pb_weighted.root'],
        'zqq75':[idirSig+'VectorDiJet1Jet_M75_1000pb_weighted.root'],
        'zqq100':[idirSig+'VectorDiJet1Jet_M100_1000pb_weighted.root'],
        'zqq125':[idirSig+'VectorDiJet1Jet_M125_1000pb_weighted.root'],
        'zqq150':[idirSig+'VectorDiJet1Jet_M150_1000pb_weighted.root'],
        'zqq200':[idirSig+'VectorDiJet1Jet_M200_1000pb_weighted.root'],
        'zqq250':[idirSig+'VectorDiJet1Jet_M250_1000pb_weighted.root'],
        'zqq300':[idirSig+'VectorDiJet1Jet_M300_1000pb_weighted.root'],
        'dy':[idir + '/DYJetsToQQ_HT180_13TeV_1000pb_weighted_v1204.root'],
        'dyll':[idir + '/DYJetsToLL_M_50_13TeV_ext_1000pb_weighted.root'],
        'stqq':[idir + '/ST_t_channel_antitop_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin_1000pb_weighted.root',
                idir + '/ST_t_channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV_powhegV2_madspin_1000pb_weighted.root',
                idir + '/ST_tW_antitop_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4_1000pb_weighted.root',
                idir + '/ST_tW_top_5f_inclusiveDecays_13TeV_powheg_pythia8_TuneCUETP8M2T4_1000pb_weighted.root'],
        'wqq':[idir + '/WJetsToQQ_HT180_13TeV_1000pb_weighted_v1204.root'],
        'wlnu':[idir + '/WJetsToLNu_HT_100To200_13TeV_1000pb_weighted.root',
                idir + '/WJetsToLNu_HT_200To400_13TeV_1000pb_weighted.root',
                idir + '/WJetsToLNu_HT_400To600_13TeV_1000pb_weighted.root',
                idir + '/WJetsToLNu_HT_600To800_13TeV_1000pb_weighted.root',
                idir + '/WJetsToLNu_HT_800To1200_13TeV_1000pb_weighted.root',
                idir + '/WJetsToLNu_HT_1200To2500_13TeV_1000pb_weighted.root'],
        'tqq':[idir + '/TT_powheg_1000pb_weighted_v1204.root'],  # Powheg is the new default
        'qcd':[idir + '/QCD_HT300to500_13TeV_all_1000pb_weighted.root',
               idir + '/QCD_HT500to700_13TeV_ext_1000pb_weighted.root',
               idir + '/QCD_HT700to1000_13TeV_ext_1000pb_weighted.root',
               idir + '/QCD_HT1000to1500_13TeV_all_1000pb_weighted.root',
               idir + '/QCD_HT1500to2000_13TeV_all_1000pb_weighted.root',
               idir + '/QCD_HT2000toInf_13TeV_1000pb_weighted.root'],
        'jethtb':[idirData+'JetHTRun2016B_03Feb2017_ver2_v2_v3.root',
                  idirData + 'JetHTRun2016B_03Feb2017_ver1_v1_v3.root'],
        'jethtc':[idirData + 'JetHTRun2016C_03Feb2017_v1_v3_0.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_1.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_2.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_3.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_4.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_5.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_6.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_7.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_8.root',
                  idirData + 'JetHTRun2016C_03Feb2017_v1_v3_9.root'],
        'jethtd':[idirData + 'JetHTRun2016D_03Feb2017_v1_v3_0.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_1.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_10.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_11.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_12.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_13.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_14.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_2.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_3.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_4.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_5.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_6.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_7.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_8.root',
                  idirData + 'JetHTRun2016D_03Feb2017_v1_v3_9.root'],
        'jethte':[idirData + 'JetHTRun2016E_03Feb2017_v1_v3_0.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_1.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_2.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_3.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_4.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_5.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_6.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_7.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_8.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_9.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_10.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_11.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_12.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_13.root',
                  idirData + 'JetHTRun2016E_03Feb2017_v1_v3_14.root'],
        'jethtf':[idirData + 'JetHTRun2016F_03Feb2017_v1_v3_0.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_1.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_2.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_3.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_4.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_5.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_6.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_7.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_8.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_9.root',
                  idirData + 'JetHTRun2016F_03Feb2017_v1_v3_10.root'],
        'jethtg':[idirData + 'JetHTRun2016G_03Feb2017_v1_v3_0.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_1.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_2.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_3.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_4.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_5.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_6.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_7.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_8.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_9.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_10.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_11.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_12.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_13.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_14.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_15.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_16.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_17.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_18.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_19.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_20.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_21.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_22.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_23.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_24.root',
                  idirData + 'JetHTRun2016G_03Feb2017_v1_v3_25.root'],
        'jethth':[idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_0.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_1.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_2.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_3.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_4.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_5.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_6.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_7.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_8.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_9.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_10.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_11.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_12.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_13.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_14.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_15.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_16.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_17.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_18.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_19.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_20.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_21.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_22.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_23.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_24.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver2_v1_v3_25.root',
                  idirData + 'JetHTRun2016H_03Feb2017_ver3_v1_v3.root'],

        'muon': [idir + '/SingleMuonRun2016B_03Feb2017_ver1_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016B_03Feb2017_ver2_v2_fixtrig.root',
                 idir + '/SingleMuonRun2016C_03Feb2017_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016D_03Feb2017_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016E_03Feb2017_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016F_03Feb2017_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016G_03Feb2017_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016H_03Feb2017_ver2_v1_fixtrig.root',
                 idir + '/SingleMuonRun2016H_03Feb2017_ver3_v1_fixtrig.root']
        }
    return tfiles

def get2017files():
    idir_1207skim = 'root://cmseos.fnal.gov//eos/uscms/store/group/lpcbacon/dazsle/zprimebits-v12.07/sklim/'
    idir_1501skim = 'root://cmseos.fnal.gov//eos/uscms/store/user/lpcbacon/dazsle/zprimebits-v15.01/skim/'

    tfiles = {'zqq50': {'VectorDiJet1Jet_madgraph_Mphi50Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi50Mchi3000_13TeV_*.root']},
              'zqq75': {'VectorDiJet1Jet_madgraph_Mphi75Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi75Mchi3000_13TeV_*.root']},
              'zqq100': {'VectorDiJet1Jet_madgraph_Mphi100Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi100Mchi3000_13TeV_*.root']}, #!!!
              'zqq115': {'VectorDiJet1Jet_madgraph_Mphi115Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi115Mchi3000_13TeV_*.root']},
              'zqq125': {'VectorDiJet1Jet_madgraph_Mphi125Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi125Mchi3000_13TeV_*.root']},
              'zqq150': {'VectorDiJet1Jet_madgraph_Mphi150Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi150Mchi3000_13TeV_*.root']},
              'zqq175': {'VectorDiJet1Jet_madgraph_Mphi175Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi175Mchi3000_13TeV_*.root']},
              'zqq200': {'VectorDiJet1Jet_madgraph_Mphi200Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi200Mchi3000_13TeV_*.root']},
              'zqq225': {'VectorDiJet1Jet_madgraph_Mphi225Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi225Mchi3000_13TeV_*.root']},
              'zqq250': {'VectorDiJet1Jet_madgraph_Mphi250Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi250Mchi3000_13TeV_*.root']},
              'zqq275': {'VectorDiJet1Jet_madgraph_Mphi275Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi275Mchi3000_13TeV_*.root']},
              'zqq300': {'VectorDiJet1Jet_madgraph_Mphi300Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi300Mchi3000_13TeV_*.root']},
              'zqq350': {'VectorDiJet1Jet_madgraph_Mphi350Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi350Mchi3000_13TeV_*.root']},
              'zqq400': {'VectorDiJet1Jet_madgraph_Mphi400Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi400Mchi3000_13TeV_*.root']},
              'zqq450': {'VectorDiJet1Jet_madgraph_Mphi450Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi450Mchi3000_13TeV_*.root']},
              'zqq500': {'VectorDiJet1Jet_madgraph_Mphi500Mchi3000_13TeV': [idir_1207skim+'VectorDiJet1Jet_madgraph_Mphi500Mchi3000_13TeV_*.root']},
              'vvqq':{'WW_TuneCP5_13TeV-pythia8':[idir_1501skim+'WW_TuneCP5_13TeV_pythia8_*.root'],
                      'WZ_TuneCP5_13TeV-pythia8':[idir_1501skim+'WZ_TuneCP5_13TeV_pythia8_*.root'],
                      'ZZ_TuneCP5_13TeV-pythia8':[idir_1501skim+'ZZ_TuneCP5_13TeV_pythia8_*.root']
                      },
              'zqq':{'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV': [idir_1501skim + '/ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV_*.root'],
                     'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV': [idir_1501skim + '/ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV_*.root'],
                     'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV':[idir_1501skim + '/ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV_*.root'],
                     },
              'zll':{'DYJetsToLL_M_50_HT_400to600_TuneCP5_13TeV'  :[idir_1501skim+'/DYJetsToLL_M_50_HT_400to600_TuneCP5_13TeV*.root'] , 
                     'DYJetsToLL_M_50_HT_600to800_TuneCP5_13TeV'  :[idir_1501skim+'/DYJetsToLL_M_50_HT_600to800_TuneCP5_13TeV*.root'] , 
                     'DYJetsToLL_M_50_HT_800to1200_TuneCP5_13TeV' :[idir_1501skim+'/DYJetsToLL_M_50_HT_800to1200_TuneCP5_13TeV*.root'],                                     
                     'DYJetsToLL_M_50_HT_1200to2500_TuneCP5_13TeV':[idir_1501skim+'/DYJetsToLL_M_50_HT_1200to2500_TuneCP5_13TeV*.root'], 
                     'DYJetsToLL_M_50_HT_2500toInf_TuneCP5_13TeV' :[idir_1501skim+'/DYJetsToLL_M_50_HT_2500toInf_TuneCP5_13TeV*.root' ] 
                     },
              'stqq':{'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8':[idir_1501skim+'ST_t_channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV_powhegV2_madspin_pythia8_*.root'],
                      'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8'    :[idir_1501skim+'ST_t_channel_top_4f_inclusiveDecays_TuneCP5_13TeV_powhegV2_madspin_pythia8_*.root'],
                      'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'                 :[idir_1501skim+'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV_powheg_pythia8_*.root'],
                      'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8'                     :[idir_1501skim+'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV_powheg_pythia8_*.root']
                      },
              'wqq':{'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV': [idir_1501skim + 'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV_*.root'],
                     'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV': [idir_1501skim + 'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV_*.root'],
                     'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV':[idir_1501skim + 'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV_*.root'],
                     },
              'wlnu':{"WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8"   :[ idir_1501skim+'WJetsToLNu_HT_200To400_*.root'],
                      "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8"   :[ idir_1501skim+'WJetsToLNu_HT_400To600_*.root'],
                      "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8"   :[ idir_1501skim+'WJetsToLNu_HT_600To800_*.root'],
                      "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8"  :[ idir_1501skim+'WJetsToLNu_HT_800To1200_*.root'],
                      "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8" :[ idir_1501skim+'WJetsToLNu_HT_1200To2500_*.root'],
                      "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8" :[ idir_1501skim+'WJetsToLNu_HT_2500ToInf*.root'],
                      },
              'tqq':{'TTToHadronic_TuneCP5_13TeV_powheg_pythia8'    :[idir_1501skim+'TTToHadronic_TuneCP5_13TeV_powheg_pythia8_*.root'],
                     'TTToSemiLeptonic_TuneCP5_13TeV_powheg_pythia8':[idir_1501skim+'TTToSemiLeptonic_TuneCP5_13TeV_powheg_pythia8_*.root'],
                     'TTTo2L2Nu_TuneCP5_13TeV_powheg_pythia8'       :[idir_1501skim+'TTTo2L2Nu_TuneCP5_13TeV_powheg_pythia8_*.root'       ],
                     },
              'qcd':{'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8'  :[idir_1501skim+'/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_*.root'  ],
                     'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8' :[idir_1501skim+'/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_*.root' ],
                     'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8':[idir_1501skim+'/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_*.root'],
                     'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8':[idir_1501skim+'/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_*.root'],
                             'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8' :[idir_1501skim+'/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_*.root' ]
                     },
              'jethtb':[idir_1501skim + 'JetHTRun2017B_17Nov2017_v1_*.root'],
              'jethtc':[idir_1501skim + 'JetHTRun2017C_17Nov2017_v1_*.root'],
              'jethtd':[idir_1501skim + 'JetHTRun2017D_17Nov2017_v1_*.root'],
              'jethte':[idir_1501skim + 'JetHTRun2017E_17Nov2017_v1_*.root'],
              'jethtf':[idir_1501skim + 'JetHTRun2017F_17Nov2017_v1_*.rootnodupl.root'],
              'muon': [idir_1501skim+'/SingleMuonRun2017B_17Nov2017_v1_*.root',
                       idir_1501skim+'/SingleMuonRun2017C_17Nov2017_v1_*.root',
                       idir_1501skim+'/SingleMuonRun2017D_17Nov2017_v1_*.root',
                       idir_1501skim+'/SingleMuonRun2017E_17Nov2017_v1_*.root',
                       idir_1501skim+'/SingleMuonRun2017F_17Nov2017_v1_*.root'
                       ]
              }
    return tfiles
