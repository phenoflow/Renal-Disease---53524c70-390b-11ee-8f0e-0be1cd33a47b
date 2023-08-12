# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"14D1.00","system":"readv2"},{"code":"D310100","system":"readv2"},{"code":"K0...00","system":"readv2"},{"code":"K00..00","system":"readv2"},{"code":"K00..11","system":"readv2"},{"code":"K000.00","system":"readv2"},{"code":"K000100","system":"readv2"},{"code":"K000111","system":"readv2"},{"code":"K001.00","system":"readv2"},{"code":"K00y.00","system":"readv2"},{"code":"K00y000","system":"readv2"},{"code":"K00y100","system":"readv2"},{"code":"K00y200","system":"readv2"},{"code":"K00y300","system":"readv2"},{"code":"K00yz00","system":"readv2"},{"code":"K00z.00","system":"readv2"},{"code":"K010.00","system":"readv2"},{"code":"K011.00","system":"readv2"},{"code":"K012.00","system":"readv2"},{"code":"K013.00","system":"readv2"},{"code":"K016.00","system":"readv2"},{"code":"K017.00","system":"readv2"},{"code":"K018.00","system":"readv2"},{"code":"K019.00","system":"readv2"},{"code":"K01B.00","system":"readv2"},{"code":"K01x411","system":"readv2"},{"code":"K02..00","system":"readv2"},{"code":"K02..11","system":"readv2"},{"code":"K020.00","system":"readv2"},{"code":"K021.00","system":"readv2"},{"code":"K022.00","system":"readv2"},{"code":"K023.00","system":"readv2"},{"code":"K02y.00","system":"readv2"},{"code":"K02y000","system":"readv2"},{"code":"K02y200","system":"readv2"},{"code":"K02y300","system":"readv2"},{"code":"K02yz00","system":"readv2"},{"code":"K02z.00","system":"readv2"},{"code":"K03..00","system":"readv2"},{"code":"K03..11","system":"readv2"},{"code":"K030.00","system":"readv2"},{"code":"K031.00","system":"readv2"},{"code":"K032.00","system":"readv2"},{"code":"K032000","system":"readv2"},{"code":"K032200","system":"readv2"},{"code":"K032300","system":"readv2"},{"code":"K032400","system":"readv2"},{"code":"K032500","system":"readv2"},{"code":"K032y00","system":"readv2"},{"code":"K032y11","system":"readv2"},{"code":"K032y13","system":"readv2"},{"code":"K032y14","system":"readv2"},{"code":"K032y15","system":"readv2"},{"code":"K032z00","system":"readv2"},{"code":"K033.00","system":"readv2"},{"code":"K03T.00","system":"readv2"},{"code":"K03W.00","system":"readv2"},{"code":"K03X.00","system":"readv2"},{"code":"K03y.00","system":"readv2"},{"code":"K03y000","system":"readv2"},{"code":"K03y200","system":"readv2"},{"code":"K03yz00","system":"readv2"},{"code":"K03z.00","system":"readv2"},{"code":"K08y500","system":"readv2"},{"code":"K08y511","system":"readv2"},{"code":"K08y513","system":"readv2"},{"code":"K08y700","system":"readv2"},{"code":"K0A0200","system":"readv2"},{"code":"K0A0700","system":"readv2"},{"code":"K0A1700","system":"readv2"},{"code":"K0A2200","system":"readv2"},{"code":"K0A2300","system":"readv2"},{"code":"K0A2500","system":"readv2"},{"code":"K0A2700","system":"readv2"},{"code":"K0A3200","system":"readv2"},{"code":"K0A3700","system":"readv2"},{"code":"K0A8.00","system":"readv2"},{"code":"K0C5.00","system":"readv2"},{"code":"K0y..00","system":"readv2"},{"code":"K0z..00","system":"readv2"},{"code":"K105.00","system":"readv2"},{"code":"K13yz11","system":"readv2"},{"code":"Kyu0900","system":"readv2"},{"code":"Kyu1000","system":"readv2"},{"code":"Kyu1E00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-glomerulnephritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-glomerulnephritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-glomerulnephritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
