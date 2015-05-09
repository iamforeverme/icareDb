import pymysql
from icareLogger import getLogger
logger = getLogger("iCareDb")


class MySqlDb:
	def __init__(self,host,port,user,passwd,db):
		logger.debug("connect database : host %s ;  port %s ; user %s ; passwd %s ; db %s" % (host, port, user, passwd, db))
		try:
			self._dbconnection = pymysql.connect(host, port=port, user=user, passwd=passwd, db=db)
			self._cur = None
			self._cur = self._dbconnection.cursor()
		except MySQLdb.Error:
			logger.debug("There was a problem in connecting to the database. Please ensure that the database exists on the local host system.")
			raise MySQLdb.Error
		except MySQLdb.Warning:
			pass


	def __del__( self ):
		self._dbconnection.close();
		if self._cur :
			self._cur.close()
			self._cur = None

	def query(self, selectStatement):
	    self.__execute_sql(self._cur, selectStatement)
	    allRows = self._cur.fetchall()
	    return allRows

	def _getId(self,table,colName,colVal):
		logger.debug("_getId : %s ; %s" % (colName,colVal))
		values = ""
		for name,value in zip(colName,colVal):
			if(isinstance(value,str)):
				values = values + " and  " + name +" = \'" + value + "\' "
			else:
				values = values + " and  " + name +" = " + str(value) + " "
		
		values = values[4:-1] 
		selectStatement =  "select id from %s WHERE %s;"%(table,values)
		logger.debug(selectStatement)
		self.__execute_sql(self._cur, selectStatement)
		allRows = self._cur.fetchall()
		if(allRows):
			return allRows[0]
		else:
			return None

	def _rmContent(self,table,id):
		selectStatement =  "delete from %s WHERE id = %s;"%(table,id)
		self.__execute_sql(self._cur, selectStatement)
		self._dbconnection.commit()

	def _updateContent(self,table,id,colName,colVal):
		selectStatement =  "update %s set %s WHERE id = %s;"%(table," , ".join((" = ".join((part[0],"\'"+part[1]+"\'")) for part in tuple(zip(colName,colVal)))),id)
		self.__execute_sql(self._cur, selectStatement)
		self._dbconnection.commit()

	def _getVal(self,table,id,colName):
		selectStatement =  "select %s from %s WHERE id = %s;"%(','.join(colName),table,id)
		logger.debug(selectStatement)
		self.__execute_sql(self._cur, selectStatement)
		allRows = self._cur.fetchall()
		if(allRows):
			return allRows[0]
		else:
			return None

	def _addContent(self,table,colName,colVal):
		logger.debug("_addContent : %s ; %s" % (colName,colVal))
		values = ""
		for item in colVal:
			if(isinstance(item,str)):
				values = values + ", \'" + item +"\' "
			else:
				values = values + ", " + str(item) +" "
		
		values = values[2:-1] 
		selectStatement = "insert into %s (%s) values (%s);"%(table,','.join(colName),values)
		self.__execute_sql(self._cur, selectStatement)
		self._dbconnection.commit()

	def _addMany(self,table,colName,valueMat):
		logger.debug("_addContent : %s ; %s" % (table,par))
		sqlStatement  =  "insert into %s (%s) values (%s);"%(table,','.join(colName))
		self.__execute_sql_many(self._cur, sqlStatement,valueMat)

	def __execute_sql(self, cur, sqlStatement):
		logger.debug("Executing : %s" % sqlStatement)
		return cur.execute(sqlStatement)

	def __execute_sql_many(self, cur, sqlStatement,par):
		logger.debug("Executing many : %s" % sqlStatement)
		return cur.executemany(sqlStatement,par)