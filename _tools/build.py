"""Generate the static Davies Kelly site (plain HTML) from the copy in the senior build specification (4 Nov 2026).
Run from the repo root:  python3 -I _tools/build.py
Output is committed static HTML; GitHub Pages serves it with no build step.
"""
import json, os, html, datetime

SITE = "https://davieskelly.com"
import hashlib as _h
INLINE_CSS = open("assets/js/vendor/lenis.css").read().replace("\n", "") + open("assets/css/site.css").read().replace("\n", "") + ".hero-media{background:#173E3F url(data:image/jpeg;base64," + open("_tools/hero_lqip.txt").read().strip() + ") center/cover no-repeat}"
ASSET_V = _h.md5((open("assets/css/site.css","rb").read()+open("assets/js/site.js","rb").read())).hexdigest()[:8]
TODAY = "2026-11-04"
ROOS_TEL, ROOS_TEL_D, ROOS_MAIL = "+971558695337", "+971 (0)55 869 5337", "michael.roos@davieskelly.com"
JAMIE_TEL, JAMIE_TEL_D, JAMIE_MAIL = "+971585693416", "+971 (0)58 569 3416", "jamie.shafto@davieskelly.com"
ENQ_TO = f"{ROOS_MAIL},{JAMIE_MAIL}"  # until F3 confirms an enquiries inbox
ADDRESS = "48 Burj Gate Tower, Sheikh Zayed Road, Downtown, PO Box 116171, Dubai, UAE"
MAPS = "https://www.google.com/maps/search/?api=1&query=Burj+Gate+Tower+Sheikh+Zayed+Road+Dubai"
LINKEDIN = "https://www.linkedin.com/company/davies-kelly/"
e = html.escape


def ph(pid, text):
    return ""


ICON = {
    "call": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.5 7.4L3 20.5l1.6-5.3A8.4 8.4 0 1 1 21 11.5z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
}

NAV = [("Experts", "/experts/"), ("Services", "/services/"), ("Sectors", "/sectors/"), ("Experience", "/experience/"), ("Independence", "/independence/"), ("About", "/about/")]

# ---------------------------------------------------------------- people (spec E)
PEOPLE = {
    "michael-roos": dict(
        name="Michael Roos", honorific="", post="BSc (Hons), LLM, MCIArb",
        role="Founding Partner, Testifying Quantum Expert", role_ph="R1", city="Dubai", testifying=True,
        tel=ROOS_TEL, tel_d=ROOS_TEL_D, tel_ph="R15", mail=ROOS_MAIL, wa_ph="R15", linkedin_ph="R9",
        card_line="Testifying quantum expert; LLM in Construction Law, Arbitration and Adjudication.",
        alt="Michael Roos, Founding Partner, Davies Kelly",
        title="Michael Roos – Quantum Expert, Dubai | Davies Kelly",
        desc="Michael Roos, founding partner of Davies Kelly, is a testifying quantum expert who has given written and oral testimony in construction disputes.",
        summary=f"Michael Roos is a founding partner of Davies Kelly and a testifying quantum expert with around 20 years in the construction industry. He has been appointed as lead quantum expert in international arbitration, court proceedings, adjudication and a pre-arbitral expert procedure, and has given written and oral testimony. He started in construction as a labourer at 16 and worked as a foreman, site manager, quantity surveyor and project manager before moving into disputes.",
        highlights=[
            "Lead quantum expert in arbitrations on process plants, oil and gas, desalination, hospitality and infrastructure projects in the Gulf and North Africa.",
            f"Written and oral testimony as quantum expert.",
            "LLM in Construction Law, Arbitration and Adjudication; Member of the Chartered Institute of Arbitrators.",
            f"Commercial team of the Engineer’s Representative on a USD 5.5bn railway project in Saudi Arabia, managing twelve quantity surveyors.",
        ],
        evidence=[
            "Role: party-appointed quantum expert, appointed by main contractors, subcontractors and developers.",
            f"Forums: international arbitration; court proceedings (Scotland); adjudication (England); a non-binding expert procedure before arbitration.",
            "Evidence: expert reports and joint statements; written and oral testimony.",
        ],
        experience=[
            "Lead quantum expert on claims at phosphate processing facilities in North Africa: first in a non-binding expert procedure, where he gave written and oral testimony, and then in the arbitration that followed, which settled before the hearing. Issues: prolongation, disruption and productivity loss, head office overheads, variations and subcontractor claims.",
            "Quantum expert for a main contractor in an arbitration with its subcontractor on an LPG extraction and fractionation plant in the Gulf: prolongation, disruption, variations and head office overheads.",
            "Quantum expert in an arbitration on a landmark hotel in the UAE: variations, prolongation and disruption across MEP packages, and alleged scope creep.",
            "Quantum expert for a main contractor in an arbitration on a desalination plant in Saudi Arabia: contract balance, retention, additional man-hours, performance bonds, liquidated damages, non-compliant work and defects.",
            "Quantum expert for a subcontractor in an arbitration on an oil and gas process plant in the UAE: prolongation, disruption and idle time.",
            f"Quantum expert for a developer in court proceedings on an office refurbishment in Scotland, and in an adjudication on a retirement complex in England.",
            "Early merits and quantum note for a litigation funder in the UAE, with sensitivity ranges and an assessment of whether the documents were sufficient.",
            "Assistant to quantum experts on airport MEP and systems disputes in Qatar, the UAE and Oman, and on energy disputes in Saudi Arabia, Abu Dhabi and Egypt.",
        ],
        expertise=["Prolongation", "Disruption and productivity loss", "Measured mile", "Head office overheads", "Variations", "Measured work and re-measurement", "Preliminaries thickening", "Subcontractor claims", "Liquidated damages", "Performance bonds and retention", "Defects counterclaims", "Late payment", "Final accounts", "First-principles valuation", "Funder merits notes", "Contract risk review"],
        sectors=["Aviation", "Oil and gas", "Rail", "Residential complexes", "Marine infrastructure", "Retail", "Hospitality", "Healthcare", "Infrastructure", "Water desalination"],
        regions="UK, Europe, the Middle East and North Africa. Countries: Saudi Arabia, UAE, Qatar, Oman, Morocco, Egypt, United Kingdom and Denmark.",
        contracts=f"FIDIC",
        career=["Davies Kelly, Founding Partner and Testifying Expert Witness, 2020 to date", "Berkeley Research Group, Senior Managing Consultant, 2018 to 2020", "Arcadis (formerly EC Harris), Senior Consultant, 2015 to 2018", "Engineer’s Representative joint venture (Louis Berger, Canarail, Systra, Khatib Alami), Quantity Surveyor, 2014 to 2015", "Veitchi Group, Project QS and Commercial Manager, 2012 to 2014", "Earlier: project manager and quantity surveyor roles in Scotland and Denmark, and site roles from labourer to site manager"],
        quals=["LLM, Construction Law, Arbitration and Adjudication, Robert Gordon University", "BSc (Hons), Quantity Surveying, Glasgow Caledonian University"],
        members=["Member, Chartered Institute of Arbitrators (MCIArb)", "Member, Society of Construction Law"],
        languages_ph="R8", speaking_ph="R19", cv_ph="R10",
        ld=dict(alumni=["Robert Gordon University", "Glasgow Caledonian University"], creds=[("degree", "LLM, Construction Law, Arbitration and Adjudication"), ("degree", "BSc (Hons), Quantity Surveying")], member=["Chartered Institute of Arbitrators", "Society of Construction Law"], knows=["Construction quantum", "Prolongation", "Disruption", "Head office overheads", "Variations", "FIDIC"]),
    ),
    "jamie-shafto": dict(
        name="Jamie Shafto", honorific="", post="BSc Construction Management",
        role="Founding Partner, Testifying Delay Expert", role_ph="J1", city="Dubai", testifying=True,
        tel=JAMIE_TEL, tel_d=JAMIE_TEL_D, tel_ph="J15", mail=JAMIE_MAIL, wa_ph="J15", linkedin_ph="J10",
        card_line="Testifying delay expert; over 25 years in construction and disputes.",
        alt="Jamie Shafto, Founding Partner, Davies Kelly",
        title="Jamie Shafto – Delay Expert, Dubai | Davies Kelly",
        desc="Jamie Shafto, founding partner of Davies Kelly, is a testifying delay expert cross-examined by King’s Counsel in ICC and DIAC arbitrations.",
        summary=f"Jamie Shafto is a founding partner of Davies Kelly and a testifying delay expert with over 25 years’ experience in dispute resolution and the delivery of complex construction projects. He is regularly appointed in international and domestic arbitrations and has given written and oral evidence under cross-examination by King’s Counsel, barristers and lawyers. Before turning to disputes he planned and programmed major projects in London and the Gulf, from airports and hospitals to towers and rail.",
        highlights=[
            "Delay expert in ICC and DIAC arbitrations on oil and gas, power, hospitality, healthcare, transport and aviation projects.",
            "Oral evidence under cross-examination by King’s Counsel.",
            "Independent determinations of extension of time claims and third-party reviews of contractors’ delay claims.",
            f"Seminars for lawyers, contractors and consultants on delay, contracts and project governance.",
        ],
        evidence=[
            "Role: party-appointed delay expert.",
            "Forums: arbitration under the ICC and DIAC rules; ICC expert determination (expert advice).",
            "Evidence: independent delay analysis, expert reports and joint statements; oral evidence under cross-examination by King’s Counsel and by counsel.",
        ],
        experience=[
            "Delay expert in an ICC arbitration between an EPC contractor and its subcontractor on an LPG extraction and fractionation plant in the Gulf, covering two subcontracts. Delay analysis, expert reports, joint statements and oral evidence under cross-examination by King’s Counsel.",
            "Delay expert in a DIAC arbitration between an owner and its main contractor on a hospital in the UAE. Oral evidence under cross-examination by King’s Counsel.",
            "Delay expert in an ICC arbitration between an EPC contractor and its civil subcontractor on a solar power plant in the Middle East. Oral evidence under cross-examination.",
            "Delay expert in an ICC arbitration between a main contractor and a specialist systems subcontractor on an international airport in the Gulf. Oral evidence under cross-examination.",
            "Delay expert in two arbitrations, one ICC and one DIAC, between an EPC contractor and subcontractors on a crude oil refinery in the UAE.",
            "Delay expert in DIAC arbitrations on a landmark hotel and on ancillary buildings for a transit system in the UAE.",
            "Expert advice in an ICC expert determination between employer and contractor on phosphate plants in North Africa.",
            "Independent reviews of contractors’ delay claims and engineer’s determinations for an owner on a commercial district development in Saudi Arabia.",
        ],
        expertise=["Delay expert witness", "Arbitration", "Forensic delay analysis", "Disruption analysis", "Delay claim preparation and defence", "Determination of delay claims", "Progress monitoring and reporting", "Master planning and development management", "Construction and tender planning"],
        sectors=["Oil and gas", "Rail", "Infrastructure", "Process plants", "Sewage treatment", "Data centres", "Retail", "High-rise commercial and residential", "Mixed-use developments", "Hospitality", "Healthcare", "Aviation", "Highways"],
        regions="UK and MENA. Projects also in Kazakhstan, Israel, Finland, Germany, Denmark, Turkey, Iraq and Libya.",
        methods="",
        contracts="",
        career=["Davies Kelly (Founding Partner)", "Berkeley Research Group", "Navigant Consulting (now Ankura)", "Arcadis (formerly EC Harris)", "Bovis Lend Lease", "ALEC", "Osoul", "SCS", "Kele Contracting", "First Line Consultancy", "ISG plc", "Bouygues UK", "Structure Tone UK"],
        career_ph=("J16", "employment dates"),
        quals=[f"BSc in Construction Management", "Higher National Certificate in Building Studies", "National Certificate in Building Studies"],
        members_ph="J4", languages_ph="J9", cv_ph="J12",
        ld=dict(alumni=[], creds=[("degree", "BSc Construction Management"), ("certificate", "Higher National Certificate in Building Studies"), ("certificate", "National Certificate in Building Studies")], member=[], knows=["Delay analysis", "Forensic delay analysis", "Disruption analysis", "Extension of time", "International arbitration"]),
    ),
    "stephen-john": dict(
        name="Stephen M John", honorific="Eur Ing", post="BEng (Hons), MBA, LLM, CEng, FICE, FCIArb, MCIHT",
        role="Partner, Engineering and Contracts Expert", role_ph=None, role_text="Partner, Engineering and Contracts Expert", city=None, city_ph=("S3", "United Kingdom"), testifying=True,
        tel="+447891784891", tel_d="+44 (0)7891 784 891", tel_ph="S3", mail=None, mail_ph="S3", wa_ph=None, linkedin_ph="S3",
        card_line="Chartered civil engineer, FICE and FCIArb; experienced testifying expert.",
        alt="Stephen M John, Davies Kelly",
        title="Stephen M John – Engineering Expert | Davies Kelly",
        desc="Eur Ing Stephen M John is a chartered civil engineer, FICE and FCIArb, giving independent technical and contract evidence in construction disputes.",
        summary=f"Stephen John is a chartered civil engineer and registered European Engineer with more than 40 years of practice, a Fellow of the Institution of Civil Engineers and of the Chartered Institute of Arbitrators, and an experienced testifying expert. He gives independent evidence on engineering, contract administration and claims, and has been cross-examined in the UK High Court and in arbitration in the DIFC, the ICDR in London and other seats. He has worked on four continents.",
        highlights=[
            "Technical expert witness in four arbitrations on works in Qatar for a major international sporting event.",
            "Technical expert in a DIAC arbitration on post-tensioning of eleven high-rise tower blocks in Dubai.",
            "FIDIC contract administration and claims expert in a high-value airport arbitration in the Middle East (appointed 2021).",
            "Owner’s contracts manager on LNG projects in Australia and the UK.",
        ],
        evidence=[
            "Roles: independent expert witness; technical expert; contract administration and claims expert.",
            f"Forums: UK High Court; arbitration in the DIFC, the ICDR London, DIAC and other seats.",
            "Training: Bond Solon expert witness training; Advanced Professional Certificate in Expert Evidence (Legal Experience Training, London).",
        ],
        experience=[
            "Technical expert witness in four arbitrations on works in Qatar for a major international sporting event.",
            "Technical expert in a DIAC arbitration about the post-tensioning of eleven tower blocks in Dubai.",
            "FIDIC contract administration and claims expert in a high-value airport arbitration in the Middle East.",
            f"Expert in arbitrations on a waterfront development in the Gulf and on slip-formed LNG tanks in Australia, and in High Court proceedings on the insolvency of a UK marina construction project.",
            f"Adviser to the employer and its representative at contested FIDIC dispute adjudication board hearings on a 28 km hard-rock water tunnel in South Asia. The board accepted the employer’s defence and rejected the contractor’s claims.",
            "Brought in by the funders to recover two wastewater treatment plants and networks in South Asia. He recovered contract administration, managed the call on the performance bond when the contractor became insolvent, prepared for arbitration and helped reach a negotiated settlement.",
            "Dispute advice and representation for the employer on a 6 × 75 MW hydro turbine refurbishment in Eastern Europe.",
        ],
        tribunal=[
            "Technical arbitrator on three-member international tribunals, including a pipeline dispute in Oman.",
            "Construction adjudicator listed on the ICE, CIC and UK Adjudicators panels. Appointments include disputes over a wind farm, a high-speed rail contract, design fees, fibre optics, ground anchors, hotel roofing, an oil storage tank and rail signage.",
            "Expert determiner on a UK land development dispute; DRBF-trained and certified dispute board member; CEDR- and NADR-trained mediator.",
            "Chair of the conduct and complaints panel of a UK professional body.",
            f"Stephen’s tribunal appointments are taken through his own practice and are included in every Davies Kelly conflict check.",
        ],
        expertise=["Design, buildability and value engineering", "Defects", "Replanning and scheduling", "Project recovery", "Cold-eyes reviews", "FIDIC contract administration", "Claims preparation and defence", "Dispute boards (DAB)", "Technical expert evidence"],
        sectors=["Engineering and design", "Construction", "Contract administration and management", "Infrastructure: roads, tunnels, water, airports and ports", "Buildings and structures", "Oil, gas and LNG", "Energy, process and hydro"],
        regions="UK, Middle East and internationally; four continents.",
        contracts="FIDIC",
        career=["Principal, SMJ Professional Services Limited", "Interim contract, claims and disputes lead, Arcadis, Qatar", "Owner’s contracts manager, LNG projects in Australia and the UK", "Director with full technical and P&L responsibility for a national consultancy office (now part of AECOM), seven years", "Professionally qualified 1984"],
        quals=[f"LLM, University of Glamorgan Law School", "MBA (International Business), Cardiff Business School", "BEng (Hons) Civil Engineering, University of Wales School of Engineering", "Chartered Engineer (CEng); Registered European Engineer (Eur Ing)", "Advanced Professional Certificate in Expert Evidence", "ICE Contract Law and Procedure Certificate", "CEDR Foundation Course in Mediation Skills; DRBF dispute board training"],
        members=["Fellow, Institution of Civil Engineers (FICE), since 1996", "Fellow, Chartered Institute of Arbitrators (FCIArb)", "Member, Chartered Institution of Highways and Transportation (MCIHT)"],
        languages_ph="S10", cv_ph="S11",
        ld=dict(alumni=["University of Wales", "Cardiff Business School", "University of Glamorgan"], creds=[("degree", "BEng (Hons) Civil Engineering"), ("degree", "MBA"), ("degree", "LLM"), ("professional", "Chartered Engineer (CEng)")], member=["Institution of Civil Engineers", "Chartered Institute of Arbitrators", "Chartered Institution of Highways and Transportation"], knows=["Civil engineering", "FIDIC contract administration", "Construction defects", "Dispute boards", "Technical expert evidence"]),
    ),
    "michael-whiting": dict(
        name="Michael Whiting", honorific="", post="BSc (Hons) Quantity Surveying · RICS Expert Witness Certificate",
        role="Partner, Quantum Expert", role_ph=None, role_text="Partner, Quantum Expert", city=None, city_ph=("M2", "city shown"), testifying=False,
        tel="+447762124220", tel_d="+44 7762 124220", tel_ph="M6", mail=None, mail_ph="M6", wa_ph="M6", wa="447762124220", linkedin_ph="M7",
        card_line="Quantum and claims consultant supporting our quantum experts with analysis of records, claims and accounts.",
        alt="Michael Whiting, Davies Kelly",
        title="Michael Whiting – Quantum Analysis | Davies Kelly",
        desc="Michael Whiting is a quantum and claims consultant supporting Davies Kelly’s quantum experts with analysis of project records, claims and accounts.",
        summary=f"Michael Whiting is a quantum expert with over 12 years’ experience in construction and engineering, from commercial management on live projects to quantum work in disputes, across the United Kingdom, the Middle East and North Africa. At Davies Kelly he supports the quantum experts with quantum assessment, document review, analysis of project records and report drafting. He began his career at 16 as an apprentice quantity surveyor with Balfour Beatty.",
        highlights=[
            "Quantum analysis supporting appointed experts in arbitrations in North Africa, the UAE and Oman, in court proceedings in Scotland and in a UK adjudication.",
            "Interim disruption claim valued by measured mile for gas export pipelines in Saudi Arabia.",
            "Commercial lead for a main contractor on a £109m, 407-apartment build-to-rent scheme in London, from procurement to final account.",
        ],
        experience=[
            "Quantum analysis for the appointed expert in an arbitration between contractor and subcontractor on phosphate plants in North Africa: prolongation, disruption, measured work, variations, loss of opportunity and head office overheads.",
            "Quantum analysis for the appointed expert in an arbitration between contractor and MEP subcontractor on a luxury hotel in the UAE.",
            "Quantum analysis for the appointed expert in an arbitration on a slaughterhouse and associated infrastructure in Oman: prolongation, disruption, variations, late payment and head office overheads.",
            f"Quantum analysis for the appointed expert in court proceedings in Scotland between a building owner and its architect: remediation and additional works, prolongation, funding and financing, energy and operating costs, and internal management costs.",
            "Interim disruption claim valued by measured mile for a contractor on gas export pipelines in Saudi Arabia, deriving disrupted labour and plant hours by activity.",
            "Reconstruction from first principles of a subcontractor’s account on a London commercial tower: delay, disruption, variations, contra charges, overheads and finance.",
            "Commercial lead on a £109m build-to-rent scheme and lifecycle quantity surveying on a £1bn regeneration scheme in London.",
        ],
        expertise=["Prolongation", "Disruption and productivity", "Measured mile", "Variations", "Loss and expense", "Final accounts", "Payment disputes", "Contra charges", "Liquidated damages", "Retention and interest", "Account reconstruction", "Commercial recovery"],
        sectors=["Energy", "Industrial", "Infrastructure", "Construction", "Residential", "Hospital", "Retail", "Hotel", "Education and PFI"],
        regions="United Kingdom, Middle East, North Africa.",
        contracts="JCT, NEC (including NEC4), FIDIC, PFI and bespoke contracts",
        career=["Avonstowe (UAE), Principal, 2022 to date", "McLaren Construction, London, Commercial Lead, 2019 to 2022", "Balfour Beatty, London, Quantity Surveyor, 2014 to 2019 (joined at 16 as an apprentice)"],
        quals=["BSc (Hons) Quantity Surveying, London South Bank University", f"RICS Expert Witness Certificate", f"LLB (Hons), University of London (expected 2027)", f"Diploma in Forensic Quantum Analysis, College of Contract Management (in progress)"],
        members=["Member, Society of Construction Law"],
        languages_ph="M8", cv_ph="M10",
        ld=dict(alumni=["London South Bank University"], creds=[("degree", "BSc (Hons) Quantity Surveying"), ("certificate", "RICS Expert Witness Certificate")], member=["Society of Construction Law"], knows=["Construction quantum", "Measured mile", "Final accounts", "Loss and expense"]),
    ),
}
ORDER = ["michael-roos", "jamie-shafto", "stephen-john", "michael-whiting"]

