import re

input_list = []
with open("./input.txt", "r") as f:
    input_list = f.read().splitlines()

field_necessary = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
ecl_values = set(["amb", "blu", "brn", "gry" ,"grn", "hzl", "oth"])

def is_height_valid(input):
    match = re.match(r"([0-9]+)(cm|in)", input, re.I)
    if match:
        hgt_pair = match.groups()
        size, unit = hgt_pair
        size = int(size)
        if unit == "cm":
            return size >= 150 and size <= 193
        else:
            return size >= 59 and size <= 76
    return False

def is_valid_hex_color(input):
    return re.search(r"^#(?:[0-9a-f]{6})$", input, re.I)


valids = 0
current_input = ""
for ldx, line in enumerate(input_list):
    if line == "" or ldx == len(input_list) - 1:
        pairs = [x.split(":") for x in current_input.strip().split(" ")]
        current_input = ""
        pair_dict = dict(pairs)
        keys = set([x[0] for x in pairs])
        if len(keys) >= 7 and field_necessary.issubset(keys):
            byr = int(pair_dict['byr'])
            if byr >= 1920 and byr <= 2002:
                iyr = int(pair_dict['iyr'])
                if iyr >= 2010 and iyr <= 2020:
                    eyr = int(pair_dict['eyr'])
                    if eyr >= 2020 and eyr <= 2030:
                        if is_height_valid(pair_dict['hgt']):
                            if is_valid_hex_color(pair_dict['hcl']):
                                if pair_dict['ecl'] in ecl_values:
                                    pid = pair_dict['pid']
                                    if len(pid) == 9:
                                        try:
                                            int(pid) #meh
                                            valids += 1
                                        except:
                                            pass
    else:
        current_input += f" {line}"
print(valids)
