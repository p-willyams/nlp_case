# %%
import pandas as pd
import re

df = pd.read_csv("../../data/raw/base_vagas.csv")


def map_seniority(title):
    if not isinstance(title, str):
        return "unknown"

    title = title.lower()
    intern_pattern = r"(intern|trainee)"
    junior_pattern = (
        r"(junior|jr|entry\b|entrylevel|entry-level|beginner|firstlevel|first-level)"
    )
    mid_pattern = (
        r"(mid|midlevel|mid-level|associate|assc|semi-senior|semisenior|intermediate)"
    )
    senior_pattern = r"(senior|sr|principal|expert|staff|lead\s*senior)"
    manager_pattern = r"(manager|supervisor|supervision|superintendent|cto|cmo|head)"
    lead_pattern = r"(lead|technicallead|techlead|teamlead|leadership|head)"

    if re.search(intern_pattern, title, flags=re.I):
        return "intern"
    if re.search(junior_pattern, title, flags=re.I):
        return "junior"
    if re.search(senior_pattern, title, flags=re.I):
        return "senior"
    if re.search(manager_pattern, title, flags=re.I):
        return "manager"
    if re.search(lead_pattern, title, flags=re.I):
        return "lead"
    if re.search(mid_pattern, title, flags=re.I):
        return "mid_level"

    if re.search(r"(\d+\s*years?\s*experience)", title):
        return "mid_level"
    return "unknown"


df["senioridade"] = df["titulo"].apply(map_seniority)


df["len_char_titulo"] = df["titulo"].str.len()

df["len_word_titulo"] = df["titulo"].str.split().str.len()

df["tit_caps_ratio"] = df["titulo"].apply(
    lambda x: (
        sum(1 for c in str(x) if c.isupper()) / len(str(x)) if len(str(x)) > 0 else 0
    )
)


df["len_char_descricao"] = df["descricao"].str.len()

df["len_word_descricao"] = df["descricao"].str.split().str.len()

# Calcula o número de frases na descrição (separadas por ".")
df["desc_n_frases"] = df["descricao"].apply(
    lambda x: len([s for s in str(x).split(".") if s.strip()])
)

df["desc_n_paragrafos"] = df["descricao"].apply(
    lambda x: len([p for p in str(x).split("\n") if p.strip()])
)

df["desc_n_bullets"] = df["descricao"].apply(
    lambda x: len(re.findall(r"^(?:\s*)([•\-*])\s+", str(x), flags=re.MULTILINE))
)

df["desc_menciona_bonus"] = df["descricao"].str.contains(
    r"bonus|commission|ote|benefits|pension|car allowance|share", case=False, na=False
)

df["desc_menciona_experiencia"] = df["descricao"].str.contains(
    r"experience|years", case=False, na=False
)

df["desc_menciona_formacao"] = df["descricao"].str.contains(
    r"degree|msc|phd|chartered|qualified|cima|aca|acca", case=False, na=False
)