BIO = {
    "michael-roos": "Testifying quantum expert with an LLM in construction law, arbitration and adjudication, appointed as lead quantum expert in international arbitration, court, adjudication and a pre-arbitral expert procedure. Started as a labourer at 16 and ran sites before moving into disputes.",
    "jamie-shafto": "Testifying delay expert with over 25 years in construction and disputes, regularly appointed in international arbitration and cross-examined by King’s Counsel. Planned major projects in London and the Gulf before turning to disputes.",
    "stephen-john": "Chartered civil engineer, European Engineer and Fellow of the Chartered Institute of Arbitrators, with more than 40 years of practice on four continents. Cross-examined in the UK High Court and in international arbitration.",
    "michael-whiting": "Quantum and claims consultant with over 12 years from commercial management on live projects to quantum in disputes, across the UK, the Middle East and North Africa. Began at 16 as an apprentice quantity surveyor with Balfour Beatty.",
}
TALK = {
    "michael-roos": "quantum, variations, prolongation and final accounts",
    "jamie-shafto": "delay, extensions of time and disruption",
    "stephen-john": "engineering, defects and contract administration",
    "michael-whiting": "quantum analysis of records, claims and accounts",
}


def first_name(slug):
    return {"stephen-john": "Stephen", "jamie-shafto": "Jamie", "michael-roos": "Michael Roos", "michael-whiting": "Michael Whiting"}[slug]


def team_rotator():
    feats, thumbs, details = [], [], []
    for k, slug in enumerate(ORDER):
        p = PEOPLE[slug]; on = " on" if k == 0 else ""
        feats.append(f'<div class="tr-feature{on}" data-i="{k}">{picture(slug, "92vw", alt=p["alt"], eager=(k == 0))}<span class="tr-name">{e(p["name"])}</span></div>')
        thumbs.append(f'<button type="button" class="tr-thumb{on}" data-i="{k}" aria-label="Show {e(p["name"])}">{picture(slug, "30vw", alt="", eager=True)}<span>{e(first_name(slug).split()[-1] if slug.startswith("michael") else first_name(slug))}</span></button>')
        mail = f'<a class="btn secondary" href="mailto:{p["mail"]}">{ICON["mail"]}Email</a>' if p.get("mail") else f'<a class="btn secondary" href="/contact/">{ICON["mail"]}Email</a>'
        call = f'<a class="btn secondary" href="tel:{p["tel"]}">{ICON["call"]}Call</a>' if p.get("tel") else ""
        details.append(f'<div class="tr-detail{on}" data-i="{k}"><p class="role">{role_html(p)}</p><p class="meta">{e(p["post"])}</p><p class="tr-bio">{e(BIO[slug])}</p><p class="tr-talk"><span>Talk to {e(first_name(slug))} about</span> {e(TALK[slug])}</p><div class="tr-acts"><a class="btn" href="/experts/{slug}/">View profile</a>{mail}{call}</div></div>')
    return f'<div class="team-rot" aria-label="Our experts"><div class="tr-stage">{"".join(feats)}</div><div class="tr-thumbs">{"".join(thumbs)}</div><div class="tr-details" aria-live="polite">{"".join(details)}</div></div>'



