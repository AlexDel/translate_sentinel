This module performs evaluation of sense-distortion in translation.
Original text and its translation are analyzed under several parameters and decision about vandalism is made.

1. Dependecies
    Module is written in Python 2.7. Encoding - utf-8.
    The following libs are required for correct functioning:
        1.1 nltk - https://github.com/nltk/nltk
            NLTK installation - http://nltk.org/install.html
            NLTK data installation - http://nltk.org/data.html
                For correct working "stopwords" and "WordNet" corpora should be installed

        1.2 requests - https://github.com/kennethreitz/requests/
            request installation - http://docs.python-requests.org/en/latest/user/install.html#install

2. Module structure
    module can be run via ython console and CGI

    2.1 To run via python console use  main.py module.

        main.py API:
            process(t_unit_raw, make_log = False)
                args:
                    t_unit_raw - json - translation unit
                    make_log - boolean - whether the debug results for the t.unit should be added to log
                r-type: json (boolean) - whether the translation is vandal or not

            debug(t_unit_raw) - takes json-input and returns values of evaluated parameteres


        Here is an example usage of Translate sentinel module:

            >>> from translate_sentinel import main
            >>> print main.process(translation_object)
             ...u'false'
            >>> print main.debug(translation_object)
             ...False
                String_target_length  218
                Length_difference  0.703196347032
                Digits_amount  0.00456621004566
                Digits_blocks_intersection  0.0
                Target_upper_case  1.0
                Longest_symbol_repetition  0
                Longest_word  15
                BLEU_metrics  0.666666666667
                Bigram_calculator  0.0
                Levenstein_calculator  0.333333333333
                Braun_Balke_calculator  0.666666666667
                Profanity_calculator  1.0
                Semantic_calculator  0.318931803491

    2.2 To run via CGI use launchcgi.py which listens for HTTP requests:
        launchcgi.py takes the same args, but takes them from 'translation_object' and 'make_log' POST or GET query string parameters


3. Input structure and requirements
   Functions process() and debug() takes json-strings as inputs and return json as well
   Structure of the the inpu json is the following:

        {
        "orig": {
            "lang": "en",
            "text": "Are your foregrounds fighting for the users’ attention?"
            },
        "target": {
            "lang": "ru",
             "text": "Объекты вашего переднего плана борются за внимание пользователей?"
             }
        }
   NB! Special symbols in json like ; " : { and { should be escaped in "text" values.

4.  Logging
    Logging is performed within "main.process()" method with argument "make_log = True" passed.
    Log entry structure:
        'SENTINEL' [DATE - TIME]
        Original text
        Translated text
        Vandal value (True|False)
        Calc_1_name - calc_1_value
        Calc_2_name - calc_2_value
        ..........................
        Calc_n_name - calc_n_value

    Log is stored in  module root directory in file 'trans_log.log'



All bugs and issues are welcome at https://bitbucket.org/AlexDel/translate_sentinel/