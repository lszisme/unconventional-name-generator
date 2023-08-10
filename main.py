import random

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def generate_random_name():
    adjective_list = read_lines_from_file('形容词.txt')
    noun_list = read_lines_from_file('名词.txt')
    verb_list = read_lines_from_file('动词.txt')
    
    adjective = random.choice(adjective_list)
    noun = random.choice(noun_list)
    verb = random.choice(verb_list)
    
    random_name = f"{adjective}{noun}{verb}"
    return random_name

if __name__ == '__main__':
    while True:
        random_name = generate_random_name()
        print(f"随机名称: {random_name}")
        
        user_input = input("按回车生成下一个随机名称，输入 'exit' 退出程序: ")
        
        if user_input.lower() == 'exit':
            break
