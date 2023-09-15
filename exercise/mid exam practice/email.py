def email_process(email):
    result = []
    split = email.split("@")
    
    part_1 = split[0].split('.')
    part_2 = split[1].split('.')
    
    result.append(part_1)
    result.append(part_2)
    
    return result

def recreate_email(list):
    email = []
    part_1 = '.'.join(list[0])
    part_2 = '@' + '.'.join(list[1])
    
    email = part_1 + part_2
    return email
    
    
def main():
    email_1 = 'lastname.firstname@northeastern.edu'
    email_2 = 'kim.sam@northeastern.edu'
    
    result_1 = email_process(email_1)
    print(result_1)
    print(recreate_email(result_1))

    result_2 = email_process(email_2)
    print(result_2)
    print(recreate_email(result_2))

if __name__ == "__main__":
    main()
