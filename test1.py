import pymysql
from icareLogger import getLogger
logger = getLogger("iCareDb")


class iCareDb:
	def __init__(self):
		self._dbconnection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd="#bigguy", db='icare')
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
		# cur = None
		# logger.debug("deleteCushion : %s" % (mac))
		# try:
		#     cur = self._dbconnection.cursor()
		#     selectStatement =  "delete from cushion WHERE cushion_mac = '%s';"%mac
		#     self.__execute_sql(cur, selectStatement)
		#     self._dbconnection.commit()
		# finally :
		#     if cur :
		#     	cur.close()
		#     	self._dbconnection.rollback()

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
		return allRows[0]

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

		# cur = None
		# logger.debug("addCushion : %s %s" % (cushionType,mac))
		# try:
		#     cur = self._dbconnection.cursor()
		#     selectStatement = "insert into cushion (type,cushion_mac) values ('%s' ,'%s')"%(cushionType,mac)
		#     self.__execute_sql(cur, selectStatement)
		#     self._dbconnection.commit()
		# finally :
		#     if cur :
		#     	cur.close()
		#     	self._dbconnection.rollback()

        

if __name__ == "__main__":
	db = iCareDb();
	print(db.query("show tables;"))