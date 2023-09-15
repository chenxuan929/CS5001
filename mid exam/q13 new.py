import os
def fee_fi_file(file_name):
    ole_text = 'Nike'
    new_text = 'Prof Keith'
    data = []
    try:
        os.path.isfile(file_name)
        
    except IOError:
        with open('error.txt', 'a+') as file:
            message = file_name + 'does not exist\n'
            file.write(message)
            
    else:
        with open(file_name, mode = 'r') as file:
            for each in file:
                data.append(each)
        for i in rang(len(data)):
            data[i] = data[i].replace(old_text, new_text)
        text = ''.join(data)
        
            

def main():
    file_name = 'KeithMsg'
    fee_fi_file(file_name)
    
if __name__ == "__main__":
    main()
