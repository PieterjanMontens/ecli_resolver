import sys
import logging
from ecli_resolver.util import NoResolverError

logger = logging.getLogger(__name__)

class Faktory:
    @staticmethod
    def getFromCC(cc):
        return getattr(sys.modules[__name__], cc)

    @classmethod
    def getResolver(cls, cc):
        try:
            if issubclass(Faktory.getFromCC(cc), Faktory):
                return Faktory.getFromCC(cc)()
            else:
                logger.info("Not a valid choice -> %s", cc)
                raise RuntimeError
        except AttributeError:
            logger.info("Not a valid resolver -> %s", cc)
            raise RuntimeError

    def resolve(cls, ecli):
        return f"{cls.root}{str(ecli)}"

class AT(Faktory):
    # Austria

    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class BE(Faktory):
    # Belgium
    # The central services of the Federal Public Service Justice  act as national coordinator for Belgium.
    root = "https://juportal.be/content/"

class BG(Faktory):
    # Bulgaria
    root = "https://legalacts.justice.bg/"

class CE(Faktory):
    # Council of Europe

    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class CZ(Faktory):
    # Czech Republic
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class DE(Faktory):
    # Germany
    # Le coordinateur ECLI pour l’Allemagne est l’instance suivante: Bundesamt für Justiz

    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class EE(Faktory):
    root = "https://www.riigiteataja.ee/kohtulahendid/ecli/"

class EL(Faktory):
    # Greece
    def resolve(cls, ecli):
        uri = f"http://www.adjustice.gr/caselaw/ecli?court={ecli.court}&year={ecli.year}&ordnumber={ecli.number}"
        return uri

class ES(Faktory):
    # Spain
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class EP(Faktory):
    # European patent organisation
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class EU(Faktory):
    # European case-law
    # nor EUR-Lex nor CURIA provide a ECLI resolver. Bad luck !
    root = "https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=ecli:"

    #https://e-justice.europa.eu/ecli/beta/EU001/lang/ECLI:EU:C:2016:652.html?index=0&text=EU%3AC%3A1997%3A58&ascending=false&lang=en

class FI(Faktory):
    # Finland
    root = "https://data.finlex.fi/oikeus/"

class FR(Faktory):
    # France
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class HR(Faktory):
    # Croatia
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class IT(Faktory):
    # Italy
    def resolve(cls, ecli):
        if ecli.court == 'COST':
            return f"https://www.cortecostituzionale.it/actionSchedaPronuncia.do?param_ecli={ecli}"

        raise NoResolverError('If possible, not yet implemented')

class LV(Faktory):
    # Latvia
    root = "https://manas.tiesas.lv/eTiesasMvc/eclinolemumi/"

class MT(Faktory):
    # Malta
    def resolve(cls, ecli):
        uri = f"https://ecourts.gov.mt/onlineservices/Judgements/Details?JudgementId=0&CaseJudgementId={ecli.number}"
        return uri

class NL(Faktory):
    # Netherlands
    # The national ECLI coordinator is the Council for the Judiciary (Raad voor de rechtspraak). You can contact the coordinator at the following email address: kennissystemen@rechtspraak.nl
    root = "https://uitspraken.rechtspraak.nl/#!/details?id="

class PT(Faktory):
    # Portugal
    root = "https://jurisprudencia.csm.org.pt/ecli/"

class RO(Faktory):
    # Romania
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class SI(Faktory):
    # Slovenia
    def resolve(cls, ecli):
        raise NoResolverError('If possible, not yet implemented')

class SK(Faktory):
    # Slovakia
    root = "https://www.slov-lex.sk/vseobecne-sudy-sr/-/ecli/"
    def resolve(self, ecli):
            converted = str(ecli).replace(':','-').replace('.','_')
            return f"{self.root}{converted}"
