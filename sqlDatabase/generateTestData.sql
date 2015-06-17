insert into device(mac) values("12331");
insert into device(mac) values("1234");
insert into device(mac) values("qweasd");
insert into device(mac) values("23eddq");
insert into device(mac) values("fgher3");
insert into staff(staff_id,name,id_card_num,password,gender,tel) values("009","小张护士","150204197606052291","password","female","13880332444");
insert into protege(name,id_card_num,telphone,mobile,contacts_name1,contacts_tel1,contacts_name2,contacts_tel2,history,province,city,address,photo_dir,birthday,monitoring_level,gender) values("张大爷","150204193206052290","027-31876542","13942365587","张小胖","13942365589","张小芳","13942365592","高血压,心脏病","上海","上海","陆家嘴张家大院","",'1935-9-9 23:22:11',"level1","男");

insert into protege(name,id_card_num,telphone,mobile,contacts_name1,contacts_tel1,contacts_name2,contacts_tel2,history,province,city,address,photo_dir,monitoring_level,gender,start_date) values("王大爷","1110332193206052290","010-31239542","13942365587","王二","13942365590","王初花","13942365664","糖尿病","北京","北京","北新桥","","level2","男",'2006-9-9 23:22:11');

insert into signal_type(type) values("WET");

insert into warning_type(type,measurement) values("LONGLEAVE","肮脏程度过高");

insert into monitor_data(protege_id,signal_type_id,rec_time) values(1,1,'2009-9-9 23:22:11');

insert into location (room_num,bed_num,build_num,start_date,end_date,protege_id,device_id) values("4","2","1",'2006-9-9 23:22:11','2009-9-9 23:22:11',1,1);

insert into location (room_num,bed_num,build_num,start_date,protege_id,device_id) values("4","2","1",'2006-9-9 23:22:11',1,1);
insert into location (room_num,bed_num,build_num,start_date,protege_id,device_id) values("4","2","1",'2010-6-15 23:24:12',2,2);

insert into command_to_device (parameters,signal_type_id,device_id) values("start up",1,1);
insert into warning (start_time,complete_time,solution,staff_id,data_id,warning_type_id) values('2006-9-9 23:22:11','2009-9-9 23:22:11',"全都擦干净了",1,1,1);


insert into place (room_num,bed_num,build_num) values("4","2","1");


	{"1":"{ name:'张大爷',
	id_card_num:'150204193206052290',
	telphone:'027-31876542',mobile:'13942365587',contacts_name1:'张小胖',contacts_tel1:'13942365589',contacts_name2:'张小芳',contacts_tel2:'13942365592',history:'高血压,心脏病',province:'上海',city:'上海',address:'陆家嘴张家大院',photo_dir:'',age:'86',monitoring_level:'level1' }"}
	