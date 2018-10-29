from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, SubmitField


class ChordForm(FlaskForm):
    instrument = RadioField(
        label='Pick an instrument',
        choices=[('ukulele', 'Ukulele'), ('guitar', 'Guitar')],
        default='ukulele'
    )
    positions = StringField(label='Positions', default='0000')
    fingers = StringField(label='Fingers', default='----')
    barre = IntegerField(label='Barre override', default=None)
    render = SubmitField(label='Render diagram')


class DownloadForm(FlaskForm):
    name = StringField(label='Name this image file', default='chord')
    submit = SubmitField('Download image')

