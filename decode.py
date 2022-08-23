import math


def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def decode_binary(value):
    if value == 1:
        return "Yes"
    elif value == 2:
        return "No"
    else:
        return "Data Not Available"


def decode_obereg(value):
    if value == 0:
        return "US Service School"
    elif value == 1:
        return "New England"
    elif value == 2:
        return "Mid East"
    elif value == 3:
        return "Great Lakes"
    elif value == 4:
        return "Plains"
    elif value == 5:
        return "Southeast"
    elif value == 6:
        return "Southwest"
    elif value == 7:
        return "Rocky Mountains"
    elif value == 8:
        return "Far West"
    elif value == 9:
        return "Outlying Area"
    else:
        return "Data Not Available"


def decode_control(value):
    if value == 1:
        return "Public"
    elif value == 2:
        return "Private Not For-Profit"
    elif value == 3:
        return "Private For-Profit"
    else:
        return "Data Not Available"


def decode_iclevel(value):
    if value == 1:
        return "4-year (or higher)"
    elif value == 2:
        return "2-year (less than 4 year)"
    elif value == 3:
        return "less than 2-year"
    else:
        return "Data Not Available"


def decode_hloffer(value):
    if value == 0:
        return "Special"
    elif value == 1:
        return "Postsecondary award, certificate, or diploma of less than one academic year"
    elif value == 2:
        return "Postsecondary award, certificate, or diploma of at least 1 but less than 2 academic years"
    elif value == 3:
        return "Associate's degree"
    elif value == 4:
        return "Postsecondary award, certificate, or diploma of at least 2 but less than 4 academic years"
    elif value == 5:
        return "Bachelor's degree"
    elif value == 6:
        return "Postbaccalaureate certificate"
    elif value == 7:
        return "Master's degree"
    elif value == 8:
        return "Doctor's degree"
    else:
        return "Data Not Available"


def decode_instcat(value):
    if value == 1:
        return "Degree granting, graduate with no undergraduate degrees"
    elif value == 2:
        return "Degree granting, primarily baccalaaureate or above"
    elif value == 3:
        return "Degree granting, not primarily baccalaaureate or above"
    elif value == 4:
        return "Degree granting, Associate's and certificates"
    elif value == 5:
        return "Nondegree granting, above the baccalaureate"
    elif value == 6:
        return "Nondegree granting, sub-baccalaureate"
    else:
        return "Data not available"


def decode_c18ipug(value):
    if value == 1:
        return "Associate's Colleges, High Transfer - Awarded associate's degrees but no bachelor's degrees with fewer than 30% of awards (degrees and certificates) in career & technical programs."
    elif value == 2:
        return "Associate's Colleges, Mixed Transfer/Career & Technical - Awarded associate's degrees but no bachelor's degrees with 30-49% of awards (degrees and certificates) in career & technical programs."
    elif value == 3:
        return "Associate's Colleges, High Career & Technical - Awarded associate's degrees but no bachelor's degrees with more than 50% of awards (degrees and certificates) in career & technical programs."
    elif value == 4:
        return "Special Focus Two - Year Institutions - Awarded associate 's degrees but no bachelor's degrees with typically more than 75 % of awards in a single career & technical program."
    elif value == 5:
        return "Baccalaureate / Associate's Colleges - Awarded both associate's and bachelor's degrees, but the majority of degrees awarded were at the associate's level."
    elif value == 6:
        return "Arts & sciences focus, no graduate coexistence - At least 80 % of bachelor's degree majors were in the arts and sciences, and no graduate degrees were awarded in fields corresponding to undergraduate majors."
    elif value == 7:
        return "Arts & sciences focus, some graduate coexistence - At least 80 % of bachelor's degree majors were in the arts and sciences, and graduate degrees were observed in up to half of the fields corresponding to undergraduate majors."
    elif value == 8:
        return "Arts & sciences focus, high graduate coexistence - At least 80 % of bachelor's degree majors were in the arts and sciences, and graduate degrees were observed in at least half of the fields corresponding to undergraduate majors."
    elif value == 9:
        return "Arts & sciences plus professions, no graduate coexistence - 60–79 % of bachelor's degree majors were in the arts and sciences, and no graduate degrees were awarded in fields corresponding to undergraduate majors."
    elif value == 10:
        return "Arts & sciences plus professions, some graduate coexistence - 60–79 % of bachelor's degree majors were in the arts and sciences, and graduate degrees were observed in up to half of the fields corresponding to undergraduate majors."
    elif value == 11:
        return "Arts & sciences plus professions, high graduate coexistence - 60–79 % of bachelor's degree majors were in the arts and sciences, and graduate degrees were observed in at least half of the fields corresponding to undergraduate majors."
    elif value == 12:
        return "Balanced arts & sciences/professions, no graduate coexistence - Bachelor's degrees awarded were relatively balanced between arts and sciences and professional fields (41–59 % in each), and no graduate degrees were awarded in fields corresponding to undergraduate majors."
    elif value == 13:
        return "Balanced arts & sciences/professions, some graduate coexistence -Bachelor's degree majors were relatively balanced between arts and sciences and professional fields (41–59 % in each), and graduate degrees were observed in up to half of the fields corresponding to undergraduate majors."
    elif value == 14:
        return "Balanced arts & sciences/professions, high graduate coexistence - Bachelor's degree majors were relatively balanced between arts and sciences and professional fields (41–59 % in each), and graduate degrees were observed in at least half of the fields corresponding to undergraduate majors."
    elif value == 15:
        return "Professions plus arts & sciences, no graduate coexistence - 60–79 % of bachelor's degree majors were in professional fields (such as business, education, engineering, health, and social employment), and no graduate degrees were awarded in fields corresponding to undergraduate majors." ""
    elif value == 16:
        return "Professions plus arts & sciences, some graduate coexistence - 60–79 % of bachelor's degree majors were in professional fields, and graduate degrees were observed in up to half of the fields corresponding to undergraduate majors."
    elif value == 17:
        return "Professions plus arts & sciences, high graduate coexistence - 60–79 % of bachelor's degree majors were in professional fields, and graduate degrees were observed in at least half of the fields corresponding to undergraduate majors."
    elif value == 18:
        return "Professions focus, no graduate coexistence - At least 80 % of bachelor's degree majors were in professional fields (such as business, education, engineering, health, and social employment), and no graduate degrees were awarded in fields corresponding to undergraduate majors."
    elif value == 19:
        return "Professions focus, some graduate coexistence - At least 80 % of bachelor's degree majors were in professional fields, and graduate degrees were observed in up to half of the fields corresponding to undergraduate majors."
    elif value == 20:
        return "Professions focus, high graduate coexistence - At least 80 % of bachelor's degree majors were in professional fields, and graduate degrees were observed in at least half of the fields corresponding to undergraduate majors."
    else:
        return "Data not available"


