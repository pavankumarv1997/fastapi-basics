import logging
import traceback

from utilities.mysql import Mysql

logger = logging.getLogger('handler_logger')

class Admin_handler(object):

    def __init__(self):
        self.db = Mysql()

    def get_admin_by_id(self,id):
        try:
            result = self.db.select_query(f"select * from admin where admin_id = {id}",1)
            return result
        except Exception as e:
            logger.error("Error while running get_admin_by_id: "+str(e))
            traceback.print_exc()
