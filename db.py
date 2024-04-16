import psycopg2

class Database:
    def_init_(self) -> None:
        self.con = psycopg2.connect(os.getenv('DATABSE_URL'))
        self.cur = self.con.cursor()
    
    def create_table:
    