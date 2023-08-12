# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"14V2.00","system":"readv2"},{"code":"14V2.11","system":"readv2"},{"code":"7A60600","system":"readv2"},{"code":"7L1A.11","system":"readv2"},{"code":"7L1A000","system":"readv2"},{"code":"7L1A011","system":"readv2"},{"code":"7L1A100","system":"readv2"},{"code":"7L1A200","system":"readv2"},{"code":"7L1A400","system":"readv2"},{"code":"7L1A600","system":"readv2"},{"code":"7L1B100","system":"readv2"},{"code":"7L1B200","system":"readv2"},{"code":"7L1f000","system":"readv2"},{"code":"8882","system":"readv2"},{"code":"Gy21.00","system":"readv2"},{"code":"Gy40.00","system":"readv2"},{"code":"Gy41.00","system":"readv2"},{"code":"Gy60.00","system":"readv2"},{"code":"SP01500","system":"readv2"},{"code":"SP0F.00","system":"readv2"},{"code":"TA02000","system":"readv2"},{"code":"TA22000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-haemodialysis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-haemodialysis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-haemodialysis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
