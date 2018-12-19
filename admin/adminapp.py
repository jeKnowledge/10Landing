from flask import Flask
from flask_admin import Admin, BaseView, expose

class AssureaAdmin(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

app = Flask(__name__)
admin = Admin(app)
admin.add_view(AssureaAdmin(name='Statistics'))
app.run()
