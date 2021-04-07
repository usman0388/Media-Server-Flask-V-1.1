class CSVData():
    Meta_CSV = []
    def GetMetaCSV(self):
        return CSVData.Meta_CSV
    def SetMetaCSV(self,structure):
        CSVData.Meta_CSV = structure
    def addRow(self,row):
        CSVData.Meta_CSV.append(row)
    def insetInto(self,itr,syp):
        CSVData.Meta_CSV[itr][1] = syp
        