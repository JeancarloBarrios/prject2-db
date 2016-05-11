import psycopg2


def _get_session():
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
        return 'error'

    return conn.cursor()


def insert_client(name, param1, param2):
    cur = _get_session()
    query = ''
    cur.execute("""%s""", querry)
    cur.close()