macro_regions = {
    "London": [
        "London",
        "Central London",
        "West London",
        "North London",
        "South London",
        "East London",
        "South East London",
        "South West London",
        "North West London",
        "North East London",
        "The City",
        "Camden Town",
        "Earls Court",
        "Westminster",
        "Kensington",
        "Islington",
        "Brixton",
        "Walthamstow",
        "Holloway",
        "Chelsea",
        "Mayfair",
        "Docklands",
        "Canary Wharf",
        "Whitechapel",
        "Ealing",
        "Fulham",
        "Kilburn",
        "Clapham",
        "Greenwich",
        "Acton",
        "Barbican",
        "Paddington",
        "Battersea",
        "Shoreditch",
        "Vauxhall",
        "Wembley",
        "Edgware",
        "Fitzrovia",
        "Chiswick",
        "Finchley",
        "Hampstead",
        "Marylebone",
        "Soho",
        "Romford",
        "Enfield",
        "Barnet",
        "Hackney",
        "Waltham Forest",
        "Lewisham",
        "Bromley",
        "Croydon",
        "Bexley",
        "Lambeth",
        "Southwark",
        "Haringey",
        "Harrow",
        "Brent",
        "Camden",
        "Hillingdon",
        "Tower Hamlets",
        "Hounslow",
        "Sutton",
        "Kingston",
        "Richmond",
        "Redbridge",
        "Newham",
        "Merton",
        "Wandsworth",
        "Greenford",
        "Woolwich",
        "Ilford",
        "Leyton",
        "Southall",
        "Putney",
        "Mill Hill",
        "Ruislip",
        "Chingford",
        "Upminster",
        "Surrey Quays",
        "Raynes Park",
        "Cricklewood",
        "Bromley-By-Bow",
        "Earls Barton",
        "Kennington",
        "Knightsbridge",
        "White City",
        "Swiss Cottage",
        "West Norwood",
        "Burntwood",
        "Stoke Newington",
    ],
    "South East England": [
        "South East",
        "Hampshire",
        "Berkshire",
        "Oxford",
        "Oxfordshire",
        "Buckinghamshire",
        "Surrey",
        "Kent",
        "West Sussex",
        "East Sussex",
        "Isle Of Wight",
        "Reading",
        "Brighton",
        "Maidstone",
        "Guildford",
        "Crawley",
        "Chichester",
        "Woking",
        "Winchester",
        "Slough",
        "Bracknell",
        "Aylesbury",
        "Milton Keynes",
        "Banbury",
        "Basingstoke",
        "Ashford",
        "Farnborough",
        "Wokingham",
        "Redhill",
        "Dover",
        "Dartford",
        "Epsom",
        "Leatherhead",
        "Godalming",
        "Chatham",
        "Bromley",
        "Tunbridge Wells",
        "Haywards Heath",
        "East Grinstead",
        "Windsor",
        "Worthing",
        "Bexhill-On-Sea",
        "Hastings",
        "Gatwick",
        "Horsham",
        "Eastbourne",
        "Sevenoaks",
        "Reigate",
        "Croydon",
        "Egham",
        "Camberley",
        "Twickenham",
        "Crawley",
        "Haywards Heath",
    ],
    "South West England": [
        "South West",
        "Devon",
        "Cornwall",
        "Somerset",
        "Dorset",
        "Bristol",
        "Bath",
        "Wiltshire",
        "Gloucestershire",
        "Swindon",
        "Torquay",
        "Yeovil",
        "Taunton",
        "Exeter",
        "Cheltenham",
        "Chippenham",
        "Weston-Super-Mare",
        "Plymouth",
        "Poole",
        "Bournemouth",
        "Truro",
        "Barnstaple",
        "Penzance",
        "Salisbury",
        "Tewkesbury",
        "Weymouth",
        "Stroud",
        "Nailsea",
    ],
    "East of England": [
        "East Anglia",
        "Norfolk",
        "Suffolk",
        "Cambridgeshire",
        "Hertfordshire",
        "Bedfordshire",
        "Essex",
        "Colchester",
        "Ipswich",
        "Cambridge",
        "Chelmsford",
        "Bury St. Edmunds",
        "St. Albans",
        "Stevenage",
        "Luton",
        "Harlow",
        "Hatfield",
        "Basildon",
        "Southend-On-Sea",
        "Peterborough",
        "Huntingdon",
        "Hemel Hempstead",
        "Watford",
        "Bedford",
        "Braintree",
        "Brentwood",
        "Bishops Stortford",
        "Witham",
    ],
    "East Midlands": [
        "East Midlands",
        "Nottingham",
        "Nottinghamshire",
        "Leicester",
        "Leicestershire",
        "Derby",
        "Derbyshire",
        "Northampton",
        "Northamptonshire",
        "Lincolnshire",
        "Boston",
        "Loughborough",
        "Corby",
        "Grantham",
        "Beeston",
        "Chesterfield",
        "Kettering",
        "Rutland",
        "Worksop",
        "Sleaford",
        "Brackley",
    ],
    "West Midlands": [
        "West Midlands",
        "Birmingham",
        "Coventry",
        "Wolverhampton",
        "Shropshire",
        "Worcestershire",
        "Herefordshire",
        "Staffordshire",
        "Solihull",
        "Dudley",
        "Walsall",
        "Telford",
        "Stoke-On-Trent",
        "West Bromwich",
        "Tamworth",
        "Leamington Spa",
        "Rugby",
        "Kidderminster",
        "Cannock",
    ],
    "Yorkshire and the Humber": [
        "Yorkshire and Humberside",
        "Yorkshire",
        "Humber",
        "Leeds",
        "Sheffield",
        "York",
        "Bradford",
        "Hull",
        "Rotherham",
        "Doncaster",
        "Wakefield",
        "Harrogate",
        "Huddersfield",
        "Halifax",
        "Barnsley",
        "Scarborough",
        "Hull",
        "East Riding",
        "Grimsby",
        "North Yorkshire",
        "South Yorkshire",
        "West Yorkshire",
        "Cleethorpes",
        "Beverley",
    ],
    "North West England": [
        "North West",
        "Manchester",
        "Lancashire",
        "Liverpool",
        "Merseyside",
        "Blackpool",
        "Bolton",
        "Preston",
        "Stockport",
        "Oldham",
        "Warrington",
        "Salford",
        "Wigan",
        "Rochdale",
        "Chorley",
        "Burnley",
        "Birkenhead",
        "Wirral",
        "Barrow-In-Furness",
        "Greater Manchester",
        "Cumbria",
    ],
    "North East England": [
        "North East",
        "Newcastle",
        "Tyne & Wear",
        "Durham",
        "Sunderland",
        "Gateshead",
        "Darlington",
        "Middlesbrough",
        "Hartlepool",
        "Stockton-On-Tees",
        "Northumberland",
        "Redcar",
        "Cleveland",
        "North Shields",
        "Berwick-Upon-Tweed",
    ],
    "Wales": [
        "Wales",
        "Cardiff",
        "Newport",
        "Swansea",
        "Bridgend",
        "Wrexham",
        "Flintshire",
        "Monmouthshire",
        "Powys",
        "Pembrokeshire",
        "Carmarthenshire",
        "Ceredigion",
        "Gwynedd",
        "Neath Port Talbot",
        "Rhondda Cynon Taff",
        "Merthyr Tydfil",
        "Denbighshire",
        "Anglesey",
        "Vale of Glamorgan",
        "Blaenau Gwent",
        "Conwy",
    ],
    "Scotland": [
        "Scotland",
        "Edinburgh",
        "Glasgow",
        "Aberdeen",
        "Dundee",
        "Stirling",
        "Highlands",
        "Fife",
        "Argyll & Bute",
        "Dumfries & Galloway",
        "Clackmannanshire",
        "East Lothian",
        "East Ayrshire",
        "East Dunbartonshire",
        "East Renfrewshire",
        "Falkirk",
        "Inverclyde",
        "Midlothian",
        "Moray",
        "North Ayrshire",
        "North Lanarkshire",
        "Perth & Kinross",
        "Renfrewshire",
        "Scottish Borders",
        "South Ayrshire",
        "South Lanarkshire",
        "West Dunbartonshire",
        "West Lothian",
        "Shetland",
        "Orkney",
        "Western Isles",
    ],
    "Northern Ireland": [
        "Northern Ireland",
        "Belfast",
        "Antrim",
        "Armagh",
        "Londonderry",
        "Derry",
        "Fermanagh",
        "Tyrone",
        "Down",
        "Lisburn",
        "Newry",
        "Magherafelt",
        "Bangor",
        "County Antrim",
        "County Down",
    ],
    "Islands": [
        "Isle Of Wight",
        "Jersey",
        "Guernsey",
        "Channel Islands",
        "Isle of Man",
        "Isle Of Skye",
        "Isle Of Arran",
        "Isle Of Harris",
        "Isle Of Lewis",
        "Isle Of Barra",
        "Isle Of North Uist",
        "Isle Of South Uist",
        "Isle Of Colonsay",
    ],
    "Other": [],
}


