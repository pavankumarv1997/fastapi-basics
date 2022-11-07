import json
import traceback

from fastapi import APIRouter
from utilities.mysql import Mysql
from schemas.admin import Admin
from handlers.admin import Admin_handler
import logging


logger = logging.getLogger('router')
admin_router = APIRouter(prefix="/fastbasics/v1",tags=["Admin"])

db = Mysql()
admin_handler = Admin_handler()

@admin_router.get('/')
async def get_admins():
    try:
        result = db.select_query("select * from admin")
        json_data = json.dumps(result)
        json_without_slash = json.loads(json_data)
        return json_without_slash
    except Exception as e:
        logger.error("Error while executing get_admins "+str(e))
        traceback.print_exc()

@admin_router.post('/add_admin')
async def add_admin(admin:Admin):
    try:
        # query = f"insert into admin(name,email,phone,password,level,login_status) " \
        #         f"values("+admin.name+","+admin.email+","+str(admin.phone)+"," \
        #         f""+admin.password+","+str(admin.level)+","+str(admin.login_status)+")"
        query = f"insert into admin(name,email,phone,password,level,login_status)"\
                f"values('{admin.name}','{admin.email}','{admin.phone}','{admin.password}'"\
                f",{admin.level},{admin.login_status})"
        result = db.insert_update(query)
        return result
    except Exception as e:
        logger.error("Error while executing add_admin "+str(e))
        traceback.print_exc()


# using mvc approach by dividing code with handlers

@admin_router.get('/admin/{id}')
async def get_admin_by_id(id):
    if id is not None:
        result = admin_handler.get_admin_by_id(id)
        json_data = json.dumps(result)
        json_without_slash = json.loads(json_data)
    return json_without_slash
