import re

# function to auto test 
def test(input: str, expected_result: str):
    try: 
        assert input == expected_result
        print('Testcase passed, results:', input)
    except:
        print('Testcase failed')

def remove_patterns(s: str):
    s = s.split(',')
    ref = s[0]
    for i in range(1, len(s)):
        ref = re.sub(s[i], '', ref)
    return ref

def check_coverage(s: str):
    s = s.split(',')
    ref = s[0]
    coverage_indexes = []
    coverage = ''
    
    # handle case for middle of ref string
    for i in range(1, len(s)):
        # find coverage indexes in the ref string for each keyword
        matches = list(re.finditer(s[i], ref))
        [coverage_indexes.append([match.start(), match.end()]) for match in matches]
    coverage_indexes.sort()
    
    # handle case for beginning of ref string
    if coverage_indexes[0][0] != 0:
        coverage += f'0-{coverage_indexes[0][0] - 1}, '
        
    for i in range(len(coverage_indexes)):
        # try except so that we won't have trouble with index out of bound error when we reach end of array
        try:
            # check for where there is a jump in the index, meaning that there is no coverage from the keyword
            if coverage_indexes[i][1] < coverage_indexes[i+1][0]:
                coverage += f'{coverage_indexes[i][1]}-{coverage_indexes[i+1][0] - 1}, '
        except:
            break
        
    # handle case for end of ref string
    if len(ref) != coverage_indexes[-1][1]:
        coverage += f'{coverage_indexes[-1][1]}-{len(ref) - 1}, '
    
    # everything is covered
    if len(coverage) == 0:
        return 'Covered'
        
    return coverage[:-2]

# test cases
test(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,EFGHIJKLMN,OPQRSTUV,WXYZ,0123456789"), 'Covered')

test(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,0123456789"), 'Covered')

test(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFG,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,23456789"), '26-27, 42-42')

test(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,GHIJKLMN,OPQRSTUV,WXYZ,0126789"), '26-35')

test(check_coverage("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,ABCDEF,HIJKLMN,OPQRSTUV,WXYZ,0123456789"), '6-6')
