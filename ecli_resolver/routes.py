from flask import render_template, redirect
import logging
from ecli_resolver import  app
from ecli_resolver.resolvers import be

logger = logging.getLogger(__name__)


@app.route('/')
def home():
    """Landing page."""
    tests = [
        'ECLI:BE:CASS:1999:ARR.19990427.9',
    ]
    return render_template(
        'index.html',
        title="ECLI Resolver",
        description="ECLI Resolver / forwarder",
        tests = tests
    )

@app.get("/<ecli>")
def resolve(ecli):
    logger.debug("Resolving %s", ecli)

    uri = be.resolve(ecli)

    return redirect(uri, code=302)
