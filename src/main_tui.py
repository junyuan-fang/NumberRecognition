import readline
import random
from time import time


from numpy.matrixlib.defmatrix import matrix 
#direction = sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from repositories import mnist_data_repository
from services import knn as K

def main():
    running = True
    welcome ="Welcome to 'no gui', the procedure is for testing the 'k-nearest neighbors algorithm' implementation."
    parameter_list = [3, 200, "D22"]
    instruction = "'Enter' button to continue\n'set' to set parameters\n'q' to quit \n:"
    print(welcome)
    while running:
        #parameters
        k = parameter_list[0]
        train_range = parameter_list[1]
        method = parameter_list[2]
        #knn
        start = time()
        marks = [' ', '*']
        index = random.randint(0,9999)
        label = K.knn.get_label(index)
        img_matrix =K.knn.get_test_img(index)
        print(f"Here is {label}'s pic:")
        show_img_matrix(img_matrix, marks)
        result = K.knn.recognition(k,index,train_range,method)
        parameters_txt = f"k = {k}, trainning range = {train_range}, method = '{method}'\n"
        print(parameters_txt)
        print(f"Image's label is '{label}'")
        print(f"The result from KNN is '{result}'\n")
        print(f"Recognition takes {time()-start} second")
        

        #continue
        repeat = True
        while repeat:
            from_keyboard = input(instruction)
            
            if from_keyboard == 'q':
                running = False
                repeat = False
            elif from_keyboard == 'set':
                set_param(parameter_list)
                running = True
                repeat = False
            elif from_keyboard == '':
                #running = True
                repeat = False
            else:
                #repeat = True
                print(f"Wrong instruction {from_keyboard}")

def set_param(parameter_list):
    #k value
    repeat = True
    while repeat:
        from_keyboard = input("\nSelect k: 1-10\n")
        if from_keyboard =='':
            break
        try:
            value = int(from_keyboard.strip())
            if value>=1 and value <=10:
                parameter_list[0]=value
                repeat = False 
            else:
                print(f"{from_keyboard} is not 1-10")
        except Exception as e:
            print(e)
            print(f"{from_keyboard} is not a int")
    #range
    repeat = True
    while repeat:
        from_keyboard = input("Select the trainning tange: 1-60000\n")
        if from_keyboard =='':
            break
        try:
            value = int(from_keyboard)
            if value>=1 and value <=60000:
                parameter_list[1]=value
                repeat = False 
            else:
                print(f"{from_keyboard} out of range 1-60000")
        except:
            print(f"{from_keyboard} is not a int")
    #method
    repeat = True
    while repeat:
        from_keyboard = input("Select the method: 'D22' or 'D23'\n")
        if from_keyboard =='':
            break
        if from_keyboard == "D22" or from_keyboard == "D23":
            parameter_list[2]=from_keyboard
            repeat = False 
        else:
            print(f"{from_keyboard} is not 'D22' or 'D23' ")
       
def show_img_matrix(img_matrix, marks):
    for y in range (len(img_matrix)):
        row = ""
        for x in range(len(img_matrix[0])):
            if img_matrix[y][x] == 0:
                row+=marks[0]
            else:
                row+=marks[1]
        print(row)

main()