def decode_c18ipgrd(value):
    if value == 1:
        return "Postbaccalaureate: Single program - Education - Awarded master's or professional practice/other doctoral degrees in education as their only postbaccalaureate program."
    elif value == 2:
        return "Postbaccalaureate: Single program - Business -  Awarded master's or professional practice/other doctoral degrees in business as their only postbaccalaureate program."
    elif value == 3:
        return "Postbaccalaureate: Single program - Other - Awarded master's or professional practice/other doctoral degrees in a single field other than education or business as their only postbaccalaureate program."
    elif value == 4:
        return "Postbaccalaureate: Comprehensive programs - Awarded at least one master's degree or professional practice/other doctoral degrees in each of the humanities, social sciences, and STEM* fields, as well as such graduate degrees in one or more professional fields."
    elif value == 5:
        return "Postbaccalaureate: Arts & sciences-dominant - Awarded master's or professional practice/other doctoral degrees in some arts and sciences fields. They may also award master's or non-research doctoral degrees in other fields, but in lesser numbers."
    elif value == 6:
        return "Postbaccalaureate: Education-dominant, with arts & sciences - Awarded master's or professional practice/other doctoral degrees in both arts and sciences and professional fields, and the field with the largest number of such graduate degrees was education."
    elif value == 7:
        return "Postbaccalaureate: Business-dominant, with arts & sciences - Awarded master's or professional practice/other doctoral degrees in both arts and sciences and professional fields, and the field with the largest number of such graduate degrees was business."
    elif value == 8:
        return "Postbaccalaureate: Other-dominant, with arts & sciences - Awarded master's or professional practice/other doctoral degrees in both arts and sciences and professional fields, and the field with the largest number of such graduate degrees was a professional field other than business or education."
    elif value == 9:
        return "Postbaccalaureate: Education-dominant, with other professional programs - Awarded master's or professional practice/other doctoral degrees in professional fields only, and the field with the largest number of such graduate degrees was education."
    elif value == 10:
        return "Postbaccalaureate: Business-dominant, with other professional programs - Awarded master's or professional practice/other doctoral degrees in professional fields only, and the field with the largest number of such graduate degrees was business."
    elif value == 11:
        return "Postbaccalaureate: Other-dominant, with other professional programs - Awarded master's or professional practice/other doctoral degrees in professional fields only, and the field with the largest number of such graduate degrees was a field other than business or education."
    elif value == 12:
        return "Research Doctoral: Single program - Education - Awarded research doctoral degrees in education but not in other fields (they may have more extensive offerings at the master's or professional practice/other doctoral level)."
    elif value == 13:
        return "Research Doctoral: Single program - Other -  Awarded research doctoral degrees in a single field other than education (they may have more extensive offerings at the master's or professional practice/other doctoral level)."
    elif value == 14:
        return "Research Doctoral: Comprehensive programs, with medical/veterinary school - Awarded research doctoral degrees in the humanities, social sciences, and STEM* fields, as well as in medicine, dentistry, and/or veterinary medicine. They also offer may also offer master's and professional practice/other doctoral degrees in other fields."
    elif value == 15:
        return "Research Doctoral: Comprehensive programs, no medical/veterinary school - Awarded research doctoral degrees in the humanities, social sciences, and STEM* fields. They may also offer master's or professional practice/other degrees in fields other than medicine, dentistry, or veterinary medicine."
    elif value == 16:
        return "Research Doctoral: Humanities/social sciences-dominant - Awarded research doctoral degrees in a range of fields, with the largest number of research doctorates in the humanities or social sciences."
    elif value == 17:
        return "Research Doctoral: STEM-dominant - Awarded research doctoral degrees in a range of fields, with the largest number of research doctorates in the STEM* fields."
    elif value == 18:
        return "Research Doctoral: Professional-dominant - Awarded research doctoral degrees in a range of fields, and the largest number of research doctorates were in professions other than engineering (such as education, health professions, law, public policy, or social employment)."
    else:
        return "Data not available"


