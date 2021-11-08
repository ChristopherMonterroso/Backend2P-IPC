from flask import Flask,request, jsonify
from flask_cors import CORS
from Usuarios import Usuario
from Imagenes import Imagen
from Videos import Video
import json
app = Flask(__name__)
CORS(app)
Usuarios = []
Imagenes = []
Videos = []
nuevo = Usuario("admin", "Abner Cardona", "M", "admin@ipc1.com", "admin@ipc1")
Usuarios.append(nuevo)
nuevo = Usuario("Chris", "Christoher", "M", "ADSF@gmail.com", "12345678")
Usuarios.append(nuevo)
#Métodos GET
@app.route("/Imagenes", methods=['GET'])
def LlamarImagenes():
    global Imagenes
    envios = []
    for Imagen in Imagenes:
        unEnvio={
            "url": Imagen.getUrl(),
            "date": Imagen.getDate(),
            "category":Imagen.getCategory()
        }    
        envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta

@app.route("/Videos", methods=['GET'])
def LlamarVideos():
    global Videos
    envios = []
    for Video in Videos:
        unEnvio={
            "url": Video.getUrl(),
            "date": Video.getDate(),
            "category":Video.getCategory()
        }    
        envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta
@app.route("/usuarios", methods=['GET'])
def LlamarUsuarios():
    global Usuarios
    envios = []
    for Usuario in Usuarios:
        unEnvio={
            "username": Usuario.getUsername(),
            "nombre": Usuario.getNombre(),
            "genero":Usuario.getGenero(),
            "correo": Usuario.getcorreo(),
            "password":Usuario.getPassword()
        }    
        envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta
@app.route("/usuarios/U", methods=['GET'])
def LlamarIDUsuarios():
    global Usuarios
    envios = []
    for Usuario in Usuarios:
        unEnvio={
            "username": Usuario.getUsername()
        }    
        envios.append(unEnvio)
    respuesta = jsonify(envios) 
    return respuesta
#Métodos POST-------------------------------------------------------------------------------

@app.route("/usuarios",methods=['POST'])
def CrearUsuario():
    global Usuarios
    nuevoUsuario = Usuario(request.json['username'],request.json['nombre'], request.json['genero'], request.json['correo'], request.json['password'])
    Usuarios.append(nuevoUsuario)
    respuesta = jsonify({'error':False,"mensaje":"Todo bien"})
    return respuesta

@app.route("/Videos",methods=['POST'])
def CrearVideo():
    global Videos
    nuevoVideo = Video(request.json['url'], request.json['date'], request.json['category']) 
    Videos.append(nuevoVideo)
    respuesta = jsonify({'error':False,"mensaje":"Todo bien"})
    return respuesta

@app.route("/Imagenes",methods=['POST'])
def CrearImagen():
    global Imagenes
    nuevaImagen = Imagen(request.json['url'], request.json['date'], request.json['category']) 
    Imagenes.append(nuevaImagen)
    respuesta = jsonify({'error':False,"mensaje":"Todo bien"})
    return respuesta


#Métodos DELETE-----------------------------------------------------------------------------

@app.route('/usuarios/<string:username>',methods=['DELETE'])
def EliminarUsuarios(username):
    global Usuarios
    for i in range(len(Usuarios)):
        if username==Usuarios[i].getUsername():
            del Usuarios[i]
            return jsonify({'mensaje:':'se eliminó el usuario'})
    return jsonify({'mensaje':'no se encontró el usuario'})

@app.route('/imagenes/<string:url>',methods=['DELETE'])
def EliminarImagen(url):
    global Imagenes
    for i in range(len(Imagenes)):
        if url==Imagenes[i].getUrl():
            del Imagenes[i]
            return jsonify({'mensaje:':'se eliminó la imagen'})
    return jsonify({'mensaje':'no se encontró la imagen'})

@app.route('/videos/<string:url>',methods=['DELETE'])
def EliminarVideo(url):
    global Videos
    for i in range(len(Videos)):
        if url==Videos[i].getUrl():
            del Videos[i]
            return jsonify({'mensaje:':'se eliminó el video'})
    return jsonify({'mensaje':'no se encontró el video'})
#Método PUT----------------------------------------------------------------------------------
@app.route('/usuarios/<string:username>',methods=['PUT'])
def ActualizarUsuario(username):
    global Usuarios
    envios= []
    for i in range(len(Usuarios)):
        if username==Usuarios[i].getUsername():
            Usuarios[i].setNombre(request.json['nombre']),
            Usuarios[i].setGenero(request.json['genero']),
            Usuarios[i].setCorreo(request.json['correo']),
            Usuarios[i].setEdad(request.json['password'])
            return jsonify({'mensaje:':'se actualizó el usuario'})
    return jsonify({'mensaje':'no se encontró el usuario'})

if __name__=='__main__':
    app.run(host="0.0.0.0",port=3000,debug=True)
