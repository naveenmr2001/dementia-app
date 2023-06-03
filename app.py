from tensorflow import keras
import base64,os,cv2
from flask import Flask, render_template, request, url_for, redirect,session
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = os.path.join('static', 'images')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'EDCBA'

@app.route('/preview', methods=['GET','POST'])
def preview():
    img_file_path = session.get('uploaded_img_file_path', None)
    model = keras.models.load_model('./model/model.h5')
    categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]
    images = []
    data = cv2.imread(img_file_path,cv2.IMREAD_GRAYSCALE)
    new_data = cv2.resize(data,(120,120),interpolation=cv2.INTER_AREA)
    new_data = new_data / 255.0
    images.append(new_data)
    ptitle = str()
    for img in images:
        image = np.array(img).reshape(-1,120,120)
        prediction = model.predict(image)
        ptitle = "Prediction: {0}".format(categories[np.argmax(prediction)])
        print(ptitle)
    return render_template("preview.html",image=img_file_path,result=ptitle)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        image = request.files['image']
        img_filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        print(image)
        session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        return redirect("/preview")
    return render_template("predict.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()