def role_html(p):
    if p.get("role") and not p.get("role_ph"):
        return e(p["role"])
    return e(p["role"]) + " " + ph(p["role_ph"], "title") if p.get("role") else ph(p["role_ph"], f"title, e.g. {p['role_text']}")


def city_html(p):
    return e(p["city"]) if p.get("city") else ph(p["city_ph"][0], p["city_ph"][1])


def picture(slug, sizes, cls="", alt="", eager=False, w=528):
    base = f"/assets/img/people/{slug}"
    srcs = "".join(f'<source type="image/{t}" srcset="{base}-160.{t} 160w, {base}-320.{t} 320w, {base}-528.{t} 528w" sizes="{sizes}">' for t in ("avif", "webp"))
    load = '' if eager else ' loading="lazy" decoding="async"'
    return f'<picture>{srcs}<img src="{base}-320.jpg" srcset="{base}-160.jpg 160w, {base}-320.jpg 320w, {base}-528.jpg 528w" sizes="{sizes}" width="{w}" height="{round(w*1.25)}" alt="{e(alt)}"{load}{(" class=" + chr(34) + cls + chr(34)) if cls else ""}></picture>'


# ---------------------------------------------------------------- cases (spec F)
CASES = [
    dict(id="C1", chips=["Quantum", "Delay"], h="Phosphate processing facilities", region="North Africa", forum="Pre-arbitral expert procedure (ICC expert determination), then arbitration", parties="Employer, contractor, subcontractor", role="Lead quantum expert; delay expert advice; quantum analysis support", who=["michael-roos", "jamie-shafto", "michael-whiting"], issues="Prolongation, disruption and productivity loss, head office overheads, variations, subcontractor claims", evid="Written and oral testimony in the expert procedure; the arbitration settled before the hearing", ph="R13"),
    dict(id="C2", chips=["Delay", "Quantum"], h="LPG extraction and fractionation plant", region="Gulf", forum="ICC arbitration", parties="EPC contractor v subcontractor (two subcontracts)", role="Delay expert; quantum expert for the main contractor", who=["jamie-shafto", "michael-roos"], issues="Responsibility for delay, prolongation, disruption, variations, head office overheads", evid="Oral evidence under cross-examination by King’s Counsel (delay)", ph="R13"),
    dict(id="C3", chips=["Delay", "Quantum"], h="Landmark hotel", region="UAE", forum="DIAC arbitration", parties="Subcontractor v main contractor (MEP packages)", role="Delay expert; quantum expert; quantum analysis support", who=["jamie-shafto", "michael-roos", "michael-whiting"], issues="Responsibility for delay; variations, prolongation and disruption across MEP packages; alleged scope creep", evid="Expert reports and a joint statement", ph="R13"),
    dict(id="C4", chips=["Delay"], h="Hospital", region="UAE", forum="DIAC arbitration", parties="Owner v main contractor", role="Delay expert", who=["jamie-shafto"], issues="Responsibility for delay", evid="Expert reports, joint statements; oral evidence under cross-examination by King’s Counsel"),
    dict(id="C5", chips=["Delay"], h="International airport", region="Gulf", forum="ICC arbitration", parties="Main contractor v specialist systems subcontractor", role="Delay expert", who=["jamie-shafto"], issues="Responsibility for delay", evid="Expert reports, joint statements; oral evidence under cross-examination"),
    dict(id="C6", chips=["Delay"], h="Solar power plant", region="Middle East", forum="ICC arbitration", parties="EPC contractor v civil subcontractor", role="Delay expert", who=["jamie-shafto"], issues="Responsibility for delay", evid="Expert reports, joint statements; oral evidence under cross-examination"),
    dict(id="C7", chips=["Delay"], h="Crude oil refinery", region="Gulf", forum="Two arbitrations (ICC and DIAC)", parties="EPC contractor v subcontractors", role="Delay expert", who=["jamie-shafto"], issues="Responsibility for delay", evid="Independent delay analysis and expert reports"),
    dict(id="C8", chips=["Quantum"], h="Desalination plant", region="Gulf", forum="Arbitration", parties="Main contractor (appointing party)", role="Quantum expert", who=["michael-roos"], issues="Contract balance, retention, additional man-hours, performance bonds, liquidated damages, non-compliant work, defects", evid="Expert report"),
    dict(id="C9", chips=["Quantum"], h="Slaughterhouse and associated infrastructure", region="Gulf", forum="Arbitration", parties="Main contractor v employer", role="Quantum expert; quantum analysis support", who=["michael-roos", "michael-whiting"], issues="Prolongation, disruption, variations, head office overheads, late payment", evid="Expert report"),
    dict(id="C10", chips=["Quantum"], h="Office building refurbishment", region="Scotland, UK", forum="Court proceedings", parties="Building owner v architect", role="Quantum expert; quantum analysis support", who=["michael-roos", "michael-whiting"], issues="Remediation and additional works, prolongation, funding and financing, energy and operating costs, internal management costs", evid="Expert report", ph="R17"),
    dict(id="C11", chips=["Technical"], h="Post-tensioned high-rise towers (eleven blocks)", region="UAE", forum="DIAC arbitration", parties="Not stated", role="Technical expert", who=["stephen-john"], issues="Post-tensioning", evid="Expert evidence", ph="S8"),
    dict(id="C12", chips=["Technical"], h="Works for a major international sporting event", region="Qatar", forum="Four arbitrations", parties="Not stated", role="Technical expert witness", who=["stephen-john"], issues="Technical issues", evid="Expert evidence", ph="S8"),
]
ADVISORY = [
    ("A1", "Early merits and quantum note for a litigation funder, UAE, with sensitivity ranges and an assessment of whether the documents were sufficient.", "michael-roos"),
    ("A2", "Independent third-party review of a contractor’s delay claims on a gas pipeline, to inform a decision on arbitration funding (assisting the delay expert).", "jamie-shafto"),
    ("A3", "Pre-action advice on a hospital project, UAE: risk assessment, litigation options and settlement scenarios; the pre-action letter led to settlement.", "michael-roos"),
    ("A4", "Interim disruption claim valued by measured mile for a contractor on gas export pipelines, Saudi Arabia.", "michael-whiting"),
    ("A5", "Employer’s defence at contested FIDIC dispute board hearings on a 28 km hard-rock water tunnel, South Asia; the board rejected the contractor’s claims.", "stephen-john"),
    ("A6", "Consolidated extension of time claims for EPC contractors on power and LPG infrastructure in the UAE.", "jamie-shafto"),
]


def case_rotator(ids):
    cs = [c for i in ids for c in CASES if c["id"] == i]
    cards = "".join(f'<div class="cr-item{" on" if k == 0 else ""}" data-i="{k}" aria-hidden="{"false" if k == 0 else "true"}">{case_card(c)}</div>' for k, c in enumerate(cs))
    dots = "".join(f'<button type="button" class="cr-dot{" on" if k == 0 else ""}" data-i="{k}" aria-label="Show example {k+1} of {len(cs)}"><span></span></button>' for k in range(len(cs)))
    return f'<div class="case-rot" aria-roledescription="carousel" aria-label="Selected experience"><div class="cr-track" aria-live="polite">{cards}</div><div class="cr-dots">{dots}</div></div>'


def case_card(c):
    who = ", ".join(f'<a href="/experts/{s}/">{e(PEOPLE[s]["name"])}</a>' for s in c["who"])
    chips = "".join(f"<span>{e(x)}</span>" for x in c["chips"])
    flag = f"" if c.get("ph") else ""
    return f'''<article class="case"><div class="chips">{chips}</div><h3>{e(c["h"])}</h3>
<dl><div><dt>Region</dt><dd>{e(c["region"])}</dd></div><div><dt>Forum</dt><dd>{e(c["forum"])}</dd></div><div><dt>Parties</dt><dd>{e(c["parties"])}</dd></div><div><dt>Our role</dt><dd>{e(c["role"])}</dd></div></dl>
<p><strong>Experts:</strong> {who}</p><p><strong>Issues:</strong> {e(c["issues"])}</p><p><strong>Evidence:</strong> {e(c["evid"])}{flag}</p></article>'''


# ---------------------------------------------------------------- layout
def header(path):
    def cur(u):
        return ' aria-current="page"' if path.startswith(u) else ""
    desk = "".join(f'<a href="{u}"{cur(u)}>{t}</a>' for t, u in NAV)
    mob = "".join(f'<li><a href="{u}"{cur(u)}>{t}</a></li>' for t, u in NAV)
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="/"><img src="/assets/img/logo/davies-kelly-logo.png" alt="Davies Kelly home" width="681" height="147"></a>
<nav class="nav-desktop" aria-label="Main">{desk}<a class="btn" href="/contact/">Make an enquiry</a></nav>
<a class="menu-btn" href="#footer-nav" aria-expanded="false" aria-controls="site-menu" role="button">{ICON["menu"]}<span>Menu</span></a>
</div></header>
<div class="drawer" id="site-menu" data-lenis-prevent role="dialog" aria-modal="true" aria-label="Site menu" hidden>
<div class="drawer-top"><img src="/assets/img/logo/davies-kelly-logo.png" alt="" width="681" height="147" style="height:32px;width:auto"><button class="menu-btn menu-close" type="button" style="display:inline-flex">{ICON["close"]}<span>Close</span></button></div>
<nav aria-label="Main"><ul>{mob}</ul></nav>
<div class="drawer-actions"><a class="btn block" href="/contact/">Make an enquiry</a>
<a class="btn secondary block" href="tel:{ROOS_TEL}">{ICON["call"]}Call {ROOS_TEL_D}</a>
<a class="btn secondary block" href="mailto:{ROOS_MAIL}">{ICON["mail"]}Email us</a></div></div>'''


def footer():
    experts = "".join(f'<li><a href="/experts/{s}/">{e(PEOPLE[s]["name"])}</a></li>' for s in ORDER)
    return f'''<footer class="site-footer on-navy" id="footer-nav"><div class="wrap">
<div class="foot-cols">
<div><span class="foot-logo"><img src="/assets/img/logo/davies-kelly-logo.png" alt="Davies Kelly" width="681" height="147" loading="lazy"></span>
<p>Independent quantum, delay and technical experts, Dubai.</p><p>{e(ADDRESS)}</p></div>
<div><h2>Contact</h2><ul><li>Michael Roos <a href="tel:{ROOS_TEL}">{ROOS_TEL_D}</a></li><li>Jamie Shafto <a href="tel:{JAMIE_TEL}">{JAMIE_TEL_D}</a></li></ul></div>
<div><h2>Experts</h2><ul>{experts}</ul></div>
<div><h2>Services</h2><ul><li><a href="/pre-contract-advice/">Pre-contract advice</a></li><li><a href="/project-advisory/">Project advisory</a></li><li><a href="/dispute-resolution/">Dispute resolution</a></li><li><a href="/expert-witness-services/">Expert witness services</a></li></ul></div>
<div><h2>Firm</h2><ul><li><a href="/experience/">Experience</a></li><li><a href="/independence/">Independence</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="{LINKEDIN}" rel="noopener noreferrer">LinkedIn</a></li></ul></div>
</div>
<div class="foot-bottom"><p>© 2026 Davies Kelly.</p>
<ul><li><a href="/privacy/">Privacy</a></li><li><a href="/cookies/">Cookies</a></li><li><a href="/terms/">Terms</a></li></ul>
</div>
</div></footer>'''


CTA = '''<section class="cta-band on-navy"><div class="wrap measure"><h2>Discuss a new matter</h2>
<p>Tell us who the parties are and we will check for conflicts before anything else. Please do not send documents until we confirm there is no conflict.</p>
<a class="btn light" href="/contact/">Make an enquiry</a></div></section>'''

CSP = "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self'; connect-src 'self'; form-action 'self' mailto:; base-uri 'self'; object-src 'none'"


def crumbs(items):
    lis, ld = [], []
    for k, (name, url) in enumerate(items):
        cls = ' class="parent"' if k == len(items) - 2 else ""
        lis.append(f'<li{cls}><a href="{url}">{e(name)}</a></li>' if url else f'<li aria-current="page">{e(name)}</li>')
        it = {"@type": "ListItem", "position": k + 1, "name": name}
        if url:
            it["item"] = SITE + url
        ld.append(it)
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>', {"@type": "BreadcrumbList", "itemListElement": ld}


PAGES = []


def page(path, title, desc, body, graph=None, og="og-default.png", ogtype="website", noindex=False, cta=True, extra_js="", preload=""):
    canon = SITE + path
    g = {"@context": "https://schema.org", "@graph": graph or []}
    ld = f'<script type="application/ld+json">{json.dumps(g, ensure_ascii=False)}</script>' if graph else ""
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    doc = f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}"><meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">{robots}
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="{ogtype}"><meta property="og:image" content="{SITE}/og/{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:site_name" content="Davies Kelly"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#173E3F">
<link rel="preload" href="/assets/fonts/source-sans-3.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>{preload}
<style>{INLINE_CSS}</style>{ld}
<script src="/assets/js/vendor/lenis.min.js?v=1.3.4" defer></script><script src="/assets/js/site.js?v={ASSET_V}" defer></script>{extra_js}
</head><body>
{header(path)}
<main id="main">
{body}
</main>
{CTA if cta else ""}
{footer()}
{'' if path.startswith('/contact') else '<a class="sticky-cta" href="/contact/">Discuss a matter</a>'}
</body></html>
'''
    out = "404.html" if path == "/404.html" else path.strip("/") + "/index.html" if path != "/" else "index.html"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    PAGES.append(dict(path=path, noindex=noindex))


