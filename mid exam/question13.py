def fee_fi_file(file_name):
    search_text = 'Nike'
    replace_text = 'Prof Keith'
    try:
        with open(f"{file_name}.txt", "r") as file:
            data = file.read()
            new_data = data.replace(search_text, replace_text)     
        with open(f"new_{file_name}.txt", "w") as file:
            file.write(new_data)
        print('replaced')
       
    except IOError:
        with open('error.txt', 'a+') as file:
            file.write(f'{file_name}.txt does not exist')
        print('error')

def main():
    file_name = 'hi'
    fee_fi_file(file_name)
    
if __name__ == "__main__":
    main()
