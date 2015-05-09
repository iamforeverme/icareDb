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




	def addCushion(self,type,mac):
		self._addContent('cushion',('type','cushion_mac'),(type,mac))

	def deleteCushion(self,mac):
		idList = self._getId('cushion',('cushion_mac',),(mac,))
		for id in idList:
			self._rmContent('cushion',id)
	def addRouter(self,type,mac):
		self._addContent('router',('type','routerco_mac'),(type,mac))

	def deleteRouter(self,mac):
		idList = self._getId('router',('routerco_mac',),(mac,))
		for id in idList:
			self._rmContent('router',id)

	def addSignalType(self,type):
		self._addContent('signal_type',('type',),(type,))

	def deleteSignalType(self,type):
		idList = self._getId('signal_type',('type',),(type,))
		for id in idList:
			self._rmContent('signal_type',id)

	def addWarningType(self,type):
		self._addContent('warning_type',('type',),(type,))

	def deleteWarningType(self,type):
		idList = self._getId('warning_type',('type',),(type,))
		for id in idList:
			self._rmContent('warning_type',id)

	def addQuickSolution(self,solution):
		self._addContent('quick_solution',('solution',),(solution,))

	def deleteQuickSolution(self,solution):
		idList = self._getId('quick_solution',('solution',),(solution,))
		for id in idList:
			self._rmContent('quick_solution',id)

	def addSetting(self,att,value):
		self._addContent('setting',('attribute','value'),(att,value))

	def deleteSetting(self,att):
		idList = self._getId('setting',('attribute',),(att,))
		for id in idList:
			self._rmContent('setting',id)


        

if __name__ == "__main__":
	db = iCareDb();
	print(db.query("show tables;"))