ORG = {"@id": f"{SITE}/#org"}


def head(h1, lead=None, crumb=None):
    c, ld = crumbs(crumb) if crumb else ("", None)
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return c + f'<div class="wrap page-head"><h1>{h1}</h1>{lead_html}</div>', ld


def expert_card(slug, sizes="(min-width:1200px) 25vw, (min-width:600px) 50vw, 100vw", show_actions=True):
    p = PEOPLE[slug]
    mail = f'<a class="btn secondary" href="mailto:{p["mail"]}">{ICON["mail"]}Email</a>' if p.get("mail") else f'<a class="btn secondary" href="/contact/">{ICON["mail"]}Contact</a>'
    acts = f'<div class="actions"><a class="btn" href="/experts/{slug}/" tabindex="-1" aria-hidden="true">Profile</a>{mail}</div>' if show_actions else ""
    city = city_html(p)
    return f'''<article class="expert-card">{picture(slug, sizes, alt=p["alt"])}<div class="body">
<h3><a href="/experts/{slug}/">{e(p["name"])}</a></h3><p class="role">{role_html(p)}</p><p class="meta">{city} · {e(p["post"])}</p><p class="card-bio">{e(BIO[slug])}</p><p class="tr-talk"><span>Talk to {e(first_name(slug))} about</span> {e(TALK[slug])}</p>{acts}</div></article>'''


# ================================================================ HOME (D.1)
SLIDES = [("wind", "Wind turbine nacelle being lifted into place", (480, 601), (960, 639), (1012, 569), [480], [960], [1012]),
          ("water", "Wastewater treatment clarifiers seen from above", (480, 600), (960, 640), (1086, 610), [480], [960], [1086]),
          ("tunnel", "Segment-lined tunnel under construction", (480, 600), (960, 640), (1920, 1080), [480, 640, 800], [960, 1280], [1280, 1920])]


def slide_html(k, s):
    name, alt, pdim, mdim, wdim, pw, mw, ww = s
    b = f"/assets/img/hero/{name}"
    def ss(tag, ws, ext):
        return ", ".join(f"{b}-{tag}-{w}.{ext} {w}w" for w in ws)
    attr = "srcset" if k == 0 else "data-srcset"
    srcs = ""
    for media, tag, ws in (("(min-width:900px)", "w", ww), ("(min-width:600px)", "m", mw), (None, "p", pw)):
        for ext in ("avif", "webp"):
            m = f' media="{media}"' if media else ""
            srcs += f'<source{m} type="image/{ext}" {attr}="{ss(tag, ws, ext)}" sizes="100vw">'
        if media:
            srcs += f'<source{m} {attr}="{ss(tag, ws, "jpg")}" sizes="100vw">'
    src = f"{b}-p-{pw[0]}.jpg"
    imgattr = f'src="{src}" fetchpriority="high"' if k == 0 else f'data-src="{src}" src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" loading="lazy" decoding="async"'
    on = " on" if k == 0 else ""
    hidden = "" if k == 0 else ' aria-hidden="true"'
    return f'<div class="slide{on}"{hidden} role="group" aria-roledescription="slide" aria-label="{k+1} of {len(SLIDES)}"><picture>{srcs}<img {imgattr} width="{pdim[0]}" height="{pdim[1]}" alt="{e(alt)}"></picture></div>'


slides = "".join(slide_html(k, s) for k, s in enumerate(SLIDES))
dots = "".join(f'<button class="dot" type="button" aria-label="Show image {k+1} of {len(SLIDES)}: {e(s[1])}"{" aria-current=" + chr(34) + "true" + chr(34) if k == 0 else ""}><span></span></button>' for k, s in enumerate(SLIDES))
pause_btn = '<button class="pause" type="button" aria-label="Pause slideshow"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg></button>'
services_cards = [
    ("Quantum expert evidence", "Independent opinion on the value of claims and counterclaims: prolongation, disruption, variations, overheads, defects and final accounts.", "/services/quantum/", ""),
    ("Delay expert evidence", "Independent analysis of what delayed a project, who was responsible and what extension of time follows.", "/services/delay/", ""),
    ("Engineering and contract evidence", "Technical opinion on design, construction and defects, and on how a FIDIC contract was administered.", "/services/technical/", ph("S13", "does DK offer this service?")),
    ("Claim review and advisory", "A frank second opinion on a claim before you spend on it, and contract and project advice before a dispute starts.", "/services/advisory/", ""),
]
svc_html = "".join(f'<article class="card service"><h3><a href="{u}">{t}</a></h3><p>{d} {flag}</p><a class="more" href="{u}" aria-label="More about {t}">Read more</a></article>' for t, d, u, flag in services_cards)
tiles = '''<a class="tile" href="/sectors/#energy"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/energy-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/energy-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/energy-sq-480.webp"><img src="/assets/img/sectors/energy-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Energy and power</span></a>
<a class="tile" href="/sectors/#water"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/water-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/water-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/water-sq-480.webp"><img src="/assets/img/sectors/water-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Water and desalination</span></a>
<a class="tile" href="/sectors/#transport"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/transport-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/transport-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/transport-sq-480.webp"><img src="/assets/img/sectors/transport-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Transport and infrastructure</span></a>
<a class="tile" href="/sectors/#oil-gas"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/oil-gas-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/oil-gas-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/oil-gas-sq-480.webp"><img src="/assets/img/sectors/oil-gas-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Oil, gas, process and industrial</span></a>
<a class="tile" href="/sectors/#buildings"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/buildings-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/buildings-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/buildings-sq-480.webp"><img src="/assets/img/sectors/buildings-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Commercial, residential and public buildings</span></a>
<a class="tile" href="/sectors/#hospitality"><picture><source media="(min-width:900px)" type="image/avif" srcset="/assets/img/sectors/hospitality-43-640.avif"><source type="image/avif" srcset="/assets/img/sectors/hospitality-sq-480.avif"><source type="image/webp" srcset="/assets/img/sectors/hospitality-sq-480.webp"><img src="/assets/img/sectors/hospitality-sq-480.jpg" width="480" height="480" alt="" loading="lazy" decoding="async"></picture><span>Hospitality and leisure</span></a>'''
steps4 = '''<ol class="steps row grid"><li><strong>Conflict check.</strong> Tell us the parties. We check every name before we discuss the substance.</li><li><strong>Scope call.</strong> A short call to understand the issues, the forum and the timetable.</li><li><strong>Written terms.</strong> Scope, fees, independence and confidentiality agreed in writing.</li><li><strong>Documents.</strong> Only then do we receive documents and start work.</li></ol>'''
home = f'''<section class="hero" aria-label="Introduction">
<div class="hero-media" aria-roledescription="carousel" aria-label="Project photographs">{slides}<div class="hero-controls">{dots}</div>{pause_btn}</div>
<div class="hero-text"><div class="wrap"><div class="inner">
<h1>Independent quantum, delay and technical experts for construction disputes</h1>
<p>We are testifying experts based in Dubai. We give clear, evidence-based opinion on delay, quantum and engineering issues in arbitration, court and adjudication across the Middle East, Africa, Asia and Europe.</p>
<div class="btn-row"><a class="btn light" href="/contact/">Make an enquiry</a><a class="btn ghost" href="/experts/">Meet the experts</a></div>
</div></div></div></section>
<section class="section"><div class="wrap"><h2 class="vh">Evidence our experts have given</h2>
<ul class="ticks grid c3"><li>Oral evidence under cross-examination by King’s Counsel in international arbitration.</li><li>Appointed as quantum, delay and technical experts in ICC, DIAC, DIFC and ICDR arbitrations, the UK High Court and Scottish courts, adjudication, dispute adjudication boards and pre-arbitral expert procedures.</li><li>Written and oral evidence on delay and extensions of time, disruption, prolongation, variations, head office overheads, defects and engineering issues.</li></ul></div></section>
<section class="section alt"><div class="wrap"><h2>What we do</h2><p class="lead measure">Most of our work is as independent experts appointed by a party or by the tribunal. We also review claims and advise before a dispute starts, and we always tell you which of those two roles we are in.</p>
<div class="grid c2">{svc_html}</div></div></section>
<section class="section"><div class="wrap"><h2>Meet the experts</h2><p class="lead measure">Four senior people. The expert you speak to is the one who does the work.</p>
{team_rotator()}<div class="grid c4 team-grid">{"".join(expert_card(s, show_actions=False) for s in ORDER)}</div></div></section>
<section class="section alt"><div class="wrap measure"><h2>How we keep our evidence independent</h2>
<ol class="steps"><li>When we are appointed as experts, our duty is to the tribunal or court, and it overrides any duty to the party that instructs or pays us.</li><li>We say what the evidence supports, we state our assumptions and limits, and we concede points when the evidence requires it.</li><li>We check for conflicts before we read any documents, and we never take on the expert role in a dispute where we have acted as advisers for the same party.</li></ol>
<p><a href="/independence/">Read how we work</a></p></div></section>
<section class="section"><div class="wrap"><h2>Sectors</h2><p class="lead measure">Energy, water, transport and buildings projects across the Middle East, Africa, Asia and Europe.</p><div class="tiles">{tiles}</div>
</div></section>
<section class="section alt"><div class="wrap"><h2>Selected experience</h2><p class="lead measure">We do not name clients or matters. Arbitration is usually confidential, and our clients’ disputes are not marketing material.</p>
{case_rotator(("C2", "C4", "C11", "C8", "C5", "C3"))}<div class="grid c3 case-grid">{"".join(case_card(c) for c in CASES if c["id"] in ("C2", "C4", "C11"))}</div><p style="margin-top:20px"><a class="btn secondary" href="/experience/">See all experience</a></p></div></section>
<section class="section"><div class="wrap"><h2>How an instruction starts</h2>{steps4}<p class="muted" style="margin-top:20px">We aim to reply to every enquiry promptly.</p></div></section>'''
home_graph = [
    {"@type": "Organization", "@id": f"{SITE}/#org", "name": "Davies Kelly", "url": f"{SITE}/", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/img/logo/davies-kelly-logo-512.png"}, "image": f"{SITE}/og/og-default.png",
     "description": "Davies Kelly is an international construction consultancy specialising in pre-contract advice, project advisory, dispute resolution and expert witness services (quantum, delay and technical) for the construction industry.", "slogan": "Independent quantum, delay and technical experts for construction disputes", "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE + u}} for n, u in [("Pre-contract advice", "/pre-contract-advice/"), ("Project advisory", "/project-advisory/"), ("Dispute resolution", "/dispute-resolution/"), ("Expert witness services", "/expert-witness-services/")]]},
     "address": {"@type": "PostalAddress", "streetAddress": "48 Burj Gate Tower, Sheikh Zayed Road, Downtown", "postOfficeBoxNumber": "116171", "addressLocality": "Dubai", "addressCountry": "AE"},
     "areaServed": [{"@type": "Place", "name": n} for n in ("Middle East", "Africa", "Asia", "Europe")],
     "knowsAbout": ["Pre-contract advice", "Project advisory", "Dispute resolution", "Expert witness services", "Construction quantum", "Delay analysis", "Technical and engineering expert evidence", "International arbitration", "FIDIC contracts", "Construction claims"],
     "founder": [{"@id": f"{SITE}/experts/michael-roos/#person"}, {"@id": f"{SITE}/experts/jamie-shafto/#person"}]},
    {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Davies Kelly", "publisher": ORG, "inLanguage": "en-GB"},
]
preload_hero = '<link rel="preload" as="image" type="image/avif" imagesrcset="/assets/img/hero/wind-p-480.avif 480w" imagesizes="100vw" media="(max-width:599px)">'
page("/", "Davies Kelly | Construction Consultancy and Expert Witnesses", "International construction consultancy in Dubai: pre-contract advice, project advisory, dispute resolution and expert witness services.", home, home_graph, preload=preload_hero)

# ================================================================ EXPERTS (D.2)
h, bc = head("Our experts", f"Davies Kelly is deliberately small. Each matter is led by one of the people below, who does the analysis and, where needed, gives the evidence. Michael Roos and Jamie Shafto founded the firm in 2020. Stephen M John and Michael Whiting are partners.", [("Home", "/"), ("Experts", None)])
body = h + f'''<section class="wrap" style="padding-bottom:var(--sec)">{team_rotator()}<div class="grid c4 team-grid">{"".join(expert_card(s) for s in ORDER)}</div>
<div class="measure" style="margin-top:48px"><h2>Types of appointment</h2><ul class="plain">
<li><strong>Party-appointed expert.</strong> Instructed by one party to give independent opinion evidence to the tribunal or court.</li>
<li><strong>Tribunal- or court-appointed expert.</strong> Appointed by the tribunal or court to report to it directly.</li>
<li><strong>Single joint expert.</strong> Instructed jointly by the parties.</li>
<li><strong>Expert in an expert determination or pre-arbitral expert procedure.</strong></li>
<li><strong>Non-testifying expert adviser.</strong> Advises a party or its lawyers privately on quantum or delay. We do not later act as that party’s testifying expert in the same dispute without disclosing it.</li></ul></div></section>'''
page("/experts/", "Our Experts | Davies Kelly", "Meet Davies Kelly’s quantum, delay and engineering experts: their qualifications, the evidence they have given and how to contact them directly.", body, [bc])


# ================================================================ PROFILES (D.3–D.6, E)
def ul(items):
    return '<ul class="plain">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


for slug in ORDER:
    p = PEOPLE[slug]
    first = p["name"].split()[0] if slug != "stephen-john" else "Stephen"
    honor = f'{p["honorific"]} ' if p["honorific"] else ""
    c, bcl = crumbs([("Home", "/"), ("Experts", "/experts/"), (p["name"], None)])
    btns = [f'<a class="btn" href="tel:{p["tel"]}">{ICON["call"]}Call</a>' + (ph(p["tel_ph"], "publish this number") if p.get("tel_ph") and slug != "michael-roos" and slug != "jamie-shafto" else "")]
    if p.get("wa"):
        btns.append(f'<a class="btn secondary" href="https://wa.me/{p["wa"]}">{ICON["wa"]}WhatsApp</a>')
    if p.get("mail"):
        btns.append(f'<a class="btn secondary" href="mailto:{p["mail"]}">{ICON["mail"]}Email</a>')
    else:
        btns.append(f'<a class="btn secondary" href="/contact/">{ICON["mail"]}Email</a>')
    contact_note = ph(p["tel_ph"], "publish mobile; WhatsApp on it?") if slug in ("michael-roos", "jamie-shafto") else (ph(p["mail_ph"], "email address to show") if p.get("mail_ph") else "")
    evidence = (f'<div class="evidence"><h2>Evidence given</h2>{ul(p["evidence"])}</div>' if p.get("evidence")
                else f'<div class="evidence"><h2>Role</h2><p>{p["role_note"]}</p></div>' if p.get("role_note") else "")
    tribunal = f'<h2>Tribunal appointments</h2>{ul(p["tribunal"])}' if p.get("tribunal") else ""
    career_extra = ""
    members = ul(p["members"]) if p.get("members") else ""
    methods = f'<div class="side-block"><h2>Methods</h2><p>{p["methods"]}</p></div>' if p.get("methods") else ""
    speaking = ""
    tags = '<ul class="tags">' + "".join(f"<li>{e(x)}</li>" for x in p["expertise"]) + "</ul>"
    mailto = p.get("mail")
    side = f'''<div class="side-block"><h2>Contact</h2><p>{"<a href='mailto:" + mailto + "'>" + mailto + "</a><br>" if mailto else ""}<a href="tel:{p["tel"]}">{p["tel_d"]}</a></p>{contact_note}</div>
<div class="downloads"><a class="btn block secondary" href="/vcard/{slug}.vcf" download>Save contact (vCard)</a></div>
<div class="side-block"><h2>Expertise</h2>{tags}</div>
<div class="side-block"><h2>Sectors</h2><p>{e(", ".join(p["sectors"]))}</p></div>
<div class="side-block"><h2>Regions</h2><p>{e(p["regions"])}</p></div>{methods}
{'<div class="side-block"><h2>Contract forms</h2><p>' + p["contracts"] + '</p></div>' if p.get("contracts") else ""}
<div class="side-block"><h2>Qualifications</h2>{ul(p["quals"])}</div>
{'<div class="side-block"><h2>Memberships</h2>' + members + '</div>' if members else ""}
{speaking}'''
    indep = f'When appointed as an expert, {first}’s duty is to the tribunal or court.' if p["testifying"] else "Our appointed experts’ duty is to the tribunal or court."
    body = c + f'''<div class="wrap">
<div class="profile-head">{picture(slug, "(min-width:600px) 200px, 40vw", alt=p["alt"], eager=True)}<div>
<h1>{e(honor + p["name"])}</h1><p class="post">{e(p["post"])}</p><p class="role">{role_html(p)}</p><p class="city">{city_html(p)}</p></div></div>
<div class="contact-row">{"".join(btns)}</div>
<div class="split" style="padding-bottom:var(--sec)"><div class="profile-main">
<p class="lead">{p["summary"]}</p>
<h2>Highlights</h2>{ul(p["highlights"])}
{evidence}
<h2>Selected experience</h2>{ul(p["experience"])}
{tribunal}
<h2>Career</h2>{ul([e(x) for x in p["career"]])}{career_extra}
<p class="note">{indep} <a href="/independence/">Read how we work</a>.</p>
</div><aside class="sticky">{side}</aside></div></div>'''
    ld = PEOPLE[slug]["ld"]
    person = {"@type": "Person", "@id": f"{SITE}/experts/{slug}/#person", "name": p["name"], "url": f"{SITE}/experts/{slug}/", "image": f"{SITE}/assets/img/people/{slug}-528.jpg", "worksFor": ORG,
              "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": cat, "name": n} for cat, n in ld["creds"]], "knowsAbout": ld["knows"]}
    if p["honorific"]:
        person["honorificPrefix"] = p["honorific"]
    if p.get("role") and not p.get("role_ph"):
        person["jobTitle"] = p["role"]
    if slug != "michael-whiting":
        person["honorificSuffix"] = p["post"]
    if ld["alumni"]:
        person["alumniOf"] = [{"@type": "CollegeOrUniversity", "name": n} for n in ld["alumni"]]
    if ld["member"]:
        person["memberOf"] = [{"@type": "Organization", "name": n} for n in ld["member"]]
    graph = [{"@type": "ProfilePage", "@id": f"{SITE}/experts/{slug}/#page", "url": f"{SITE}/experts/{slug}/", "mainEntity": {"@id": f"{SITE}/experts/{slug}/#person"}}, person, bcl]
    page(f"/experts/{slug}/", p["title"], p["desc"], body, graph, og=f"{slug}.png", ogtype="profile")


