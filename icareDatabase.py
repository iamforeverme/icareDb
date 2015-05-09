from MySqlDb import MySqlDb
from icareLogger import getLogger
logger = getLogger("iCareDb")


class iCareDb (MySqlDb):
	def __init__(self):
		super(iCareDb, self).__init__(host='127.0.0.1', port=3306, user='root', passwd="#bigguy", db='icare')


	def add(self,table,para):
		self._addContent(table,para.keys(),para.values())

	def rm(self,table,idList):
		for id in idList:
			self._rmContent(table,id)

	def queryId(self,table,para):
		return self._getId(table,para.keys(),para.values())

	def queryValue(self,table,id,colName):
		return self._getVal(table,id,colName)

	def update(self,table,id,para):
		self._updateContent(table,id,para.keys(),para.values())


        

if __name__ == "__main__":
	db = iCareDb();
	print(db.query("show tables;"))