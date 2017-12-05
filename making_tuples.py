my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def in_out(name_num):
    output = []
    for name in name_num:
        output.append((name, name_num[name]))
    return (output)
print (in_out(my_dict))