import pymysql
from icareLogger import getLogger
logger = getLogger("iCareDb")


class MySqlDb:
	def __init__(self,host,port,user,passwd,db):
		logger.debug("connect database : host %s ;  port %s ; user %s ; passwd %s ; db %s" % (host, port, user, passwd, db))
		self._dbconnection = pymysql.connect(host, port=port, user=user, passwd=passwd, db=db)

	def __del__( self ):
		self._dbconnection.close();

	def query(self, selectStatement):
		cur = None
		try:
		    cur = self._dbconnection.cursor()
		    self.__execute_sql(cur, selectStatement)
		    allRows = cur.fetchall()
		    return allRows
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()

	def _getId(self,table,colName,colVal):
		cur = None
		logger.debug("_getId : %s ; %s" % (','.join(colName),','.join(colVal)))
		try:
		    cur = self._dbconnection.cursor()
		    selectStatement =  "select id from %s WHERE %s;"%(table," and ".join((" = ".join((part[0],"\'"+part[1]+"\'")) for part in tuple(zip(colName,colVal)))))
		    self.__execute_sql(cur, selectStatement)
		    allRows = cur.fetchall()
		    logger.debug(allRows)
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()
		if(allRows):
			return allRows[0]
		else:
			return None

	def _rmContent(self,table,id):
		cur = None
		logger.debug("_rmContent : %s %s" % (table,id))
		try:
		    cur = self._dbconnection.cursor()
		    selectStatement =  "delete from %s WHERE id = %s;"%(table,id)
		    self.__execute_sql(cur, selectStatement)
		    self._dbconnection.commit()
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()

	def _updateContent(self,table,id,colName,colVal):
		cur = None
		logger.debug("_updateContent : %s %s" % (table,id))
		try:
		    cur = self._dbconnection.cursor()
		    selectStatement =  "update %s set %s WHERE id = %s;"%(table," , ".join((" = ".join((part[0],"\'"+part[1]+"\'")) for part in tuple(zip(colName,colVal)))),id)
		    self.__execute_sql(cur, selectStatement)
		    self._dbconnection.commit()
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()

	def _getVal(self,table,id,colName):
		cur = None
		logger.debug("_getVal : %s " % (','.join(colName)))
		try:
		    cur = self._dbconnection.cursor()
		    selectStatement =  "select %s from %s WHERE id = %s;"%(','.join(colName),table,id)
		    logger.debug(selectStatement)
		    self.__execute_sql(cur, selectStatement)
		    allRows = cur.fetchall()
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()
		if(allRows):
			return allRows[0]
		else:
			return None

	def _addContent(self,table,colName,colVal):
		cur = None
		logger.debug("_addContent : %s ; %s" % (','.join(colName),','.join(colVal)))
		try:
		    cur = self._dbconnection.cursor()
		    selectStatement = "insert into %s (%s) values ('%s')"%(table,','.join(colName),"\',\'".join(colVal))
		    self.__execute_sql(cur, selectStatement)
		    self._dbconnection.commit()
		finally :
		    if cur :
		    	cur.close()
		    	self._dbconnection.rollback()

	def __execute_sql(self, cur, sqlStatement):
		logger.debug("Executing : %s" % sqlStatement)
		return cur.execute(sqlStatement)