# ================================================================ SERVICES (D.7–D.11)
def lead_card(slug, extra=""):
    p = PEOPLE[slug]
    mail = f'<a class="btn secondary" href="mailto:{p["mail"]}">{ICON["mail"]}Email</a>' if p.get("mail") else f'<a class="btn secondary" href="/contact/">{ICON["mail"]}Contact</a>'
    return f'''<div class="card" style="display:grid;grid-template-columns:96px 1fr;gap:16px;align-items:start">{picture(slug, "96px", alt=p["alt"])}<div><h3 style="margin:0"><a href="/experts/{slug}/">{e(p["name"])}</a></h3><p class="muted" style="margin:0 0 10px">{role_html(p)}</p>
<div class="btn-row"><a class="btn" href="tel:{p["tel"]}">{ICON["call"]}Call</a>{mail}</div>{extra}</div></div>'''


h, bc = head("Services", "Davies Kelly is an international construction consultancy providing pre-contract advice, project advisory, dispute resolution and expert witness services. We give independent expert evidence on quantum, delay and engineering issues, and we advise on claims before and during a dispute. Expert and adviser are different roles with different duties, so we keep them apart.", [("Home", "/"), ("Services", None)])
rows = [("Quantum expert evidence", "/services/quantum/", "michael-roos", "Opinion on the value of claims and counterclaims, from prolongation and disruption to variations, overheads and defects. For arbitration, court, adjudication and expert procedures.", ""),
        ("Delay expert evidence", "/services/delay/", "jamie-shafto", "Forensic analysis of delay and disruption: what happened, why, who was responsible and what time follows.", ""),
        ("Engineering and contract evidence", "/services/technical/", "stephen-john", "Technical opinion on design, construction methods and defects, and on how a FIDIC contract was administered.", ph("S13", "does DK offer this service?")),
        ("Claim review and advisory", "/services/advisory/", None, "Independent reviews of claims before you commit to them, claim preparation and defence, contract and risk advice, and planning and commercial support on live projects.", "")]
rows_html = "".join(f'''<article class="card service"><h2 style="font-size:var(--fs-h3)"><a href="{u}">{t}</a></h2><p>{d} {f}</p><p class="muted">{"Led by " + e(PEOPLE[s]["name"]) if s else "Led by all our experts"}</p><a class="btn secondary block" href="{u}">Read more</a></article>''' for t, u, s, d, f in rows)
FOUR = [("Pre-contract advice", "/pre-contract-advice/", "Review and drafting of construction contracts and professional services agreements, and identification of contractual risk before you sign."),
        ("Project advisory", "/project-advisory/", "Project controls, planning, cost and change management, and commercial and risk management on live projects."),
        ("Dispute resolution", "/dispute-resolution/", "Preparation and defence of extension of time and cost claims, and impartial advice and determinations to resolve them."),
        ("Expert witness services", "/expert-witness-services/", "Independent quantum, delay and technical expert evidence in arbitration, court and adjudication.")]
four_html = "".join(f'<article class="card service"><h2 style="font-size:var(--fs-h3)"><a href="{u}">{t}</a></h2><p>{d}</p><a class="btn secondary block" href="{u}">Read more</a></article>' for t, u, d in FOUR)
body = h + f'''<section class="wrap" style="padding-bottom:var(--sec)"><div class="grid c2">{four_html}</div><h2 style="margin-top:48px">Expert evidence by discipline</h2><div class="grid c2">{rows_html}</div>
<div class="box measure" style="margin-top:32px"><h2 style="font-size:var(--fs-h3)">Two roles, kept separate</h2><p>As advisers we work in your interest. As experts our duty is to the tribunal. We tell you at the outset which role we are in, and we do not switch roles in the same dispute without telling everyone affected.</p></div></section>'''
page("/services/", "Services | Davies Kelly", "Pre-contract advice, project advisory, dispute resolution and expert witness services for the construction industry, from Dubai.", body, [bc])

HOW5 = ["We agree the questions we are asked to answer, in writing.", "We go to the contract and the contemporaneous records first, then the parties’ claims.", "We value each head of claim on a stated method and say where the records do not support a figure.", "We meet the other side’s expert in good faith and record agreements and disagreements in a joint statement.", "We give oral evidence when required and answer questions as we would for the tribunal, whoever asks them."]


def service_page(path, crumb, h1, intro, sections, how, leads, cases_ids, title, desc):
    h, bc = head(h1, intro, [("Home", "/"), ("Services", "/services/"), (crumb, None)])
    secs = "".join(f"<h2>{t}</h2>{c}" for t, c in sections)
    howh = '<h2>How we work</h2><ol class="steps">' + "".join(f"<li>{x}</li>" for x in how) + "</ol>" if how else ""
    rel = "".join(case_card(c) for c in CASES if c["id"] in cases_ids)
    body = h + f'''<div class="wrap"><div class="split" style="padding-bottom:var(--sec)"><div class="measure">{secs}{howh}
<h2>Related experience</h2><div class="grid">{rel}</div></div>
<aside class="sticky"><h2 style="font-size:var(--fs-h3)">Who leads this work</h2>{leads}</aside></div></div>'''
    page(path, title, desc, body, [bc])


