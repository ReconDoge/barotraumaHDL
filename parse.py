import re


key_strings = {"IN": re.compile(r"(?<=IN:)(.*?)(?=;)"),
               "OUT": re.compile(r"(?<=OUT:)(.*?)(?=;)"),
               "PARTS": re.compile(r"\w+\s*\(.*\)"),
               "CHIP": re.compile(r"(?<=CHIP)(.*?)(?=:)")}


class HDLParser():

    def __init__(self, file):
        self.content = file.read()

    def get_values_after_key(self, key):
        if key is not "PARTS":
            string = str(re.findall(key_strings[key], self.content))
            return re.findall("\w+", string)
        else:
            component_dic = {}
            for match in re.findall(key_strings[key], self.content):
                k = re.findall(r"[A-Z]\w*", match)
                v = re.findall(r"\(.*\)", match)
                component_dic[k[0]] = v[0]
            return component_dic
      
        
if __name__ == "__main__":
    with open("TextFile1.txt", "r+") as f:
        p = HDLParser(f)
        print(p.get_values_after_key("PARTS"))