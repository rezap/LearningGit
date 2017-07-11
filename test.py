def trim_func(input_str, test_char):
        input_str_list = list(input_str);
        print input_str_list
        print len(input_str_list)
        for i in xrange(len(input_str_list)):
                if input_str_list[i]==test_char:
                        input_str_list[i] = ' '
                        print input_str_list
        return ''.join(input_str_list)
input_str = "reza";
trimmed_str = trim_func(input_str,'r');
print trimmed_str
