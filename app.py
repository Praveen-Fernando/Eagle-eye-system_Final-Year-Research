from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/criminal_investigation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class VideoDetails(db.Model):  # Articles
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    path = db.Column(db.String(250))

    def __init__(self, name, path):
        self.name = name
        self.path = path


class VideoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'path')


class Values:
    class Meta:
        fields = 'value'


video_file = VideoSchema()
video_files = VideoSchema(many=True)

value_field = Values()


@app.route('/get', methods=['GET'])
def get_videos():
    videos = VideoDetails.query.all()
    results = video_files.dump(videos)
    return jsonify(results)


@app.route('/get/<id>/', methods=['GET'])
def get_video(id):
    video = VideoDetails.query.get(id)
    return video_file.jsonify(video)


@app.route('/getEnhancedVideo/<id>/', methods=['GET'])
def get_enhanced_video(id):
    video = EnhancedVideos.query.get(id)
    return EnhancedVideoFile.jsonify(video)


@app.route('/add', methods=['POST'])
def add_video():
    name_from_path = request.json['path']
    name_from_path = str(name_from_path).split('\\')

    # name = request.json['name']
    name = name_from_path[2]
    path = request.json['path']

    video = VideoDetails(name, path)
    db.session.add(video)
    db.session.commit()

    return video_file.jsonify(video)


""" Start of the image enhancement function """


class EnhancedVideos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    path = db.Column(db.String(150))

    def __init__(self, name, path):
        self.name = name
        self.path = path


class EnhancedVideosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'path')


class EnhancedValues:
    class Meta:
        fields = 'value'


EnhancedVideoFile = EnhancedVideosSchema()

EnhancedVideo_value_field = EnhancedValues()


@app.route('/StartImageEnhance', methods=['POST'])
def StartImageEnhance():
    from imageEnhancement import VidToFrames
    path = request.json['path']

    path = str(path).split('\\')
    print(path)

    value = VidToFrames.FrameCapture("E:\\BACKBONE\\videos\\" + path[2])

    name = value
    Video_path = "E:\\BACKBONE\\image_enhancement\\EnhancedVideos\\" + value
    data = EnhancedVideos(name, Video_path)
    db.session.add(data)
    db.session.commit()

    values = {'id': data.id, 'name': data.name, 'path': data.path}

    return values


""" End of the image enhancement function """

""" Start of the abnormal behavior detection function """


class AbnormalBehaviourDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeOfAttack = db.Column(db.String(100))
    usedWeapon = db.Column(db.String(100))

    def __init__(self, typeOfAttack, usedWeapon):
        self.usedWeapon = usedWeapon
        self.typeOfAttack = typeOfAttack


class AbnormalBehaviourSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usedWeapon', 'typeOfAttack')


class Values:
    class Meta:
        fields = 'value'


AbnormalBehaviour = AbnormalBehaviourSchema()
AbnormalBehaviours = AbnormalBehaviourSchema(many=True)

AbnormalBehaviour_value_field = Values()


@app.route('/startAbnormalBehaviourDetection', methods=['POST'])
def startAbnormalBehaviourDetection():
    from abnormal_behavior_detection.ScriptsOrder import Scripts_Order

    name = request.json['name']
    path = request.json['path']
    # data = get_video(id)

    # path = str(path).split('\\')
    print("print->" + path)

    data = {'id': id, 'name': name, 'path': path}
    # data = {'id': id, 'name': name, 'path': path}

    # Human_Detection_Video.capture_humans('C:/Users/Givindu/Desktop/New folder/'+path[2])
    print("app -> " + path)
    AbDetection = Scripts_Order.data(path+"\\Enhanced_Video.avi")

    return jsonify(AbDetection)


class behavior_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    incident_type = db.Column(db.String(100))
    used_weapon = db.Column(db.String(100))
    detected_time = db.Column(db.Float())

    def __init__(self, incident_type, used_weapon, detected_time):
        self.incident_type = incident_type
        self.used_weapon = used_weapon
        self.detected_time = detected_time


class behavior_details_schema(ma.Schema):
    class Meta:
        fields = (
            'id', 'incident_type', 'used_weapon', 'detected_time')


behaviors_schema = behavior_details_schema()
behaviors_schema = behavior_details_schema(many=True)


class criminal_result_schema(ma.Schema):
    class Meta:
        fields = (
            'id', 'incident_type', 'used_weapon', 'detected_time')


criminal_schema = criminal_result_schema()
criminals_schema = criminal_result_schema(many=True)

""" End of the abnormal behavior detection function """

""" Start of the face recognition function """


