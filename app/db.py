import os,sqlite3
def path(): return os.environ.get('DATABASE_PATH','data/app.db')
def upgrade():
 os.makedirs(os.path.dirname(path()) or '.',exist_ok=True)
 with sqlite3.connect(path()) as d: d.execute('create table if not exists schema_version(version integer not null)'); d.execute('insert into schema_version select 1 where not exists(select 1 from schema_version)')
if __name__=='__main__': upgrade(); print('SQLite schema ready')
