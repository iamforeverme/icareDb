import unittest
from icareDatabase import *

class iCareDatabaseTestCase(unittest.TestCase):
	def setUp(self):
		self._db = iCareDb()

	def testDbexists(self):
		""" test if icare database exists"""
		returnVal = self._db.query("show tables;")
		assert(returnVal)

	def testAdd(self):
		self._db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001"})
		returnVal = self._db.queryId("cushion",{"cushion_mac":"TEST001"})
		self._db.rm("cushion",returnVal)
		returnValDel = self._db.queryId("cushion",{"cushion_mac":"TEST001"})
		assert( returnVal and (not returnValDel))

	# def testCushionOpt(self):
	# 	self._db.addCushion("r1v1","TEST001")
	# 	returnVal = self._db.query("SELECT type FROM cushion WHERE cushion_mac = 'TEST001';")
	# 	self._db.deleteCushion('TEST001')
	# 	returnValDel = self._db.query("SELECT type FROM cushion WHERE cushion_mac = 'TEST001';")
	# 	assert( ("r1v1" in returnVal[0]) and (not returnValDel))

	# def testRouterOpt(self):
	# 	self._db.addRouter("r1v1","TEST001")
	# 	returnVal = self._db.query("SELECT type FROM router WHERE routerco_mac = 'TEST001';")
	# 	self._db.deleteRouter('TEST001')
	# 	returnValDel = self._db.query("SELECT type FROM router WHERE routerco_mac = 'TEST001';")
	# 	assert( ("r1v1" in returnVal[0]) and (not returnValDel))

	# def testSignalTypeOpt(self):
	# 	self._db.addSignalType("TEST001")
	# 	returnVal = self._db.query("SELECT type FROM signal_type WHERE type = 'TEST001';")
	# 	self._db.deleteSignalType('TEST001')
	# 	returnValDel = self._db.query("SELECT type FROM signal_type WHERE type = 'TEST001';")
	# 	assert( ("TEST001" in returnVal[0]) and (not returnValDel))

	# def testWarningTypeOpt(self):
	# 	self._db.addWarningType("TEST001")
	# 	returnVal = self._db.query("SELECT type FROM warning_type WHERE type = 'TEST001';")
	# 	self._db.deleteWarningType('TEST001')
	# 	returnValDel = self._db.query("SELECT type FROM warning_type WHERE type = 'TEST001';")
	# 	assert( ("TEST001" in returnVal[0]) and (not returnValDel))

	# def testQuickSolutionOpt(self):
	# 	self._db.addQuickSolution("TEST001")
	# 	returnVal = self._db.query("SELECT solution FROM quick_solution WHERE solution = 'TEST001';")
	# 	self._db.deleteQuickSolution('TEST001')
	# 	returnValDel = self._db.query("SELECT solution FROM quick_solution WHERE solution = 'TEST001';")
	# 	assert( ("TEST001" in returnVal[0]) and (not returnValDel))

	# def testSettingOpt(self):
	# 	self._db.addSetting("TEST001","r1v1")
	# 	returnVal = self._db.query("SELECT attribute FROM setting WHERE attribute = 'TEST001';")
	# 	self._db.deleteSetting('TEST001')
	# 	returnValDel = self._db.query("SELECT attribute FROM setting WHERE attribute = 'TEST001';")
	# 	assert( ("TEST001" in returnVal[0]) and (not returnValDel))


	def testException(self):
		try:
			returnVal = self._db.addCushion("r1v1")
		except :
			pass
		else:
			fail("expected a ValueError")

if(__name__=="__main__"):
	unittest.main()
	# runner = unittest.TextTestRunner()
	# suite = unittest.TestSuite()
	# suite.addTest(iCareDatabaseTestCase("testDbexists"))
	# runner.run(suite)