service_page("/services/quantum/", "Quantum", "Quantum expert evidence",
             "Quantum is the money in a construction dispute: what the claims and counterclaims are worth, on the contract and on the records. Our quantum experts started on site and in commercial teams, and they value claims the way the contract and the evidence require, not the way either party would like.",
             [("What we assess", ul(["Prolongation and time-related costs", "Disruption and loss of productivity, including measured-mile analysis", "Head office overheads and loss of profit or opportunity", "Variations, measured work and re-measurement", "Preliminaries thickening, acceleration and idle time", "Subcontractor claims and pass-through claims", "Liquidated damages, retention and performance bonds", "Defects, rectification and counterclaims for work not to specification", "Late payment, financing and interest", "Final accounts and accounts reconstructed from first principles", "Early merits and quantum opinions for funders, with sensitivity ranges"])),
              ("Where we give evidence", ul([f"International arbitration.", "Court proceedings, including in Scotland, and in support of matters before UAE courts.", "Adjudication in the UK.", "Pre-arbitral expert procedures and expert determination."]))],
             HOW5, lead_card("michael-roos") + f'<p class="muted" style="margin-top:12px">Supported by <a href="/experts/michael-whiting/">Michael Whiting</a>, Partner, Quantum Expert.</p>', ("C8", "C9"),
             "Quantum Expert Witness, Dubai | Davies Kelly", "Independent quantum expert evidence on prolongation, disruption, variations, overheads, defects and final accounts in construction arbitration.")
how_d = HOW5[:2] + ["We build the analysis from the programmes and the progress records, and we state every assumption and every gap in the records."] + HOW5[3:]
service_page("/services/delay/", "Delay", "Delay expert evidence",
             "Delay analysis answers three questions: what delayed completion, who was responsible, and what extension of time and costs follow. Our delay expert spent years planning and programming major projects before turning to disputes, so the analysis starts from how the work was actually built.",
             [("What we analyse", ul(["Forensic delay analysis and responsibility for delay", "Disruption analysis", "Extension of time entitlement, claims and defences", "Independent determinations of extension of time claims", "Reviews of engineer’s and employer’s determinations", "Progress monitoring records, baseline and as-built programmes", "Planning and programming on live projects, including master planning for developments"])),
              ("Methods", f"<p>We choose the method to suit the contract, the records available and the question the tribunal must answer, and we explain why it was chosen.</p>"),
              ("Where we give evidence", "<p>International arbitration under the ICC and DIAC rules, ICC expert determination, and amicable settlement panels.</p>")],
             how_d, lead_card("jamie-shafto"), ("C4", "C5"),
             "Delay Expert Witness, Dubai | Davies Kelly", "Independent delay expert evidence: forensic delay analysis, disruption and extension of time in ICC and DIAC construction arbitrations.")
service_page("/services/technical/", "Engineering and contracts", "Engineering and contract expert evidence",
             f"Some disputes turn on engineering: whether a design worked, whether the work was built properly, or how a contract was administered. Stephen John is a chartered civil engineer with more than 40 years of practice who gives independent technical and contract evidence.",
             [("What we cover", ul(["Design, buildability and construction method", "Defects: identification, cause and rectification", "Post-tensioned and high-rise structures", "Tunnels, water and wastewater works, hydro and energy plant, pipelines and LNG tanks", "FIDIC contract administration and claims", "Dispute adjudication board (DAB) proceedings", "Independent “cold eyes” reviews of troubled projects"])),
              ("Where evidence has been given", f"<p>The UK High Court and arbitration in the DIFC, the ICDR in London and other seats, including the Dubai International Arbitration Centre.</p>")],
             None, lead_card("stephen-john"), ("C11", "C12"),
             "Engineering and Contract Expert Evidence | Davies Kelly", "Independent technical evidence on design, construction, defects and FIDIC contract administration from a chartered civil engineer.")

h, bc = head("Claim review and advisory", None, [("Home", "/"), ("Services", "/services/"), ("Claim review and advisory", None)])
body = h + f'''<div class="wrap measure" style="padding-bottom:var(--sec)">
<div class="box"><p>Advisers and experts have different duties. As advisers we work in your interest and help you make decisions. As experts our duty is to the tribunal. We tell you at the outset which role we are in, and if we have advised you on a dispute we will not act as your testifying expert in it without telling everyone affected.</p></div>
<h2>Independent claim review</h2><p>A candid view of a claim before you spend on it: whether the entitlement holds, whether the records support it, and what a tribunal is likely to make of the numbers. We also give early merits and quantum notes to funders, with sensitivity ranges.</p>
<h2>Claim preparation and defence</h2><p>Extension of time, prolongation, disruption and variation claims prepared or answered from the contract and the records, including consolidated claims on major projects.</p>
<h2>Pre-contract and contract advice</h2><p>Review of contracts and professional appointments for risk allocation, notices and change and claims provisions, with practical recommendations before you sign.</p>
<h2>Project advisory</h2><p>Planning and project controls, commercial management, productivity reviews and recovery of projects in difficulty.</p>
<h2>Support to counsel</h2><p>Analysis to support pleadings and settlement strategy, as a non-testifying consultant. We do not provide this support in a matter where one of us is, or may become, the testifying expert.</p>
<h2>A frank second opinion</h2><p>An international engineering and contracting company asked us to review a claim valued by another consultancy. We found significant weaknesses in both the analysis and the valuation, and advised that only a fraction of the sum was likely to be recovered. The client decided not to pursue it, avoiding legal and expert fees and the risk of paying the other side’s costs. It cost us the work. It also told the client what our advice is worth.</p>

</div>'''
page("/services/advisory/", "Claim Review and Construction Advisory | Davies Kelly", "Candid reviews of construction claims, claim preparation and defence, and contract and project advice before and during a dispute.", body, [bc])

# ================================================================ SECTORS (D.12)
SECTORS = [
    ("energy", "Energy and power", "Power stations, solar plant, hydro-electric refurbishment and wider energy projects.", ["jamie-shafto", "stephen-john", "michael-whiting"], "C6", "energy"),
    ("oil-gas", "Oil, gas, process and industrial", "Oil and gas, LNG plant and tanks, LPG extraction and fractionation, crude oil refining, gas processing and pipelines, process plants, phosphate processing and industrial facilities.", ORDER, "C2", "oil-gas"),
    ("water", "Water, wastewater and desalination", "Desalination plants, water distribution, sewage and wastewater treatment, and water tunnels.", ["michael-roos", "jamie-shafto", "stephen-john"], "C8", "water"),
    ("transport", "Transport and infrastructure", "Rail, metro and tram, highways and roads, airports and aviation, marine infrastructure, ports and tunnels.", ORDER, "C5", "transport"),
    ("buildings", "Commercial, residential and public buildings", "High-rise commercial and residential towers, residential complexes, mixed-use developments, offices, retail and data centres, and public buildings: hospitals and healthcare facilities, education and PFI projects.", ORDER, "C11", "buildings"),
    ("hospitality", "Hospitality and leisure", "Hotels and resorts, and works for major international sporting events.", ORDER, "C3", "hospitality"),
]
h, bc = head("Sectors", "Our experts have worked on, and given evidence about, projects across six broad sectors in the Middle East, Africa, the UK, Europe, Central Asia and Australia.", [("Home", "/"), ("Sectors", None)])
secs = ""
for sid, t, d, who, cid, photo in SECTORS:
    if not photo:
        img = f'<div class="tile noimg sector-tile" style="aspect-ratio:3/2"><span>{t}</span></div>'
    else:
        img = f'<picture><source type="image/avif" srcset="/assets/img/sectors/{photo}-32-640.avif 640w, /assets/img/sectors/{photo}-32-960.avif 960w" sizes="(min-width:900px) 50vw, 100vw"><source type="image/webp" srcset="/assets/img/sectors/{photo}-32-640.webp 640w, /assets/img/sectors/{photo}-32-960.webp 960w" sizes="(min-width:900px) 50vw, 100vw"><img src="/assets/img/sectors/{photo}-32-640.jpg" width="640" height="427" alt="" loading="lazy" decoding="async"></picture>'
    names = ", ".join(f'<a href="/experts/{s}/">{e(PEOPLE[s]["name"])}</a>' for s in who)
    card = case_card([c for c in CASES if c["id"] == cid][0])
    secs += f'<section class="sector section" id="{sid}"><div class="sector-img">{img}</div><div><h2>{t}</h2><p>{d}</p><p><strong>Experts in this sector:</strong> {names}</p>{card}</div></section>'
body = h + f'<div class="wrap">{secs}</div>'
page("/sectors/", "Sectors | Davies Kelly", "Construction disputes in energy, oil and gas, water, transport, commercial, residential and public buildings, and hospitality, from Dubai.", body, [bc])

# ================================================================ EXPERIENCE (D.13, F)
h, bc = head("Experience", "A selection of matters from our experts’ CVs. Each is described by sector, region, forum, our role and the issues. We do not name parties, projects or values.", [("Home", "/"), ("Experience", None)])
adv = "".join(f'<article class="case"><div class="chips"><span>Advisory</span></div><p>{e(t)}</p><p class="muted small">{e(PEOPLE[s]["name"])}</p></article>' for _, t, s in ADVISORY)
body = h + f'''<div class="wrap" style="padding-bottom:var(--sec)"><div class="box measure"><p><strong>Confidentiality.</strong> Arbitration is usually confidential and so is most of our work. If you need fuller details for a proposal or a tribunal disclosure, ask us: we will share what we can once we have checked our obligations.</p><p>{ph("F20", "approve each card and the naming level (region or country)")}</p></div>
<div class="grid c3">{"".join(case_card(c) for c in CASES)}</div>
<h2 style="margin-top:56px">Advisory examples</h2><div class="grid c3">{adv}</div></div>'''
page("/experience/", "Experience (Anonymised) | Davies Kelly", "Selected anonymised matters: sector, region, forum and our role as quantum, delay or technical experts in arbitration, court and adjudication.", body, [bc])

# ================================================================ INDEPENDENCE (D.14)
IND = [
    ("duty", "Our duty as experts", "<p>When we are appointed as experts, our duty is to help the tribunal or court on matters within our expertise. That duty overrides any obligation to the party who instructs or pays us. We give the same opinion whoever asks the question.</p>"),
    ("rules", "The rules we follow", "<p>Depending on the forum, our evidence is governed by:</p>" + ul(["the procedural rules the tribunal adopts, including the IBA Rules on the Taking of Evidence in International Arbitration;", "the Chartered Institute of Arbitrators’ Protocol for the Use of Party-Appointed Expert Witnesses in International Arbitration, where it is adopted;", "in the courts of England and Wales, Part 35 of the Civil Procedure Rules and its Practice Direction;", "the rules of the court or tribunal in any other forum."]) + "<p>We read the applicable rules at the start of each appointment and follow them.</p>"),
    ("conduct", "Seven conduct rules", '<ol class="steps">' + "".join(f"<li>{x}</li>" for x in ["We give opinions only on matters within our expertise, and say so when a question falls outside it.", "We base our opinion on the evidence and the contract, not on the outcome our client wants.", "We state every assumption and every limit on the documents we were given.", "We consider the documents that do not support our client’s case as carefully as those that do.", "We use recognised methods and explain why we chose them.", "We meet the other side’s expert in good faith, and we concede points when the evidence requires it.", f"Our fees for expert work never depend on the outcome of the case."]) + "</ol>"),
    ("conflicts", "Conflicts of interest", f"<p>Before we discuss a matter we check every party, and their parent and related companies, against our records. That check includes appointments our people hold as arbitrators, adjudicators and dispute board members. We tell you the result before you send any documents. If a conflict appears later, we tell everyone affected straight away.</p>"),
    ("roles", "Adviser or expert: one role per dispute", f"<p>As advisers we act in your interest; as experts our duty is to the tribunal. We tell you which role we are in at the outset. We do not act as testifying expert in a dispute in which we have advised the same party, unless that has been disclosed and the tribunal and the parties have had the chance to object.</p>"),
    ("confidentiality", "Confidentiality", "<p>We keep everything about our clients’ matters confidential, including the fact that we are instructed. We do not name clients, parties or projects on this website or in our marketing.</p>"),
    ("fees", "Fees", f"<p>We work on time-based fees agreed in writing before work starts. We do not publish rates. For expert work, our fees never depend on the result.</p>"),
    ("engagement", "Engagement", "<p>Contacting us does not create an engagement. An engagement starts only when we have cleared conflicts and both sides have signed written terms.</p>"),
]
h, bc = head("Independence and how we work", "An expert is only useful to a tribunal if the opinion is honest, competent and independent. This page sets out the rules we work to.", [("Home", "/"), ("Independence", None)])
toc = '<nav aria-label="On this page"><ul class="toc">' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in IND) + "</ul></nav>"
secs = "".join(f'<section id="{i}"><h2>{t}</h2>{c}</section>' for i, t, c in IND)
body = h + f'<div class="wrap"><div class="split" style="padding-bottom:var(--sec)"><div class="measure">{secs}</div><aside class="sticky" style="order:-1">{toc}</aside></div></div>'
page("/independence/", "Independence and Expert Duties | Davies Kelly", "Our duty as experts is to the tribunal. How we keep our evidence independent, handle conflicts and keep matters confidential.", body, [bc])

