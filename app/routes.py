from app import app
from app.controllers.product_controller import product_blueprint
from app.controllers.user_controller import user_blueprint

app.register_blueprint(product_blueprint)
app.register_blueprint(user_blueprint)