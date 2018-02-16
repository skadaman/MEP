import glob


def MEP_ParseUpload(report,process):
    if report="PML":
        powerfiles=glob.iglob('/Users/W1/MEP/MEP/CENACEdata/PML*.xml')
    