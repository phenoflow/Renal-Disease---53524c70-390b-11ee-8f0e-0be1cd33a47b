# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"A160200","system":"readv2"},{"code":"K03V.00","system":"readv2"},{"code":"K0A0.00","system":"readv2"},{"code":"K0A0000","system":"readv2"},{"code":"K0A0100","system":"readv2"},{"code":"K0A0600","system":"readv2"},{"code":"K0A3.00","system":"readv2"},{"code":"K0A3000","system":"readv2"},{"code":"K0A3600","system":"readv2"},{"code":"K100.00","system":"readv2"},{"code":"K100000","system":"readv2"},{"code":"K100100","system":"readv2"},{"code":"K100500","system":"readv2"},{"code":"K100z00","system":"readv2"},{"code":"K101.00","system":"readv2"},{"code":"K101000","system":"readv2"},{"code":"K101z00","system":"readv2"},{"code":"K104.00","system":"readv2"},{"code":"K106.00","system":"readv2"},{"code":"K10y.00","system":"readv2"},{"code":"K10y000","system":"readv2"},{"code":"K10y300","system":"readv2"},{"code":"K10yz00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-nephrit---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-nephrit---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-nephrit---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