def decode_c18ugprf(value):
    if value == 1:
        return "Higher part-time -  60 percent of undergraduates are enrolled part-time at these associate's degree granting institutions."
    elif value == 2:
        return "Mixed part/full-time - 40–59 percent of undergraduates are enrolled part-time at these associate's degree granting institutions."
    elif value == 3:
        return "Medium full-time -  10–39 percent of undergraduates are enrolled part-time at these associate's degree granting institutions."
    elif value == 4:
        return "Higher full-time -  Less than 10 percent of undergraduates enrolled part-time at these associate's degree granting institutions."
    elif value == 5:
        return "Higher part-time - At least 40 percent of undergraduates are enrolled part-time at these bachelor's or higher degree granting institutions."
    elif value == 6:
        return "Medium full-time, inclusive, lower transfer-in - 60–79 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. These institutions either did not report test score data or the scores indicate that they extend educational opportunity to a wide range of students with respect to academic preparation and achievement. Fewer than 20 percent of entering undergraduates are transfer students."
    elif value == 7:
        return"Medium full-time, inclusive, higher transfer-in - 60–79 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. These institutions either did not report test score data or the scores indicate that they extend educational opportunity to a wide range of students with respect to academic preparation and achievement. At least 20 percent of entering undergraduates are transfer students."
    elif value == 8:
        return "Medium full-time, selective or more selective, lower transfer-in - 60–79 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are selective or more selective in admissions. Fewer than 20 percent of entering undergraduates are transfer students."
    elif value == 9:
        return "Medium full-time, selective or more selective, higher transfer-in - 60–79 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are selective or more selective in admissions. At least 20 percent of entering undergraduates are transfer students."
    elif value == 10:
        return "Full-time, inclusive, lower transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. These institutions either did not report test score data or the scores indicate that they extend educational opportunity to a wide range of students with respect to academic preparation and achievement. Fewer than 20 percent of entering undergraduates are transfer students."
    elif value == 11:
        return "Full-time, inclusive, higher transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. These institutions either did not report test score data or the scores indicate that they extend educational opportunity to a wide range of students with respect to academic preparation and achievement. At least 20 percent of entering undergraduates are transfer students."
    elif value == 12:
        return "Full-time, selective, lower transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are selective in admissions (40th to 80th percentile of selectivity among all baccalaureate institutions). Fewer than 20 percent of entering undergraduates are transfer students."
    elif value == 13:
        return "Full-time, selective, higher transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are selective in admissions (40th to 80th percentile of selectivity among all baccalaureate institutions). At least 20 percent of entering undergraduates are transfer students."
    elif value == 14:
        return "Full-time, more selective, lower transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are more selective in admissions (80th to 100th percentile of selectivity among all baccalaureate institutions). Fewer than 20 percent of entering undergraduates are transfer students."
    elif value == 15:
        return "Full-time, more selective, higher transfer-in - At least 80 percent of undergraduates are enrolled full-time at these bachelor's or higher degree granting institutions. Test score data for first-year students indicate that these institutions are more selective in admissions (80th to 100th percentile of selectivity among all baccalaureate institutions). At least 20 percent of entering undergraduates are transfer students."
    else:
        return "Data not available"


def decode_c18enprf(value):
    if value == 1:
        return "Exclusively undergraduate two-year - Only undergraduates enrolled at these associate's degree granting institutions."
    elif value == 2:
        return "Exclusively undergraduate four-year - Only undergraduates enrolled at these bachelor's or higher degree granting institutions."
    elif value == 3:
        return "Very high undergraduate - Undergraduate and graduate students enrolled, with the latter group accounting for less than 10 % of FTE* enrollment."
    elif value == 4:
        return "High undergraduate - Undergraduate and graduate students enrolled, with the latter group accounting for 10–24 % of FTE* enrollment."
    elif value == 5:
        return "Majority undergraduate - Undergraduate and graduate students enrolled, with the latter group accounting for 25–49 % of FTE* enrollment."
    elif value == 6:
        return "Majority graduate - Undergraduate and graduate students enrolled, with the latter group accounting for at least half of FTE* enrollment."
    elif value == 7:
        return "Exclusively graduate - Only graduate students enrolled."
    else:
        return "Data not available"