# For Face Recognition
class FaceRecognitionDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    path = db.Column(db.String(250))

    def __init__(self, name, path):
        self.name = name
        self.path = path


class FaceRecognitionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'path')


class Values:
    class Meta:
        fields = 'value'


faceRecognitionSchema = FaceRecognitionSchema()
faceRecognitionSchemas = FaceRecognitionSchema(many=True)

FaceRecognitionSchema_field = Values()

""" End of the abnormal behavior detection function """

""" Start of the face detection function """


# Criminals table input fields
# Table Name : Criminals_details
class Criminals_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Age = db.Column(db.Integer())
    Gender = db.Column(db.String(100))
    DOB = db.Column(db.DATE())
    Address = db.Column(db.String(100))
    Blood_Group = db.Column(db.String(100))
    NIC = db.Column(db.Integer())
    Height = db.Column(db.Float())
    Crimes = db.Column(db.String(100))
    fileinput = db.Column(db.String(250))

    def __init__(self, Name, Age, Gender, DOB, Address, Blood_Group, NIC, Height, Crimes, fileinput):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.DOB = DOB
        self.Address = Address
        self.Blood_Group = Blood_Group
        self.NIC = NIC
        self.Height = Height
        self.Crimes = Crimes
        self.fileinput = fileinput


class Criminals_Schema(ma.Schema):
    class Meta:
        fields = (
            'id', 'Name', 'Age', 'Gender', 'DOB', 'Address', 'Blood_Group', 'NIC', 'Height', 'Crimes', 'fileinput')


criminals_Schema = Criminals_Schema()
criminals_Schema = Criminals_Schema(many=True)


# POST Criminals details
@app.route('/add_Criminals', methods=['POST'])
def add_Criminals_details():
    from face_detection_recognition import script_file
    Name = request.json['Name']
    Age = request.json['Age']
    Gender = request.json['Gender']
    DOB = request.json['DOB']
    Address = request.json['Address']
    Blood_Group = request.json['Blood_Group']
    NIC = request.json['NIC']
    Height = request.json['Height']
    Crimes = request.json['Crimes']
    fileinput = request.json['fileinput']

    criminals_details = Criminals_details(Name, Age, Gender, DOB, Address, Blood_Group, NIC, Height, Crimes, fileinput)
    db.session.add(criminals_details)
    db.session.commit()

    data = criminals_details.fileinput.split('\\')

    script_file.criminalRegistration(criminals_details.id, 'E:/BACKBONE/face_detection_recognition/Criminals_images/')
    return criminals_Schema.jsonify(data)


# GET Criminals details
@app.route('/get_Criminals', methods=['GET'])
def get_Criminals_details():
    all_criminals_details = Criminals_details.query.all()
    results = criminals_Schema.dump(all_criminals_details)
    return jsonify(results)


# GET Criminals details by specific id
@app.route('/get_Criminals/<id>/', methods=['GET'])
def post_details(id):
    # criminals_details = Criminals_details.query.get(id)
    # return criminals_Schema.jsonify(criminals_details)
    from face_detection_recognition import script_file
    criminalDetails = Criminals_details.query.get(id)
    script_file.criminalRegistration(criminalDetails.id, criminalDetails.fileinput)


# UPDATE Criminals details according to the specific id
@app.route('/update/<id>/', methods=['PUT'])
def update_Criminals_details(id):
    criminals_details = Criminals_details.query.get(id)
    Name = request.json['Name']
    Age = request.json['Age']
    Gender = request.json['Gender']
    DOB = request.json['DOB']
    Address = request.json['Address']
    Blood_Group = request.json['Blood_Group']
    NIC = request.json['NIC']
    Height = request.json['Height']
    Crimes = request.json['Crimes']

    # Assing new values
    criminals_details.Name = Name
    criminals_details.Age = Age
    criminals_details.Gender = Gender
    criminals_details.DOB = DOB
    criminals_details.Address = Address
    criminals_details.Blood_Group = Blood_Group
    criminals_details.NIC = NIC
    criminals_details.Height = Height
    criminals_details.Crimes = Crimes

    db.session.commit()
    return criminals_Schema.jsonify(criminals_details)


class criminal_result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Age = db.Column(db.Integer())
    Gender = db.Column(db.String(100))
    DOB = db.Column(db.DATE())
    Address = db.Column(db.String(100))
    Blood_Group = db.Column(db.String(100))
    NIC = db.Column(db.Integer())
    Height = db.Column(db.Integer())
    Crimes = db.Column(db.String(100))

    def __init__(self, Name, Age, Gender, DOB, Address, Blood_Group, NIC, Height, Crimes):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.DOB = DOB
        self.Address = Address
        self.Blood_Group = Blood_Group
        self.NIC = NIC
        self.Height = Height
        self.Crimes = Crimes


