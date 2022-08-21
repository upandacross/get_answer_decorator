def get_answer(func):
    '''Decorated function to accept input from stdin with a custom prompt and specific conversion
and validity tests. In all cases, a reply of "Q" simply returns "Q" avoiding conversion and validity
 testing.

Arguments
    question - prompt displayed on stdout answering for input
    default  - decoration will return this value if no entry is given other than CR
                unless default is None, in which case decoration considers CR invalid
    max_try  - decoration will return None after max_try attempts - default 999
    
    func - the function that is decorated. Typically includes conversion (e.g. int(output))
            and validity test(s) (e.g. assert 0 < output < 10). In the case of one or more assert
            statements, the next prompt for input will have the exception message prepended

Input:
    answer - string response to question prompt and to be validated except:
          Input of "Q" is always returned as "Q"
          Input of "?" prints answers string and then repeats question prompt.
          Input of invalid data results in display of answers string
Example
    @get_answer
    def get_int(answer, answers, default, max_try=3):
        assert answer > 10, answers
        answer = int(answer) # if exception raised, decoration will query for new answer
        return answer
    
    integer = get_int('Enter int', 'answer > 10, default 5', 5):
        
'''

    def decorated_function(question, answers, default, max_try, **kwargs):
        error          = ''
        current_answer = question
        for cnt in range(max_try):
            input_response = input(f'{current_answer} ({answers})?: ')
            if input_response == '' and default != None:
                return default
            elif isinstance(input_response, str) and input_response.upper() == 'Q':
                return 'Q'
            elif isinstance(input_response, str) and input_response.upper() == '?':
                print(answers);
                continue
            else:
                try:
                    converted_valid_response = func(input_response, answers,
                                                    default, max_try, **kwargs)
                    return converted_valid_response
                except Exception as e:
                    current_answer = f'{e}\n{question} '
            
            if cnt == max_try - 1:
                print(f'maximum attempts made')
                input_response == None
            
        return input_response
    
    return decorated_function

