import csv

CSV_FILE_PATH = "State.csv"
OWL_FILE_PATH = "output.owl"

with open(CSV_FILE_PATH, "r") as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)
    class_dict = {header_row[i]: header_row[i].replace(" ", "_") for i in range(len(header_row))}
    individuals = []
    for row in reader:
        individual = []
        individual_name = row[0].replace(" ", "_")
        individual.append(f"<owl:NamedIndividual rdf:about=\"#{individual_name}\">")
        individual.append(f"    <rdf:type rdf:resource=\"#{class_dict[header_row[0]]}\"/>")
        for i in range(1, len(header_row)):
            if row[i] != "":
                property_name = class_dict[header_row[i]]
                individual.append(f"    <{property_name}>{row[i]}</{property_name}>")
        individual.append("</owl:NamedIndividual>")
        individuals.append('\n'.join(individual))


with open(OWL_FILE_PATH, "w") as owl_file:
    owl_file.write("""<?xml version="1.0"?>
<rdf:RDF xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns="http://example.com/ontologies/example-ontology#">\n""")
    owl_file.write('\n'.join([f'    <owl:Class rdf:about="#{class_dict[h]}" />' for h in header_row]))
    owl_file.write('\n')
    owl_file.write('\n'.join(individuals))
    owl_file.write("\n</rdf:RDF>")