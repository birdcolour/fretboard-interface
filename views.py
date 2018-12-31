from flask import render_template, request, url_for, Blueprint

from diagram import UkuleleChord, GuitarChord

from forms import ChordForm, DownloadForm


my_view = Blueprint('my_view', __name__)


@my_view.route('/', methods=['GET', 'POST'])
def home():
    def create_diagram(chord_form):
        """Create chord diagram and return filename."""
        if chord_form.instrument.data == 'guitar':
            chord_cls = GuitarChord
        if chord_form.instrument.data == 'ukulele':
            chord_cls = UkuleleChord

        diagram = chord_cls(
            positions=chord_form.positions.data,
            fingers=chord_form.fingers.data,
            barre=chord_form.barre.data,
            title=chord_form.title.data,
        )

        # This is obviously dumb, but works for now
        filename = 'static/{ins}/{title}_{pos}_{fin}_{bar}.svg'.format(
            title=chord_form.title.data,
            ins=chord_form.instrument.data,
            pos=chord_form.positions.data,
            fin=chord_form.fingers.data,
            bar=chord_form.barre.data,
        )
        diagram.save(filename)

        return filename

    chord_form = ChordForm(request.form)
    # download_form = DownloadForm(request.form)

    if request.method == 'POST':
        # Diagram
        if chord_form.validate_on_submit():
            return render_template(
                'index.html',
                diagram=create_diagram(chord_form),
                chord_form=chord_form,
                # download_form=download_form
            )

    return render_template(
                'index.html',
                diagram=create_diagram(chord_form),
                chord_form=chord_form,
                # download_form=download_form
            )