specific_degrees = {
    1.00: 'Agriculture, General',
    1.01: 'Agricultural Business and Management',
    1.02: 'Agricultural Mechanization',
    1.03: 'Agricultural Production Operations',
    1.04: 'Agricultural and Food Products Processing',
    1.05: 'Agricultural and Domestic Animal Services',
    1.06: 'Applied Horticulture and Horticultural Business Services',
    1.07: 'International Agriculture',
    1.08: 'Agricultural Public Services',
    1.09: 'Animal Sciences',
    1.10: 'Food Science and Technology',
    1.11: 'Plant Sciences',
    1.12: 'Soil Sciences',
    1.13: 'Agriculture/Veterinary Preparatory Programs',
    1.80: 'Veterinary Medicine',
    1.81: 'Veterinary Biomedical and Clinical Sciences',
    1.82: 'Veterinary Administrative Services',
    1.83: 'Veterinary/Animal Health Technologies/Technicians',
    1.99: 'Agricultural/Animal/Plant/Veterinary Science and Related Fields, Other',
    3.01: 'Natural Resources Conservation and Research',
    3.02: 'Environmental/Natural Resources Management and Policy',
    3.03: 'Fishing and Fisheries Sciences and Management',
    3.05: 'Forestry',
    3.06: 'Wildlife and Wildlands Science and Management',
    3.99: 'Natural Resources and Conservation, Other',
    4.02: 'Architecture',
    4.03: 'City/Urban, Community, and Regional Planning',
    4.04: 'Environmental Design',
    4.05: 'Interior Architecture',
    4.06: 'Landscape Architecture',
    4.08: 'Architectural History, Criticism, and Conservation',
    4.09: 'Architectural Sciences and Technology',
    4.10: 'Real Estate Development',
    4.99: 'Architecture and Related Services, Other',
    5.01: 'Area Studies',
    5.02: 'Ethnic, Cultural Minority, Gender, and Group Studies',
    5.99: 'Area, Ethnic, Cultural, Gender, and Group Studies, Other',
    9.01: 'Communication and Media Studies',
    9.04: 'Journalism',
    9.07: 'Radio, Television, and Digital Communication',
    9.09: 'Public Relations, Advertising, and Applied Communication',
    9.10: 'Publishing',
    9.99: 'Communication, Journalism, and Related Programs, Other',
    10.01: 'Communications Technologies/Technicians',
    10.02: 'Audiovisual Communications Technologies/Technicians',
    10.03: 'Graphic Communications',
    10.99: 'Communications Technologies/Technicians and Support Services, Other',
    11.01: 'Computer and Information Sciences, General',
    11.02: 'Computer Programming',
    11.03: 'Data Processing',
    11.04: 'Information Science/Studies',
    11.05: 'Computer Systems Analysis',
    11.06: 'Data Entry/Microcomputer Applications',
    11.07: 'Computer Science',
    11.08: 'Computer Software and Media Applications',
    11.09: 'Computer Systems Networking and Telecommunications',
    11.10: 'Computer/Information Technology Administration and Management',
    11.99: 'Computer and Information Sciences and Support Services, Other',
    12.03: 'Funeral Service and Mortuary Science',
    12.04: 'Cosmetology and Related Personal Grooming Services',
    12.05: 'Culinary Arts and Related Services',
    12.06: 'Casino Operations and Services',
    12.99: 'Culinary, Entertainment, and Personal Services, Other',
    13.01: 'Education, General',
    13.02: 'Bilingual, Multilingual, and Multicultural Education',
    13.03: 'Curriculum and Instruction',
    13.04: 'Educational Administration and Supervision',
    13.05: 'Educational/Instructional Media Design',
    13.06: 'Educational Assessment, Evaluation, and Research',
    13.07: 'International and Comparative Education',
    13.09: 'Social and Philosophical Foundations of Education',
    13.10: 'Special Education and Teaching',
    13.11: 'Student Counseling and Personnel Services',
    13.12: 'Teacher Education and Professional Development, Specific Levels and Methods',
    13.13: 'Teacher Education and Professional Development, Specific Subject Areas',
    13.14: 'Teaching English or French as a Second or Foreign Language',
    13.15: 'Teaching Assistants/Aides',
    13.99: 'Education, Other',
    14.01: 'Engineering, General',
    14.02: 'Aerospace, Aeronautical, and Astronautical/Space Engineering',
    14.03: 'Agricultural Engineering',
    14.04: 'Architectural Engineering',
    14.05: 'Biomedical/Medical Engineering',
    14.06: 'Ceramic Sciences and Engineering',
    14.07: 'Chemical Engineering',
    14.08: 'Civil Engineering',
    14.09: 'Computer Engineering',
    14.10: 'Electrical, Electronics, and Communications Engineering',
    14.11: 'Engineering Mechanics',
    14.12: 'Engineering Physics',
    14.13: 'Engineering Science',
    14.14: 'Environmental/Environmental Health Engineering',
    14.18: 'Materials Engineering',
    14.19: 'Mechanical Engineering',
    14.20: 'Metallurgical Engineering',
    14.21: 'Mining and Mineral Engineering',
    14.22: 'Naval Architecture and Marine Engineering',
    14.23: 'Nuclear Engineering',
    14.24: 'Ocean Engineering',
    14.25: 'Petroleum Engineering',
    14.27: 'Systems Engineering',
    14.28: 'Textile Sciences and Engineering',
    14.32: 'Polymer/Plastics Engineering',
    14.33: 'Construction Engineering',
    14.34: 'Forest Engineering',
    14.35: 'Industrial Engineering',
    14.36: 'Manufacturing Engineering',
    14.37: 'Operations Research',
    14.38: 'Surveying Engineering',
    14.39: 'Geological/Geophysical Engineering',
    14.40: 'Paper Science and Engineering',
    14.41: 'Electromechanical Engineering',
    14.42: 'Mechatronics, Robotics, and Automation Engineering',
    14.43: 'Biochemical Engineering',
    14.44: 'Engineering Chemistry',
    14.45: 'Biological/Biosystems Engineering',
    14.47: 'Electrical and Computer Engineering',
    14.48: 'Energy Systems Engineering',
    14.99: 'Engineering, Other',
    15.00: 'Engineering Technologies/Technicians, General',
    15.01: 'Architectural Engineering Technologies/Technicians',
    15.02: 'Civil Engineering Technologies/Technicians',
    15.03: 'Electrical/Electronic Engineering Technologies/Technicians',
    15.04: 'Electromechanical Technologies/Technicians',
    15.05: 'Environmental Control Technologies/Technicians',
    15.06: 'Industrial Production Technologies/Technicians',
    15.07: 'Quality Control and Safety Technologies/Technicians',
    15.08: 'Mechanical Engineering Related Technologies/Technicians',
    15.09: 'Mining and Petroleum Technologies/Technicians',
    15.10: 'Construction Engineering Technology/Technician',
    15.11: 'Engineering-Related Technologies/Technicians',
    15.12: 'Computer Engineering Technologies/Technicians',
    15.13: 'Drafting/Design Engineering Technologies/Technicians',
    15.14: 'Nuclear Engineering Technology/Technician',
    15.15: 'Engineering-Related Fields',
    15.16: 'Nanotechnology',
    15.17: 'Energy Systems Technologies/Technicians',
    15.99: 'Engineering/Engineering-Related Technologies/Technicians, Other',
    16.01: 'Linguistic, Comparative, and Related Language Studies and Services',
    16.02: 'African Languages, Literatures, and Linguistics',
    16.03: 'East Asian Languages, Literatures, and Linguistics',
    16.04: 'Slavic, Baltic and Albanian Languages, Literatures, and Linguistics',
    16.05: 'Germanic Languages, Literatures, and Linguistics',
    16.06: 'Modern Greek Language and Literature',
    16.07: 'South Asian Languages, Literatures, and Linguistics',
    16.08: 'Iranian/Persian Languages, Literatures, and Linguistics',
    16.09: 'Romance Languages, Literatures, and Linguistics',
    16.10: 'American Indian/Native American Languages, Literatures, and Linguistics',
    16.11: 'Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics',
    16.12: 'Classics and Classical Languages, Literatures, and Linguistics',
    16.14: 'Southeast Asian and Australasian/Pacific Languages, Literatures, and Linguistics',
    16.15: 'Turkic, Uralic-Altaic, Caucasian, and Central Asian Languages, Literatures, and Linguistics',
    16.16: 'American Sign Language',
    16.17: 'Second Language Learning',
    16.18: 'Armenian Languages, Literatures, and Linguistics',
    16.99: 'Foreign Languages, Literatures, and Linguistics, Other',
    19.01: 'Family and Consumer Sciences/Human Sciences, General',
    19.02: 'Family and Consumer Sciences/Human Sciences Business Services',
    19.04: 'Family and Consumer Economics and Related Studies',
    19.05: 'Foods, Nutrition, and Related Services',
    19.06: 'Housing and Human Environments',
    19.07: 'Human Development, Family Studies, and Related Services',
    19.09: 'Apparel and Textiles',
    19.10: 'Work and Family Studies',
    19.99: 'Family and Consumer Sciences/Human Sciences, Other',
    21.01: 'Reserved',
    22.00: 'Non-Professional Legal Studies',
    22.01: 'Law',
    22.02: 'Legal Research and Advanced Professional Studies',
    22.03: 'Legal Support Services',
    22.99: 'Legal Professions and Studies, Other',
    23.01: 'English Language and Literature, General',
    23.13: 'Rhetoric and Composition/Writing Studies',
    23.14: 'Literature',
    23.99: 'English Language and Literature/Letters, Other',
    24.01: 'Liberal Arts and Sciences, General Studies and Humanities',
    25.01: 'Library Science and Administration',
    25.03: 'Library and Archives Assisting',
    25.99: 'Library Science, Other',
    26.01: 'Biology, General',
    26.02: 'Biochemistry, Biophysics and Molecular Biology',
    26.03: 'Botany/Plant Biology',
    26.04: 'Cell/Cellular Biology and Anatomical Sciences',
    26.05: 'Microbiological Sciences and Immunology',
    26.07: 'Zoology/Animal Biology',
    26.08: 'Genetics',
    26.09: 'Physiology, Pathology and Related Sciences',
    26.10: 'Pharmacology and Toxicology',
    26.11: 'Biomathematics, Bioinformatics, and Computational Biology',
    26.12: 'Biotechnology',
    26.13: 'Ecology, Evolution, Systematics, and Population Biology',
    26.14: 'Molecular Medicine',
    26.15: 'Neurobiology and Neurosciences',
    26.99: 'Biological and Biomedical Sciences, Other',
    27.01: 'Mathematics',
    27.03: 'Applied Mathematics',
    27.05: 'Statistics',
    27.06: 'Applied Statistics',
    27.99: 'Mathematics and Statistics, Other',
    28.01: 'Air Force ROTC, Air Science and Operations',
    28.03: 'Army ROTC, Military Science and Operations',
    28.04: 'Navy/Marine ROTC, Naval Science and Operations',
    28.05: 'Military Science and Operational Studies',
    28.06: 'Security Policy and Strategy',
    28.07: 'Military Economics and Management',
    28.08: 'Reserved',
    28.99: 'Military Science, Leadership and Operational Art, Other',
    29.02: 'Intelligence, Command Control and Information Operations',
    29.03: 'Military Applied Sciences',
    29.04: 'Military Systems and Maintenance Technology',
    29.05: 'Reserved',
    29.06: 'Military Technology and Applied Sciences Management',
    29.99: 'Military Technologies and Applied Sciences, Other',
    30.00: 'Multi-/Interdisciplinary Studies, General',
    30.01: 'Biological and Physical Sciences',
    30.05: 'Peace Studies and Conflict Resolution',
    30.06: 'Systems Science and Theory',
    30.08: 'Mathematics and Computer Science',
    30.10: 'Biopsychology',
    30.11: 'Gerontology',
    30.12: 'Historic Preservation and Conservation',
    30.13: 'Medieval and Renaissance Studies',
    30.14: 'Museology/Museum Studies',
    30.15: 'Science, Technology and Society',
    30.16: 'Accounting and Computer Science',
    30.17: 'Behavioral Sciences',
    30.18: 'Natural Sciences',
    30.19: 'Nutrition Sciences',
    30.20: 'International/Globalization Studies',
    30.21: 'Holocaust and Related Studies',
    30.22: 'Classical and Ancient Studies',
    30.23: 'Intercultural/Multicultural and Diversity Studies',
    30.25: 'Cognitive Science',
    30.26: 'Cultural Studies/Critical Theory and Analysis',
    30.27: 'Human Biology',
    30.28: 'Dispute Resolution',
    30.29: 'Maritime Studies',
    30.30: 'Computational Science',
    30.31: 'Human Computer Interaction',
    30.32: 'Marine Sciences',
    30.33: 'Sustainability Studies',
    30.34: 'Anthrozoology',
    30.35: 'Climate Science',
    30.36: 'Cultural Studies and Comparative Literature',
    30.37: 'Design for Human Health',
    30.38: 'Earth Systems Science',
    30.39: 'Economics and Computer Science',
    30.40: 'Economics and Foreign Language/Literature',
    30.41: 'Environmental Geosciences',
    30.42: 'Geoarcheaology',
    30.43: 'Geobiology',
    30.44: 'Geography and Environmental Studies',
    30.45: 'History and Language/Literature',
    30.46: 'History and Political Science',
    30.47: 'Linguistics and Anthropology',
    30.48: 'Linguistics and Computer Science',
    30.49: 'Mathematical Economics',
    30.50: 'Mathematics and Atmospheric/Oceanic Science',
    30.51: 'Philosophy, Politics, and Economics',
    30.52: 'Digital Humanities and Textual Studies',
    30.53: 'Thanatology',
    30.70: 'Data Science',
    30.71: 'Data Analytics',
    30.99: 'Multi/Interdisciplinary Studies, Other',
    31.01: 'Parks, Recreation, and Leisure Studies',
    31.03: 'Parks, Recreation, and Leisure Facilities Management',
    31.05: 'Sports, Kinesiology, and Physical Education/Fitness',
    31.06: 'Outdoor Education',
    31.99: 'Parks, Recreation, Leisure, Fitness, and Kinesiology, Other',
    32.01: 'Basic Skills and Developmental/Remedial Education',
    32.02: 'General Exam Preparation and Test-Taking Skills',
    33.01: 'Citizenship Activities',
    34.01: 'Health-Related Knowledge and Skills',
    35.01: 'Interpersonal and Social Skills',
    36.01: 'Leisure and Recreational Activities',
    36.02: 'Noncommercial Vehicle Operation',
    37.01: 'Personal Awareness and Self-Improvement',
    38.00: 'Philosophy and Religious Studies, General',
    38.01: 'Philosophy',
    38.02: 'Religion/Religious Studies',
    38.99: 'Philosophy and Religious Studies, Other',
    39.02: 'Bible/Biblical Studies',
    39.03: 'Missions/Missionary Studies and Missiology',
    39.04: 'Religious Education',
    39.05: 'Religious Music and Worship',
    39.06: 'Theological and Ministerial Studies',
    39.07: 'Pastoral Counseling and Specialized Ministries',
    39.08: 'Religious Institution Administration and Law',
    39.99: 'Theology and Religious Vocations, Other',
    40.01: 'Physical Sciences, General',
    40.02: 'Astronomy and Astrophysics',
    40.04: 'Atmospheric Sciences and Meteorology',
    40.05: 'Chemistry',
    40.06: 'Geological and Earth Sciences/Geosciences',
    40.08: 'Physics',
    40.10: 'Materials Sciences',
    40.11: 'Physics and Astronomy',
    40.99: 'Physical Sciences, Other',
    41.00: 'Science Technologies/Technicians, General',
    41.01: 'Biology/Biotechnology Technologies/Technicians',
    41.02: 'Nuclear and Industrial Radiologic Technologies/Technicians',
    41.03: 'Physical Science Technologies/Technicians',
    41.99: 'Science Technologies/Technicians, Other',
    42.01: 'Psychology, General',
    42.27: 'Research and Experimental Psychology',
    42.28: 'Clinical, Counseling and Applied Psychology',
    42.99: 'Psychology, Other',
    43.01: 'Criminal Justice and Corrections',
    43.02: 'Fire Protection',
    43.03: 'Homeland Security',
    43.04: 'Security Science and Technology',
    43.99: 'Homeland Security, Law Enforcement, Firefighting and Related Protective Services, Other',
    44.00: 'Human Services, General',
    44.02: 'Community Organization and Advocacy',
    44.04: 'Public Administration',
    44.05: 'Public Policy Analysis',
    44.07: 'Social Work',
    44.99: 'Public Administration and Social Service Professions, Other',
    45.01: 'Social Sciences, General',
    45.02: 'Anthropology',
    45.03: 'Archeology',
    45.04: 'Criminology',
    45.05: 'Demography',
    45.06: 'Economics',
    45.07: 'Geography and Cartography',
    45.09: 'International Relations and National Security Studies',
    45.10: 'Political Science and Government',
    45.11: 'Sociology',
    45.12: 'Urban Studies/Affairs',
    45.13: 'Sociology and Anthropology',
    45.15: 'Geography and Anthropology',
    45.99: 'Social Sciences, Other',
    46.00: 'Construction Trades, General',
    46.01: 'Mason/Masonry',
    46.02: 'Carpenters',
    46.03: 'Electrical and Power Transmission Installers',
    46.04: 'Building/Construction Finishing, Management, and Inspection',
    46.05: 'Plumbing and Related Water Supply Services',
    46.99: 'Construction Trades, Other',
    47.00: 'Mechanics and Repairers, General',
    47.01: 'Electrical/Electronics Maintenance and Repair Technologies/Technicians',
    47.02: 'Heating, Air Conditioning, Ventilation and Refrigeration Maintenance Technology/Technician (HAC, HACR, HVAC, HVACR)',
    47.03: 'Heavy/Industrial Equipment Maintenance Technologies/Technicians',
    47.04: 'Precision Systems Maintenance and Repair Technologies/Technicians',
    47.06: 'Vehicle Maintenance and Repair Technologies/Technicians',
    47.07: 'Energy Systems Maintenance and Repair Technologies/Technicians',
    47.99: 'Mechanic and Repair Technologies/Technicians, Other',
    48.00: 'Precision Production Trades, General',
    48.03: 'Leatherworking and Upholstery',
    48.05: 'Precision Metal Working',
    48.07: 'Woodworking',
    48.08: 'Boilermaking/Boilermaker',
    48.99: 'Production, Other',
    49.01: 'Air Transportation',
    49.02: 'Ground Transportation',
    49.03: 'Marine Transportation',
    49.99: 'Transportation and Materials Moving, Other',
    50.01: 'Visual and Performing Arts, General',
    50.02: 'Crafts/Craft Design, Folk Art and Artisanry',
    50.03: 'Dance',
    50.04: 'Design and Applied Arts',
    50.05: 'Drama/Theatre Arts and Stagecraft',
    50.06: 'Film/Video and Photographic Arts',
    50.07: 'Fine and Studio Arts',
    50.09: 'Music',
    50.10: 'Arts, Entertainment, and Media Management',
    50.11: 'Community/Environmental/Socially-Engaged Art',
    50.99: 'Visual and Performing Arts, Other',
    51.00: 'Health Services/Allied Health/Health Sciences, General',
    51.01: 'Chiropractic',
    51.02: 'Communication Disorders Sciences and Services',
    51.04: 'Dentistry',
    51.05: 'Advanced/Graduate Dentistry and Oral Sciences',
    51.06: 'Dental Support Services and Allied Professions',
    51.07: 'Health and Medical Administrative Services',
    51.08: 'Allied Health and Medical Assisting Services',
    51.09: 'Allied Health Diagnostic, Intervention, and Treatment Professions',
    51.10: 'Clinical/Medical Laboratory Science/Research and Allied Professions',
    51.11: 'Health/Medical Preparatory Programs',
    51.12: 'Medicine',
    51.14: 'Medical Clinical Sciences/Graduate Medical Studies',
    51.15: 'Mental and Social Health Services and Allied Professions',
    51.17: 'Optometry',
    51.18: 'Ophthalmic and Optometric Support Services and Allied Professions',
    51.20: 'Pharmacy, Pharmaceutical Sciences, and Administration',
    51.22: 'Public Health',
    51.23: 'Rehabilitation and Therapeutic Professions',
    51.26: 'Health Aides/Attendants/Orderlies',
    51.27: 'Medical Illustration and Informatics',
    51.31: 'Dietetics and Clinical Nutrition Services',
    51.32: 'Health Professions Education, Ethics, and Humanities',
    51.33: 'Alternative and Complementary Medicine and Medical Systems',
    51.34: 'Alternative and Complementary Medical Support Services',
    51.35: 'Somatic Bodywork and Related Therapeutic Services',
    51.36: 'Movement and Mind-Body Therapies and Education',
    51.37: 'Energy and Biologically Based Therapies',
    51.38: 'Registered Nursing, Nursing Administration, Nursing Research and Clinical Nursing',
    51.39: 'Practical Nursing, Vocational Nursing and Nursing Assistants',
    51.99: 'Health Professions and Related Clinical Sciences, Other',
    52.01: 'Business/Commerce, General',
    52.02: 'Business Administration, Management and Operations',
    52.03: 'Accounting and Related Services',
    52.04: 'Business Operations Support and Assistant Services',
    52.05: 'Business/Corporate Communications',
    52.06: 'Business/Managerial Economics',
    52.07: 'Entrepreneurial and Small Business Operations',
    52.08: 'Finance and Financial Management Services',
    52.09: 'Hospitality Administration/Management',
    52.10: 'Human Resources Management and Services',
    52.11: 'International Business',
    52.12: 'Management Information Systems and Services',
    52.13: 'Management Sciences and Quantitative Methods',
    52.14: 'Marketing',
    52.15: 'Real Estate',
    52.16: 'Taxation',
    52.17: 'Insurance',
    52.18: 'General Sales, Merchandising and Related Marketing Operations',
    52.19: 'Specialized Sales, Merchandising and Marketing Operations',
    52.20: 'Construction Management',
    52.21: 'Telecommunications Management',
    52.99: 'Business, Management, Marketing, and Related Support Services, Other',
    53.01: 'High School/Secondary Diploma Programs',
    53.02: 'High School/Secondary Certificate Programs',
    54.01: 'History',
    55.01: 'Reserved',
    55.13: 'Reserved',
    55.14: 'Reserved',
    55.99: 'Reserved',
    60.01: 'Dental Residency/Fellowship Programs',
    60.03: 'Veterinary Residency/Fellowship Programs',
    60.07: 'Nurse Practitioner Residency/Fellowship Programs',
    60.08: 'Pharmacy Residency/Fellowship Programs',
    60.09: 'Physician Assistant Residency/Fellowship Programs',
    60.99: 'Health Professions Residency/Fellowship Programs, Other',
    61.01: 'Combined Medical Residency/Fellowship Programs',
    61.02: 'Multiple-Pathway Medical Fellowship Programs',
    61.03: 'Allergy and Immunology Residency/Fellowship Programs',
    61.04: 'Anesthesiology Residency/Fellowship Programs',
    61.05: 'Dermatology Residency/Fellowship Programs',
    61.06: 'Emergency Medicine Residency/Fellowship Programs',
    61.07: 'Family Medicine Residency/Fellowship Programs',
    61.08: 'Internal Medicine Residency/Fellowship Programs',
    61.09: 'Medical Genetics and Genomics Residency/Fellowship Programs',
    61.10: 'Neurological Surgery Residency/Fellowship Programs',
    61.11: 'Neurology Residency/Fellowship Programs',
    61.12: 'Nuclear Medicine Residency/Fellowship Programs',
    61.13: 'Obstetrics and Gynecology Residency/Fellowship Programs',
    61.14: 'Ophthalmology Residency/Fellowship Programs',
    61.15: 'Orthopedic Surgery Residency/Fellowship Programs',
    61.16: 'Osteopathic Medicine Residency/Fellowship Programs',
    61.17: 'Otolaryngology Residency/Fellowship Programs',
    61.18: 'Pathology Residency/Fellowship Programs',
    61.19: 'Pediatrics Residency/Fellowship Programs',
    61.20: 'Physical Medicine and Rehabilitation Residency/Fellowship Programs',
    61.21: 'Plastic Surgery Residency/Fellowship Programs',
    61.22: 'Podiatric Medicine Residency/Fellowship Programs',
    61.23: 'Preventive Medicine Residency/Fellowship Programs',
    61.24: 'Psychiatry Residency/Fellowship Programs',
    61.25: 'Radiation Oncology Residency/Fellowship Programs',
    61.26: 'Radiology Residency/Fellowship Programs',
    61.27: 'Surgery Residency/Fellowship Programs',
    61.28: 'Urology Residency/Fellowship Programs',
    61.99: 'Medical Residency/Fellowship Programs, Other'
}