# ================================================================ ABOUT (D.15)
h, bc = head("About Davies Kelly", None, [("Home", "/"), ("About", None)])
strip = "".join(f'<a href="/experts/{s}/" style="display:flex;gap:12px;align-items:center;min-height:64px;text-decoration:none">{picture(s, "64px", alt="")}<span><strong>{e(PEOPLE[s]["name"])}</strong></span></a>' for s in ORDER)
strip = strip.replace('width="528" height="660"', 'width="64" height="80" style="width:64px;height:80px;object-fit:cover;border-radius:4px"')
body = h + f'''<div class="wrap" style="padding-bottom:var(--sec)"><div class="measure">
<p class="lead">Davies Kelly is a Dubai firm of construction experts, founded in 2020 by Michael Roos and Jamie Shafto, a quantum expert and a delay expert. We give independent expert evidence in construction and engineering disputes and advise on claims before and during a dispute. We have been appointed as independent experts and advisers by international law firms, contractors and developers, in matters from mediation to international arbitration.</p>
<h2>Why a small firm</h2>
<p><strong>The expert does the work.</strong> The person named in the report is the person who analysed the records.</p>
<p><strong>Fewer conflicts.</strong> A small firm with a focused practice is less often conflicted on large projects. We tell you the result of our conflict check before you send documents.</p>
<p><strong>Built on site experience.</strong> Our experts started as a labourer, a planner, an engineer and an apprentice quantity surveyor. They value and analyse claims the way projects are actually built.</p>
<h2>What we stand for</h2><ol class="steps"><li>Our duty as experts is to the tribunal.</li><li>We say what the evidence supports, including when it is not what the instructing party hoped to hear.</li><li>We use recognised methods and show our working.</li><li>We state our assumptions and the limits of what we were given.</li><li>Senior people do the work.</li><li>We keep our clients’ matters confidential.</li></ol>
<h2>Our office</h2><p>{e(ADDRESS)}</p><p><a class="btn secondary" href="{MAPS}" rel="noopener noreferrer">Open in Google Maps</a></p>
<h2>Our people</h2><div class="grid c2">{strip}</div></div></div>'''
page("/about/", "About Davies Kelly | Construction Experts, Dubai", "Davies Kelly is a small Dubai firm of independent quantum, delay and technical experts, founded by Michael Roos and Jamie Shafto.", body, [bc])

# ================================================================ INSIGHTS (D.16) — noindex until live
h, bc = head("Insights", "Short, practical notes from our experts on quantum, delay and contracts in construction disputes.", [("Home", "/"), ("Insights", None)])
body = h + f'<div class="wrap measure" style="padding-bottom:var(--sec)"><p>Our first articles are being written.</p></div>'
page("/insights/", "Insights | Davies Kelly", "Practical notes from our experts on quantum, delay and contracts in construction disputes.", body, [bc], noindex=True)


# ================================================================ CONTACT (D.17)
def chips(name, opts):
    return f'<div class="chipset">' + "".join(f'<label><input type="radio" name="{name}" value="{e(o)}" required><span>{o}</span></label>' for o in opts) + "</div>"


def contact_card(name, role, tel, tel_d, mail, wa_ph):
    return f'''<div class="card"><h3>{name}</h3><p class="muted">{role}</p><div class="btn-row" style="grid-template-columns:1fr"><a class="btn block" href="tel:{tel}">{ICON["call"]}Call {tel_d}</a><a class="btn secondary block" href="mailto:{mail}">{ICON["mail"]}Email</a></div><p class="small muted" style="margin-top:8px">WhatsApp</p></div>'''


h, bc = head("Contact us", f"Tell us about the matter and who the parties are. We will check for conflicts and reply promptly.", [("Home", "/"), ("Contact", None)])
form = f'''<div class="box"><p><strong>Please do not send documents or confidential information yet.</strong> Tell us who the parties are so we can check for conflicts first.</p></div>
<form id="enquiry" class="cf" novalidate data-to="{ENQ_TO}">
<div class="cf-progress" aria-hidden="true"><span></span></div>
<div class="cf-step" tabindex="-1">Step <b>1</b> of 3</div>
<div class="cf-summary" tabindex="-1" hidden><h3>There is a problem</h3><ul></ul></div>
<div class="cf-panel" data-step="1">
<fieldset class="cf-field" id="f-role"><legend>You are…</legend><p class="cf-err" hidden></p><div class="cf-chips">{"".join(f'<label class="cf-chip"><input type="radio" name="role" value="{e(o)}"><span>{e(o)}</span></label>' for o in ["A law firm", "A contractor", "A subcontractor", "An employer or developer", "A consultant", "Other"])}</div></fieldset>
<fieldset class="cf-field" id="f-stage"><legend>Where is the matter now?</legend><p class="cf-err" hidden></p><div class="cf-chips">{"".join(f'<label class="cf-chip"><input type="radio" name="stage" value="{e(o)}"><span>{e(o)}</span></label>' for o in ["On a live project", "Claim being prepared", "Adjudication", "Arbitration", "Court proceedings", "Not sure yet"])}</div></fieldset>
</div>
<div class="cf-panel" data-step="2" hidden>
<div class="cf-field" id="f-name"><label for="cf-name">Your name</label><p class="cf-err" hidden></p><input class="cf-input" id="cf-name" name="name" autocomplete="name" maxlength="120"></div>
<div class="cf-field" id="f-organisation"><label for="cf-organisation">Organisation <span class="cf-opt">(optional)</span></label><input class="cf-input" id="cf-organisation" name="organisation" autocomplete="organization" maxlength="160"></div>
<div class="cf-field" id="f-email"><label for="cf-email">Email address</label><p class="cf-hint">We will reply to this address.</p><p class="cf-err" hidden></p><input class="cf-input" id="cf-email" name="email" type="email" autocomplete="email" inputmode="email" spellcheck="false" autocapitalize="off" maxlength="200"></div>
<div class="cf-field" id="f-phone"><label for="cf-phone">Phone or WhatsApp <span class="cf-opt">(optional)</span></label><p class="cf-hint">Include the country code.</p><p class="cf-err" hidden></p><input class="cf-input" id="cf-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" maxlength="30"></div>
</div>
<div class="cf-panel" data-step="3" hidden>
<div class="cf-field" id="f-outline"><label for="cf-outline">Overview <span class="cf-opt">(optional)</span></label><p class="cf-hint">A few basic details: the parties (for our conflict check), the project and country, and what you need. Nothing confidential.</p><p class="cf-err" hidden></p><textarea class="cf-input" id="cf-outline" name="outline" rows="6" maxlength="1550"></textarea></div>
<dl class="cf-review"><div><dt>You are</dt><dd><span data-r="who"></span> <button type="button" class="cf-change" data-go="1">Change</button></dd></div><div><dt>Your details</dt><dd><span data-r="details"></span> <button type="button" class="cf-change" data-go="2">Change</button></dd></div></dl>
<p class="small muted">Sending opens your email app with your enquiry filled in, addressed to our partners. We use these details only to reply and to check for conflicts (<a href="/privacy/">privacy notice</a>). Sending this does not create an engagement.</p>
</div>
<div class="cf-hp" aria-hidden="true"><label for="cf-website">Website</label><input id="cf-website" name="website" tabindex="-1" autocomplete="off"></div>
<div class="cf-nav"><button type="button" class="btn secondary" data-back hidden>Back</button><button type="submit" class="btn">Continue</button></div>
</form>
<div id="result" class="result box" hidden role="status"><h2 tabindex="-1" style="font-size:var(--fs-h3)">Your email app should now open with your enquiry</h2>
<p>If it did not open, copy your enquiry and email it to <a href="mailto:{ENQ_TO}">{ROOS_MAIL}</a> and <a href="mailto:{JAMIE_MAIL}">{JAMIE_MAIL}</a>.</p>
<label for="copy-text" class="vh">Your enquiry</label><textarea id="copy-text" readonly></textarea>
<p style="margin-top:12px"><button class="btn secondary" type="button" id="copy-enquiry">Copy my enquiry</button></p><p id="copy-status" aria-live="polite"></p></div>'''

side = f'''<h2 id="direct">Or contact a partner directly</h2><div class="grid">{contact_card("Michael Roos", "Founding Partner, Testifying Quantum Expert", ROOS_TEL, ROOS_TEL_D, ROOS_MAIL, "R15")}{contact_card("Jamie Shafto", "Founding Partner, Testifying Delay Expert", JAMIE_TEL, JAMIE_TEL_D, JAMIE_MAIL, "J15")}</div>
<h2 style="margin-top:32px">Office</h2><p>{e(ADDRESS)}</p><p><a class="btn secondary block" href="{MAPS}" rel="noopener noreferrer">Open in Google Maps</a></p>
<h2 style="margin-top:32px">What happens next</h2><ol class="steps"><li><strong>Conflict check.</strong> We check every party.</li><li><strong>Scope call.</strong> The issues, forum and timetable.</li><li><strong>Written terms.</strong> Scope, fees, independence, confidentiality.</li><li><strong>Documents.</strong> Only then.</li></ol>'''
body = h + f'<div class="wrap"><div class="split form" style="padding-bottom:var(--sec)"><div>{form}</div><aside>{side}</aside></div></div>'
page("/contact/", "Contact and Conflict Check | Davies Kelly", "Tell us the parties and the matter. We check for conflicts first. Please do not send confidential documents until we confirm.", body, [bc], cta=False, extra_js='<script src="/assets/js/contact.js?v={ASSET_V}" defer></script>')

body = head("Thank you", None)[0] + f'<div class="wrap measure" style="padding-bottom:var(--sec)"><p>Your enquiry has reached Davies Kelly. We will reply by email. If it is urgent, call Michael Roos on <a href="tel:{ROOS_TEL}">{ROOS_TEL_D}</a> or Jamie Shafto on <a href="tel:{JAMIE_TEL}">{JAMIE_TEL_D}</a>.</p></div>'
page("/contact/thank-you/", "Thank you | Davies Kelly", "Your enquiry has reached Davies Kelly.", body, noindex=True, cta=False)

# ================================================================ LEGAL (D.18–D.20)
LAST = f"<p class='muted'>Last updated: 4 November 2026</p>"
privacy = [
    ("Who we are", f"<p>This website is run by Davies Kelly, {e(ADDRESS)} (“Davies Kelly”, “we”). For privacy questions, email <a href='mailto:{ROOS_MAIL}'>{ROOS_MAIL}</a>.</p>"),
    ("What we collect and why", "<p><strong>Enquiries.</strong> When you use the contact form or email us, we collect your name, organisation, role, email address, phone number (if given) and what you tell us about the matter, including the names of the parties. We use this to reply to you and to check for conflicts of interest before we can act. Our lawful basis is taking steps at your request before entering into a contract, and our legitimate interest in managing conflicts.</p><p><strong>Website use.</strong> We do not run analytics on this website. Our host, GitHub Pages, processes technical data such as IP addresses in its server logs to deliver and secure the site.</p><p><strong>Fonts.</strong> Our fonts are served from our own website, so no font provider receives your data.</p>"),
    ("Who we share it with", "<p>The contact form opens your own email app, so your enquiry travels through your email provider and ours (Microsoft 365). Our website host is GitHub, Inc. (USA). We do not sell your data or use it for marketing.</p>"),
    ("International transfers", f"<p>Some of these providers process data outside the UAE, including in the USA.</p>"),
    ("How long we keep it", f"<p>Enquiries that do not lead to an engagement are deleted once they are no longer needed. Records of conflict checks are kept so that we can show our checks were made.</p>"),
    ("Your rights", f"<p>You can ask for access to, correction of, or deletion of your data, and you can object to our use of it, under the UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021) and, where it applies to you, the UK or EU GDPR.</p>"),
    ("Changes", "<p>We will post any changes on this page with a new date.</p>"),
]


