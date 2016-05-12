import psycopg2


def _get_session():
    try:
        conn = psycopg2.connect("dbname='CRM' user='root' host='localhost' password='root'")
    except:
        print "I am unable to connect to the database"
        return 'error'

    return conn.cursor()

def _insert_client(nombre, type, phone, url, email, addr, city, netvalue, clientsince, twitteracct, pic)
    cur = _get_session()
    query= 'INSERT INTO Clientes (id_cliente, nombre, cliente_type, telefono, sitio_web, correo_electronico, direccion, ciudad, valor_net, cliente_desde, twitter_acct, foto) VALUES (nextval(val_id_cliente),'+name+ ',' +type+ ',' +phone + ','+ url + ',' + email +','+ addr+ ','+city+','+netvalue+','+clientsince+','+twitteracct+','+pic+';')
    cur.execute(query)


def _update_client(campos[], oldVals[], newVals[]):
    cur = _get_session()
    for i in campos[]:
        query= 'UPDATE Clientes SET '+campos[i]+'= '+newVals[i]+' WHERE '+campos[i]+' = '+oldVals[i]+';'
        cur.execute(query)

def _delete_client(id):
    cur = _get_session()
    query = 'DELETE FROM Clientes WHERE id_cliente='+id+';'
    cur.execute(query)
