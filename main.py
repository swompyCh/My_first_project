import random

from flask import Flask, render_template

app = Flask(__name__)


# list_animal = [
#         'Абботины',
#         'Абелизавриды',
#         'Абиссинский заяц',
#         'Абиссобротула',
#         'Азиатские храмули',
#         'Азиатские щучки',
#         'Азиатский лапчатоног',
#         'Азиатский лев',
#         'Азиатский муравей-портной',]

d = {
    'Абботины': 'Абботины[2] (лат. Abbottina) — род лучепёрых рыб семейства карповых. Название роду дано в честь зоолога Джеймса Фишера Эбботта, который был профессором в Японской военной академии в Этадзиме[3].',
    'Абелизавриды': 'Абелизавриды (лат. Abelisauridae) — клада (семейство) тероподовых динозавров из группы цератозавров. Абелизавриды процветали во время мелового периода на территории древнего южного суперконтинента Гондваны. В настоящее время их ископаемые остатки найдены на территории нынешней Африки и Южной Америки, а также в Индии и на Мадагаскаре. Также сообщается об окаменелых изолированных зубах, обнаруженных в позднеюрских отложениях Португалии, и в позднемеловых отложений Франции, где они существовали с Arcovenator. Впервые абелизавриды возникли в геологической летописи в начале средней юры, и по крайней мере два рода (марокканский Chenanisaurus и мадагаскарский Majungasaurus) сохранились до конца мезозойской эры, исчезнув 66 млн лет назад.',
    'Азиатский муравей-портной': 'Азиатский муравей-портной (лат. Oecophylla smaragdina) — вид муравьёв-портных, приспособленных к обитанию на деревьях. ',
    }

d_items = d.items()
d_key = d.keys()
for i in d_key:
    print(i, d.get(i))


@app.route('/animal')
def animal():
    animal = d[random.randint(1, len(d))]
    return render_template("index_animal.html", animal=animal, d=d)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/first')
def rome():
    return render_template("index_first.html")


@app.route('/second')
def rom():
    return render_template("index_second.html")


if __name__ == '__main__':
    app.run(debug=True)
