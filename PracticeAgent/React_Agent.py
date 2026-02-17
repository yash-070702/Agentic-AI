def think(index,data):
    """Reason about what to do next based on the current index and data
    if there is more data to process , check if the number is even or odd 
    if there is no data , the task is done
    """

    if index < len(data):
        curr_val=data[index]

        if curr_val%2==0:
            return "add_even"

        else:
            return "skip"


    return "done"




def act(action , index , data , result):
    """act based on the action decided by the "think" function 
    --"add_even": add the even number to the result
    --"skip":skip the odd number
    """

    if action=='add_even':
        result+=data[index]
        print("adding curr val to result")

    elif action=="skip":
        print(f"skipping {data[index]}")

    return index+1,result


def observe(result):
    """Observe the current state of the result ( sum of even numbers)
    """

    print(f"Agents current sum of even numbers :{result}")


def run_agent(data):
    """
    Run the agent through the reAct streew untill the task is completly"""

    index=0
    result=0

    while True:
        action=think(index,data)
        if action=="done":
            print(f"Task completely final sum of even numbers : {result}")
            break

        index , result=act(action, index , data , result)
        observe(result)

data=[1,2,3,4,5,6,7,8,9,10]

run_agent(data)