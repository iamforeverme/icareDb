insert into device(mac) values("12331");
insert into device(mac) values("1234");
insert into device(mac) values("qweasd");
insert into device(mac) values("23eddq");
insert into device(mac) values("fgher3");
insert into staff(staff_id,name,id_card_num,password,gender,age,tel) values("009","小张护士","150204193206052291","password","female",38,"13880332444");
insert into protege(name,id_card_num,telphone,mobile,contacts_name1,contacts_tel1,contacts_name2,contacts_tel2,history,province,city,address,photo_dir,age,monitoring_level) values("张大爷","150204193206052290","027-31876542","13942365587","张小胖","13942365589","张小芳","13942365592","高血压,心脏病","上海","上海","陆家嘴张家大院","",86,"level1");

insert into protege(name,id_card_num,telphone,mobile,contacts_name1,contacts_tel1,contacts_name2,contacts_tel2,history,province,city,address,photo_dir,age,monitoring_level) values("王大爷","1110332193206052290","010-31239542","13942365587","王二","13942365590","王初花","13942365664","糖尿病","北京","北京","北新桥","",88,"level2");

insert into signal_type(type) values("WET");

insert into warning_type(type,measurement) values("LONGLEAVE","肮脏程度过高");

insert into monitor_data(protege_id,signal_type_id,rec_time) values(1,1,'2009-9-9 23:22:11');

insert into location (room_num,bed_num,build_num,start_date,end_date,protege_id,device_id) values("4","2","1",'2006-9-9 23:22:11','2009-9-9 23:22:11',1,1);

insert into command_to_device (parameters,signal_type_id,device_id) values("start up",1,1);
insert into warning (start_time,complete_time,solution,staff_id,data_id,warning_type_id) values('2006-9-9 23:22:11','2009-9-9 23:22:11',"全都擦干净了",1,1,1);
	