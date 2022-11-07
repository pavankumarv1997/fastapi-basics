import traceback

import pymysql
import logging
from constants.config import *

logger = logging.getLogger('simple_example')


class Mysql(object):

    def __init__(self):
        try:
            logger.info("mysql connection initialization")
            self.host = DB_HOST
            self.username = DB_USER_NAME
            self.password = DB_PASSWORD
            self.db_name = DB_NAME
        except Exception as e:
            logger.error('Exception while mysql connection initialization ' + str(e))
            traceback.print_exc()

    def select_query(self, query , resulttype = 2):
        """
                This method is used for selecting records from tables.
                :param query: The select query to be executed
                """
        connection = None
        result = ""
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name)
            with connection.cursor() as cursor:
                cursor.execute(query)
                if resulttype == 1:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
        except Exception as e:
            logger.error('Exception while while executing select query ' + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))

        return result

    def insert_update(self,query):
        """
            This method is used for inserting and updating records from tables.
            :param query: The insert/update query to be executed
            """
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name)
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
            flag = True
        except Exception as e:
            logger.error("Exception while running insert_update function: "+str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

