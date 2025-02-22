import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils
import pkg_resources

sys.path.append(os.getcwd())

home_dir = os.getcwd()
#master_url = 'http://127.0.0.1:8000'
master_url = 'https://daveparillo.github.io/cisc187-reader/'
master_app = 'cisc187-reader'
serving_dir = "./docs"
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir=serving_dir,
        sourcedir="_sources",
        outdir=serving_dir,
        confdir=".",
        project_name = "cisc187-reader",
        template_args={'course_id': 'cisc187-reader',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'false',
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'false',
                       'allow_pairs': 'false',
                       'dynamic_pages': False,
                       'minimal_outside_links': True,
                       'python3': 'true',
                       'dburl': '',
                       'default_ac_lang': 'cpp',
                       'basecourse': 'cisc187-reader',
                       'jobe_server': 'https://red-voice-1370.fly.dev/http://jobe2.cosc.canterbury.ac.nz',
                       'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                       'proxy_uri_files': '/jobe/index.php/restapi/files/'
                       }
        )
    )

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBUSER etc. are in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.
