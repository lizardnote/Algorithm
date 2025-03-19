def solution(s):
    answer = True
    st_list = [0]
    for i in s:
        if i ==")":
            if st_list[-1] == "(":
                st_list.pop()
                # print(st_list)
            else:
                st_list.append(i)
        else:
            st_list.append(i)
        
    return True if len(st_list) == 1 else False