from flask import Flask, render_template, request, redirect
import speech_recognition as sr
@app.route("/", methods=['GET', 'POST'])
def index():
    app = Flask(__name__)
    transcript =""
    if request.method == 'POST':
        print("Data Recieved")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as src:
                data = recognizer.record(src)
            text = recognizer.recognize_google(data,key = None, language = "en-US")
            transcript = text
    return render_template("index.html", transcript=transcript)


if __name__ == '__main__':
    app.run(debug=True, threaded= True)
