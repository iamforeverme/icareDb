import unittest
from icareDatabase import *

class iCareDatabaseTestCase(unittest.TestCase):
	def setUp(self):
		self._db = iCareDb()

	def testDbexists(self):
		""" test if icare database exists"""
		returnVal = self._db.query("show tables;")
		assert(returnVal)

	def testCushion(self):
		self._db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001"})
		returnVal = self._db.queryId("cushion",{"cushion_mac":"TEST001"})
		assert( returnVal )
		self._db.update("cushion",returnVal[0],{'type':"r1v2"})

		type = self._db.queryValue("cushion",returnVal[0],("type",))
		assert( type[0] ==  "r1v2")

		self._db.rm("cushion",returnVal)
		returnValDel = self._db.queryId("cushion",{"cushion_mac":"TEST001"})
		assert( not returnValDel)

	def testRouter(self):
		self._db.add("router",{'type':"r1v1",'routerco_mac':"TEST001"})
		returnVal = self._db.queryId("router",{"routerco_mac":"TEST001"})
		assert( returnVal )
		self._db.update("router",returnVal[0],{'type':"r1v2"})

		type = self._db.queryValue("router",returnVal[0],("type",))
		assert( type[0] ==  "r1v2")

		self._db.rm("router",returnVal)
		returnValDel = self._db.queryId("router",{"routerco_mac":"TEST001"})
		assert( not returnValDel)


	def testSignalType(self):
		self._db.add("signal_type",{'type':"r1v1"})
		returnVal = self._db.queryId("signal_type",{"type":"r1v1"})
		assert( returnVal )
		self._db.update("signal_type",returnVal[0],{'type':"r1v2"})

		type = self._db.queryValue("signal_type",returnVal[0],("type",))
		assert( type[0] ==  "r1v2")

		self._db.rm("signal_type",returnVal)
		returnValDel = self._db.queryId("signal_type",{"type":"r1v2"})
		assert( not returnValDel)

	def testWarningType(self):
		self._db.add("warning_type",{'type':"r1v1"})
		returnVal = self._db.queryId("warning_type",{"type":"r1v1"})
		assert( returnVal )
		self._db.update("warning_type",returnVal[0],{'type':"r1v2"})

		type = self._db.queryValue("warning_type",returnVal[0],("type",))
		assert( type[0] ==  "r1v2")

		self._db.rm("warning_type",returnVal)
		returnValDel = self._db.queryId("warning_type",{"type":"r1v2"})
		assert( not returnValDel)

	def testWarningType(self):
		self._db.add("quick_solution",{'solution':"r1v1"})
		returnVal = self._db.queryId("quick_solution",{"solution":"r1v1"})
		assert( returnVal )
		self._db.update("quick_solution",returnVal[0],{'solution':"r1v2"})

		solution = self._db.queryValue("quick_solution",returnVal[0],("solution",))
		assert( solution[0] ==  "r1v2")

		self._db.rm("quick_solution",returnVal)
		returnValDel = self._db.queryId("quick_solution",{"solution":"r1v2"})
		assert( not returnValDel)

	def testSetting(self):
		self._db.add("setting",{'attribute':"r1v1",'value':"TEST001"})
		returnVal = self._db.queryId("setting",{"attribute":"r1v1"})
		assert( returnVal )
		self._db.update("setting",returnVal[0],{'attribute':"r1v2"})

		attribute = self._db.queryValue("setting",returnVal[0],("attribute",))
		assert( attribute[0] ==  "r1v2")

		self._db.rm("setting",returnVal)
		returnValDel = self._db.queryId("setting",{"attribute":"TEST001"})
		assert( not returnValDel)

	def testStaff(self):
		self._db.add("staff",{'staff_id':"212328000",'name':"Xiaoming","id_card_num":"150204xxxxxxx","password":"helloWorld"})
		returnVal = self._db.queryId("staff",{"staff_id":"212328000"})
		assert( returnVal )
		self._db.update("staff",returnVal[0],{'name':"Xiaoming2"})

		attribute = self._db.queryValue("staff",returnVal[0],("name",))
		assert( attribute[0] ==  "Xiaoming2")

		self._db.rm("staff",returnVal)
		returnValDel = self._db.queryId("staff",{"name":"Xiaoming2"})
		assert( not returnValDel)


	def testProtege(self):
		self._db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})
		returnVal = self._db.queryId("protege",{'name':"XiaoHe"})
		assert( returnVal )
		self._db.update("protege",returnVal[0],{'name':"XiaoRan"})

		attribute = self._db.queryValue("protege",returnVal[0],("name",))
		assert( attribute[0] ==  "XiaoRan")

		self._db.rm("protege",returnVal)
		returnValDel = self._db.queryId("protege",{"name":"XiaoRan"})
		assert( not returnValDel)

	def testComment(self):
		self._db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})
		self._db.add("staff",{'staff_id':"212328000",'name':"Xiaoming","id_card_num":"150204xxxxxxx","password":"helloWorld"})

		protegeId = self._db.queryId("protege",{"id_card_num":"150214xxxxxxx"})[0]
		staffId = self._db.queryId("staff",{"id_card_num":"150204xxxxxxx"})[0]

		self._db.add("comment",{'staff_id':staffId,'protege_id':protegeId,'rate':3})

		commentId = self._db.queryId("comment",{'staff_id':staffId,'protege_id':protegeId})[0]
		assert( commentId )
		
		self._db.rm("comment",(commentId,))
		self._db.rm("protege",(protegeId,))
		self._db.rm("staff",(staffId,))

	def testStaffOnline(self):
		self._db.add("staff",{'staff_id':"212328000",'name':"Xiaoming","id_card_num":"150204xxxxxxx","password":"helloWorld"})
		staffId = self._db.queryId("staff",{"id_card_num":"150204xxxxxxx"})[0]
		self._db.add("staff_online",{'staff_id':staffId})
		onlineId = self._db.queryId("staff_online",{'staff_id':staffId})[0]
		assert( onlineId )
		self._db.rm("staff",(staffId,))
		
	def testLocation(self):
		self._db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001C"})
		self._db.add("router",{'type':"r1v1",'routerco_mac':"TEST001R"})
		self._db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})

		cushionId = self._db.queryId("cushion",{"cushion_mac":"TEST001C"})[0]
		routerId = self._db.queryId("router",{"routerco_mac":"TEST001R"})[0]
		protegeId = self._db.queryId("protege",{"id_card_num":"150214xxxxxxx"})[0]
		self._db.add("location",{'cushion_id':cushionId,'router_id':routerId,"protege_id":protegeId})

		locationId = self._db.queryId("location",{'router_id':routerId,'protege_id':protegeId,'cushion_id':cushionId})[0]
		assert( locationId )

		self._db.rm("router",(routerId,))
		self._db.rm("cushion",(cushionId,))
		self._db.rm("protege",(protegeId,))

	def testMonitorData(self):
		self._db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001C"})
		self._db.add("router",{'type':"r1v1",'routerco_mac':"TEST001R"})
		self._db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})

		cushionId = self._db.queryId("cushion",{"cushion_mac":"TEST001C"})[0]
		routerId = self._db.queryId("router",{"routerco_mac":"TEST001R"})[0]
		protegeId = self._db.queryId("protege",{"id_card_num":"150214xxxxxxx"})[0]
		self._db.add("location",{'cushion_id':cushionId,'router_id':routerId,"protege_id":protegeId})
		locationId = self._db.queryId("location",{'router_id':routerId,'protege_id':protegeId,'cushion_id':cushionId})[0]

		self._db.add("signal_type",{'type':"r1v1"})
		signalTypeId = self._db.queryId("signal_type",{"type":"r1v1"})[0]

		self._db.add("monitor_data",{'signal_id':signalTypeId,'location_id':locationId})
		dataId = self._db.queryId("monitor_data",{'signal_id':signalTypeId,'location_id':locationId})[0]
		assert( dataId )

		self._db.rm("router",(routerId,))
		self._db.rm("cushion",(cushionId,))
		self._db.rm("protege",(protegeId,))
		self._db.rm("signal_type",(signalTypeId,))

	def testWarning(self):
		self._db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001C"})
		self._db.add("router",{'type':"r1v1",'routerco_mac':"TEST001R"})
		self._db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})

		cushionId = self._db.queryId("cushion",{"cushion_mac":"TEST001C"})[0]
		routerId = self._db.queryId("router",{"routerco_mac":"TEST001R"})[0]
		protegeId = self._db.queryId("protege",{"id_card_num":"150214xxxxxxx"})[0]
		self._db.add("location",{'cushion_id':cushionId,'router_id':routerId,"protege_id":protegeId})
		locationId = self._db.queryId("location",{'router_id':routerId,'protege_id':protegeId,'cushion_id':cushionId})[0]

		self._db.add("signal_type",{'type':"r1v1"})
		signalTypeId = self._db.queryId("signal_type",{"type":"r1v1"})[0]

		self._db.add("monitor_data",{'signal_id':signalTypeId,'location_id':locationId})
		dataId = self._db.queryId("monitor_data",{'signal_id':signalTypeId,'location_id':locationId})[0]

		self._db.add("warning_type",{'type':"r1v1"})
		warningTypeId = self._db.queryId("warning_type",{"type":"r1v1"})[0]

		self._db.add("staff",{'staff_id':"212328000",'name':"Xiaoming","id_card_num":"150204xxxxxxx","password":"helloWorld"})
		staffId = self._db.queryId("staff",{"staff_id":"212328000"})[0]


		self._db.add("warning",{'data_id':dataId,'process_staff_id':staffId,'warning_id':warningTypeId})
		warningId = self._db.queryId("warning",{'data_id':dataId,'process_staff_id':staffId,'warning_id':warningTypeId})[0]


		assert( warningId )

		self._db.rm("staff",(staffId,))
		self._db.rm("warning_type",(warningTypeId,))
		self._db.rm("router",(routerId,))
		self._db.rm("cushion",(cushionId,))
		self._db.rm("protege",(protegeId,))
		self._db.rm("signal_type",(signalTypeId,))


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