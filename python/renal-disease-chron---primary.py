# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1Z10.00","system":"readv2"},{"code":"1Z11.00","system":"readv2"},{"code":"1Z12.00","system":"readv2"},{"code":"1Z13.00","system":"readv2"},{"code":"1Z14.00","system":"readv2"},{"code":"1Z15.00","system":"readv2"},{"code":"1Z16.00","system":"readv2"},{"code":"1Z17.00","system":"readv2"},{"code":"1Z18.00","system":"readv2"},{"code":"1Z19.00","system":"readv2"},{"code":"1Z1A.00","system":"readv2"},{"code":"1Z1B.00","system":"readv2"},{"code":"1Z1C.00","system":"readv2"},{"code":"1Z1D.00","system":"readv2"},{"code":"1Z1E.00","system":"readv2"},{"code":"1Z1F.00","system":"readv2"},{"code":"1Z1G.00","system":"readv2"},{"code":"1Z1H.00","system":"readv2"},{"code":"1Z1J.00","system":"readv2"},{"code":"1Z1K.00","system":"readv2"},{"code":"1Z1L.00","system":"readv2"},{"code":"K02..12","system":"readv2"},{"code":"K05..00","system":"readv2"},{"code":"K05..11","system":"readv2"},{"code":"K05..13","system":"readv2"},{"code":"K051.00","system":"readv2"},{"code":"K052.00","system":"readv2"},{"code":"K053.00","system":"readv2"},{"code":"K054.00","system":"readv2"},{"code":"K055.00","system":"readv2"},{"code":"K100200","system":"readv2"},{"code":"Kyu2100","system":"readv2"},{"code":"SP08J00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-chron---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-chron---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-chron---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
