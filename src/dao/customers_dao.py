import random
from src.utilities.dbUtility import DBUtility

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}users 
                  WHERE user_email = '{email}';'''
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_from_db(self, quantity=1):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}users 
                 ORDER BY id DESC LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(quantity))
