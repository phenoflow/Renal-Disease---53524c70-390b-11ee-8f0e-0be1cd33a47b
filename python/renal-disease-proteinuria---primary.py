# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1Z17.11","system":"readv2"},{"code":"1Z19.11","system":"readv2"},{"code":"1Z1A.11","system":"readv2"},{"code":"1Z1B.11","system":"readv2"},{"code":"1Z1C.11","system":"readv2"},{"code":"1Z1D.11","system":"readv2"},{"code":"1Z1E.11","system":"readv2"},{"code":"1Z1F.11","system":"readv2"},{"code":"1Z1G.11","system":"readv2"},{"code":"1Z1H.11","system":"readv2"},{"code":"1Z1J.11","system":"readv2"},{"code":"1Z1K.11","system":"readv2"},{"code":"1Z1L.11","system":"readv2"},{"code":"K136.00","system":"readv2"},{"code":"K136.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-proteinuria---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-proteinuria---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-proteinuria---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
