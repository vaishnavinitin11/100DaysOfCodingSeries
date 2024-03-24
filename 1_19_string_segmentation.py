# String segmentation
string="datacamp"

def str_segment(string,dictionary):
    # nstring=[]
    # for ind,i in enumerate(string):
    #     for l in range(ind,len(string)):
    #         nstring.append(string[ind:l])
            
    # dictionary = ["data", "camp", "cam", "lack"]
    # for d in dictionary:
    #     if d in nstring:
    #         print(True)
    
    for i in range(1,len(string)+1):
        sstr=string[0:i]
        if sstr in dictionary:
            tstr=string[i:]
            if(tstr in dictionary or str_segment(tstr,dictionary)):
                return(True)
    return False

def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        first_str = s[0:i]
        if first_str in dictionary:
            second_str = s[i:]
            if (
                not second_str
                or second_str in dictionary
                or can_segment_str(second_str, dictionary)
            ):
                return True
    return False


s = "datacamp"
dictionary = ["datal", "camp", "cam", "data"]
print(can_segment_str(s, dictionary))
print('-----------------------')
print(str_segment(s, dictionary))

