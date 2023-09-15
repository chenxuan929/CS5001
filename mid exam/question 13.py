def fee_fi_file(file_name):
    
    search_text = 'Nike'
    replace_text = 'Prof Keith'

    try:
        with open("file_name.txt", "r") as file:
            
            new_data = []
            for each in file:
                new_data.append(each)
            for i in range(len(new_data)):
                new_data[i] = new_data[i].replace(search_text, replace_text)
            new_data = ''.join(new_data)
            
        with open("new_file_name.txt", "a+") as out_file:
            out_file.write(new_data)
            
    except IOError:
        with open('error.txt', 'a+') as file:
            file.write('file_name.txt does not exist')
    
def main():
    file_name = 'file_name'
    fee_fi_file(file_name)
    
if __name__ == "__main__":
    main()
