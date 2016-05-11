import psycopg2


def _get_session():
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
        return 'error'

    return conn.cursor()
