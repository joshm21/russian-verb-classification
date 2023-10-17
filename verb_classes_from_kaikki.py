import json
import csv

results = [["infinitive", "conjugation_class"]]
seen = set()
with open("kaikki_dot_org-dictionary-Russian-by-pos-verb.json", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)

        if data["lang_code"] != "ru":
            #print(f"  Non russian entry for {data['word']}")
            continue
        
        for form in data.get("forms", []):
            if "infinitive" in form["tags"] and not "dated" in form["tags"]:
                inf = form["form"]
            if "class" in form["tags"]:
                cls = form["form"]

        if not inf in seen:
            seen.add(inf)
            results.append([inf,cls]) 


with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(results)