def assign_macro_region(location):
    loc = str(location).strip().lower()
    loc_clean = loc.replace("united kingdom", "").replace("uk", "")
    for region, patterns in macro_regions.items():
        for pattern in patterns:
            p = pattern.lower()
            if loc_clean == p or loc_clean.startswith(p):
                return region
            if f" {p} " in f" {loc_clean} ":
                return region
            if p in loc_clean and len(p) >= 5:
                return region
    if re.search(r"\blondon\b", loc):
        return "London"
    if re.search(r"\bcardiff\b", loc):
        return "Wales"
    if re.search(r"\bglasgow|edinburgh|aberdeen|dundee\b", loc):
        return "Scotland"
    if re.search(r"\bbelfast|lisburn|newry|derry|londonderry\b", loc):
        return "Northern Ireland"
    if re.search(r"\bbirmingham|coventry|wolverhampton\b", loc):
        return "West Midlands"
    if re.search(r"\bmanchester|liverpool|salford|blackpool\b", loc):
        return "North West England"
    if re.search(r"\bleeds|sheffield|york|bradford\b", loc):
        return "Yorkshire and the Humber"
    if re.search(r"\bnottingham|leicester|derby\b", loc):
        return "East Midlands"
    if re.search(r"\bnorfolk|suffolk|cambridge|hertford|essex\b", loc):
        return "East of England"
    if re.search(r"\bokay\b", loc):
        return "Other"
    if "isle" in loc or "jersey" in loc or "guernsey" in loc or "orkney" in loc:
        return "Islands"
    return "Other"


df["macro_regiao"] = df["localizacao"].apply(assign_macro_region)

df.to_csv("../../data/processed/base_vagas.csv", index=False)
