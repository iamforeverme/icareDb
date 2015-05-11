from icareDatabase import *

def createData():
	db = iCareDb()
	db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001C"})
	db.add("cushion",{'type':"r1v1",'cushion_mac':"TEST001C2"})
	db.add("router",{'type':"r1v1",'routerco_mac':"TEST001R"})
	db.add("router",{'type':"r1v1",'routerco_mac':"TEST001R1"})
	db.add("protege",{'gender':"male",'name':"XiaoHe","id_card_num":"150214xxxxxxx","mobile":"13033331234","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})
	db.add("protege",{'gender':"female",'name':"ZhangQiang","id_card_num":"150214xxxx23x","mobile":"13033331212","contacts_name1":"XiaoWang","contacts_tel1":"13033333214"})

	cushionId = db.queryId("cushion",{"cushion_mac":"TEST001C"})[0]
	routerId = db.queryId("router",{"routerco_mac":"TEST001R"})[0]
	protegeId = db.queryId("protege",{"id_card_num":"150214xxxxxxx"})[0]
	db.add("location",{'cushion_id':cushionId,'router_id':routerId,"protege_id":protegeId})
	locationId = db.queryId("location",{'router_id':routerId,'protege_id':protegeId,'cushion_id':cushionId})[0]

	db.add("signal_type",{'type':"r1v1"})
	signalTypeId = db.queryId("signal_type",{"type":"r1v1"})[0]

	

	db.addMany("monitor_data",('signal_id','location_id','rec_time'),((signalTypeId,locationId,"2009-12-02 12:14"),
	(signalTypeId,locationId,"2009-12-05 12:14"),(signalTypeId,locationId,"2010-3-05 12:14"),(signalTypeId,locationId,"2015-3-25 11:14")))

if __name__ =="__main__":
	createData()