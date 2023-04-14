# def solution(order):
#     count = 0
#     count += str(order).count('3')
#     count += str(order).count('6')
#     count += str(order).count('9')
#     return count

# import re
# re.sub('[^369]', '', '123123efjdksajfa123123f6699999')
# re.findall('[369]', '3398764819731')

import re
def solution(order):
    return len(re.findall('[369]', str(order)))