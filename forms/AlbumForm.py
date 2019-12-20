from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators

class AlbumForm(FlaskForm):

    id = HiddenField()

    album_name = StringField("Назва: ", [
        validators.DataRequired("Введіть назву альбому."),
        validators.Length(3, 15, "Назва має містити від 3 до 15 символів.")
    ])

    album_performer = IntegerField("Код виконавця: ", [
        validators.data_required("Це поле є обов'язковим.")
    ])

    submit = SubmitField("Зберегти")