categories = {
    1:'AGRICULTURAL/ANIMAL/PLANT/VETERINARY SCIENCE AND RELATED FIELDS',
    3: 'NATURAL RESOURCES AND CONSERVATION',
    4: 'ARCHITECTURE AND RELATED SERVICES',
    5: 'AREA, ETHNIC, CULTURAL, GENDER, AND GROUP STUDIES',
    9: 'COMMUNICATION, JOURNALISM, AND RELATED PROGRAMS',
    10: 'COMMUNICATIONS TECHNOLOGIES/TECHNICIANS AND SUPPORT SERVICES',
    11: 'COMPUTER AND INFORMATION SCIENCES AND SUPPORT SERVICES',
    12: 'CULINARY, ENTERTAINMENT, AND PERSONAL SERVICES',
    13: 'EDUCATION',
    14: 'ENGINEERING',
    15: 'ENGINEERING/ENGINEERING-RELATED TECHNOLOGIES/TECHNICIANS',
    16: 'FOREIGN LANGUAGES, LITERATURES, AND LINGUISTICS',
    19: 'FAMILY AND CONSUMER SCIENCES/HUMAN SCIENCES',
    21: 'RESERVED',
    22: 'LEGAL PROFESSIONS AND STUDIES',
    23: 'ENGLISH LANGUAGE AND LITERATURE/LETTERS',
    24: 'LIBERAL ARTS AND SCIENCES, GENERAL STUDIES AND HUMANITIES',
    25: 'LIBRARY SCIENCE',
    26: 'BIOLOGICAL AND BIOMEDICAL SCIENCES',
    27: 'MATHEMATICS AND STATISTICS',
    28: 'MILITARY SCIENCE, LEADERSHIP AND OPERATIONAL ART',
    29: 'MILITARY TECHNOLOGIES AND APPLIED SCIENCES',
    30: 'MULTI/INTERDISCIPLINARY STUDIES',
    31: 'PARKS, RECREATION, LEISURE, FITNESS, AND KINESIOLOGY',
    32: 'BASIC SKILLS AND DEVELOPMENTAL/REMEDIAL EDUCATION',
    33: 'CITIZENSHIP ACTIVITIES',
    34: 'HEALTH-RELATED KNOWLEDGE AND SKILLS',
    35: 'INTERPERSONAL AND SOCIAL SKILLS',
    36: 'LEISURE AND RECREATIONAL ACTIVITIES',
    37: 'PERSONAL AWARENESS AND SELF-IMPROVEMENT',
    38: 'PHILOSOPHY AND RELIGIOUS STUDIES',
    39: 'THEOLOGY AND RELIGIOUS VOCATIONS',
    40: 'PHYSICAL SCIENCES',
    41: 'SCIENCE TECHNOLOGIES/TECHNICIANS',
    42: 'PSYCHOLOGY',
    43: 'HOMELAND SECURITY, LAW ENFORCEMENT, FIREFIGHTING AND RELATED PROTECTIVE SERVICES',
    44: 'PUBLIC ADMINISTRATION AND SOCIAL SERVICE PROFESSIONS',
    45: 'SOCIAL SCIENCES',
    46: 'CONSTRUCTION TRADES',
    47: 'MECHANIC AND REPAIR TECHNOLOGIES/TECHNICIANS',
    48: 'PRECISION PRODUCTION',
    49: 'TRANSPORTATION AND MATERIALS MOVING',
    50: 'VISUAL AND PERFORMING ARTS',
    51: 'HEALTH PROFESSIONS AND RELATED PROGRAMS',
    52: 'BUSINESS, MANAGEMENT, MARKETING, AND RELATED SUPPORT SERVICES',
    53: 'HIGH SCHOOL/SECONDARY DIPLOMAS AND CERTIFICATES',
    54: 'HISTORY',
    55: 'RESERVED',
    60: 'HEALTH PROFESSIONS RESIDENCY/FELLOWSHIP PROGRAMS',
    61: 'MEDICAL RESIDENCY/FELLOWSHIP PROGRAMS'
}

decode_level = {
    3: "Certificates of at least 1 year but less the 2 years",
    12: "NA",
    15: "NA",
    4: "Associate's degree",
    13: "NA",
    5: "Certificates of at least 2 years but less the 4 years",
    7: "Postbaccalaureate certificate",
    17: "Doctor's degree - research/scholarship",
    8: "Master's degree", 14: "NA",
    18: "Doctor's degree - professional practice;",
    2: "Certificates of at least 12 weeks but less than 1 year",
    6: "Bachelor's degree",
    19: "Doctor's degree - other",
    1: "Certificates of less than 12 weeks includes programs",
    20: "NA",
    21: "NA"}

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}

states_reverse = dict((v, k) for k, v in states.items())


all_cipcodes = {**specific_degrees, **categories}


def decode_cipcode(cipcode):
    return specific_degrees[cipcode]