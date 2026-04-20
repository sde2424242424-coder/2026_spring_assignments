import os
import sys

os.system("chcp 65001")
sys.stdout.reconfigure(encoding='utf-8')

from init import init_db
from create import insert_data
from read import read_data
from update import update_data
from delete import delete_data

conn = init_db()

insert_data(conn)
read_data(conn)

update_data(conn)
delete_data(conn)

print("\nAfter update/delete:")
read_data(conn)

conn.close()