@app.route('/RunFaceRecognition/<id>/', methods=['POST'])
def RunFaceRecognition(id):
    from face_detection_recognition import script_file
    id = request.json['id']
    name = request.json['name']
    path = request.json['path']
    # data = get_video(id)

    path = str(path).split('\\')
    print(path)

    data = {'id': id, 'name': name, 'path': path}
    # data = {'id': id, 'name': name, 'path': path}

    # FaceRecognition = Scripts.data('C:/Users/Praveen/Desktop/Research project/PP1 input/Input video/' + path[2])
    FDRecognition = script_file.data('E:\\BACKBONE\\videos\\' + path[2])

    return jsonify(FDRecognition)


@app.route('/StartFaceRecognition', methods=['POST'])
def StartFaceRecognition():
    from face_detection_recognition import script_file

    # path = request.json['path']
    # # data = get_video(id)
    #
    # path = str(path).split('\\')
    # print(path)

    # FaceRecognition = Scripts.data('C:/Users/Praveen/Desktop/Research project/PP1 input/Input video/' + path[2])
    FDRecognition = script_file.imagetovideo_process(
        'E:/BACKBONE/abnormal_behavior_detection/frames/All Detected Humans/')

    return jsonify(FDRecognition)


""" End of the face detection function """

""" Start of the figure recognition function """


# Figure
class FigureDetails(db.Model):  # Articles
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(20))
    gender = db.Column(db.String(6))
    height = db.Column(db.String(15))

    def __init__(self, age, gender, height):
        self.age = age
        self.gender = gender
        self.height = height


class FigureSchema(ma.Schema):
    class Meta:
        fields = ('id', 'age', 'gender', 'height')


class Values():
    class Meta:
        fields = 'value'


figure_data = FigureSchema()
figure_datas = FigureSchema(many=True)


@app.route('/GetAllData', methods=['GET'])
def GetAllData():
    abnormalData = behavior_details.query.get(1)

    figureDataAll = FigureDetails.query.all()

    a = 0
    max1 = 0
    for i in figureDataAll:
        if i.id > a:
            max1 = i.id
            print(max1)

    figureData = FigureDetails.query.get(max1)

    faceRecogDataAll = criminal_result.query.all()

    b = 0
    max2 = 0
    for i in faceRecogDataAll:
        if i.id > b:
            max2 = i.id
            print(max2)

    faceRecogData = criminal_result.query.get(max2)

    data1 = {'id': abnormalData.id, 'incident_type': abnormalData.incident_type,
             'used_weapon': abnormalData.used_weapon, 'detected_time': abnormalData.detected_time}
    data2 = {'id': faceRecogData.id, 'Name': faceRecogData.Name, 'Age': faceRecogData.Age,
             'Gender': faceRecogData.Gender, 'DOB': faceRecogData.DOB, 'Address': faceRecogData.Address,
             'Blood_Group': faceRecogData.Blood_Group, 'NIC': faceRecogData.NIC, 'Height': faceRecogData.Height,
             'Crimes': faceRecogData.Crimes}
    data3 = {'id': figureData.id, 'age': figureData.age, 'gender': figureData.gender, 'height': figureData.height}

    return jsonify(data1, data2, data3)


@app.route('/RunFigureRecognition', methods=['POST'])
def RunFigureRecognition():
    from figure_recognition.ScriptList import Script_List
    path = request.json['path']
    # data = get_video(id)
    path = str(path).split('\\')
    print(path)

    # data = {'id': id, 'name': name, 'path': path}
    # data = {'id': id, 'name': name, 'path': path}
    age, gender = Script_List.data('C:/Users/USER/Desktop/Research/image/' + path[2])

    # figure_data.jsonify({'id':0, 'age':age, 'gender':gender, 'height':0})
    return jsonify(age, gender)


@app.route('/StartFigureRecognition', methods=['GET'])
def StartFigureRecognition():
    from figure_recognition.ScriptList import Script_List

    age, gender = Script_List.figure()

    # figure_data.jsonify({'id':0, 'age':age, 'gender':gender, 'height':0})
    return jsonify(age, gender)


@app.route('/SaveFigureData', methods=['POST'])
def SaveFigureData():
    age = request.json['age']
    gender = request.json['gender']
    height = "(160 - 170)"

    data = FigureDetails(age, gender, height)
    db.session.add(data)
    db.session.commit()

    return jsonify("Done");


""" End of the figure recognition function """

if __name__ == "__main__":
    app.run(debug=False)
