from flask_assets import Bundle, Environment
from sinapse.buildup import app


bundles = {

    'js': Bundle(
        'js/vendor/d3.min.js',
        'js/vendor/neo4jd3.min.js',
        'js/main.js',
    ),
    'css': Bundle(
        'css/font-awesome.min.css', # Font Awesome não pode ficar em 'vendor/' porque se referencia às fontes como '../fonts/'
        'css/vendor/neo4jd3.min.css',
        'css/main.css',
        'css/busca.css',
        'css/sidebarRight.css',
    ),
}


assets = Environment(app)

assets.register(bundles)