def legal(path, h1, secs, title, desc, crumb):
    h, bc = head(h1, None, [("Home", "/"), (crumb, None)])
    body = h + '<div class="wrap measure legal" style="padding-bottom:var(--sec)">' + LAST + "".join(f"<h2>{t}</h2>{c}" for t, c in secs) + "</div>"
    page(path, title, desc, body, [bc], cta=False)


legal("/privacy/", "Privacy notice", privacy, "Privacy Notice | Davies Kelly", "How Davies Kelly uses the personal data you send us through this website.", "Privacy")
legal("/cookies/", "Cookies", [("Our approach", "<p>This website does not set cookies and does not use any tracking technology that stores information on your device. If that changes, we will update this page and ask for your consent before setting any cookie that is not strictly necessary.</p>")], "Cookies | Davies Kelly", "This website sets no cookies.", "Cookies")
legal("/terms/", "Website terms", [
    ("About these terms", f"<p>These terms apply to your use of davieskelly.com, run by Davies Kelly.</p>"),
    ("No advice, no engagement", "<p>The content of this website is general information, not advice on any matter. Contacting us or sending the enquiry form does not create a client relationship or an expert appointment. An engagement starts only when conflicts are cleared and written terms are signed.</p>"),
    ("Do not send confidential information", "<p>Please do not send confidential or privileged information until we have confirmed in writing that we have no conflict and can act. We may not be able to treat unsolicited information as confidential.</p>"),
    ("Accuracy", "<p>We keep the information on this website up to date, but we cannot promise that it is complete or current.</p>"),
    ("Intellectual property", "<p>The content, logo and images on this website belong to Davies Kelly or are used under licence. Do not copy them without permission.</p>"),
    ("Links", "<p>We are not responsible for the content of websites we link to.</p>"),
    ("Liability", "<p>To the extent the law allows, we are not liable for any loss arising from use of this website.</p>"),
    ("Law", f"<p>These terms are governed by the laws of the Emirate of Dubai and the federal laws of the UAE, and the courts of Dubai have exclusive jurisdiction.</p>"),
], "Website Terms | Davies Kelly", "Terms of use for davieskelly.com. Information on this site is not advice.", "Terms")

# ================================================================ 404 + redirect stub
body = '<div class="wrap measure section"><h1>Page not found</h1><p>The page you asked for is not here. It may have moved when we rebuilt our website.</p><div class="btn-row" style="grid-template-columns:1fr"><a class="btn block" href="/">Home</a><a class="btn secondary block" href="/experts/">Our experts</a><a class="btn secondary block" href="/services/">Services</a><a class="btn secondary block" href="/contact/">Contact us</a></div></div>'
page("/404.html", "Page not found | Davies Kelly", "Page not found.", body, noindex=True, cta=False)
os.makedirs("contact-us", exist_ok=True)
open("contact-us/index.html", "w", encoding="utf-8").write('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Contact us | Davies Kelly</title><meta name="robots" content="noindex"><link rel="canonical" href="https://davieskelly.com/contact/"><meta http-equiv="refresh" content="0; url=/contact/"></head><body><p>This page has moved to <a href="/contact/">Contact us</a>.</p></body></html>\n')

# ================================================================ vCards (E.7) — confirmed fields only
os.makedirs("vcard", exist_ok=True)
for slug in ORDER:
    p = PEOPLE[slug]
    last, firstn = p["name"].split()[-1], p["name"].split()[0]
    lines = ["BEGIN:VCARD", "VERSION:3.0", f"N:{last};{firstn};;;", f"FN:{p['name']}", "ORG:Davies Kelly"]
    if slug in ("michael-roos", "jamie-shafto"):
        lines += [f"TEL;TYPE=CELL,VOICE:{p['tel']}", f"EMAIL;TYPE=WORK:{p['mail']}", "ADR;TYPE=WORK:;;48 Burj Gate Tower, Sheikh Zayed Road, Downtown;Dubai;;116171;United Arab Emirates"]
    lines += [f"URL:{SITE}/experts/{slug}/", "END:VCARD"]
    open(f"vcard/{slug}.vcf", "w", encoding="utf-8", newline="\r\n").write("\n".join(lines) + "\n")

# ================================================================ FOUR CORE SERVICES (old WordPress addresses kept)
def core_page(path, name, lead, blocks, related, title, desc):
    h, bc = head(name, lead, [("Home", "/"), ("Services", "/services/"), (name, None)])
    inner = "".join(f"<h2>{t}</h2>{c}" for t, c in blocks)
    rel = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in related)
    body = h + f'<section class="wrap measure" style="padding-bottom:var(--sec)">{inner}<h2>Related</h2><ul class="plain">{rel}</ul><p style="margin-top:28px"><a class="btn" href="/contact/">Discuss a matter</a></p></section>'
    page(path, title, desc, body, [bc])


core_page("/pre-contract-advice/", "Pre-contract advice",
    "Before a construction project starts, contractors and employers need a clear understanding of the objectives, and a contract that defines each party’s obligations and works in practice.",
    [("What we do", "<p>We review and draft construction contracts and professional services agreements, and identify contractual risk. We check that obligations and responsibilities are clearly defined and that the contract’s mechanisms and provisions are workable.</p>"),
     ("Why it matters", "<p>We highlight adverse risks and explain their consequences, so they can be removed or managed before you sign. Time spent on the contract at the start is usually far cheaper than resolving a dispute later.</p>"),
     ("Example", "<p>A UAE civil engineering contractor asked us to review the contract for a large infrastructure project. We found ambiguities and inconsistencies and a risk that could have led to a loss of around USD 1 million. Our client renegotiated and agreed revised terms.</p>")],
    [("Project advisory", "/project-advisory/"), ("Claim review and advisory", "/services/advisory/")],
    "Pre-Contract Advice | Davies Kelly", "Review and drafting of construction contracts and professional services agreements, and identification of contractual risk, from Dubai.")

core_page("/project-advisory/", "Project advisory",
    "Time, cost and quality are the three key variables on any construction project. We help contractors and employers deliver on time and on budget without compromising quality.",
    [("What we do", "<p>Drawing on our experience at project level, we put in place processes, procedures and tools that let our clients manage and reduce risk.</p>"),
     ("Our expertise", ul(["Project controls", "Planning and scheduling", "Cost estimating and management", "Scope and change management", "Earned value management", "Document control", "Project and progress reporting", "Schedule management", "Commercial management", "Risk management and mitigation"])),
     ("Example", "<p>We reviewed a contractor’s project systems, processes and procedures against its contractual obligations, put in place procedures to manage the commercial and contractual risks that had not been addressed, and reported on progress throughout construction.</p>")],
    [("Pre-contract advice", "/pre-contract-advice/"), ("Delay expert evidence", "/services/delay/")],
    "Project Advisory | Davies Kelly", "Project controls, planning and scheduling, cost and change management, and commercial and risk management for construction projects.")

core_page("/dispute-resolution/", "Dispute resolution",
    "Prevention is better than cure, but claims for time and money often arise during construction and too often become disputes. We help clients identify and resolve them, before and after they arise.",
    [("What we do", "<p>We act for employers, main contractors and subcontractors in preparing and defending extension of time and cost claims, and we help parties resolve claims through impartial third-party advice and determinations.</p>"),
     ("Our expertise", ul(["Claim preparation", "Claim defence", "Independent determinations"])),
     ("Example", "<p>For a UAE main contractor we built a consolidated extension of time and cost claim from first principles, focused on the issues with the greatest impact, and managed it through to the engineer’s determination. The contractor was awarded an extension of time of about a year and around USD 10 million.</p>"),
     ("Advice and evidence are different roles", "<p>When we advise on a claim we work in your interest. If we are later asked to act as the independent expert in the same dispute, we tell you at the outset, because an expert’s duty is to the tribunal.</p>")],
    [("Expert witness services", "/expert-witness-services/"), ("Independence", "/independence/")],
    "Dispute Resolution | Davies Kelly", "Preparation and defence of extension of time and cost claims, and independent determinations, for construction disputes.")

core_page("/expert-witness-services/", "Expert witness services",
    "Expert evidence is a key element of any formal dispute. Our experts are appointed by international law firms and contractors to give independent opinion evidence.",
    [("What we do", "<p>We give written and oral expert evidence in international arbitration, court proceedings and adjudication. Our experts have given evidence in ICC and DIAC arbitrations and have been cross-examined by King’s Counsel.</p>"),
     ("Our disciplines", ul(['<a href="/services/quantum/">Quantum</a>', '<a href="/services/delay/">Delay</a>', "Disruption", '<a href="/services/technical/">Technical and engineering</a>'])),
     ("Our duty", "<p>An expert’s overriding duty is to the tribunal or court, not to the party that instructs or pays them. Our opinions are reasoned, evidence-based and independent. <a href='/independence/'>How we keep our evidence independent</a>.</p>")],
    [("Our experts", "/experts/"), ("Selected experience", "/experience/")],
    "Expert Witness Services | Davies Kelly", "Independent quantum, delay, disruption and technical expert witness services in ICC and DIAC arbitration, court and adjudication.")

# ================================================================ robots, sitemap, llms (H.6–H.8)
open("robots.txt", "w").write("""# davieskelly.com: open to all crawlers, including AI search and assistant crawlers
User-agent: *
Allow: /
Disallow: /_tools/

User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: Bingbot
User-agent: CCBot
Allow: /
Disallow: /_tools/

Sitemap: https://davieskelly.com/sitemap.xml
""")
urls = [p["path"] for p in PAGES if not p["noindex"]]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open("sitemap.xml", "w").write(sm)
open("llms.txt", "w").write(f"""# Davies Kelly

> Davies Kelly is an international construction consultancy in Dubai providing pre-contract advice, project advisory, dispute resolution and expert witness services (independent quantum, delay and technical experts) for construction and engineering disputes. Its experts give written and oral expert evidence in international arbitration, court proceedings and adjudication across the Middle East, Africa, Asia and Europe, and it also reviews claims and advises on contracts before and during disputes. When appointed as experts, its people owe their duty to the tribunal or court.

## Experts
- [Michael Roos]({SITE}/experts/michael-roos/): founding partner and testifying quantum expert; BSc (Hons) Quantity Surveying (Glasgow Caledonian University), LLM Construction Law, Arbitration and Adjudication (Robert Gordon University), MCIArb; prolongation, disruption, head office overheads, variations, defects and final accounts; Middle East, North Africa, UK and Europe.
- [Jamie Shafto]({SITE}/experts/jamie-shafto/): founding partner and testifying delay expert; appointed in ICC and DIAC arbitrations; oral evidence under cross-examination by King's Counsel; forensic delay and disruption analysis; UK and MENA.
- [Stephen M John]({SITE}/experts/stephen-john/): Eur Ing, chartered civil engineer, FICE, FCIArb, MCIHT; independent technical and FIDIC contract evidence.
- [Michael Whiting]({SITE}/experts/michael-whiting/): quantum and claims consultant supporting the quantum experts; BSc (Hons) Quantity Surveying, RICS Expert Witness Certificate.

## Services
- [Pre-contract advice]({SITE}/pre-contract-advice/): review and drafting of construction contracts and professional services agreements; contractual risk.
- [Project advisory]({SITE}/project-advisory/): project controls, planning and scheduling, cost and change management, commercial and risk management.
- [Dispute resolution]({SITE}/dispute-resolution/): preparation and defence of extension of time and cost claims; independent determinations.
- [Expert witness services]({SITE}/expert-witness-services/): independent quantum, delay, disruption and technical expert evidence in arbitration, court and adjudication.
- [Quantum expert evidence]({SITE}/services/quantum/): prolongation, disruption (including measured mile), head office overheads, variations, liquidated damages, defects counterclaims, final accounts.
- [Delay expert evidence]({SITE}/services/delay/): forensic delay analysis, disruption, extension of time entitlement, independent determinations.
- [Claim review and advisory]({SITE}/services/advisory/): independent claim reviews, claim preparation and defence, contract and project advice. Kept separate from expert appointments.

## How we work
- [Independence]({SITE}/independence/): duty to the tribunal; seven conduct rules; conflict checks before documents; one role per dispute; client matters are never named.
- [Experience]({SITE}/experience/): anonymised matters by sector, region, forum and role.

## Contact
- [Contact and conflict check]({SITE}/contact/): Davies Kelly, {ADDRESS}. Please do not send confidential documents before the conflict check.
""")

# facts file for the checker
json.dump({s: {"name": PEOPLE[s]["name"], "tel_d": PEOPLE[s]["tel_d"], "mail": PEOPLE[s].get("mail")} for s in ORDER}, open("_tools/facts.json", "w"), indent=1)
print(len(PAGES), "pages written")
