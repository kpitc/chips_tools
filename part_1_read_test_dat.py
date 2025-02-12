import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

level_pack = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)

print(str(level_pack))

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data
output_file_path = "data/ppfgd_test.txt"
with open(output_file_path, "w") as file:
    file.write(str(level_pack))

