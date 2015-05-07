import unittest
from icareDatabase import *

class iCareDatabaseTestCase(unittest.TestCase):
	def setUp(self):
		self._db = iCareDb()

	def testDbexists(self):
		""" test if icare database exists"""
		returnVal = self._db.query("show tables;")
		assert(returnVal)

	def testCushionOpt(self):
		self._db.addCushion("r1v1","TEST001")
		returnVal = self._db.query("SELECT type FROM cushion WHERE cushion_mac = 'TEST001';")
		self._db.deleteCushion('TEST001')
		returnValDel = self._db.query("SELECT type FROM cushion WHERE cushion_mac = 'TEST001';")
		assert( ("r1v1" in returnVal[0]) and (not returnValDel))

	def testRouterOpt(self):
		self._db.addRouter("r1v1","TEST001")
		returnVal = self._db.query("SELECT type FROM router WHERE routerco_mac = 'TEST001';")
		self._db.deleteRouter('TEST001')
		returnValDel = self._db.query("SELECT type FROM router WHERE routerco_mac = 'TEST001';")
		assert( ("r1v1" in returnVal[0]) and (not returnValDel))

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