from flask import render_template, redirect
import logging
from ecli_resolver import app
import ecli_resolver.resolvers as resolvers
from ecli_resolver.resolver import Faktory
from ecli_resolver.util import NoResolverError

logger = logging.getLogger(__name__)


@app.route('/')
def home():
    """Landing page."""
    tests = [
        # Belgium
        'ECLI:BE:CASS:1999:ARR.19990427.9',
        # Bulgaria
        'ECLI:BG:DC530:2017:20160100630.001',
        # Greece
        "ECLI:EL:COS:2019:0716A1319.15E1049",
        # Estonia
        'ECLI:EE:RK:1995:3.2.1.23.95.92',
        # EU
        'ECLI:EU:C:1997:58',
        'ECLI:EU:C:2016:652',
        # Finland
        'ECLI:FI:KKO:2011:43',
        # Italy - Const
        'ECLI:IT:COST:1962:46',
        # Latvia
        'ECLI:LV:AT:2019:0226.A420227714.4.S',
        # Malta
        'ECLI:MT:AKI:2020:119835',
        # Netherlands
        'ECLI:NL:RBZWB:2019:3544',
        # Portugal
        'ECLI:PT:STJ:2022:1167.15.9T9GRD.C1.S1.F7',
        # Slovakia
        'ECLI:SK:NSSR:2018:6017200055.1',
    ]
    other = [
        # AT
        "ECLI:AT:VWGH:2020:RA2020020033.L01",
        # EP
        'ECLI:EP:BA:2002:D000300.20020503',
        # Council of Europe
        'ECLI:CE:ECHR:JJJJ:MMTTabc123456789',
        # CZ
        'ECLI:CZ:NS:2012:6.TDO.1416.2012.1',
        # Spain
        'ECLI:ES:AN:2014:2389',
        # Germany
        'ECLI:DE:BGH:2022:131222UVIZR54.21.0',
        'ECLI:DE:BVerwG:2002:170402U9CN1.01.0',
        # France
        'ECLI:FR:CESSR:2013:355099.20130301',
        'ECLI:FR:CCASS:2013:CR00710',
        'ECLI:FR:CC:2012:2012.270.QPC',
        # Croatia
        'ECLI:HR:VSRH:2004:6455',
        # Italy - other
        'ECLI:IT:CASS:2015:5513CIV',
        'ECLI:IT:TRGABZ:2019:178SENT',
        # Slovenia
        'ECLI:SI:VSRS:2009:IV.IPS.36.2009.A',

    ]
    new = [
        "ECLI:DK:HJR:2023:BS0000003218",
        "ECLI:LU:TADM:2023:46266",
    ]
    return render_template(
        'index.html',
        title="ECLI Resolver",
        description="ECLI Resolver / forwarder",
        tests = tests,
        other = other,
        new = new,
    )

@app.get("/<ecli:ecli>")
def resolve_cc(ecli):

    try:
        cl = Faktory.getResolver(ecli.cc)
        uri = cl.resolve(ecli)
        logger.debug("Resolving ecli %s -> %s", ecli, uri)
        return redirect(uri, code=302)
    except NoResolverError as e:
        return f"404: {str(e)}", 404
    except Exception as e:
        logger.exception(e)
        return 'Error!', 500

@app.get("/<ecli>")
def resolve(ecli):
    logger.debug("Resolving %s", ecli)

    uri = be.resolve(ecli)

    return redirect(uri, code=302)
