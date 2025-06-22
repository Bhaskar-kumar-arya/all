from flask import Flask
from flask_restful import Api, Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/database.db"
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50),nullable = False)
    likes = db.Column(db.Integer,default = 0)

    def __repr__(self):
        return f"VideoModel(id={self.id}, title={self.title}, likes={self.likes})"

if False :
    with app.app_context():
        db.create_all()

video_args = reqparse.RequestParser()
video_args.add_argument("title",type = str,help = "title required",required = True)
video_args.add_argument("likes",type = str,help = "setting likes to 0",default = 0)

resource_fields = {
    "id" : fields.Integer,
    "title" : fields.String,
    "likes" : fields.Integer(default = 0)
}

class Video (Resource) :
    @marshal_with(resource_fields)
    def get(self,id) :
        result = VideoModel.query.get(id)
        if not result :
            abort(404, message = "id not found")

        return result
    @marshal_with(resource_fields)
    def put(self) :
        args = video_args.parse_args()
        video = VideoModel(title = args["title"], likes = args["likes"])
        db.session.add(video)
        db.session.commit()
        print(video.id)
        return video
    @marshal_with(resource_fields)
    def patch(self,id) :
        args = video_args.parse_args()
        video  = VideoModel.query.get(id)
        if not video :
            abort(404, message = "id not found")
        else :
            if args["title"] :
                video.title = args["title"]
            if args["likes"] :
                video.likes = args["likes"]    
            db.session.commit()
        return video
    def delete(self,id) :
        video = VideoModel.query.get(id)
        if not video : 
            abort(404,message = "id not found")
        db.session.delete(video)
        db.session.commit()
        return {"message" : "video deleted successfully"} 

api.add_resource(Video,"/Video","/Video/<string:id>")


if __name__ == "__main__" :
    app.run(debug = True)