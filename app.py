from flask import Flask, request, url_for, redirect,flash, send_from_directory, render_template
from flask_mysqldb import MySQL
from datetime import datetime
import os

app = Flask(__name__)

#MySQL Connection
app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3307
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='sistema'
mysql = MySQL(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA


@app.route('/gestion')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    print(data)
    return render_template('contactos/index.html', contactos=data)

@app.route('/create', methods=['POST'])
def agregar():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        pais = request.form['pais']
        genero = request.form['genero']
        foto = request.files['foto'] 
        print(fullname)
        print(phone)
        print(email)
        print(pais)
        print(genero)
        
        now= datetime.now()
        tiempo= now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto=tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
        else:
            nuevoNombreFoto = ''
            
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactos (nombre, email, telefono, pais, genero, foto) VALUES (%s, %s, %s, %s, %s, %s)', (fullname, email, phone, pais, genero, nuevoNombreFoto))
        mysql.connection.commit()
        flash('Contacto agregado exitosamente')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contacto(id):
    cur = mysql.connection.cursor()
    
    cur.execute('SELECT foto FROM contactos WHERE id=%s', (id,))
    fila = cur.fetchall()
    if len(fila) > 0:
        existing_photo = fila[0][0]
    if existing_photo:
        os.remove(os.path.join(app.config['CARPETA'], existing_photo))
    
    cur.execute('DELETE FROM contactos WHERE id = {0}'.format(id))
    
    mysql.connection.commit()
    flash('Contacto borrado exitosamente')
    return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_contact_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(data[0])
    return render_template('contactos/edit.html', contacto = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contacto(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        pais = request.form['pais']
        genero = request.form['genero']
        foto = request.files['foto']
        
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contactos
        SET nombre = %s,
        genero = %s,
        email = %s,
        telefono = %s,
        pais = %s
        WHERE id = %s
        """, (fullname, genero, email, phone, pais, id))
        
        now= datetime.now()
        tiempo= now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto=tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
        else:
            nuevoNombreFoto = ''
            
        cur.execute('SELECT foto FROM contactos WHERE id=%s', (id,))
        fila = cur.fetchall()
        
        if len(fila) > 0:
           existing_photo = fila[0][0]
        if existing_photo:
            os.remove(os.path.join(app.config['CARPETA'], existing_photo))
            
        cur.execute('UPDATE contactos SET foto = %s WHERE id = %s;', (nuevoNombreFoto, id))
        
        mysql.connection.commit()
        
        flash('Contacto actualizado exitosamente')
        
        return redirect(url_for('index'))

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
 return send_from_directory(app.config['CARPETA'], nombreFoto)

@app.route('/index')
def inicio():
    return render_template('original/index.html')

@app.route('/cursos')
def cursos():
    return render_template('original/cursos.html')

@app.route('/contacto')
def contacto():
    return render_template('original/contacto.html')

@app.route('/contactos')
def contactos():
    return render_template('original/contactos.html')

@app.route('/about')
def about():
    return render_template('original/about.html')

@app.route('/galeria')
def aboutus():
    return render_template('original/aboutUs.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    
    


