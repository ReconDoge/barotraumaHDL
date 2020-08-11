import re

'''A parser that works on the psuedo code written in TextFile1.txt, which will become an example of the
hardware description language. This is used to make custom chips from built-in chips, and eventually make
more complex chips from custom chips.

CHIP specifies the chip's name
IN specifies where the input pins are
OUT where the output pins are
PARTS specifies what other chips this one is made up of. Content of the brackets sets the input, output as
well as the chip's properties'''

key_strings = {"IN": re.compile(r"(?<=IN:)(.*?)(?=;)"),
               "OUT": re.compile(r"(?<=OUT:)(.*?)(?=;)"),
               "PARTS": re.compile(r"\w+\s*\(.*\)"),
               "CHIP": re.compile(r"(?<=CHIP)(.*?)(?=:)")}


class HDLParser():

    def __init__(self, file):
        self.content = file.read()

    def get_values_after_key(self, key):
       
        if key is not "PARTS":
        # returns the values after the keywords (except for PARTS) in a list
            string = str(re.findall(key_strings[key], self.content))
            return re.findall("\w+", string)
        else:
        #returns the parts in a dictionary with the chip's name as key and the contents within the
        #brackets as the values
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